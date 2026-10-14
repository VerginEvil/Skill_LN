# Chapter 11: 4GL Reports

## 4GL Reports Overview

LN 4GL reports are used to output data from the database to a variety of devices (for example, printers,
displays, and files).
One or more LN 4GL reports must be linked either to an LN print session or to an LN SQL Query. The
print session or SQL Query reads the data from the Database tables and the data will be printed by the
Report objects.
4GL reports can automatically generated on two ways:
- By creating a Print session
- By creating a SQL Query
- Before.report
- Header
- Before.field
- Detail
- After.field
- Footer
- After.report
LN 4GL reports contain one or more of the following layouts:
The contents and layouts of 4GL reports are defined in the data dictionary. In addition, you can link a
report script to a report. In a report script, you can program actions that you want to be performed at
particular stages of the report execution. For example, you can create a script to perform calculations
on the report data or to read records from related tables that are not automatically available to the report.
You program report scripts in the same way as you program 4GL program scripts, except that report
scripts use different event sections and some special functions.
A report script consists of one or more event sections in which you program actions to be performed at
particular states of execution of the report to which the report script is linked. The statements programmed
in a report script section consist of a combination of 3GL language statements and report script functions.
Report scripts support the following event sections:
- program sections
- report sections
- text field sections
- declaration
- before.program
- after.program
- after.receive.data
- functions
- before.report
- after.report
- header
- footer
- before.field
- after.field
- detail
The following program sections can be used:
The following report sections can be used:
> [!NOTE]
Report sections consist of a main section and a subsection. You use a main section to specify the
particular layout for which the programmed actions are to be executed. You must follow a main section
with either a before.layout or an after.layout subsection. These latter specify whether the actions are
to be executed before or after the particular layout is printed.
The following Special Report functions can be used in a Report script:
- layout.again()
- need( expr )
- page()
- reset.suppress()
- skip( expr )
- skip.to( expr )
- to.page( expr )
For details on Report scripts, refer to "Report Script Features" in the Infor ES Programmer's Guide.
