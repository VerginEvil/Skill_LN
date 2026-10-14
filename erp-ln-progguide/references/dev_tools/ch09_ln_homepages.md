# Chapter 9: LN Homepages

## Homepages introduction

## Introduction

Infor delivers various predefined homepages with LN, such as the following:
- Sales Administrator homepage.
- Accounts Payable Administrator homepage.
- Accounting Manager homepage.
- Service Coordinator homepage.
Homepages are used as a start point for navigation for particular roles, such as Warehouse Manager
or Warehouse Administrator. A homepage automatically preselects all the work a user must do in LN.
Each homepage contains various dockable panels that can show HTML content. The homepage functions
as an up-to-date dashboard on performance and workload.
> [!NOTE]
Homepages are only available in Web UI.
## Homepage structure

A homepage consists of multiple panes such as the following.
A homepage delivered by Infor usually consists of the following panes, but this is not mandatory:
Alert pane
Displays the alerts (if any).
Examples of alerts are:
- Orders that have passed the due date.
- Late receipts.
- Orders that are not released yet.
- A price variance that falls outside the tolerance.
Alerts are linked to conditions. An Alert is only displayed if the corresponding condition is met.
Workload pane
Displays the workload assigned to a specific record,
for example a specific buyer.
The Workload pane in the previous figure shows
the tasks that you must perform for a specific buyer:
- There are purchase orders waiting for ap-
- A number of purchase orders must be con-
- There are no requisitions that must be pro-
- And so on.
proval.
firmed.
cessed.
When you double-click a task, the corresponding
(overview) session starts. For example, when you
double-click the Unapproved Orders task, the Purchase Orders (tdpur4100m000) session starts.
Shortcut pane (Quick Links pane)
Displays useful quick links.
A quick link is a shortcut to a details (data entry)
session, or to a batch session, for example a global
update session.
Report pane
Contains hyperlinks to frequently used reports. The
hyperlinks can start LN sessions or Web pages, for
example Cognos reports.
Graph pane
Displays reports that show major statistics or key
performance indicators. The reports offer many
useful features, such as:
- Many chart types are supported, for example
- A graph can have a dialog attached, where
pie charts, line charts, and bar charts.
you can enter selection criteria.
Resource files
The language-dependent content of an LN homepage, such as the homepage's title and the titles of the
panes used in the homepage, is stored in resource files.
Each resource file contains data for only one language. The homepages and reports developed by Infor
are delivered with English resource files. To run these homepages and reports in other languages, you
must translate the corresponding resource files.
For more information, refer to To translate resource files (p. 199) .
Personalization by Web UI end users
To change the look and feel of their homepages, end users can do the following:
- Move and dock panels in different locations.
- Resize, minimize, and maximize panels.
- Drag items to another position within the Work Load pane, the Alert pane, and the Shortcut
- Add new shortcuts.
- Switch between large and small icons.
- Personalize the Work Load pane and Alert pane: For example, an end user can define
pane.
thresholds. A Web UI administrator can also specify refresh rates.
For more information, refer to the Web UI online help.
## To create LN homepages

## Prerequisites

To create homepages, one of the following must apply:
- You must be a Web UI administrator.
- Your Web UI user profile must have the “homepage creator” role assigned.
## To create homepages

To create a new homepage, complete the following steps:
Step 1: Create an empty homepage

