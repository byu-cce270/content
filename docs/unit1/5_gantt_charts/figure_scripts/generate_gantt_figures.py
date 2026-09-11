"""Generate the Topic 5 instructional figures with desktop Microsoft Excel.

The script creates temporary example workbooks. It does not modify either
student starter workbook. Run it from the repository root with the Conda
Python installation that provides openpyxl, Pillow, and pywin32.
"""

from __future__ import annotations

import argparse
from copy import copy
import shutil
import tempfile
import time
from datetime import date, timedelta
from pathlib import Path

import pythoncom
import win32com.client
from openpyxl import load_workbook
from openpyxl.formatting.rule import DataBarRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.workbook.properties import CalcProperties
from PIL import ImageGrab


REPO_ROOT = Path(__file__).resolve().parents[4]
TOPIC_DIR = REPO_ROOT / "docs" / "unit1" / "5_gantt_charts"
STARTER = TOPIC_DIR / "(Starter-Workbook)-Class-Gantt-Chart.xlsx"
IMAGE_DIR = TOPIC_DIR / "images"

HEADER_FILL = PatternFill("solid", fgColor="8DB4E2")
PHASE_FILL = PatternFill("solid", fgColor="D9E5F6")
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")
TASK_FILL = PatternFill("solid", fgColor="70AD47")
PHASE_BAR_FILL = PatternFill("solid", fgColor="4472C4")
WEEKEND_FILL = PatternFill("solid", fgColor="E7E6E6")
THIN_GRAY = Side(style="thin", color="808080")
TODAY_SIDE = Side(style="medium", color="C00000")


def next_monday_on_or_before(day: date) -> date:
    return day - timedelta(days=day.weekday())


def add_workdays(start: date, offset: int) -> date:
    current = start
    remaining = offset
    while remaining > 0:
        current += timedelta(days=1)
        if current.weekday() < 5:
            remaining -= 1
    return current


def as_date(value) -> date:
    return value.date() if hasattr(value, "date") else value


def configure_base(workbook_path: Path) -> None:
    wb = load_workbook(workbook_path)
    ws = wb["Sheet1"]
    ws.sheet_view.showGridLines = True

    ws["A1"] = "CCE 270 In-Class Gantt Chart"
    ws["A2"] = "CCE Department"
    ws["A3"] = "Project Manager"
    ws["C3"] = "Project Start:"
    project_start = date.today()
    ws["D3"] = project_start

    wb.defined_names.add(
        DefinedName("project_start", attr_text="'Sheet1'!$D$3")
    )

    ws["F6"] = "WORK DAYS"
    for cell in ws[6][0:6]:
        cell.fill = HEADER_FILL
        cell.font = Font(name="Arial", size=10, bold=True)
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    ws["A7"] = "Phase 1"
    ws["A12"] = "Phase 2"
    tasks = {
        8: ("1.1 Define requirements", "Project Manager", 0, 2),
        9: ("1.2 Identify inputs", "Team Member 2", 1, 3),
        10: ("1.3 Plan workbook layout", "Team Member 3", 2, 3),
        13: ("2.1 Build input section", "Team Member 2", 5, 3),
        14: ("2.2 Build formulas (after 2.1)", "Team Member 3", 7, 3),
        15: ("2.3 Verify workbook", "Project Manager", 9, 2),
    }

    for row, (task, role, offset, duration) in tasks.items():
        ws.cell(row, 1, task)
        ws.cell(row, 2, role)
        task_start = add_workdays(project_start, offset)
        ws.cell(row, 4, task_start)
        ws.cell(row, 5, add_workdays(task_start, duration - 1))
        ws.cell(row, 6, duration)
        ws.cell(row, 1).alignment = Alignment(indent=1)
        for col in (4, 6):
            ws.cell(row, col).fill = INPUT_FILL

    for phase_row in (7, 12):
        for cell in ws[phase_row][0:33]:
            cell.fill = PHASE_FILL
            cell.font = Font(name="Arial", size=10, bold=True)

    for row in range(1, 16):
        for col in range(1, 36):
            font = copy(ws.cell(row, col).font)
            font.name = "Arial"
            font.size = 10
            ws.cell(row, col).font = font

    ws["A1"].font = Font(name="Arial", size=20, bold=True, color="1F4E78")
    ws["D3"].number_format = "mmm d, yyyy"
    ws.column_dimensions["A"].width = 31
    ws.column_dimensions["B"].width = 18
    ws.column_dimensions["C"].width = 12
    ws.column_dimensions["D"].width = 12
    ws.column_dimensions["E"].width = 12
    ws.column_dimensions["F"].width = 12
    ws.column_dimensions["G"].width = 2
    ws.row_dimensions[6].height = 26

    for row in range(7, 16):
        for col in range(1, 7):
            ws.cell(row, col).border = Border(bottom=THIN_GRAY)
    for row in (8, 9, 10, 13, 14, 15):
        ws.cell(row, 3).number_format = "0%"
        ws.cell(row, 4).number_format = "m/d/yyyy"
        ws.cell(row, 5).number_format = "m/d/yyyy"

    wb.calculation = wb.calculation or CalcProperties()
    wb.calculation.fullCalcOnLoad = True
    wb.calculation.forceFullCalc = True
    wb.calculation.calcMode = "auto"
    wb.save(workbook_path)


