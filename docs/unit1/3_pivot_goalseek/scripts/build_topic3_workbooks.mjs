import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const base = "docs/unit1/3_pivot_goalseek";
const outDir = ".codex_tmp/topic3_outputs";
await fs.mkdir(outDir, { recursive: true });

const scenarios = [
  { h:[90,40,0], d:[0.140,0.090,0.080], l:[175,350,400], f:[0.017,0.018,0.023] },
  { h:[0,90,40], d:[0.140,0.085,0.100], l:[200,450,250], f:[0.017,0.023,0.022] },
  { h:[40,0,90], d:[0.090,0.080,0.120], l:[300,450,175], f:[0.022,0.023,0.016] },
  { h:[90,40,0], d:[0.085,0.100,0.140], l:[450,350,150], f:[0.023,0.022,0.016] },
  { h:[0,90,40], d:[0.085,0.140,0.090], l:[450,200,350], f:[0.025,0.017,0.018] },
  { h:[40,0,90], d:[0.090,0.130,0.075], l:[350,200,450], f:[0.018,0.016,0.021] },
  { h:[90,0,40], d:[0.130,0.080,0.090], l:[200,400,250], f:[0.017,0.023,0.018] },
  { h:[40,90,0], d:[0.090,0.075,0.140], l:[350,350,150], f:[0.022,0.023,0.015] },
  { h:[0,40,90], d:[0.080,0.110,0.120], l:[350,350,200], f:[0.025,0.020,0.016] },
  { h:[90,0,40], d:[0.080,0.140,0.110], l:[400,150,350], f:[0.021,0.016,0.018] },
];

const g = 9.81;
function branchAt(hj, d, l, f, h) {
  const inflow = h > hj;
  const denominator = f*l/d + (inflow ? 1 : -1);
  if (denominator <= 0) throw new Error(`Invalid denominator ${denominator}`);
  const velocity = Math.sqrt(2*g*Math.abs(h-hj)/denominator);
  const flow = velocity*Math.PI*d*d/4;
  return { direction: inflow ? "Inflow" : "Outflow", velocity, flow };
}
function solveScenario(s) {
  let lo = Math.min(...s.h) + 1e-10;
  let hi = Math.max(...s.h) - 1e-10;
  const net = hj => s.h.reduce((sum,h,i) => {
    const b = branchAt(hj,s.d[i],s.l[i],s.f[i],h);
    return sum + (b.direction === "Inflow" ? b.flow : -b.flow);
  },0);
  if (!(net(lo) > 0 && net(hi) < 0)) throw new Error("Scenario does not bracket a balanced head");
  for (let i=0;i<120;i++) {
    const mid=(lo+hi)/2;
    if (net(mid)>0) lo=mid; else hi=mid;
  }
  const hj=(lo+hi)/2;
  const branches=s.h.map((h,i)=>branchAt(hj,s.d[i],s.l[i],s.f[i],h));
  return {hj,branches,net:net(hj)};
}

const solved = scenarios.map(solveScenario);
const dataset = [["Scenario","Pipe","Diameter (m)","Length (m)","Darcy Friction Factor","Reservoir Head (m)","Junction Head, Hj (m)","Flow Direction","Velocity (m/s)","Flow Rate (m³/s)"]];
solved.forEach((solution,si)=>solution.branches.forEach((b,pi)=>dataset.push([
  `Set ${si+1}`, `Pipe ${pi+1}`, scenarios[si].d[pi], scenarios[si].l[pi], scenarios[si].f[pi], scenarios[si].h[pi],
  solution.hj, b.direction, b.velocity, b.flow,
])));

const directionByPipe = [0,1,2].map(pi => new Set(solved.map(s=>s.branches[pi].direction)));
if (directionByPipe.some(set => set.size < 2)) throw new Error("Every pipe must vary direction across scenarios");
for (let i=0;i<solved.length;i++) {
  if (Math.abs(solved[i].net) > 1e-10) throw new Error(`Unbalanced scenario ${i+1}`);
}