1. Start the Web UI, and on the View menu, click Create Home Page. The Home Page Settings
dialog appears.
2. Enter the ID and title for the new homepage, and click OK. An empty homepage is displayed
in the Work Area.
Step 2: Add a Workload pane
To add a Work Load pane, right-click the homepage's title bar and on the shortcut menu click Add Work
Load Pane. A dialog appears, where you must enter the following properties for the pane.
Plugin
Use predefined Workload
From the list, select Infor ERP.
- If this check box is selected, you can select
one of the predefined workload functions delivered by Infor, from the list. The full name of
the selected function is displayed in the
Workload list field. For example, if you select
"Warehouse Manager Tasks" from the list, the
"owhinh0800.get.dashboard.workload.items"
function is selected and displayed in the
Workload list field.
- To select a workload function that is not predefined, such as an own workload function, clear
this check box. You must type the name of the
function in the Workload list field.
Title:
Enter a title for the pane.
Workload list
You can only access this field if the Use predefined
Workload check box is cleared.
Enter the name of the workload function; this function must be present on the LN server. For details
on the structure of workload functions, refer to To
create functions for LN homepages (p. 192) .
You must enter the function name in the following
format:
o<script or library that contains the
function>.<name of the function>
For example:
otdpurdll8500.get.dashboard.workload.
items
To save the settings and close the dialog, click OK.
Step 3: Add an Alert pane
To add an Alert pane, right-click the homepage's title bar and on the shortcut menu click Add Alert
Pane. A dialog appears, where you must enter the following properties for the pane.
Plugin
Use predefined Alert
From the list, select Infor ERP.
- To select one of the predefined alert functions
delivered by Infor, select this check box. The
full name of the selected function is displayed
in the Alert list field. For example, if you select
"Planner Alerts" from the list, the "ocpintdllhpage.get.planner.alerts" function is selected
and displayed in the Alert list field.
- To select an alert function that is not predefined, such as an own alert function, clear this
check box. You must type the name of the
function in the Alert list field.
Title:
Enter a title for the pane.
Alert list
You can only access this field if the Use predefined
Alert check box is cleared.
Enter the name of the alert function. This function
must be present on the LN server. For details on
the structure of alert functions, refer to To create
functions for LN homepages (p. 192) .
You must enter the function name in the following
format:
o<script or library that contains the
function>.<name of the function>
For example:
otdslsdll0801.get.dashboard.alerts
To save the settings and close the dialog, click OK.
Step 4: Add a Report pane
To add a Report pane, right-click the homepage's title bar and on the shortcut menu click Add Report
Pane. A dialog appears, where you must enter the following properties for the pane.
Plugin
Use predefined Report
From the list, select Infor ERP.
- To select one of the predefined report functions delivered by Infor, select this check box.
The full name of the selected function is displayed in the Report field. For example, if you
select "Processed Sales Orders" from the list,
the "otdslsdll0700.processed.orders.chart"
function is selected and displayed in the Report field.
- To select a report function that is not predefined, such as an own report function, clear
this check box. You must type the name of the
function in the Report field.
Title:
Enter a title for the pane.
Report
You can only access this field if the Use predefined
Report check box is cleared.
Enter the name of the report function; this function
must be present on the LN server. For details on
the structure of report functions, refer to To create
functions for LN homepages (p. 192) .
You must enter the function name in the following
format:
o<script or library that contains the
function>.<name of the function>
For example:
ocpintdllhpage.utilization.chart
To save the settings and close the dialog, click OK.
Step 5: Add a Shortcut pane
To add a shortcut pane, complete the following steps:

1. Right-click the homepage's title bar and on the shortcut menu click Add Shortcut Pane. A
dialog appears, where you must enter the ID and title for the pane.
2. To save the settings and close the dialog, click OK.
3. Add shortcuts to the new shortcut pane. To do this, complete the following steps:
- Right-click in the shortcut pane and, on the shortcut menu, click Add new Shortcut. A
- To save the settings and close the dialog, click OK.
dialog appears, where you can specify a shortcut to a Web Page, an LN Homepage, or
an LN session.
Step 6: Position the panes in the homepage
All panes you add are displayed as tabs in the Work Area, so you can only view one pane at a time.
Drag the panes to the homepage's title bar so they are displayed within the homepage. Move the panes
to the appropriate locations so you can view all panes in one glance. Resize the panes when necessary.
Step 7: Save the homepage
To save the homepage, right-click the homepage's title bar. On the shortcut menu, click Save Home
Page. Therefore, a shortcut to the homepage is displayed in the Home Pages panel.
## To create functions for LN homepages

## Introduction

When you create a homepage, you must create functions on the LN server, which contain the logic to
display the homepage's workload items, alerts, and so on.
To create a homepage function, complete the following steps:

1. Log on to the LN server.
2. Start the Program Scripts / Libraries (ttadv2530m000) session.
3. Either create a library and start the editor, or edit an existing library.
4. Add the function syntax to the library.
5. Save and compile the library.
You can now link the function to a homepage. For details, refer to To create LN homepages (p. 188) .
## Homepage function types

