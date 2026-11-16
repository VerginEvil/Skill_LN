# Chapter 12: Session-based Reporting

## Session-based Reporting

You can convert existing 4GL reports to a report design in XML format, so that the report becomes
Report Viewer enabled. You can customize the layout of the converted report in the Reporting Studio.
To print the report, run the corresponding print session on the LN server, and send the output to a Report
Viewer device. All business logic defined in the session and the original 4GL report is executed, therefore,
a session-based report can be part of the business process. For example, the report can perform
transactions in the database, or change the status of a record.
Setup
To set up session-based reporting, you must:

1. Create a report project. For details, refer to To create a report project (p. 207) .
2. Create session-based report designs. For details, refer to To create session-based reports
(p. 213) in this chapter.
3. Create a Report Viewer device. For details, refer to To create a Report Viewer device for
session-based reports (p. 217) in this chapter.
Execution
For information on how to run session-based reports, refer to To run session-based reports (p. 218)
## To create session-based reports

To create session-based reports that are Report Viewer enabled, you must convert existing 4GL reports
to XML report designs. Subsequently, you can enhance the report designs in the Infor LN Reporting
Studio. For details, see the procedure steps.
To create a session-based report, complete the following steps:
Step 1: Convert the report to an XML report design
Start the Enable Reports for RPT Design (ttadv3241m000) session. Specify the required information
and click Convert.
For details, see the session help.
The generated report designs are stored in the report sources folder and have a ".rptdesign" filename
extension.
Note: the following steps are optional. Only perform these steps if you want to customize the report
design in Reporting Studio.
Step 2: Transfer the report design to your client PC
Before you can edit a report design in Reporting Studio, you must transfer the report design to your
client PC. To do this, complete the following steps:

1. Start the Reports (ttadv3530m000) session.
2. Select the report and, on the appropriate menu, click Export RPT file.... The Export/import
file dialog is displayed.
3. In the Export to field, specify the destination directory and file name. The default export
destination is the ${BSE_TMP} directory on your client PC.
4. To transfer the report design, click Continue. The following message is displayed: Export
file successfully processed. To close the message window, click OK.
5. Close the Reports (ttadv3530m000) session.
Step 3: Start the Reporting Studio
To start the Reporting Studio, run the eclipse.exe executable in the eclipse subdirectory in the
Reporting Studio installation directory.
For example, run C:\Infor\ERP\ReportingStudio\eclipse\eclipse.exe.
Step 4: Import the report into a report project
To import the report, complete the following steps:

1. In the Navigator, right-click the report project and, on the shortcut menu, click Import.
Alternatively, on the File menu, click Import. The Import wizard's Select dialog starts.
Note If there is no report project, you must first create one. For details, refer to To create a
report project (p. 207) .
2. In the Select an import source pane, expand the General folder and select File System.
Then click Next. The File system page is displayed.
3. Specify the location where the report design you want to import is stored. To do this, click the
Browse... button next to the From directory field. Note Select the directory specified during
the check out/export of the report, such as the ${BSE_TMP} directory on your client PC.
In the right-hand pane, the wizard displays all files from the selected directory. Report designs
have a ".rptdesign" filename extension. Select the report design you want to import.
4. In the Into folder field, specify the report project into which you want to import the report
design. To select the appropriate project, click Browse....
5. Select Create selected folders only.
6. Click Finish.
The report design is now displayed in the Navigator.
Step 5: Open the report design
To open the report design, go to the Navigator and double-click the report design. Alternatively, select
the report design and, on the shortcut menu, click Open.
The report layout is displayed in the editor area and report data is displayed in the Property Editor.
This diagram shows an example:
Step 6: Customize the report design
Beautify the layout of the report. For example, you can add a graph or company logo.
You can add charts and images through the Insert menu, the report editor's shortcut menu, and the
Palette.
When you select a component in the report layout, the component's properties are displayed in the
Property Editor. Here you can edit, for example, the font type, size and color.
> [!IMPORTANT]
- Only use Reporting Studio to beautify the layout of the report. For example, you can add a
graph or a company logo.
- To change the structure of the report, for example to add layouts, input fields, or labels, use
the classic report editor. For details, refer to To edit reports (p. 103) .
Step 7: Save and close the report
Click Save, and close the report layout in the editor area.
Step 8: Upload the report design into the LN data dictionary
To upload the report design into the data dictionary on the LN server, complete the following steps:

1. Start the Reports (ttadv3530m000) session.
2. Select the report concerned and, on the appropriate menu, click Import RPT file.... The
Export/import file dialog is displayed.
3. In the Import from field, specify the directory and file name of the exported report design on
your client PC.
4. To import the report design, click Continue. This message is displayed:
Import successfully processed.
5. To remove the message window, click OK.
6. Close the Reports (ttadv3530m000) session.
> [!IMPORTANT]
If you install a solution for a customized report, all changes made in Reporting Studio will be lost.
To create a Report Viewer device for session-based
reports
To print session-based reports, you need a device that sends the report output to the LN Report Viewer.
To create a Report Viewer device, complete the following steps:

1. Start the Device Data (ttaad3500m000) overview session.
2. To add a new device, click New. The Device Data (ttaad3100s000) details session starts.
3. Enter the properties for the new device. Points of attention are as follows:
- Device: RPT
- Description: Report Viewer
- Device Type: Rewrite File
- Locale: <empty>
- Intermediate File in XML Format: Yes
- Driver: <empty>
- Shell Command: <empty>
- 4GL Program: <empty>
- Argument: XML -RPT
- Path: ${HOME}/rpt
4. Save the new device and close the sessions.
## To run session-based reports

This section describes how to print a session-based report to the LN Report Viewer.
To print a session-based report to the LN Report Viewer, complete the following steps:

1. Start Web UI and log onto your LN server.
2. Start the print session to which the report is linked.
3. Enter the required selection ranges and print options, and click Print. The Select Device
(ttstpsplopen ) session starts.
4. Select a Report Viewer device and click Continue.
> [!NOTE]
The LN Report Viewer only works with Web UI. Worktop users cannot print Report Viewer enabled
reports.
From the Report Viewer, you can send a report to, among other things, a printer or a PDF file. For details,
refer to To use the Report Viewer (p. 208) .