function styleBox(sheet, titleRange, promptRange, answerRange, title, prompt) {
  sheet.mergeCells(titleRange);
  sheet.mergeCells(promptRange);
  sheet.mergeCells(answerRange);
  const titleCell = sheet.getRange(titleRange.split(":")[0]);
  titleCell.values = [[title]];
  sheet.getRange(titleRange).format = {
    fill: "#1F4E78", font: { name: "Arial", bold: true, color: "#FFFFFF" },
    horizontalAlignment: "left", verticalAlignment: "center",
    borders: { preset: "outside", style: "thin", color: "#1F1F1F" },
  };
  const promptCell = sheet.getRange(promptRange.split(":")[0]);
  promptCell.values = [[prompt]];
  sheet.getRange(promptRange).format = {
    fill: "#D9EAF7", font: { name: "Arial", color: "#1F1F1F" }, wrapText: true,
    verticalAlignment: "top", borders: { preset: "outside", style: "thin", color: "#7F8C8D" },
  };
  sheet.getRange(answerRange).format = {
    fill: "#FFF2CC", font: { name: "Arial", color: "#1F1F1F" }, wrapText: true,
    verticalAlignment: "top", borders: { preset: "outside", style: "thin", color: "#7F8C8D" },
  };
}

async function open(name) {
  return SpreadsheetFile.importXlsx(await FileBlob.load(path.join(base,name)));
}
async function save(wb,name) {
  const blob=await SpreadsheetFile.exportXlsx(wb);
  await blob.save(path.join(outDir,name));
}

// Pre-class workbook: remove the pre-solved positive root.
{
  const name="(Starter-Workbook)-Pre-Pivot-GoalSeek-DataV.xlsx";
  const wb=await open(name);
  const fishing=wb.worksheets.getItem("Fishing");
  fishing.getRange("E25").values=[[0]];
  const pivot=wb.worksheets.getItem("PivotTable");
  styleBox(pivot,"A1:F1","A2:F3","A4:F4","PivotTable check","Which sales representative and product combination has the greatest total sales?");
  pivot.getRange("A1:F4").format.rowHeight=24;
  await save(wb,name);
}

// Class workbook: clarify the fourth validation field and add an observation box.
{
  const name="(Starter-Workbook)-Class-Pivot-GoalSeek-DataV.xlsx";
  const wb=await open(name);
  const validation=wb.worksheets.getItem("Data Validation");
  validation.getRange("D10").values=[["Discount Rate"]];
  validation.getRange("D11:D23").format.numberFormat="0%";
  const pivot=wb.worksheets.getItem("Pivot Table");
  styleBox(pivot,"A1:H1","A2:H3","A4:H5","PivotTable observation","After comparing Department in Rows and Columns, describe one pattern in job counts or average salaries.");
  pivot.getRange("A1:H5").format.rowHeight=24;
  await save(wb,name);
}

