# Customer Defined Fields

Tailoring is adding functionality to existing components. Tailoring includes the concept of Customer Defined Fields (CDFs).

Those fields can be added to tables, screens, reports, BODs, BDEs, and REST APIs and validation and calculation logic can be defined around those fields.

Use the Customer Defined Fields (CDF) concept to store additional data in the standard Infor LN tables. The CDF definitions are stored separately from the table definitions in the Data Dictionary. For the end user, the CDFs behave in the same way as the standard fields, if defaulting, validations, etc. are built using the CDF logic of the table extension point. The session extension point also has features for the CDFs.

See Customer defined field logic and Customer Defined Field.

CDFs are configured per package combination. This implies that when moving your companies from one package combination to another, the CDF definitions must be present in the target package combination. Otherwise you lose the data in the CDFs.

New export and import procedure

From Enterprise Server 10.6.0.1, PMC is used to export and import CDFs through extensions.

See Exporting and importing CDFs through PMC on page 19.

Old export and import procedure

The old procedure to export and import CDFs should only be used to copy CDF definitions from or to LN 10.5 and older LN versions. In the old procedure, these sessions are used:

- Export Customer Defined Fields (ttadv4291m000)

- Import Customer Defined Fields (ttadv4292m000)

See Exporting and importing CDFs through ttadv4291m000 and ttadv4292m000 on page 20.

## CDF types

CDFs can be defined with standard domains, or your own domains that you can create with LN Studio. If you do not use a standard or own domain, the CDFs are added to the table with an implicit domain that is dependent on the data type. This table shows the supported data types:

| Data Type | Remark | Implicit Domain |
|---|---|---|
| String | Multibyte string, length between 1 <pk>cdf___str<lll> (3 underscores) and 999; default length is 30 |  |
| Integer | Integer number (long) | <pk>cdf______int (6 underscores, for integers with 10 positions and format ZZZZZZZZZ9) |

<pk>cdf____i<ll><ss> (4 underscores)

Numeric Numeric number (double) <pk>cdf______num (6 underscores, for doubles with 9 digits before and 5 digits after decimal point and format ZZZZZZZZ9VD99999) <pk>cdf__n<bb><aa><ss> (2 underscores)

Date Date/Time, local time on screen, <pk>cdf______dat (6 underscores, for dates with stored as UTC format %u001 %U001) <pk>cdf______u<ss>, 6 underscores)

Checkbox true or false <pk>cdf______chk (6 underscores)

List A predefined list of choices <pk>cdf_lst<list> (1 underscore)

Text Text field <pk>cdf______txt (6 underscores)

Explanation for the domain codes:

- <pk> the package code of the table to which the CDF is added

- <ll[l]> length of the string or integer

- <ss> sequence number, per format a different sequence number is generated

- <bb> digits before

- <aa> digits after

- <list> list code that holds the predefined list of choices

The domain codes can be required during the development of the extensions with the Extension Modeler.

See Extension Modeler on page 21.

You can also add calculated CDFs; those are not physically stored in the table, but calculated based on other table fields and presented in the UI. This type of CDF is deprecated. We recommend that you use the Calculated Field extension type of the session extension point.

See Calculated Field on page 81

CDFs, except the calculated ones and text fields, can be defined with multiple elements (arrays).

## CDF Configuration

Go to Tools > Application Configuration for the sessions to define CDFs. To configure customer defined fields:

1 Start the Customer Defined Fields Parameters (ttadv4590m000) session. 2 Select CDF Active and click OK. 3 Define customer defined fields in one of these ways:

- Customer Defined Fields option in the Settings (gear icon) menu in a session you started Use the in LN UI.

- Customer Defined Fields (ttadv4591m000) session. Use the

- Lists To create customer defined fields of type ‘List’, specify the lists and their constants in the (ttadv4592m000) and List Constants (ttadv4593m000) sessions.

4 In the Customer Defined Fields (ttadv4591m000) session, click Actions and select Convert to Runtime. The Convert to Runtime Data Dictionary (ttadv5215m000) session starts. Convert the customer defined fields and the related implicit domains to the runtime data dictionary.

Note: Converting to runtime changes the physical structure of the LN tables. The users must be logged out from the system.

Infor Enterprise Server Administration Guide (Cloud)

## Exporting and importing CDFs through PMC

1 Ensure that a table extension exists. Alternatively, create an empty table extension for the tables that include the CDFs. See Table extension point on page 31.

2 Export or import the solutions that contain these table extensions through PMC. See Extension Deployment on page 161.

The old way of exporting and importing CDFs through ttadv4291m000 and ttadv4292m000 is still supported. CDFs that are imported with PMC are not overwritten with CDFs from ttadv4292m000.

If CDFs already exist on the system, they may be overwritten by PMC. If you then uninstall through PMC, the original CDFs are still available.

The “Customer Defined Fields” table has a new field: Origin (orig). This orig field is used to distinguish between CDFs that are manually created and CDFs that are imported through PMC. This field is displayed in the Customer Defined Fields session.

You can import a PMC solution for a table extension that did not exist before. If the same CDFs for that table already existed with origin “Manual”, they are restored if you perform an uninstall of this solution.

## Exporting and importing CDFs through ttadv4291m000

## and ttadv4292m000

Note: You should perform the export and import through PMC. CDFs that are imported through PMC are not overwritten with CDFs from the Import Customer Defined Fields (ttadv4292m000) session.

The format of CDF files has been changed. If you use a 10.6 version of LN, you can export CDFs to a pre-10.6 version. To do this, you must select Before 10.6 format in the Export Customer Defined Fields (ttadv4291m000) session. Otherwise you cannot import CDFs from a 10.6 LN version into a pre-10.6 LN version.

In LN versions before 10.6, all lists were exported and imported. From 10.6 onwards, only the lists that are used by the exported and imported CDFs are exported and imported.

Suppose that a CDF with origin “FromPMC” was exported through ttadv4291m00 and then imported into a system without this CDF. In that case, the CDF origin is set to the default value: “Manual”. If the CDF already existed on the import system and was “FromPMC”, it remains “FromPMC”.

## CDF Limitations

- `tl` and `tt` packages). You cannot define customer defined fields for tables within Tools (the

- Infor Integration, EDI, Office Integration, and SOA-based integration, do External integrations, such as not support customer defined fields.

- You can use customer defined fields within 4GL reports, if editing the 4GL report layouts is still supported in your environment. Or you can use the report personalization features of Infor LN Report Designer. For external reporting, only Infor Reporting and Microsoft Reporting (SSRS) support customer defined fields.

- There is no direct limitation on the number of CDFs in a table. The actual number of fields in a table and the total length of all fields may be limited by the RDBMS you use.

- Convert to Runtime Data Dictionary (ttadv5215m000) session to convert Only super users can run the the customer defined fields and the related domains to the runtime data dictionary.

- If you add customer defined fields in display sessions, these customer defined fields are always read-only.

Note: The full functionality of customer defined fields is only available within Web UI and LN UI. Customer defined fields are not displayed in the classic Infor LN BW UI.
