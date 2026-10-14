# Chapter 13: Query-based Reporting

## Query-based Reporting

In Reporting Studio you can develop query-based reports that read data from the LN database. A
query-based report only reads data; it does not perform any transactions or updates, and therefore
cannot be part of the business process.
Architecture
The following figure shows an architectural overview of the Reporting Studio and the Enterprise Server
runtime environment.
Query-based reporting architecture
Reporting Studio uses the Infor JDBC driver to connect to the LN query-based data source. The Infor
JDBC connector must be available on the development client machine. The JDBC connector uses the
JBDB API to connect to the LN database driver.
> [!NOTE]
- In LN, the report designs are stored in the Reports (ttadv330) table. The runtime files are
- When you run a report, Web UI downloads the report design to your machine.
stored in the report sources folder and have a ".rptdesign" filename extension.
Resource files
The report designs are language independent.
When you want to insert label and text elements in a report, you specify resource keys rather than static
text. The report design is linked to one or more resource files that contain the resource keys and their
values.
You can create resource files per ISO 639-1 language code and ISO 3166 country code.
In this way you can localize report titles, column headings, chart titles, and other static labels.
When you print a report, Web UI passes the locale to the Report Viewer. The locale of the machine is
not used. Therefore, when you create resource files, you must use the same language – country codes
as Web UI does.
When you print a report, the Report Viewer uses the locale passed by Web UI, the resource keys, and
resource files to find the appropriate text value to display.
See the following figure for an example.
Sample resource files
The figure shows the following elements:
- Resource files for English, German, French, and Dutch. Each file contains the resource key
- Report design. The design is linked to the resource files, and contains the resource key
- Report output when the report is run in the English, German, French, and Dutch locales.
"customer", and the corresponding localized text value.
"customer".
> [!NOTE]
- In LN, the resource files are stored in the Additional Files table (ttadv270). The runtime files
- When you run a report, Web UI downloads the locale-specific resource file to your machine.
are stored in the additional files folder and have a ".properties" filename extension.
Report libraries
Reporting Studio supports the use of shared report elements through libraries: You can create report
libraries that contain code you want to share in multiple reports, and link them to your query-based report
designs.
> [!NOTE]
- In LN, the report libraries are stored in the Reports (ttadv330) table. The runtime files are
- When you run a report, Web UI downloads the report libraries, which are linked to the report
stored in the report sources folder and have a ".rptlibrary" filename extension.
design, to your machine.
Setup
To set up query-based reporting, you must:

1. Create a report project. For details, refer to To create a report project (p. 207) .
2. Create query-based report designs. For details, refer to To create query-based reports (p. 222)
. When you design a report, you must also create the required resource files and libraries,
and link them to the report design. For details, refer to To create resource files (p. 228) and To
create report libraries (p. 230) .
3. Add the report to a Web UI homepage, or create a 4GL session and link the report to this
session. For details, refer to To create a print session for query-based reports (p. 232) .
Implementation
You can execute a query-based report from a Web UI homepage, and through a 4GL print session on
the LN server.
For details, refer to To run query-based reports (p. 234) .
## To create query-based reports

To create a query-based report, you must first define a new, empty, report on the LN server. Subsequently,
you must define the layout of the report in the Infor LN Reporting Studio.
To create a query-based report, complete the following steps:
Step 1: Create a report definition
To create an empty report definition, complete the following steps:

1. Start the Reports (ttadv3530m000) session. Ensure you select the correct development VRC
as your current package VRC.
2. Click New. The following question is displayed:
Start report generator?
3. Click No. The Reports (ttadv3130s000) details session starts.
4. Specify the module and report code and the description for the new report. In the Report Type
field, select "Query Based Report".
5. Save the new report and close the details session.
The generated report design is stored in the report sources folder and has a ".rptdesign" filename
extension.
Step 2: Transfer the report design to your client PC
Before you can edit a report design in Reporting Studio, you must transfer the report design to your
client PC. To do this, complete the following steps:

1. In the Reports (ttadv3530m000) session, complete one of the following steps:
- If SCM is active, select the report and click Check-Out. The report is checked out and the
- If SCM is not active, for example if LN runs on a Windows platform, select the report. Then,
Export/import file dialog is displayed.
on the appropriate menu, click Export RPT file.... The Export/import file dialog is
displayed.
2. In the Export to field, specify the destination directory and file name. The default export
destination is the ${BSE_TMP} directory on your client PC.
3. To transfer the report design, click Continue. The following message is displayed: Export
file successfully processed. To close the message window, click OK.
4. Close the Reports (ttadv3530m000) session.
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
An empty report layout is displayed in the editor area and report data is displayed in the Property Editor.
See the following figure for an example.
Step 6: Define a data source for the report
To define a data source, complete the following steps:

1. Go to the Data Explorer.
2. Right-click Data Sources and, on the shortcut menu, click New Data Source. The New Data
Source dialog is displayed.
3. Select Create from a data source type in the following list. Then select Infor BDB Data
Source and specify a data source name, such as "ERP". Then click Next. The Infor BDB
DataSource dialog is displayed.
4. Click Test Connection. If the "DB Connection Client" has been installed properly, the following
message is displayed :
Connection successful.
5. To remove the message, click OK. In the Infor BDB DataSource dialog, click Finish. The
Data Source to access the LN database has now been added to the report.
Step 7: Define a Data Set for the report
A data set is a query that specifies the data to retrieve from the data source.
To add a data set, complete the following steps:

1. Go to the Data Explorer.
2. Right-click Data Sets and, on the shortcut menu, click New Data Set. The New Data Set
dialog is displayed.
3. Specify an appropriate name for the data set, such as “Employees”, and select the new Data
Source. In the Data Set Type field, select Infor BDB Data Set. Then click Next. The BDB
DataSet Wizard starts.
4. In the left pane, use the appropriate package and module to navigate to the table for which
you want to define a query. To create a query, drag the table and one or more of its columns
from the left pane to the right pane. You can also manually edit the query in the right pane.
When the query is finished, click Finish. The Edit Data Set window is displayed.
5. Optionally, make additional changes to the data set. For details, in the window’s lower left
corner, click ?.
In the left pane, click Preview Results to display a preview of the data that will be retrieved
by the query.
When finished, click OK. The new data set is now ready to be used in the report.
Step 8: Define the Report Layout
In the report layout, you can add table columns and various other components, such as text, labels,
grids, images, charts, and crosstabs.
- To add a table column, in the Data Explorer, expand the data set and drag the column to the
- To add another component type, complete one of the following steps:
- On the Insert menu, click the desired component type.
- Right-click in the Editor area and, on the shortcut menu, click Insert. Then click the desired
- Go to the Palette and double-click the desired component type.
report layout.
component type.
Depending on the component type, a dialog may appear, where you must specify the properties
for the new component. For example, when you add a grid, you must specify the number of
columns and the number of rows.
- Note
- To display a preview of the report, click the Editor's Preview tab.
- Optionally, you can create resource files and report libraries, and link them to the report design.
When you select a component in the report layout, the component's properties are displayed
in the Property Editor. Here you can edit, for example, the font type, size and color.
For details, refer to To create resource files (p. 228) and To create report libraries (p. 230) .
For details on report editing, refer to the Reporting Studio documentation.
Sample report layout with grid, labels, table columns, and image
Step 9: Save and close the report
Click Save, and close the report layout in the editor area.
Step 10: Upload the report design into the LN data dictionary
To upload the report design into the data dictionary on the LN server, complete the following steps:

1. Start the Reports (ttadv3530m000) session.
2. Complete one of the following steps:
- If SCM is active, select the report concerned and click Check-In. The Export/import file
- If SCM is not active, select the report concerned and, on the appropriate menu, click
dialog is displayed.
Import RPT file.... The Export/import file dialog is displayed.
3. In the Import from field, specify the directory and file name of the exported/checked out report
design on your client PC.
4. To import the report design, click Continue. The following message is displayed:
Import successfully processed.
5. To remove the message window, click OK. If SCM is active, the following question is displayed:
Do you want to check in this Report?
6. Click Yes. A text editor starts. Then, to check-in the report, specify a revision text and close
the text editor.
7. Close the Reports (ttadv3530m000) session.
## To create resource files

To create a resource file, you must first create an initial, empty, resource file on the LN server.
Subsequently, you must complete the resource file in the Infor LN Reporting Studio.
To create a resource file:
Step 1: Create an initial resource file
To create an initial resource file, complete the following steps:

1. Start the Additional Files (ttadv2570m000) session. Ensure you select the correct development
VRC as your current package VRC.
2. Click New. The Additional File (ttadv2170s000) details session starts.
3. Enter the properties for the resource file:
- Enter the module code.
- In the Additional File field, enter the name of the new resource file. The name must have
the following structure: <filename>_<ISO 639 language code>_<ISO 3166
country code>.properties. For example: MyResource_en_US.properties.
Note: Use the same language – country codes as Web UI does.
- In the Additional File Description field, enter a description.
- Select the Editable check box.
4. Click Save. A message indicating the file does not yet exist is displayed. You are prompted
to create the file.
5. To create the file, click Yes. A text editor starts.
6. Close the text editor and do not enter any text.
7. Close the details session and overview session.
The initial resource file is stored in the additional files folder and has a ".properties" filename extension.
Step 2: Transfer the resource file to your client PC
Before you can edit a resource file in Reporting Studio, you must transfer the file to your client PC.
To transfer a resource file to your client PC, complete the following steps:

1. Start the Additional Files (ttadv2570m000) session.
2. Select the resource file and, on the appropriate menu, click Export RPT file.... The
Export/import RPT file dialog appears.
3. In the Export to field, enter the destination directory and file name. The default export
destination is the ${BSE_TMP} directory on your client PC.
4. Click Continue to transfer the resource file.
5. Import the resource file into the Eclipse workspace.
Step 3: Edit the resource file

1. Start Reporting Studio and open the resource file.
2. In the file, enter the resource keys and their values for the language and country concerned.
For details, refer to the Reporting Studio documentation.
Step 4: Upload the resource file into the LN data dictionary
When you have completed a resource file, you must upload the file into the data dictionary on the LN
server.
To upload a resource file, complete the following steps:

1. Start the Additional Files (ttadv2570m000) session.
2. Select the resource file concerned and, on the appropriate menu, click Import RPT file.... The
Export/import RPT file dialog appears.
3. In the Import from field, enter the directory and file name of the exported/checked-out resource
file on your client PC.
4. To import the resource file, click Continue.
## To link a resource file to a report design

To use the resources defined in a resource file, you must link the resource file to your reports. For details,
refer to the Reporting Studio documentation.
## To create report libraries

To create a report library, you must first create an initial report library on the LN server. Subsequently,
you must complete the new library in the Infor LN Reporting Studio. For details, see the procedure steps.
To create a report library:
Step 1: Create an initial report library
To create an initial report library:

1. Start the Reports (ttadv3530m000) session. Make sure you select the proper development
VRC as your current package VRC.
2. Click New. A question "Start report generator?" is displayed.
3. Click No. The Reports (ttadv3130s000) details session starts.
4. Enter the module and report code and the description for the new report library. In the Report
Type field, select "Report Library".
5. Save the new report library and close the details session.
The initial report library is stored in the report sources folder and has a ".rptlibrary" filename extension.
Step 2: Transfer the report library to your client PC
Before you can edit a report library in Reporting Studio, you must transfer the report library to your client
PC:
- If SCM is not active, for example if LN runs on a Windows platform, you must export the report
- If SCM is active, you must check out and export the report library before you can edit it.
library before you can edit it.
To transfer a report library to your client PC:

1. In the Reports (ttadv3530m000) session, take one of the following steps:
- If SCM is active, select the report library and click Check-Out.
- If SCM is not active, select the report library and, on the appropriate menu, click Export
RPT file....
The Export/import RPT file dialog appears.
2. In the Export to field, enter the destination directory and file name. The default export
destination is the ${BSE_TMP} directory on your client PC.
3. Click Continue to transfer the report library.
Step 3: Edit the report library
Start Reporting Studio and open the report library. Enter the desired code in the library. You can, for
example, define functions you want to share in multiple reports.
For details, refer to the Reporting Studio documentation.
Step 4: Upload the report library into the LN data dictionary
Once you have completed a report library, you must upload the report library into the data dictionary on
the LN server:
- If SCM is not active, you must import the report library on your LN server.
- If SCM is active, you must import and check in the report library.
To upload a report library:

1. Start the Reports (ttadv3530m000) session.
2. Take one of the following steps:
- If SCM is active, select the report library concerned and click Check-In.
- If SCM is not active, select the report library concerned and, on the appropriate menu,
click Import RPT file....
The Export/import RPT file dialog appears.
3. In the Import from field, enter the directory and file name of the exported/checked out report
library on your client PC.
4. Click Continue to import the report library.
5. If SCM is active, a question "Do you want to check in this Report?" is displayed. Click Yes
and enter a revision text to check in the report library.
## To link a report library to a report design

To share the functionality in a report library, you can link the library to multiple report designs. For details,
refer to the Reporting Studio documentation.
Example- code in a report design to link report libraries
The following code shows how the ChartDataFinal and GeneralFinal report libraries are linked to a report
design.
<list-property name="libraries">
<structure>
<property name="fileName">ChartDataFinal.rptlibrary</property>
<property name="namespace">ChartDataFinal</property>
</structure>
<structure>
<property name="fileName">GeneralFinal.rptlibrary</property>
<property name="namespace">GeneralFinal</property>
</structure>
</list-property>
## To create a print session for query-based reports

To create a print session that can print a query-based report, take the following steps:
Step 1: Define a print session

1. Start the Sessions (ttadv2500m000) session. Make sure you select the proper development
VRC as your current package VRC.
2. Click New. The Sessions (ttadv2100s000) details session starts.
3. Enter the module and session code and the description for the new session, and specify the
following session properties:
- Standard Script: No
- Generate Script: No
- Program Script: <The program script's code, consisting of package code, module code
- Main Table: <Empty>
- Session Type: Print
- Window Type: Dialog
- Main Session: Yes
- Synchronized Dialog: <Empty>
and the first 4 characters of the session code.>
For the other fields, use the default values.
4. Save the new session and close the Sessions (ttadv2100s000) details session.
5. In the Sessions (ttadv2500m000) overview session, click Compile.
Step 2: Link a query-based report to the session

1. In the Sessions (ttadv2500m000) session, select the new session and, on the appropriate
menu, click Reports.... The Reports (ttadv3530m000) session starts.
2. Click New. The Add Report to Session (ttadv2112s000) session starts.
3. Enter the report group and the serial number. Select the desired report and click OK.
4. Save the changes and close the Reports (ttadv3530m000) session.
Step 3: Edit the session's UI script

1. In the Sessions (ttadv2500m000) session, select the new session and, on the appropriate
menu, click Program Scripts.... The Program Scripts / Libraries (ttadv2530m000) session
starts.
2. Select the script and click Edit / View Script .... The script editor starts.
3. Edit the script. For example:
- Declare the variables you want to use as input fields on the session's form. Note: the
- Define defaults for the input fields on the form.
variable names must be identical to the variable names you defined in the Reporting
Studio.
See the following sample UI script.
4. Save the script and close the editor.
5. Compile the script and close the Program Scripts / Libraries (ttadv2530m000) session.
Sample UI script:
declaration:
extern domain ttaad.pacc  pack_from fixed
extern domain ttaad.pacc  pack_to  fixed
extern domain ttyeno  incl_pack | print packages y/n
|**************************** field sections ***********************************
field.pacc_from:
before.zoom:
ttaad120.pacc = ""
when.field.changes:
pack_to = pack_from
display("pack_to")     |#icc2.6.n
field.pacc_to:
before.zoom:
ttaad120.pacc = pack_from
The sample script belongs to a session that prints the package combinations, and optionally, the
corresponding package VRCs. Points of attention:
- The pack_from and pack_to variables are used as input fields in the form, to enter the selection
range. In the report design in Reporting Studio, pack_from and pack_to are mapped to
parameters "1" and "2" that are used in the query's between statement ( between :1 and
:2).
- The incl_pack variable is used as an input field on the form. The value entered by the user
(Yes or No) determines whether the packages are printed. In Reporting Studio, the incl_pack
variable is used in a print condition. Based on the value of incl_pack, the detail that contains
the package VRCs is printed or suppressed.
Step 4: Design the session's form

1. In the Sessions (ttadv2500m000) session, select the new session and click Edit Form .... The
Dynamic Form Editor starts.
2. Edit the form: Add form fields for the input variables you defined in the UI script, and customize
the structure of the form until it matches the requirements. See the following figure for an
example.
3. Save the form and close the editor.
4. In the Sessions (ttadv2500m000) session, click Compile.
Sample form
## To run query-based reports

