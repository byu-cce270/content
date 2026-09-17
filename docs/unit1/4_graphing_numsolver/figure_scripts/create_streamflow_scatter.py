"""Export the Topic 4 streamflow example as an Excel XY scatter chart."""

from pathlib import Path
import shutil
import tempfile

import win32com.client


XL_CATEGORY = 1
XL_VALUE = 2
XL_LEGEND_POSITION_RIGHT = -4152
XL_XY_SCATTER_LINES_NO_MARKERS = 75


def main() -> None:
    topic_dir = Path(__file__).resolve().parents[1]
    source = topic_dir / "(Starter-Workbook)-HW-Graphing-and-Solver.xlsx"
    output = topic_dir / "graphing_images" / "streamflow_chart.png"

    with tempfile.TemporaryDirectory(prefix="cce270_streamflow_") as temp_dir:
        workbook_copy = Path(temp_dir) / source.name
        shutil.copy2(source, workbook_copy)

        excel = win32com.client.DispatchEx("Excel.Application")
        excel.Visible = False
        excel.DisplayAlerts = False

        workbook = None
        try:
            workbook = excel.Workbooks.Open(str(workbook_copy), UpdateLinks=0, ReadOnly=False)
            worksheet = workbook.Worksheets("Streamflow Data")

            chart_object = worksheet.ChartObjects().Add(20, 20, 1100, 620)
            chart = chart_object.Chart
            chart.ChartType = XL_XY_SCATTER_LINES_NO_MARKERS

            while chart.SeriesCollection().Count:
                chart.SeriesCollection(1).Delete()

            for column in range(2, 7):
                series = chart.SeriesCollection().NewSeries()
                series.Name = worksheet.Cells(3, column).Value.strip()
                series.XValues = worksheet.Range("A4:A2883")
                series.Values = worksheet.Range(
                    worksheet.Cells(4, column), worksheet.Cells(2883, column)
                )

            chart.HasTitle = True
            chart.ChartTitle.Text = "Provo River Streamflow"
            chart.HasLegend = True
            chart.Legend.Position = XL_LEGEND_POSITION_RIGHT

            horizontal_axis = chart.Axes(XL_CATEGORY)
            horizontal_axis.HasTitle = True
            horizontal_axis.AxisTitle.Text = "Date and time"
            horizontal_axis.TickLabels.NumberFormat = "m/d/yy"

            vertical_axis = chart.Axes(XL_VALUE)
            vertical_axis.HasTitle = True
            vertical_axis.AxisTitle.Text = "Streamflow (ft^3/s)"
            vertical_axis.MinimumScale = 0

            output.parent.mkdir(parents=True, exist_ok=True)
            if not chart.Export(str(output), "PNG"):
                raise RuntimeError("Excel did not export the streamflow chart")
        finally:
            if workbook is not None:
                workbook.Close(SaveChanges=False)
            excel.Quit()


if __name__ == "__main__":
    main()