def add_timeline(workbook_path: Path, dynamic: bool = False) -> None:
    wb = load_workbook(workbook_path)
    ws = wb["Sheet1"]

    ws["C4"] = "Display Week:"
    ws["D4"] = 1
    wb.defined_names.add(
        DefinedName("display_week", attr_text="'Sheet1'!$D$4")
    )

    project_start = as_date(ws["D3"].value)
    timeline_start = next_monday_on_or_before(project_start) if dynamic else project_start
    for col in range(8, 36):
        ws.cell(5, col, timeline_start + timedelta(days=col - 8))
    for col in range(8, 36):
        ws.cell(6, col, as_date(ws.cell(5, col).value).strftime("%a")[0])
        ws.cell(5, col).number_format = "d"
        ws.cell(5, col).alignment = Alignment(horizontal="center")
        ws.cell(6, col).alignment = Alignment(horizontal="center")
        ws.column_dimensions[ws.cell(1, col).column_letter].width = 3.2

    for start_col in (8, 15, 22, 29):
        end_col = start_col + 6
        ws.merge_cells(start_row=4, start_column=start_col, end_row=4, end_column=end_col)
        ws.cell(4, start_col, ws.cell(5, start_col).value)
        ws.cell(4, start_col).number_format = "mmm d, yyyy"
        ws.cell(4, start_col).alignment = Alignment(horizontal="left")
        for col in range(start_col, end_col + 1):
            ws.cell(4, col).border = Border(
                top=THIN_GRAY, bottom=THIN_GRAY, left=THIN_GRAY, right=THIN_GRAY
            )

    for col in range(8, 36):
        ws.cell(6, col).fill = HEADER_FILL
        ws.cell(6, col).font = Font(name="Arial", size=10, bold=True)

    wb.calculation.fullCalcOnLoad = True
    wb.calculation.forceFullCalc = True
    wb.save(workbook_path)


def add_task_bars(workbook_path: Path) -> None:
    wb = load_workbook(workbook_path)
    ws = wb["Sheet1"]
    for row in (8, 9, 10, 13, 14, 15):
        task_start = as_date(ws.cell(row, 4).value)
        task_end = as_date(ws.cell(row, 5).value)
        for col in range(8, 36):
            timeline_date = as_date(ws.cell(5, col).value)
            if task_start <= timeline_date <= task_end:
                ws.cell(row, col).fill = TASK_FILL
    for col in range(8, 36):
        if as_date(ws.cell(5, col).value) == date.today():
            for row in range(5, 16):
                existing = ws.cell(row, col).border
                ws.cell(row, col).border = Border(
                    left=TODAY_SIDE,
                    right=TODAY_SIDE,
                    top=existing.top,
                    bottom=existing.bottom,
                )
    wb.save(workbook_path)


def add_progress(workbook_path: Path) -> None:
    wb = load_workbook(workbook_path)
    ws = wb["Sheet1"]
    for row, progress in {
        8: 1.00,
        9: 0.50,
        10: 0.25,
        13: 0.00,
        14: 0.00,
        15: 0.00,
    }.items():
        ws.cell(row, 3, progress)
        ws.cell(row, 3).number_format = "0%"
    ws["C7"] = "=AVERAGE(C8:C10)"
    ws["C12"] = "=AVERAGE(C13:C15)"
    ws["C7"].number_format = "0%"
    ws["C12"].number_format = "0%"
    ws.conditional_formatting.add(
        "C7:C15",
        DataBarRule(
            start_type="num",
            start_value=0,
            end_type="num",
            end_value=1,
            color="5B9BD5",
            showValue=True,
        ),
    )
    wb.save(workbook_path)


