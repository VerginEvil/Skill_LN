# Chapter 10: LN Reporting Overview

## LN Reporting Overview

LN supports the following report types:
- 4GL reports
- Report Viewer enabled reports
See the following sections for details.
## 4GL reports

Most reports in LN are 4GL reports. These reports consist of a layout part and, optionally, a report script.
The layout part usually consists of multiple report layouts, such as a header, a before.field and a detail.
You can edit these report layouts in the 4GL Report Editor. This editor has an ASCII user interface and
does not support advanced features, such as charts and (animated) gif files.
4GL Report in LN 4GL Report Editor
When you finished a 4GL report, you must compile the report. The compiler generates a report object
in the runtime data dictionary.
You can print the 4GL reports to different device types, such as a printer, a file, or your own display.
The reports generate a fixed font output.
For details on 4GL reports, refer to:
- Reports (p. 42)
- "Report Script Features" in the Infor ES Programmer's Guide
> [!NOTE]
You can convert 4GL reports to XML report designs. Subsequently, you can enhance the report designs
in the Infor LN Reporting Studio. For more information, refer to Session-based Reporting (p. 213)
## Report Viewer enabled reports

LN also supports Report Viewer enabled reports. You can edit these reports in the Reporting Studio
Report Designer. When printed, these reports are displayed in the LN Report Viewer.
The Reporting Studio Report Designer offers various useful features. For example, you can:
- Add various chart types to your reports, for example pie charts, line charts, and bar charts.
- Attach a dialog to a graph, where users can enter selection criteria.
- Create crosstab reports that show data in two dimensions, for example: sales per quarter.
For details on the Reporting Studio Report Designer, refer to the Reporting Studio online help.
Report Preview in Reporting Studio Report Designer
Report in Reporting Studio Report Designer
In the runtime data dictionary, the report designs are stored in XML files with a ".rptdesign" filename
extension.
> [!NOTE]
The LN Report Viewer only works in combination with Web UI. Worktop users cannot print Report Viewer
enabled reports.
From the Report Viewer, you can send a report to, among other things, a printer or a PDF file. For details,
refer to To use the Report Viewer (p. 208) .
Report Viewer enabled reports are created in a report project. For details, refer to To create a report
project (p. 207) .
Report types
You can create 2 types of Report Viewer enabled reports:
- Session-based reports. For details , refer to Session-based Reporting (p. 213) .
- Query-based reports. For details , refer to Query-based Reporting (p. 219) .
## To create a report project

Before you can create Report Viewer enabled reports, you must first create a report project.
To create a report project, complete the following steps:

1. Start the Reporting Studio.
2. On the File menu, click New. Then click Project. The New Project dialog starts.
3. In the Wizards pane, expand the Business Intelligence and Reporting Tools folder and
select Report Project.
4. Click Next. The New Report Project wizard starts.
5. Specify the name of the project, such as LN, and define the location to store the project's files.
The Location property is optional and maps to the directory structure in the file system in
which the project and the project's resources are stored.
If you select the Use default location check box, the Eclipse workspace is used as the root
directory for the project. To create the project and the project's related resources in a different
location, clear the Use default location check box and specify the new location.
6. Click Finish.
The project is displayed in the Navigator view. See the following figure for an example.
## To use the Report Viewer

The Report Viewer is used to display session-based and query-based reports.
In the Report Viewer you can perform the following actions:
- Navigate through the report data.
- Export report data.
- Print the report.
For details, refer to the descriptions of the toolbar buttons.
### Toolbar buttons

The following toolbar buttons are available.
Button
Name
Description
Export data
Starts the Export Data dialog,
where you can select report
columns and meta data, such as
layout names and data types, to
be exported. The data is exported
in csv (Comma Separated Values)
format. You can store the data in
a file or view it directly, for example in MS Excel.
Export report
Starts the Export Report dialog,
where you can select the following:
- The output format: Excel,
- The pages to export.
- The report size.
PostScript, PDF, Word, or
PowerPoint.
You can store the data in a file or
view it directly.
Print report
Starts the Print Report dialog,
where you can select the following:
- The output format: HTML or
- The report size (only for
- The pages to export.
PDF.
PDF).
The output is displayed in a print
preview window. If you selected
HTML, you are automatically
prompted to select a printer. If you
selected PDF, click Print to print
the output.
First page
Navigates to the first page.
Previous page
Navigates to the previous page.
Next page
Navigates to the next page.
Last page
Navigates to the last page.
Go to
Navigates to the page specified in
the Go to page field.