// Homework workbook: corrected source data and labeled response areas.
{
  const name="(Starter-Workbook)-HW-Pivot-GoalSeek-DataV.xlsx";
  const wb=await open(name);
  const problem=wb.worksheets.getItem("Three Reservoir Problem");
  problem.getRange("B4").values=[["Gravity, g (m/s²)"]];
  problem.getRange("B5").values=[["Junction head, Hj (m)"]];
  problem.getRange("B10").values=[["Darcy friction factor, f"]];
  problem.getRange("B14").values=[["Q (m³/s)"]];
  problem.getRange("B16").values=[["Net flow, Qj (m³/s)"]];
  problem.mergeCells("A18:E18");
  problem.getRange("A18").values=[["Goal Seek record"]];
  problem.getRange("A18:E18").format={fill:"#1F4E78",font:{name:"Arial",bold:true,color:"#FFFFFF"},borders:{preset:"outside",style:"thin",color:"#1F1F1F"}};
  problem.mergeCells("A19:E19");
  problem.getRange("A19").values=[["Enter the three Goal Seek settings, then record the result and final net flow."]];
  problem.getRange("A19:E19").format={fill:"#D9EAF7",font:{name:"Arial"},wrapText:true,borders:{preset:"outside",style:"thin",color:"#7F8C8D"}};
  problem.getRange("A21:E23").values=[
    ["Set Cell",null,"To Value",null,null],
    ["By Changing Cell",null,"Solved Hj (m)",null,null],
    ["Final Qj (m³/s)",null,null,null,null],
  ];
  problem.getRange("A21:E23").format.font={name:"Arial"};
  problem.getRange("A21:E23").format.borders={preset:"all",style:"thin",color:"#7F8C8D"};
  problem.getRange("B21:B23").format.fill="#FFF2CC";
  problem.getRange("D21:D22").format.fill="#FFF2CC";
  problem.getRange("B23:E23").format.fill="#FFF2CC";
  problem.mergeCells("B23:E23");
  problem.getRange("A18:E23").format.autofitRows();

  const flow=wb.worksheets.getItem("Reservoir Flow");
  flow.getRange("A1:J31").values=dataset;
  flow.getRange("C2:C31").format.numberFormat="0.000";
  flow.getRange("D2:D31").format.numberFormat="0";
  flow.getRange("E2:E31").format.numberFormat="0.000";
  flow.getRange("F2:G31").format.numberFormat="0.000";
  flow.getRange("I2:I31").format.numberFormat="0.000";
  flow.getRange("J2:J31").format.numberFormat="0.00000";
  flow.getRange("A1:J31").format.autofitColumns();

  const pivot=wb.worksheets.getItem("PivotTable");
  styleBox(pivot,"A1:E1","A2:E3","A4:E6","Part 2 observation","Describe what this dataset shows about average flow rate or velocity for inflow and outflow.");
  styleBox(pivot,"G1:K1","G2:K3","G4:K6","Part 3 observation","Describe one relationship or pattern shown by your personal PivotTable.");
  pivot.getRange("A1:K6").format.rowHeight=24;
  await save(wb,name);
}

console.log(JSON.stringify({
  outputs:[
    "(Starter-Workbook)-Pre-Pivot-GoalSeek-DataV.xlsx",
    "(Starter-Workbook)-Class-Pivot-GoalSeek-DataV.xlsx",
    "(Starter-Workbook)-HW-Pivot-GoalSeek-DataV.xlsx",
  ],
  scenarios: solved.map((s,i)=>({set:i+1,hj:Number(s.hj.toFixed(6)),net:s.net,directions:s.branches.map(b=>b.direction)})),
},null,2));

const renderJobs = [
  ["(Starter-Workbook)-Pre-Pivot-GoalSeek-DataV.xlsx", "Fishing"],
  ["(Starter-Workbook)-Pre-Pivot-GoalSeek-DataV.xlsx", "PivotTable"],
  ["(Starter-Workbook)-Class-Pivot-GoalSeek-DataV.xlsx", "Data Validation"],
  ["(Starter-Workbook)-Class-Pivot-GoalSeek-DataV.xlsx", "Pivot Table"],
  ["(Starter-Workbook)-HW-Pivot-GoalSeek-DataV.xlsx", "Three Reservoir Problem"],
  ["(Starter-Workbook)-HW-Pivot-GoalSeek-DataV.xlsx", "Reservoir Flow"],
  ["(Starter-Workbook)-HW-Pivot-GoalSeek-DataV.xlsx", "PivotTable"],
];
const renderDir=path.join(outDir,"renders");
await fs.mkdir(renderDir,{recursive:true});
for(const [name,sheetName] of renderJobs){
  const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(path.join(outDir,name)));
  const rendered=await wb.render({sheetName,autoCrop:"all",scale:1,format:"png"});
  const short=name.includes("Pre-")?"pre":name.includes("Class-")?"class":"hw";
  await fs.writeFile(path.join(renderDir,`${short}_${sheetName.replaceAll(" ","_")}.png`),new Uint8Array(await rendered.arrayBuffer()));
}