def add_summaries(workbook_path: Path) -> None:
    wb = load_workbook(workbook_path)
    ws = wb["Sheet1"]
    ws["D7"] = min(as_date(ws.cell(row, 4).value) for row in (8, 9, 10))
    ws["E7"] = max(as_date(ws.cell(row, 5).value) for row in (8, 9, 10))
    ws["D12"] = min(as_date(ws.cell(row, 4).value) for row in (13, 14, 15))
    ws["E12"] = max(as_date(ws.cell(row, 5).value) for row in (13, 14, 15))
    ws["E3"] = "Project End:"
    ws["F3"] = max(as_date(ws.cell(row, 5).value) for row in (8, 9, 10, 13, 14, 15))
    ws["F3"].number_format = "mmm d, yyyy"
    for cell in ("D7", "E7", "D12", "E12"):
        ws[cell].number_format = "m/d/yyyy"
    for row in (7, 12):
        phase_start = as_date(ws.cell(row, 4).value)
        phase_end = as_date(ws.cell(row, 5).value)
        for col in range(8, 36):
            timeline_date = as_date(ws.cell(5, col).value)
            if phase_start <= timeline_date <= phase_end:
                ws.cell(row, col).fill = PHASE_BAR_FILL
    wb.save(workbook_path)


def add_weekends(workbook_path: Path) -> None:
    wb = load_workbook(workbook_path)
    ws = wb["Sheet1"]
    for col in range(8, 36):
        if as_date(ws.cell(5, col).value).weekday() > 4:
            for row in range(5, 16):
                cell = ws.cell(row, col)
                if cell.fill.fill_type is None:
                    cell.fill = WEEKEND_FILL
    wb.save(workbook_path)


def export_range(excel, workbook_path: Path, output_path: Path, cell_range: str) -> None:
    workbook = excel.Workbooks.Open(str(workbook_path.resolve()), UpdateLinks=0, ReadOnly=False)
    try:
        worksheet = workbook.Worksheets("Sheet1")
        workbook.Application.CalculateFull()
        workbook.Save()
        worksheet.Activate()
        workbook.Windows(1).Zoom = 100
        source = worksheet.Range(cell_range)
        source.CopyPicture(Appearance=1, Format=2)
        for _ in range(20):
            time.sleep(0.2)
            image = ImageGrab.grabclipboard()
            if image is not None and hasattr(image, "save"):
                image.save(output_path, "PNG")
                break
        else:
            raise RuntimeError(f"Excel did not place {cell_range} on the clipboard")
    finally:
        workbook.Close(SaveChanges=False)


def build_figures(keep_workbooks: bool) -> None:
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    temp_dir = Path(tempfile.mkdtemp(prefix="cce270_gantt_"))
    pythoncom.CoInitialize()
    excel = win32com.client.DispatchEx("Excel.Application")
    excel.Visible = True
    excel.DisplayAlerts = False

    try:
        stages = [
            ("gantt_start.png", 0, "A1:F8"),
            ("gantt_step1.png", 1, "A1:F15"),
            ("gantt_step2.png", 2, "A1:AI15"),
            ("gantt_step4.png", 4, "A1:AI15"),
            ("gantt_step5-1.png", 5, "A1:AI15"),
            ("gantt_step6.png", 6, "A1:AI15"),
            ("gantt_step7-1.png", 7, "A1:AI15"),
        ]

        for image_name, stage, cell_range in stages:
            workbook_path = temp_dir / f"stage_{stage}.xlsx"
            shutil.copy2(STARTER, workbook_path)
            if stage >= 1:
                configure_base(workbook_path)
            if stage >= 2:
                add_timeline(workbook_path, dynamic=stage >= 4)
            if stage >= 4:
                add_task_bars(workbook_path)
            if stage >= 5:
                add_progress(workbook_path)
            if stage >= 6:
                add_summaries(workbook_path)
            if stage >= 7:
                add_weekends(workbook_path)
            export_range(excel, workbook_path, IMAGE_DIR / image_name, cell_range)

        if keep_workbooks:
            retained = TOPIC_DIR / "figure_scripts" / "_generated_workbooks"
            if retained.exists():
                shutil.rmtree(retained)
            shutil.copytree(temp_dir, retained)
    finally:
        excel.Quit()
        pythoncom.CoUninitialize()
        shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--keep-workbooks",
        action="store_true",
        help="Retain generated example workbooks for troubleshooting.",
    )
    args = parser.parse_args()
    build_figures(args.keep_workbooks)