For descriptions and examples of the following homepage function types, see the following section:
- A function to display workload items.
- A function to display alerts.
- A count function.
- A function to start a session.
- A report item function.
Workload items function
Interface
function extern long <workloadFunction>(long i.node)
i.node has the following content:
<CompanyInfo>
<compnr> </compnr>
<logcompnr> </logcompnr>
<fincompnr> </fincompnr>
</CompanyInfo>
Always returns an XML node:
<WorkloadItems>
<Item>
<id> </id>
<label> </label> Label in personalize dialog
[<type> </type>] Long (could be extended in the future when there are requirements for it). If not
specified, not possible to filter
[<unit> </unit>] Only used for filter
<countFunction> </countFunction>
<sessionStartFunction> </sessionStartFunction>
[<supportCount> </supportCount>] default = false
[<supportAmount> </supportAmount>] default = false
[<additionalInfo> </additionalInfo>] xml node which is send back to the backend for the count and
start function to prevent additional reads.
</Item>
. . .
</WorkloadItems>
Example
function extern long get.dashboard.workload.items(long i.node)
{
long items
items = xmlNewNode("WorkloadItems")

< Add the Items >

return(items)
}
The items node could look like the following:
<WorkloadItems>
<Item>
<id>wl_1</id>
<label>Open Orders</label>
<countFunction>get.open.orders.count</countFunction>
<sessionStartFunction>start.open.orders</sessionStartFunction>
<supportCount>true</supportCount>
<supportAmount>false</supportAmount>
<additionalInfo>
<buyer>76300</buyer>
</additionalInfo>
</Item>
<Item>
<id>wl_2</id>
<label>Created Orders greater than</label>
<type>long</type>
<unit>Eur</unit>
<countFunction>get.create.orders.count</countFunction>
<sessionStartFunction>start.create.orders</sessionStartFunction>
<supportCount>true</supportCount>
<additionalInfo>
<buyer>76300</buyer>
</additionalInfo>
</Item>
</WorkloadItems>
Alerts function
Interface
function extern long <alertFunction>(long i.node)