You can run a query-based report in 2 ways:
- From a Web UI homepage.
- Through a 4GL print session on the LN server.
To run a query-based report from a Web UI homepage
To run a query-based report from a Web UI homepage:

1. Start Web UI and log on to your LN server.
2. Open the homepage that contains the report you want to run. The report is displayed in the
LN Report Viewer.
For details on homepages, refer to the Web UI online help.
To run a query-based report through a 4GL print session
To run a query-based report through a 4GL print session:

1. Start Web UI and log on to your LN server.
2. Start the print session to which the report is linked.
3. Enter any selection ranges and print options, and click Print.
- If only one report is linked to the session, the report is displayed in the LN Report Viewer.
- If multiple reports are linked to the session, you must first select the desired report from
a list.
> [!NOTE]
The LN Report Viewer only works in combination with Web UI. Worktop users cannot print Report Viewer
enabled reports.
From the Report Viewer, you can send a report to, among other things, a printer or a PDF file. For details,
refer to To use the Report Viewer (p. 208) .
### To translate resource files

Resource files contain language-dependent content of LN homepages and query-based reports. Each
resource file belongs to a particular homepage or query-based report. For example:
- A resource file linked to a homepage, contains the homepage's title and the titles of the panes
- A resource file linked to a query-based report contains the report title, column headings, chart
used in the homepage.
titles, and other static labels used in the report. For more information, refer to Query-based
Reporting (p. 219) .
> [!NOTE]
- Resource files do not contain language dependent LN content such as label and message
- Each resource file contains data for only one language. The homepages and reports developed
- When a user opens a homepage or report, Web UI automatically downloads the corresponding
descriptions.
by Infor are delivered with English resource files. To run these homepages and reports in
other languages, you must translate the corresponding resource files.
resource file from the LN server. Web UI automatically selects the resource file that corresponds
to the user's language, as defined in the User Data (ttaad2500m000) session, so that the
homepage or report is displayed in the user's own language. If there is no resource file for the
user's language, Web UI downloads the original (English) resource file delivered with the
homepage.
### To translate resource files

To translate a resource file, complete the following steps:
Step 1: Export resource files

1. Start the Export Resource Files (ttadv8913m000) session.
2. Enter the required settings and export the resource files to a directory on the LN server. The
session generates an ASCII file for each exported resource file.
Step 2: Rename ASCII files
The names of the generated ASCII files have the following structure:
<filename>_<ISO 639 language code>_<ISO 3166 country code>.properties
> [!NOTE]
- The country code is optional and used for only a few languages.
- The language code of a report's resource file must be identical to the language code of the
resource file of the homepage to which the report is linked. For details, refer to the Infor Web
UI - Installation and Configuration Guide (U8715 US).
Rename the ASCII files so they match the target language code and optionally the target country code.
Ensure you use the correct ISO codes, because otherwise the Web UI cannot read the resource file at
runtime.
For example, the Export Resource Files (ttadv8913m000) session has generated the following ASCII
file: bwhwmdwarehousemanagerhomepage_en.properties.
- To translate the file into German, rename the file to bwhwmdwarehousemanagerhomepage_
- To translate the file into French, rename the file to bwhwmdwarehousemanagerhomepage_
- To translate the file into Dutch, rename the file to bwhwmdwarehousemanagerhomepage_
de.properties.
fr.properties.
nl.properties.
Step 3: Translate content of ASCII files
The ASCII files consist of lines with the following structure: resource ID=resource description.
For example, the bwhwmdwarehousemanagerhomepage_en.properties file contains the following
lines:
warehousemanagerhomepage.whinh2400m000=Warehouse Orders
warehousemanagerhomepage.whinh2100m000=Warehouse Orders
warehousemanagerhomepage.whinh4130m000=Create Shipments
warehousemanagerhomepage.workload=Warehouse Manager Tasks
warehousemanagerhomepage.Warehouse_Orders=Warehouse Orders
warehousemanagerhomepage.whinr1400m000=Inventory Transactions
warehousemanagerhomepage.whina1210m000=Inventory Valuation
Translate the resource descriptions in the ASCII files (the text behind the "=" in each line) to the target
language.
Step 4: Import resource files

1. Start the Import Resource Files (ttadv8923m000) session.
2. Enter the required settings and import the translated ASCII files into a VRC in the LN
environment.