i.node has the following content:
<CompanyInfo>
<compnr> </compnr>
<logcompnr> </logcompnr>
<fincompnr> </fincompnr>
</CompanyInfo>
Always returns an XML node:
<Alerts>
<Item>
<id> </id>
<label> </label> Label in personalize dialog
[<type> </type>] Long (could be extended in the future when there are requirements for it). If not
specified, not possible to filter
[<unit> </unit>] Only used for filter
<countFunction> </countFunction>
<sessionStartFunction> </sessionStartFunction>
[<supportCount> </supportCount>] default = false
[<supportAmount> </supportAmount>] default = false
[<additionalInfo> </additionalInfo>] xml node which is send back to the backend for the count and
start function to prevent additional reads.
</Item>
. . .
</Alerts>
Example
function extern long get.dashboard.alerts(long i.node)
{
long items
items = xmlNewNode("Alerts")

< Add the Items >

return(items)
}
The items node could look like the following:
<Alerts>
<Item>
<id>al_1</id>
<label>Open Orders</label>
<countFunction>get.open.orders.count</countFunction>
<sessionStartFunction>start.open.orders</sessionStartFunction>
<supportCount>true</supportCount>
<supportAmount>false</supportAmount>
</Item>
<Item>
<id>al_2</id>
<label>Late Orders</label>
<type>long</type>
<unit>days late</unit>
<countFunction>get.late.orders.count</countFunction>
<sessionStartFunction>start.late.orders</sessionStartFunction>
<supportCount>true</supportCount>
<imageLarge>td/ipu/bipuoutbox.gif</imageLarge>
<imageSmall>td/ipu/bipuoutbox_s.gif</imageSmall>
</Item>
</Alerts>
Count function
Interface
function extern void <countFunction >(long i.node)
i.node has the following content:
<Item>
<id> </id>
<compnr> </compnr>
<logcompnr> </logcompnr>
<fincompnr> </fincompnr>
[<amount> <amount>]   If a type is defined
[<additionalInfo> </additionalInfo>]
</Item>
Return always an XML node:
<Item>
<id> </id>
<description> </description>
[<count><count>]
[<amount><amount>]
[<amountDescription><amountDescription>]
</Item>
Example
function extern long get.create.orders.count(long i.node)
{
string id(5)
long amount
long infoNode
id = xmlDataElement$(i.node, "id", 0)
amount = xmlDataElement$(i.node, "amount", 0)
infoNode = xmlFindFirst("additionalInfo", i.node)

select . . .
. . .
return(node)
}
The node could look like the following:
<Item>
<id>wl_2</id>
<description>Orders greater than 100.000 Eur</description>
<count>5<count>
</Item>
Function to start a session
Interface
function extern void <sessionStartFunction>(long i.node)
i.node has the following content:
<Item>
<id> </id>
<compnr> </compnr>
<logcompnr> </logcompnr>
<fincompnr> </fincompnr>
[<amount> <amount>]   If a type is defined
[<additionalInfo> </additionalInfo>]
</Item>
The function does not return anything, but should start a session.
Example
function extern void start.create.orders(long i.node)
{
string id(5)
long amount
id = xmlDataElement$(i.node, "id", 0)
amount = xmlDataElement$(i.node, "amount", 0)
. . .
start.session(., .,  ., .)
}
The node could look like the following:
<Item>
<id>wl_2</id>
<amount>100000</amount>
</Item>
Report item function
Interface
function extern long <reportFunction>(long i.node)
i.node has the following content:
<CompanyInfo>
<compnr> </compnr>
<logcompnr> </logcompnr>
<fincompnr> </fincompnr>
</CompanyInfo>
Always returns an XML node:
<Report>
<design> </design> Name of the report design
[<parameterSession> </parameterSession>] Session to start to change the parameters by the end user
[<parameter
[name=’. . .’]  Attribute ‘name’ specifies the name of the parameter.
> </parameter>]* The value of each parameter should be specified.
</Report>
Example
function extern long purchased.order.amount.report(long i.node)
{
long node
. . .
return(node)
}
The node could look like the following:
<Report>
<design>Purchased Order Amount</design>
<parameterSession>gazzzreptest</parameterSession>
<parameter name=’Period Table’>MONTH</parameter>
<parameter name=’Start Date’>Jan 01, 2006</parameter>
<parameter name=’End Date’>Dec 31, 2006</parameter>
<parameter name=’Buyer’>jsmith</parameter>
<parameter name=’Default Currency’>EUR</parameter>
</Report>
At runtime this node creates the following link to the report:
... /run?__report=Report\Purchased Order Amount.rptdesign&Period Table=MONTH&Start Date=Jan 01,
2006&End Date=Dec 31, 2006&Buyer=jsmith&Default Currency=EUR
The user can click the link to display a graph. For an example, see the following figure:
When you have defined a parameter session for the report, a Parameters button is displayed. When
the user presses the button, the corresponding parameter session starts.
With the session you created, the user can change the parameters.
The parameter session is an LN session. Therefore, when developing this session, you have all LN
programming possibilities such as browsing and so on. In the choice.end.program section you must call
the send.parameters.to.report(…) function. This function requires the parameters specified as pairs,
with the name of the parameter followed by the value. See the following example:
choice.end.program:
before.choice:
send.parameters.to.report("Start Date", start.date, "End Date", end.date)
At runtime, this code results in a call to the backend. For example:
<RESPONSE>
<ARG NAME="callResult">
<callResult>
<SESSION ID="6-2" STATE="CLOSED">
<REPORTPARAMETERS>
<parameter NAME="Start Date">Jan 01, 2007</parameter>
<parameter NAME="End Date">Jan 31, 2007</parameter>
<processinfo>report_0</processinfo>
</REPORTPARAMETERS>
</SESSION>
</callResult>
</ARG>
</RESPONSE>
As a result of this call, the homepage does the following:
- Searches for the correct report and replaces the parameters with the new values. The values
- Refreshes the pane where the graph is displayed.
are only replaced for the parameters sent to the report. For parameters not sent to the report,
the values stay the same.
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
de.properties.
- To translate the file into French, rename the file to bwhwmdwarehousemanagerhomepage_
- To translate the file into Dutch, rename the file to bwhwmdwarehousemanagerhomepage_
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
