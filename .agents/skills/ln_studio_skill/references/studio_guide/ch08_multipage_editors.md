# Chapter 8: Multipage Editors

LN Studio contains various multipage editors that you can use to edit software components, such as sessions,
menus, labels, libraries and messages.
For a detailed explanation of an editor, see the editor's online help.
Editor tabs
Each multipage editor consists of various tabs.
For example, the Session Editor consists of these tabs:
Session Editor tabs
Tab
Overview
Script
Source
User Interface
Form Commands
Satellite Sessions
Documentation
TDE Documentation
Description
Use this tab to specify the general properties for the session.
Use this tab to specify the properties of the session's UI script. You can also link libraries to the session.
Use this tab to view and edit the source of the session's script (if available). The tab
consists of a session-specific Script Editor, which forms an integral part of the Session Editor.
Use this tab to specify the form properties. You can also link reports and charts to
the session, and specify text fields.
Use this tab to maintain the form commands for the session.
If the session is a multi-main table (MMT) controller session, use this tab to maintain
the MMT satellites for the session.
Use this tab to enter the session's release notes and technical documentation.
Use this tab to view an XML tree with the technical information on the session's
Technical Data Entity.
The number of tabs can vary for the different editors. However, the Overview and Documentation tabs exist
in all multipage editors. The TDE Documentation tab is displayed depending on the multipage editor
preferences.
For details on the editor tabs, see the online help of the multipage editors.
Note: The Source tab is only displayed if the source code of the component is present on the LN server. If
you edit a component, for which no source code is present, the Source tab is hidden.
By default, when you start a multipage editor, the editor opens the Overview tab. To change this default
setting, click  in the Activity Explorer view. As a result, the Source tab (if the source code is available) is
directly opened when you start an editor. Click  again to restore the default setting.
See Activity Explorer view on page 299.
The editor displays error markers when you enter incorrect or insufficient information on an editor tab. When
you save a component which contains errors, the component is only stored in your local workspace but is
not saved to the server. In the Activity Explorer, the component has a dirty state ( ) decorator in the bottom
right corner of the software component image. When you solve the error and save the component, the
component is saved to the server again and the decorator disappears.
Preferences
To specify preference settings for the multipage editors:
1 Select Window > Preferences.
2 In the left pane of the Preferences window, select Infor LN Studio Application > Multipage.
The Preferences - Multipage dialog box is displayed. In this dialog box, you can perform these actions:
- Enable or disable the TDE Documentation tab for all multipage editors. This tab is primarily intended
for support and troubleshooting purposes. Therefore it is recommended to display the tab only in
case of problems.
- Specify the directory where LN Studio stores the additional files that you edit in the Additional File
Editor.
See Setting user preferences on page 32.
Starting a multipage editor
To start a multipage editor, double-click a software component in the Activity Explorer view, or right-click
the component and select Open.
You can also start the editor from various other views, such as the Problems view and the Tasks view. For
example:
- When you double-click a problem or task that is associated with a specific library, LN Studio starts the
Library Editor and opens the library in the editor's Source tab.
- When you double-click a problem or task that is associated with a UI script, LN Studio opens the session
to which the script belongs in the Session Editor, and opens the script in the editor's Source tab.
- When you double-click a problem or task that is associated with a specific line in a source, the editor
opens the source on that line.
## Additional File Editor

Use this editor to define and maintain additional files.
### Overview tab

Use this tab to define and maintain additional files.
General Information
Additional File
The name of the additional file, which includes the package code, the module code, the file identification
code, and the filename extension.
For example: tctaxdetermine_tax.gif, or tcccpbl001blsrp0000.xsd.
Description
The description of the additional file. For example, the description of the tcccpbl001blsrp0000.xsd file is
"tcccp001-List-Response".
Editable
If this check box is selected, you can view and edit the file. Click the Additional File hyper link to open the file
with its default external editor, for example Notepad or Picture Manager.
If this check box is cleared, you cannot edit the file, and you cannot view the file in its default external editor.
However, you can view the file in the Preview section of this tab.
Download File
Downloads the file to your client computer. Starts a dialog box where you must specify the file name and
destination folder. After the download, the full pathname of the file is displayed behind the Open File link.
Upload File
Uploads an additional file to the LN server. Starts a dialog box where you must select the file to upload. After
the upload, the full pathname of the file is displayed behind the Open File link.
You can only perform this action if the file is checked out.
Open File
Opens the file, depending on the file extension, in the corresponding default editor.
If the file is not checked out, you are prompted to check out the file. If you do not check out the file, you can
open the file but any changes you make in the editor are lost.
If no file location is displayed behind the Open File link, the file is downloaded before the editor starts.
Preview
This field shows a preview of the file.
For example:
- For a .xsd file, the XML content of the file is displayed.
- For an image file, such as a .gif file or a .jpg file, the corresponding image is displayed.
- Click  to enlarge the image.
- Click  to reduce the image.
- Click  to view the image at its actual size. For large images, only the upper left part of the image
is displayed.
- Click  to resize the preview image so that it fits exactly in the preview area.
These actions do not change the size of the image file, but only affect the preview image.
Note: To optimize performance, for text files, only the first couple of lines is displayed.
### TDE Documentation tab

Use this tab to view an XML tree with the technical information on the additional file's Technical Data Entity.
This optional tab is displayed depending on the multipage editor preferences.
See Multipage Editors on page 150.
## BFlow Editor

Use this editor to edit BFlow test scripts and test cases.
Before you can edit a BFlow test, you must create or import the test in LN Studio. See the Infor LN BFlow
Development Guide and the LN Studio online help.
Note: In a multi-tenant environment you cannot run or debug BFlows with LN Studio. You can run BFlows in
the LN UI to see the result.
### General tab

This tab shows general information and contains a comment section.
General Information
Name
The name of the test.
The name has this format:
[package][module][filename].bflow in case of test script
[package][module][filename].bfcase in case of test case
Description
The description of the test.
Domain
The domain of the test. Only applicable for test cases.
Owner
The owner of the test. Only applicable for test cases.
Company
The company to start the test in. Only applicable for test cases.
Logistic Company
The logistic company to start the test in. Only applicable for test cases.
Financial Company
The financial company to start the test in. Only applicable for test cases.
Comment
Comment
Shows the comment section of the test.
### Variables tab

Use this tab to add, modify, or delete variables.
Variables
Name
The name of the variable.
Type
The variable type such as Long or String.
Domain
The LN domain name such as tcyesno.
Scope
The scope of the variable. For example, In or Internal.
Initialized
Indicates whether the variable is initialized.
Initial Value
The initial value of the variable.
Description
The description of the variable.
Buttons
Add
Adds a variable in the grid.
Up
Moves the selected variable one row up in the grid.
Down
Moves the selected variable one row down in the grid.
Remove
Removes the selected variable from the grid.
### Actions tab

Use this tab to add, modify, or delete test actions.
The tab consists of these sections:
- Overview
This section shows the test actions. If you select an action in the tree, the corresponding action details
are displayed in the Details section.
The tree supports cut/copy/paste and drag/drop functionality.
You can expand or collapse all nodes of the tree by clicking the icons above the tree.
Click the show palette link above the tree to open the BFlow Palette view. This view shows all available
actions. To add an action to the test, drag and drop an action from the palette, or use the shortcut menu
of the tree.
- Details
This section shows the details of the action selected in the Overview section.
For details about the different action types, see the Infor LN BFlow Development Guide and the LN Studio
online help.
### XML tab

Use this tab to edit the XML source code of the test directly. The XML must be valid before you can save the
test or switch to other tabs.
### TDE Documentation tab

Use this tab to view an XML tree with the technical information on the test's Technical Data Entity.
This optional tab is displayed depending on the multipage editor preferences. See the  Infor LN Studio
Application Development Guide and the LN Studio online help.
## Business Object Editor

Use this editor to maintain business objects.
You can change the Business Object Name. The other fields are read-only.
### Overview tab

Use this tab to maintain business objects.
General Information
Business Object
The code that identifies the business object.
Label Code
The name of the label that contains the business object's description.
To edit or view the label in the Label Editor, click the hyperlink.
Description
The business object's description.
Allowed values:
This field is read-only, because the description originates from a label. To edit this label, click Label Code.
Business Object Name
The name of the business object. By default this name is identical to the Description.
Business Object Document
The business object's BOD file.
To view this file in the Additional File Editor, click the hyperlink.
Interface Project
The business object's interface implementation.
To switch to the Integration perspective and open the implementation in the Interface Implementation
editor, click the hyperlink.
Linked Libraries
This list contains the records of all libraries linked to the business object.
To sort the libraries by position, name, or description, click the corresponding column header. When you
sort by position, the sort mode is always ascending. When you sort by name or description, click the involved
column header to toggle between ascending and descending sort mode.
### TDE Documentation tab

Use this tab to view an XML tree with the technical information on the business object's Technical Data Entity.
This optional tab is displayed depending on the multipage editor preferences.
See Multipage Editors on page 150.
## Domain Editor

Use this editor to maintain the properties of a domain.
A domain specifies various properties of a field or variable, such as:
- data type
- length
- value range
- (default) display format
Domains can be linked to table fields, form fields, and program variables.
### Overview tab

Use this tab to specify the general properties of a domain.
General Information
Domain
The unique name of the domain.
A domain is identified by the unique combination of package code and domain code.
Allowed values:
This field is read-only.
You can only specify a domain name when you create a new domain. The domain name is an ASCII text and
must start with the code of the package for which the domain is used. After you created a new domain, you
cannot change its name.
A good practice is to always include the module code in the domain name. When you fill in a domain name,
we recommend the following format:
<package code><module code>.<domain code>
For example, tdsls.hdst is the name of the Header Status domain of the Sales Control module (sls) of the
Distribution package (td).
Description
The description of the domain.
Allowed values:
An ASCII text with a maximum length of 60 characters.
Data Type
The data type of the domain. This is the internal representation of data.
For example:
- string
- long
- double
- date
- UTC Date Time
Allowed values:
Whole number for which physically 1 byte is reserved.
Whole number for which physically 2 bytes are reserved.
Whole number for which physically 4 bytes are reserved.
Byte
Integer
Long
Float
Double
String
Enumerated
Set
Date
Text
Multibyte
String
UTC Date
Time
A data type for floating-point numbers, that is, any number containing a decimal point.
Physically, 8 bytes are reserved for each float data type.
Whole number for which physically 8 bytes are reserved.
A data structure that contains a number of ASCII characters that represent readable text.
Each character consists of a single byte.
A data type that consists of a single value from of a list of predefined text values (up to
255). You can define enumerate values with name and language-dependent descriptions
on the Enum/Set Constants tab of the Domain editor.
Example:
A field can contain values such as 'yes', 'no' or 'maybe', or color values such as 'red', 'white',
'blue', and so on.
A data type that consists of a set of predefined text values (up to 32). You can maintain
the set name and its language-dependent descriptions on the Enum/Set Constants tab
of the Domain editor.
Example:
The display feature set, which can contain the values 'bold', 'blinking', 'reverse', but also
combinations of these, such as 'bold' and 'blinking'.
A data type that represents a date as string in the form YYYYMMDD, where Y stands for the
year, M for the month and D for the day of the month. The date can optionally be appended
by the time, which has the following format: THHMMSS, where T stands for time, H for
hours, M for the minutes and S for seconds.
Example:
Date '19990816T040000' denotes eight o' clock in the morning, August 16th, 1999.
Data type used for fields that refer to a text number in the text database.
Example:
To make it possible to link a text to an item in an item table, you must add a field with a
domain of the text data type in the item table definition.
A data structure that contains a number of multibyte characters that represent readable
text. Each character consists of one or more bytes.
A time/date format. LN stores UTC Date Time as the number of seconds (a Long value)
after the beginning of the year 1970 (00:00:00 GMT, January 1th).
Note: The data type you selected for the domain will largely determine which fields you can fill in for this
domain and how you can specify these fields.
Runtime
Convert: Convert Domain to Runtime
This link is only available if the domain is checked in.
Click this link to convert domains and tables to the runtime data dictionary:
- For LN servers with Enterprise Server 10.5 or later, the Convert to Runtime dialog box is started.
- For LN servers with older Enterprise Server versions, the Convert to Runtime Data Dictionary
(ttadv5215m000) session is started.
You must be authorized to run this session.
Note: In the Convert to Runtime dialog box or the Convert to Runtime Data Dictionary (ttadv5215m000)
session, select the package combination that contains the Project VRC of your current Software Project.
Domains and tables in all Activities linked to the software project are converted. Therefore, not only domains
in your own Activity VRC are converted, but changed domains in activity VRCs of other developers are also
converted.
Read the online help of the dialog box or session before you start the conversion.
Formatting
Length
The length in characters, if the data type of the domain is a (multi-byte) string, or the default display length
for data types UTC Date Time, Date, Enumerated and Set. For the latter two data types, the length defines
the maximum number of characters of the descriptions of the Enumerated or Set data type. Any description
with more characters will simply be cut off at the specified length.
Allowed values:
A whole number in the range 1 – 999.
Allowed values:
Default value
Not relevant for this data type.
Data type
Date
UTC Date/Time
Other
Not Applicable
Note: You can use this field for the following data types:
- String
- Multibyte String
- Enumerated
- Set
- Date
- UTC Date/Time
The field does not apply to other data types.
Alignment
The alignment method for various components:
- (multi-byte) strings
- enumerated values
- sets
- dates
Allowed values:
Default value
No text alignment.
Aligns text to the left.
Data type
Not
Left
Data type
Right
Centered
Not Applicable
Default value
Aligns text to the right.
Centers text.
Not relevant for this data type.
Allowed values:
Not
Note: You can use this field for the following data types:
- String
- Multibyte String
- Date
- UTC Date/Time
For other data types, the field is automatically set to value ‘Not Applicable’.
Conversion
Conversion method for strings. You can convert text strings into upper or lower case.
Allowed values:
Default value
No text conversion.
Converts entire text into lower case.
Converts entire text into upper case.
Data type
Not
Lower Case
Upper Case
Allowed values:
Not
Note: Only use this field for String and Multibyte String data types. For other data types, the field is
automatically set to value ‘Not Applicable’.
Internal Format
This field indicates how a number, entered in a form input field with the string data type, must be internally
formatted.
For example, if number 37 must be stored as 00000037, use the format 99999999.
Note: Only use this field for String data types. The field does not apply to other data types.
Allowed values:
A formatting text string with a maximum length of 30 characters. Allowed characters are restricted to the
following set:
- -
- +
- *
- Z
- 9
- V
- ,
- :
Display Format
The display format used in forms and reports to display specific data.
Allowed values:
The value for the display format must be less than 30 characters. To specify a pre-defined display format
from the server, use the browse button and select a value from the select dialog box.
Format description
A string of 'Z' characters followed by '9' characters. The number of characters in the string
indicates the number of positions used to display the number. The '9' sign reserves a
position for a digit. The sign 0 is displayed if there is no significant digit on this position.
The 'Z' sign also reserves a position for a digit, but displays a blank instead of a zero for
an empty position.
In the format of fractional numbers, the decimal sign is denoted by the letters 'VD'. The
'9' sign reserves a position for a digit. In runtime, the sign 0 will be displayed if there is
no significant digit on this position. To the right of the decimal point, the 'Z' sign also
reserves a position for a digit, but displays a blank instead of a zero if the involved digit
is not significant. To the right of the decimal sign ('VD'), .'9' signs are used to indicate the
number of decimal places.
When the data type is a double, you can use a generic format. To use a generic format,
the display format value must contain ‘%A’. The string that follows %A must be an existing
generic format on the back end, for example '%A001'.
For example, if you want to display the number '123.45678' as '....000123.45' (points denote
blanks), you must specify display format 'ZZZZ999999VD99'.
The format for Date data types must contain '%D' and the string that follows '%D' must
exist as a date format on the server, for example '%D001'.
UTC Date/Time The format for UTC Date/Time data types must contain '%u' and '%U'. The string that
follows '%u' (until blank character) must exist as a date format on the server. The string
that follows '%U' must exist as a time format on the server, for example '%u001 %U002'.
A string of 'Z' characters followed by '9' characters. The number of characters in the string
indicates the number of positions used to display the text.
Data type
Byte, Integer,
Long
Float, Double
Date
Text
Note: You cannot use this field for data types Enumerated and Set.
Numeric Data
Digits Before Decimal
For numeric data types, the maximum number of digits before the decimal sign. This implies the maximum
number of digits for long, integer and byte data types.
Allowed values:
The value for this field is a whole positive number less than 100. For byte, integer and long data types, the
following maximum values apply.
Maximum value
Data Type
Byte
Data Type
Integer
Long
Maximum value
Allowed values:
Data type
Byte
Integer
Long
Float
Double
Default value
If the Display Format of this domain contains '%A', the default value of a double is 15.
Note: Only use this field for numeric data types:
- Byte
- Integer
- Long
- Float
- Double
For non-numeric data types, the field is automatically set to value 0.
Digits After Decimal
The maximum number of digits after the decimal sign.
Allowed values:
The value for this field is a whole positive number less than 100.
Allowed values:
If the Display Format of this domain contains '%A', the default value for a double is 4. For a float data type,
the default value is 0.
Note: Only use this field for Float and Double data types. For whole numbers and non-numeric data types,
the field is automatically set to value 0.
Divide Factor
The factor by which the entry in a field is divided.
Divide Factor can be useful for fields containing amounts.
Example:
The Divide factor amounts to 100. When a user enters 25009 in the field for which this factor is set, LN divides
25009 by 100 and displays 250.09.
Allowed values:
A whole number (max. 9 digits).
Allowed values:
Note: Only use this field for Float and Double data types. The field does not apply to other data types.
Rounding Method
The way in which a field with the float or double data type can be rounded.
Rounding takes place at the last digit as specified by the number of digits after the decimal point.
Example:
In the following examples, the number of digits after the decimal sign is one.
Round off downwards
1.5
2.7
1.5
Entered by
user
1.51
2.78
1.55
Round
off
1.5
2.8
1.6
Round off upwards
1.6
2.8
1.6
Allowed values:
- Round off
- Round off upwards
- Round off downwards
- Not Applicable
For an explanation of these rounding methods, see the previous example.
Allowed values:
Round off
Note: Only use this field for Float and Double data types. The field does not apply to other data types.
Validation
Illegal Characters
The illegal characters that cannot be entered in a form input field.
Allowed values:
All characters are allowed, with the exception that the characters ' " ^ \ must be preceded by a backslash [\],
for example \\ and \". Maximum length is 30.
Note: You cannot use this field for the following data types:
- Enumerated
- Set
- Date
- UTC Date/Time
- Text
The field can be used for all other data types.
If you define some characters as illegal, all other characters are legal, and vice-versa. Therefore, you cannot
use this field if a value for Legal Characters is filled in.
Legal Characters
The legal characters that can be entered in a form input field. If you do not specify any legal characters, all
characters are legal.
Example:
If only numbers can be entered in a field with string data type, the legal characters are specified as: 1234567890.
Allowed values:
All characters are allowed, with the exception that the characters ' " ^ \ must be preceded by a backslash [\],
for example \\ and \". Maximum length is 30.
Note: You cannot use this field for the following data types:
- Enumerated
- Set
- Date
- UTC Date/Time
- Text
The field can be used for all other data types.
If you define some characters as legal, all other characters are illegal, and vice-versa. Therefore, you cannot
use this field if a value for Illegal Characters is filled in.
Range
The range used to check the validity of the input. If you enter a value in a form input field outside the specified
range, LN produces a range message and will ask for input again.
For simple validation checks, you can use the following:
- The data type
- Legal and illegal characters
- The length of the field
- The number of digits before and after the decimal point
For more complicated validation checks, you need the range attribute.
Examples of restrictive ranges:
A string starting with a capital
$$ in ^[A-Z].*$ (regular expressio
n)
Allowed values:
The range can be an expression with evaluated value true (valid value) or false (invalid value) (true <> 0, false
= 0). Other variables can also be used in the expression. To test the current value in the expression, use 2
dollar signs: $$
The following operators can be used (listed in order of decreasing precedence):
Description
tor
equal to
not equal to
equal to or less than
greater than or equal to
less than
greater than

Opera-
Description
Example

Operator
( )
IN
- 
^
*
/
\
expression in brackets
range test
unary minus
raise to power
multiply
divide
remainder
2*(3+5)
$$ IN [10,20]
- 10
2^3 = 8
2*3 = 6
6/2 = 3
3\2 = 1

=
<>
<=
>=
<
>

Operator
&
+
- 
Description
Example

Operator
Description
string concatenation
addition
subtracting
"A"&"B" = "AB"
2+3 = 5
2-3 = -1

not
and
or
logical negation
logical and
logical or
Note: You cannot use this field for data type Text. The field can be used for all other data types.
Range Message
The name of the message, including package code, which is issued if an entered value falls outside the
specified range.
Allowed values:
You can use the browse button and select a message name from the select dialog box. This dialog box contains
all messages available in the package of the domain. You can also enter an existing message name.
Range Message Description
The actual message as shown when activated.
Note:  Range Message Description is an information field. You cannot change the message, because the
field is read-only. You can create messages in the Message Editor.
### Enum - Set Data tab

This tab only applies to domains with data type Enumerated or Set.
Use this tab to define the constants that belong to a domain of data type Enumerate, or Set, with
language-dependent descriptions.
To define a constant:
1 Specify the constant number for internal usage.
2 Specify the name of the constant used in program scripts and defaults in form fields.
3 Specify the language-dependent description that a form field shows at runtime.
This tab contains a table with all the constants used in an Enumerated or Set domain. The constants are
displayed as records with the following arguments:
- Constant
- Constant Name
- Description
- Label
In the Enum or Set Values table, you can add and remove constant records.
- To add a constant record to a domain, click Add and fill in the required fields. Specify a code and a name.
Alternatively, right-click in the table and, on the shortcut menu, select Add.
- To remove a constant record, right-click the record and, on the shortcut menu, select Remove.
Enum or Set Values
Constant
The constant number that represents the internal enumerated field value. This number determines the
sequence in which the enum descriptions are displayed at runtime.
If a table index includes/consists of an enumerate field, the constant determines the sequence of records
according to the index.
You can also use the constant number for greater than and less than expressions in scripts. For example,
domain tryesno has value yes, with constant number 1, and value no, with constant number 2. For this domain,
the expression tryesno.no > tryesno.yes is true.
Allowed values:
Whole number in the range 1 -255.
Allowed values:
The highest present constant number raised by 1.
Constant Name
The constant name combined with the package code and domain code. This is used to refer to an enumerated
constant in scripts or expressions on forms and reports.
Example:
Consider package code ti (Manufacturing), domain code yesno and constant name yes. To refer to this
constant in a form field with domain code tiyesno, use the expression tiyesno.yes.
Allowed values:
A text string that starts with an alphabetic character. Spaces are only allowed at the end of the string.
Description
The content description of the label. This description is used as a constant value of enumerated or set data
types.
Allowed values:
This field is read-only for existing constant records, because the description is a property of the Label. You
can modify the description text in the label editor.
You can specify a constant description in the domain editor when you add a new constant record. This
description is an ASCII text with a maximum label length of 70 characters.
Label
The label name for the Description of the enumerated or set constant.
When hovering above the label name, the domain editor shows a hyperlink. Use this hyperlink to edit the
label with the enumerate description in the label editor.
Allowed values:
This field is read-only and is automatically generated when you save the domain.
The generated label name is a concatenation of package code, module code, domain code and constant
number. For example:
ttadv.cmpt0001
Note: The label is generated when you save the domain and can be modified in the label editor.
Step Size
A number used to automatically generate subsequent constant values.
For example, if the first constant value is 10, and the step size is 10, the second and third constant number
are 20 and 30. This step size enables you to insert in-between constant values later.
Allowed values:
### Documentation tab

Use this tab to enter the domain's release notes and technical documentation.
Release Notes
Use this field to specify the release notes of the domain.
Technical Documentation
Use this field to specify the technical documentation of the domain.
### TDE Documentation tab

Use this tab to view an XML tree with the technical information on the domain's Technical Data Entity.
This optional tab is displayed depending on the multipage editor preferences.
See Multipage Editors on page 150.
## Function Editor

Use this editor to maintain the properties of a function.
A function is a self-contained software routine that can perform a task for the program in which the function
is written, or for another program. With the #include statement, you can include a function in a program
script. It can be useful to define a function and use it in more than one program script.
### Overview tab

Use this tab to specify the properties of a function.
General Information
Function
The unique function name, which identifies the function.
A function name consists of a combination of these codes:
- package
- module
- function
The function name forms the identifying attribute of the function and is used in a program script as an include
statement.
Allowed values:
This field is read-only.
You can only specify a function name when you create a new function. Afterwards, you cannot change this
name.
When you create a new function, enter the full name of the function, which is a combination of the package
code, the module code and the function code, for example: ttaad0001.
Illegal characters are: $ \ / ~ &
Example:
The Application Administration module of the LN Tools package includes the function Convert User to Runtime
DD.
Description
LN Tools
Application Administration
Convert User to Runtime DD
Component
Package
Module
Function
Code
tt
aad
The name to refer to this function is: ttaad0001
If you want to include a function in a program script, use the following statement:
#include "i<entire code>"
Therefore, in this example use the following:
#include "ittaad0001"
Description
The description of the function.
Allowed values:
An ASCII text with a maximum length of 60 characters.
### Source tab

Use this tab to edit the function's source code. The tab consists of a script editor, which forms an integral
part of the function editor.
See Script Editor on page 267.
### Documentation tab

Use this tab to enter the function's release notes and technical documentation.
Release Notes
Use this field to specify the release notes of the function.
Technical Documentation
Use this field to specify the technical documentation of the function.
### TDE Documentation tab

Use this tab to view an XML tree with the technical information on the function's Technical Data Entity.
This optional tab is displayed depending on the multipage editor preferences.
See Multipage Editors on page 150.
## Label Editor

Use this editor to maintain the properties of a label.
Labels are used instead of language-dependent text in these LN components:
- Forms
- Reports
- Domains
- Menus
Labels can also be used in LN Workbenches.
A label consists of a name and a content description. Use the label name as a reference to the label description.
The description of a label can differ by language, but the label name remains the same for all languages.
You can specify a label description for each label code. This is the label text you can edit and translate. You
can define different variants for a label. Therefore, a label can have a different description in a different context
or with a different length or height.
The label editor automatically calculates the length and height of a label description. The length is the number
of characters of the description. The height is the number of lines of the description.
Note: The Languages property of the application, assigned to the current software development project,
determines the primary language of a label. It determines whether you can specify secondary languages and
which languages are used as secondary languages.
For more information on the application properties, see Create a new Application on page 134.
### Overview tab

Use this tab to view the label name and to maintain all label variants in the primary language, such as English.
General Information
Label
The name of the label used as identification code.
Allowed values:
This field is read-only.
You can only specify the label name when you create a new label. The name must start with the code of the
package for which the label is defined.
After a label is created, you cannot change its name.
Description
The description of the label, which corresponds with the longest variant description in the primary language.
Allowed values:
This field is read-only.
The value of this field corresponds with the value of the description field of the primary language variant
with the longest description. This field is a read-only copy of this variant description.
All Variants in (primary language)
All Variants in
The All Variants in list contains all label variants in the primary language. Only the variant descriptions are
displayed.
The Variant Properties field group displays all properties of the label variant you selected in this list.
You can add and remove label variants in the All Variants in list:
- To add a label variant, click Add and specify a Context. Then, enter the Description for the new variant
in the Variant Properties field group.
- To remove a label variant, select a variant and click Remove on the variant shortcut menu.
Note: The name of this field includes the primary language of the label. For example, if the primary language
is English, the name of the field will read the following: All Variants in English. The primary language is
determined by the Primary Language property of the application for the current software development
project.
Allowed values:
A label must have at least one variant. Labels without a variant cannot be saved.
When you create a new variant, specify the Context and Description of the variant. When you specify the
variant Description, you cannot enter a text longer than 70 characters or a text that ends with a blank space.
When you enter the variant Context, select a value from a drop-down list. You can choose one of the following
context values:
- General use
- Form Commands
- Cascading Item on Button
For more information on the Context and Description fields of a variant, see the Variant Properties field
group.
Note: When you create a new label in the Create New Label wizard, you can specify an External Use context.
These External Use labels cannot possess multiple variants. Therefore, the Add button is disabled for these
labels.
Variant Properties
Context
The context of the label variant selected in the All Variants in field. This indicates how the variant is used in
forms, reports, menus, and so on.
Allowed values:
Note: When you add a new variant to a label, you can choose between three contexts:
- General use
- Form Commands
- Cascading Item on Button
However, the label variants not created with the label editor, such as session description labels, can show
many other context values.
These other context values are used for labels that are generated automatically.
For example:
- When you create a new enumeration for an Enumerated domain, LN Studio generates a label with the
Enumerates context.
- When you create a new session, table or report, LN Studio generates a label with the Session, Table or
Report Description context.
Example:
When you create a session with session code tezzzrx and session description MyNewSession, LN Studio
generates a label called tezzzrx001 with label description MyNewSession.
Description
The description of the label variant selected in the All Variants in field.
This is the text that appears where this label variant is used in the following:
- forms
- reports
- menus
Allowed values:
An ASCII text with a maximum length of 70 characters.
Use a % sign to indicate the line break. If the description includes a line break, the height of the label variant
is automatically adjusted to a value greater than one. To include the % sign in the description, type %%.
The maximum number of lines (height) is 3.
Example:
Length
Code
Description
Item Code
Item%Code
Result
Item Code
Item
Height
Percentage [%%]
Percentage [%]
Description
Perc.%[%%]
Result
Perc.
[%]
Height
Length
Note: The description of a label variant automatically sets the length, height and search argument of this
label variant:
- The variant Length corresponds with the number of characters in the description's longest line of text.
- The variant Height corresponds with the number of text lines in the description.
- The variant Search Argument corresponds with the first 10 characters of the description.
Length
The length of the label variant selected in the All Variants in field. This is the maximum number of characters
on a text line of the variant description.
Allowed values:
This field is read-only.
The length value is generated by the label editor. The length is automatically adjusted to a changed label
variant description. For examples of how the length of a label variant is derived from the description, see
the Description field.
Height
The height of the label variant selected in the All Variants in field. This is the maximum number of text lines
in the variant description.
Allowed values:
This field is read-only.
The height value is generated by the label editor and corresponds with the number of text lines in the variant's
Description. The height is the number of % signs in the description text raised by one, with an exception for
the "%%" string, which you use to include the % sign in the label text displayed to the user.
The height is automatically adjusted to a changed variant description. For examples of how the height of a
label variant is derived from the description, see the Description field.
Search Argument
The search argument of the label variant selected in the All Variants in field.
Allowed values:
This field is read-only.
The search argument is generated by the label editor and corresponds with first 10 characters of the variant's
Description, including the % signs. The search argument is automatically adjusted to a changed variant
description.
Note: The label editor changes lowercase characters to uppercase characters.
Expired
If this check box is selected, the label variant selected in the All Variants in field has expired.
Expired label variants cannot be used in the release (VRC) of the application of the current development
project or any releases derived from it.
When all label variants are expired, the label becomes expired.
Note: If only one variant exists, this check box is disabled. In that case, you can expire the label in the Activity
Explorer.
### Translation tab

Use this tab to view and maintain all label variants in the secondary languages, which represent translations
of the primary language label variants on the Overview tab.
The Translation tab is only available if secondary languages are defined for the application. The properties
of the application of the current software development project determine whether a label has secondary
languages and which secondary languages are used.
For more information on the application properties, see Create a new Application on page 134.
All Variants in (primary language)
Context / Description
List of all label variants in the primary language. The list is identical to the All Variants in (primary language)
list on the Overview tab.
To copy a label variant from the primary language to a new label variant in a secondary language:
1 In the Software Language field, select a secondary language.
2 In the All Variants in (primary language) list, select a label.
3 Click Copy. A new label appears in the All Variants in Software Language list.
You can now change the properties of the new variant in the Variant Properties field group.
Allowed values:
This field is read-only.
All Variants in Software Language
Software Language
The secondary language of the label variants displayed in the All Variants in Software Language list.
Allowed values:
Select a secondary language from the drop-down list. Note that the available secondary languages are
determined by the settings of the application of the current software development project.
Context / Description
A list of all label variants in the selected secondary language.
The properties of the label variant you select in this field are displayed in the Variant Properties field group
on this tab. Some properties are read-only, while some are editable.
In the list, you can add and remove label variants, as described for the All Variants in field on the Overview
tab. You can copy a label variant in the primary language as a new label variant in the secondary language.
To do this, use the Copy command of the All Variants in field on this Translation tab.
Variant Properties
Context / Description / Length / etc.
See Variant Properties on the Overview tab.
### Documentation tab

Use this tab to enter documentation on the label.
Technical Documentation
Use this field to specify the technical documentation of the label.
### TDE Documentation tab

Use this tab to view an XML tree with the technical information on the label's Technical Data Entity.
This optional tab is displayed depending on the multipage editor preferences.
See Multipage Editors on page 150.
## Using labels

Using labels instead of plain text has these advantages:
- Improved standardization: a single label is used by all software components
- Easier software maintenance: the layout of forms, reports, and menus becomes language-independent
- Easy and fast translation: the label description is only translated once
- Enhanced customization facilities: changes in the central label file have an effect on all the packages
- The alignment of a label (left or right) on multi-occurrence forms and reports is linked to the alignment
of the associated table field
For example, using labels makes it possible to display and print the text in the correct language on these
components:
- Forms
- Reports
- Menus
For each label, specify this information:
- The label code, which identifies the label.
- The label variant descriptions which can be translated into different languages.
You can specify multiple descriptions with different lengths or heights for a label.
## Library Editor

Use this editor to maintain the properties of a library.
A library is a collection of files, programs or subroutines that is used to carry out specific tasks for other
libraries, program scripts or sessions of LN applications. A dynamic link library (DLL) can be linked as a function
call to a program or session at runtime.
LN distinguishes three types of libraries, all of which are DLL libraries:
- General Library DLL
- Integration DLL
- Business Object Layer DLL
### Overview tab

Use this tab to specify the properties of a library.
General Information
Library
The unique name of the library.
It consists of a combination of the following:
- package code
- module code
- library code
Allowed values:
An ASCII text with a maximum length of 14 characters that conforms to the following format:
<package code><module code><library code>
Example:
LN Financials
Accounts Payable
Receive Purchase Invoices
Package Code:
Module Code :
Script Code :
tf
acf
dll1250
The total identification of the library is: tfacfdll1250.
Description
The description of the library, such as "Validate Financial Calendar" or "Calculate Tax."
Allowed values:
An ASCII text with a maximum length of 60 characters.
Library Type
The library type. To enter a value, select a library type from the drop-down list.
Allowed values:
The following library types are used:
General DLL - Dynamic Link Library
brary
General Li-
Integration
DLL
Dynamic Link Library that integrates between packages.
Compile Flags
The compile flag.
In (3GL and 4GL) sources you can use compile flags. This is in order to compile part of the source depending
on certain conditions and is called conditional compiling. For more information on conditional compiling
and other compile options, see the "Preprocessor" and "Compiler" sections of the Infor ES Programmers
Guide (Infor Customer Portal KB2924522).
Allowed values:
Infor 3GL or Infor 4GL source code with a maximum length of 200 characters.
Example:
| Compile Flag: -DMYTEST | Source ... #if MYTEST message(Some debug information) #endif ...
You can specify several compile flags separated by a space " ". For example:
Compile Flags: -DMYTEST -DVERSION_1 -DVERSION3.0
Note: The preprocessor only works during compilation of a 3GL source. This is because the standard generator
std_gen6.2 does not have a preprocessor pass. Therefore, you cannot use 4GL events in a #if, #ifdef or #ifndef.
Tools Interface Version
The Tools Interface Version (TIV) number of the library.
This is used to guarantee backward compatibility and is related to a particular version of the porting set, the
Enterprise Server and the 4GL Tools. For example, the TIV number for Enterprise Server 7, delivered together
with LN 6.1 FP1, is 1010. When you insert a new library, the TIV is automatically set to the highest supported
TIV number.
Setting a TIV number for each object can result in the behavior of these objects being different. This can
occur for incompatible features executed with different versions of the porting set or the LN 4GL Engine.
For example, the "set.synchronized.dialog" function was changed in TIV 1000. Therefore objects in which
this function is used, show different behavior for different TIVs:
- If the object's TIV is less than 1000, a synchronized dialog is started when a record is inserted or duplicated
in an editable grid.
- If the object's TIV is 1000, no synchronized dialog is started when a record is inserted or duplicated: the
new record is entered directly in the grid.
For details about the TIV, see the Infor ES Programmers Guide (Infor Customer Portal KB2924522).
Allowed values:
Numeric value (max. 9999).
Keywords
Search Key 1
The first search key.
Allowed values:
An ASCII text with a maximum length of 20 characters.
Search Key 2
The second search key.
Allowed values:
An ASCII text with a maximum length of 20 characters.
Search Key 3
The third search key.
Allowed values:
An ASCII text with a maximum length of 20 characters.
Linked Libraries
This list contains the records of all libraries linked to the current library.
Sorting
- To sort the libraries by position, name, or description, click the corresponding column header.
- When you sort by position, the sort mode is always ascending. When you sort by name or description,
click the involved column header to toggle between ascending and descending sort mode.
- When you sort by name or description, the Up and Down commands are disabled.
Add / remove libraries, change linking order
You can only perform the following actions if you sort the libraries by position.
- To add a library, click Add. Then, press CTRL+SPACE in the Name field and select a library from the select
dialog box.
- To remove a library, right-click a library and, on the shortcut menu, select Remove.
- To change the linking order of the libraries, move them up or down the list.
Note: To edit a library, click the icon behind the library name.
Pos
The library sequence number (Position). This field indicates the linking order of the libraries.
This field is read-only. It is filled automatically when you link a library.
Name
The name of the library.
Allowed values:
To specify this attribute, press CTRL+SPACE and select a library from the select dialog box.
Description
The description of the library.
Allowed values:
This field is read-only. LN Studio automatically fills in the library description after you specified the Name
of the library.
License
Product ID Source
The product ID for which a license is needed to compile the object. If the field is empty, no license is needed
to compile the object.
To enter a product ID, click Browse and select an ID from the select dialog box.
Product ID Object
The product ID for which a license is needed to run the object. If the field is empty, no license is needed to
run the object.
To enter a product ID, click Browse and select an ID from the select dialog box.
### Source tab

Use this tab to edit the library's source code. The tab consists of a script editor, which forms an integral part
of the library editor.
See Script Editor on page 267.
### Documentation tab

Use this tab to enter the library's release notes and technical documentation.
Release Notes
Use this field to specify the release notes of the library.
Technical Documentation
Use this field to specify the technical documentation of the library.
### TDE Documentation tab

Use this tab to view an XML tree with the technical information on the library's Technical Data Entity.
This optional tab is displayed depending on the multipage editor preferences.
See Multipage Editors on page 150.
## Menu Editor

Use the Menu Editor to define and maintain menus.
An LN menu is a list of options from which a user can perform a desired action, such as starting a session,
another menu, and a query.
### Overview tab

Use this tab to specify the following:
General Informa- The general properties of a menu, such as the name and description.
tion
These are the options a user can start from the menu.
The All Menu Entries list contains all options the user can start from the menu, such
as sessions, other menus, and queries.
In the All Menu Entries list, you can add and remove menu entries:
- To add a menu entry, click Add and specify the properties for the new entry in the
grid.
- To remove an entry, right-click the entry and, on the shortcut menu, select Remove.
The order of the entry records in the table corresponds with the order of the entries
on the menu. To determine the menu entry sequence, click Up or Down to move the
entry records up or down the table.
Menu entries
General Information
Menu
The name of the menu.
This includes the following:
- package code
- module code
- menu identification code
Allowed values:
This field is read-only.
You can only specify the name of a menu when you create a new menu. After a menu is created, you cannot
modify its name.
Label Name
The code of the label that contains the menu description.
To modify the description, click the hyperlink to open the displayed label in the Label Editor.
Allowed values:
This field is read-only. You can only set the label name when you create a new menu. You cannot change this
name afterwards.
Description
The menu description, as displayed in the user interface.
Allowed values:
This field is read-only, because the description originates from a label. To edit this label, click Label Name.
All Menu Entries
Type
Type of menu entry. This indicates the type of action activated by the menu entry.
Allowed values:
Select one of these entry types:
- Session
- Menu
- Shell Program
- Query
Code
Code of the menu entry. This is the code of the session, menu, shell program, or query activated when you
select this menu option. The type of code used depends on the value specified for the Type field.
> [!NOTE]
- If the menu entry type is Session, Menu, or Query, press CTRL+SPACE and select a component from the
select dialog box. Click the icon behind the code to open the component in the corresponding editor.
- If the menu entry type is Shell Program, manually enter the program name.
Allowed values:
An ASCII text with a maximum length determined by the value of the Entry Type field.
Text length
13 characters.
13 characters.
15 characters.
9 characters.
Entry type
Session
Menu
Shell Program
Query
Description Linked
If you select a session, menu, or query, the corresponding description is automatically placed in the
Description field.
If this check box is selected, the description is read-only.
If this check box is cleared, you can modify the description.
Note: You cannot select this check box if the menu entry type is Shell Program. You must manually enter the
program description in the Description field.
Description
The description of the menu entry, as displayed in the menu.
This Description field only applies if the Description Linked check box is cleared and the Label Code field
is not filled in. The field is disabled if these conditions are not satisfied.
Note: If you enter the description manually, LN Studio automatically stores the description in a label. The
code of this label is displayed in the Label field.
Allowed values:
ASCII text of less than 60 characters.
Label
The code of the label that contains the menu entry description. Click the icon behind the label code to open
the label in the Label Editor.
To select a label, press CTRL+SPACE and select a label from the select dialog box.
The Label field only applies if the Description Linked check box is cleared.
Allowed values:
A code of a label that exists on the LN server.
Process Info
This field contains information that is passed to the program activated by the menu.
If the program is a session, this information can be retrieved in the session with the procesinfo variable. If
the program is a shell program, the information is used as the argument of the program.
This field only applies to menu entries of type Session or Shell Program. This field is disabled for all other
menu entry types.
Allowed values:
ASCII text of less than 50 characters.
Active
If this check box is selected, the menu entry is active. Therefore, the menu entry is visible on the menu.
If this check box is cleared, the menu entry is disabled. Therefore, the menu entry is not visible on the menu.
Filter Library
The library/dal to determine whether the menu item, session, or complete menu tree, must be hidden based
on the parameter settings of the company of the user. Zooming starts a session that only shows libraries/dals.
To open the filter library in the Library Editor, click the icon behind the library name.
Note: This setting has only effect for users that use LN UI. This setting is only available if it is supported by
the LN server.
Filter Function
The name of the function in the Filter Library that must be called, without the () at the end of the function.
This function has no parameters and must return true or false.
If the function returns false when called without parameters, the menu entry is not displayed in LN UI . In
this way you can filter sessions that depend on parameter settings.
Note: This setting has only effect for users that use LN UI. This setting is only available if it is supported by
the LN server.
Hidden
If this check box is selected, the menu item is not displayed in the menu at runtime. However, in LN UI users
can make the menu visible through the Personalize Menu command. Administrators can centrally maintain
these personalizations through the Overview Menu Personalizations (ttadv9505m000) session.
Note: This setting has only effect for users that use LN UI. This setting is only available if it is supported by
the LN server.
### Preview tab

This tab shows a preview of the menu.
### Documentation tab

Use this tab to enter the menu's release notes and technical documentation.
Release Notes
Use this field to specify the release notes of the menu.
Technical Documentation
Use this field to specify the technical documentation of the menu.
### TDE Documentation tab

Use this tab to view an XML tree with the technical information on the menu's Technical Data Entity.
This optional tab is displayed depending on the multipage editor preferences.
See Multipage Editors on page 150.
## Message Editor

Use this editor to maintain the messages displayed to the user.
LN messages are language-dependent software components used to show situation-dependent information
to the user. You can use LN messages to customize dialog messages.
Message codes can be included in program scripts and can be linked to these components:
- Domains
- Tables
- Table fields
- Form fields
- And so on
For each message, you can specify this information:
- The unique message code. This identifies the message across all languages.
- The message type, such as "Warning", "Information", or "Critical".
- The message. This is the message text which you can edit and translate. It can contain codes that are
substituted when the message is displayed. For details on substitution symbols, see the description of
the sprintf$() function in the Infor ES Programmers Guide (Infor Customer Portal KB2924522).
Note: The properties of the application assigned to the current software development project determine the
following:
- the primary language of a message
- whether you can specify secondary languages
- which languages are used as secondary languages
For more information on the application properties, see Create a new Application on page 134.
If an application does not have secondary languages, the message editor does not show the translation fields.
### Overview tab

Use this tab to view and maintain the message properties.
General Information
Message
The unique message name which identifies the message.
Allowed values:
This field is read-only.
You can only specify the message name when you create a new message. The message is identified by the
unique combination of the package code and the message code. So, the entire message name you enter in
the Message field must start with the code of the package for which the message is defined followed by a
code for the specific message.
After a message is created, you cannot change its code.
Description in (primary language)
The message expressed in the primary language. This is the text that appears in the message box.
Note: The name of this field includes the primary language of the label. For example, if the primary language
is English, the name of the description field will read the following: Description in English. The primary
language is determined by the Primary Language property of the application for the current software
development project.
Allowed values:
A multi-byte text with a maximum length of 132 characters.
The message can contain codes that are substituted when the message is displayed. This table shows some
examples:
Substitution of a string
Substitution of a digit
Substitution of an exponent
%1$s
%1$d
%1$e
For details on substitution symbols, see the description of the sprintf$ function in the Infor ES Programmers
Guide (Infor Customer Portal KB2924522).
Message Type
The message type indicates a categorization of the messages.
Allowed values:
To specify a value for this field, select one of the following message types:
All goes fine but there is something you may want to know.
Something went wrong, but the process is still running.
A fatal error occurred and the process is aborted.
Information
Warning
Critical
Help Text
If this check box is selected, a help text is linked to this message.
Translation
Target Software Language
Select a language for input of translation. You can only select a secondary language that is not already used
for a translation.
To add a new message translation to the Translations field, select a target software language. Click Copy
and translate the message into the selected language.
Note: Selecting a target software language enables the Copy button.
Allowed values:
To specify a value for this field, select a language from the drop-down list. This list contains all the secondary
languages of the application that are not already used for a translation in the Translations field.
Software Language
The software language in which the message text is translated.
Allowed values:
This field is read-only.
The language used for the translation is one of the secondary software languages of the application. You can
only specify this software language when you create a new message translation, see Target Software
Language.
Description
The translated message text.
Allowed values:
A multi-byte text with a maximum length of 132 characters.
The message can contain codes that are substituted when the message is displayed. This table shows some
examples:
Substitution of a string
Substitution of a digit
Substitution of an exponent
%1$s
%1$d
%1$e
For details on substitution symbols, see the description of the sprintf$ function in the Infor ES Programmers
Guide (Infor Customer Portal KB2924522).
### TDE Documentation tab

Use this tab to view an XML tree with the technical information on the message's Technical Data Entity.
This optional tab is displayed depending on the multipage editor preferences.
See Multipage Editors on page 150.
### Messages

Messages are language-dependent software components that allow you to customize dialog messages.
For each message, you can specify this information:
- The unique message name that identifies the message across all languages.
- The message type, such as "Warning", "Information", or "Critical".
- The message. This is the message text you can edit and translate. It can contain codes that are substituted
when the message is displayed. For details on substitution symbols, see the description of the sprintf$()
function in the Infor ES Programmers Guide (Infor Customer Portal KB2924522).
This table shows a sample message:
Message
name
tipcss0292
Message
Type
Warning
Language
(Dutch)
2 (English)
Message
Artikel reeds aanwezig als component in productiestuklijst
tipcss0292
Warning
Item already found as component in production BOM
Messages are used in a variety of places within the application. You can use messages in these scenarios:
- To replace the default reference error message on table definitions
- Within program scripts and libraries
- To set error messages from a DAL
- As the contents of a form field using the form.text$ function
If a message is produced while a session is executing, a dialog box is displayed. Click OK to continue. If the
session is running in a job, the message is logged in the job history messages.
Creating messages
To create messages, use the Create a New Infor LN Software Component wizard. To start this wizard, select
File > New > Infor LN Component.
For more information, see:
- The LN Web Help
- The Message Handling subtopic. This is located in the Functions topic in the Infor ES Programmers Guide
(Infor Customer Portal KB2924522)
## Question Editor

Use this editor to maintain the questions to which the user must respond.
LN questions are language independent software components. They are used to ask questions to which the
user must respond. At runtime, the questions are displayed in the language specified for the current user.
For each question, you can specify the following:
- The unique question code that identifies the question across all languages.
- The question type, such as a "Warning".
- The question. This is the text of the question you can edit and translate.
- The answers to the question to which the system must respond.
Note: The properties of the application assigned to the current software development project determine the
primary language of a question and whether you can specify secondary languages. The properties also specify
which languages are used as secondary languages.
For more information on the application properties, see the Create a new Application dialog box.
If an application does not have secondary languages, the question editor will not display the translation
fields.
### Overview tab

Use this tab to view and maintain the question properties.
General Information
Question
The name of the question, which uniquely identifies the question.
Allowed values:
This field is read-only.
You can only specify the question name when you create a new question. A question is uniquely identified
by the combination of package code and question code. So, the entire question name you enter in the
Question field must start with the code of the package for which the question is defined followed by a code
for the specific question.
After a question is created, you cannot change its name anymore.
Description in (primary language)
The question put in the primary language of the application.
Note: The actual name of this field includes the primary language of the question. For example, if the primary
language is English, the name of the description field is: Description in English. The primary language is
determined by the Primary Language property of the application for the current software development
project.
Allowed values:
A multi-byte text with a maximum length of 132 characters.
The question can contain codes that are substituted when the question is displayed. This table shows some
examples:
Substitution of a string
Substitution of a digit
Substitution of an exponent
%1$s
%1$d
%1$e
For details on substitution symbols, see the description of the sprintf$ function in the Infor ES Programmers
Guide (Infor Customer Portal KB2924522).
Question Type
The question type indicates a categorization of the questions.
Allowed values:
To specify a value for this field, select one of the following question types:
All goes fine but there is something you may want to know.
Something went wrong, but the process is still running.
A fatal error occurred and the process is aborted.
Information
Warning
Critical
Domain
The domain that determines the possible answers to the question.
Note: Click the Domain hyperlink to open the domain in the Domain Editor.
Allowed values:
Click Browse to select a domain. The domain must have the data type Enumerated.
Example:
A question is linked to the tcyesno domain. The domain consists of the enumerate constants Yes and No.
The question is displayed with a Yes button and a No button.
Default Answer
The default answer to the question.
Allowed values:
Select one of the enumerate constants belonging to the specified domain.
Help Text
If this check box is selected, a help text is linked to this question.
Translation
Target Software Language
Select the language for input of a translation. You can only select a secondary language of the application
not already used for a translation.
To add a new translation of a question to the Translations field, select a target software language. Click
Copy and translate the question into the selected language.
Allowed values:
To specify a value for this field, select a language from the drop-down list. This list contains all the secondary
languages of the application not already used for a translation in the Translations field.
Software Language
The language into which the question text is translated.
Allowed values:
This field is read-only.
The language used for the translation is one of the secondary software languages of the application. You can
only specify this software language when you create a new translation for the question, see Target Software
Language.
Description
The translated question.
Allowed values:
A multi-byte text with a maximum length of 132 characters.
The question can contain codes that are substituted when the question is displayed. This table shows some
examples:
Substitution of a string
Substitution of a digit
Substitution of an exponent
%1$s
%1$d
%1$e
For details on substitution symbols, see the description of the sprintf$ function in the Infor ES Programmers
Guide (Infor Customer Portal KB2924522).
### TDE Documentation tab

Use this tab to view an XML tree with the technical information on the question's Technical Data Entity.
This optional tab is displayed depending on the multipage editor preferences.
See Multipage Editors on page 150.
## Questions

Questions are language independent software components used to ask questions to which the user must
respond. At runtime, the questions are displayed in the language specified for the current user.
For example, if you change the name of an employee in the Employees - General (tccom0101m000) session,
this question is displayed: Rebuild Search key? You must respond by clicking Yes or No.
For each question, you can specify this information:
- The unique question name that identifies the question across all languages.
- The question type, such as "Warning".
- The question. This is the question text as it is shown when activated. The question text can contain codes
that are substituted when the question is displayed. For details on substitution symbols, see the description
of the sprintf$() function in the Infor ES Programmers Guide (Infor Customer Portal KB2924522).
- The domain belonging to the question, and the default answer. The domain determines the possible
answers to the question. The domain must have the Enumerated data type.
This table shows a sample question:
Question
name
ttaad31022
Question
Type
Warning
Language
Domain
ttyeno 1
ttaad31022
Warning
(Dutch)
ttyeno 2 (English)
Question
Device %1$ geblokkeerd, opnieuw
proberen?
Device %1$ is locked, try again?
Creating questions
To create questions, use the Create a New Infor LN Software Component wizard. To start this wizard, select
File > New > Infor LN Component.
You can use questions within program scripts and libraries using the ask.enum() function.
See this documentation:
- Creating a question on page 107
- The description of the ask.enum() function in the Infor ES Programmers Guide (Infor Customer Portal
KB2924522)
## Report Editor

Use this editor to maintain the properties of a report.
LN reports are used to output data from the database to a variety of devices, such as printers, displays, and
files. One or more LN reports must be linked to an LN print session or to an LN SQL Query. The print session,
or SQL Query, reads the data from the Database tables and the data is printed by the Report objects.
The contents and layouts of reports are defined in the data dictionary. You can link a report script to a report.
In a report script, you can program actions you want to be performed at particular stages of the report
execution. For example, you can create a script to perform calculations on the report data or to read records
from related tables not automatically available to the report.
You program report scripts in the same way as you program 4GL program scripts, except report scripts use
different event sections and special functions. A report script consists of one or more event sections. Here,
you can program actions to be performed at particular states of execution of the report to which the report
script is linked. The statements programmed in a report script section consist of a combination of 3GL language
statements and report script functions.
The report editor consists of various tabs. Each tab is designed to view particular properties or to carry out
specific tasks.
### Overview tab

Use this tab to perform these tasks:
- Maintain general report information.
- Set various options to customize the page design of a report.
- Manage the libraries (DLLs) used in the report script. You can add or remove DLLs.
- View the debug script. In this script you can set breakpoints for the debug process.
General Information
Report
The identification code of the report.
A report is identified by the unique combination of package code, module code, and report code.
Example:
Tools.
Application Administration
Time Zones
Package Code:
Module Code :
Report Code :
tt
aad
046011000
The total identification of the report is: ttaad046011000.
Allowed values:
This field is read-only and can only be set when you create a new report.
Label Name
The code of the report description label.
Allowed values:
This field is read-only and can only be set when you create a new report.
Note: To open the label in the Label Editor, click the Label Name hyperlink.
Description
The description of the report. For example, "Help Topics Overview by Search Argument."
Allowed values:
This field is read-only, because the description originates from a label. To edit this label, click Label Name.
Tools Interface Version
The Tools Interface Version (TIV) number of the script or library. It is used to guarantee backward compatibility
and related to a particular version of the porting set, the Enterprise Server, and the 4GL Tools.
For details about the TIV, see the Infor ES Programmers Guide (Infor Customer Portal KB2924522).
Allowed values:
Whole number in the range 1 - 9999. Initially, the server returns a default version number.
Report Size
The default size of the report.
Allowed values:
To specify a value, click Browse and select a report size from the select dialog box. This dialog box provides
all predefined report sizes in the development repository of the connected LN server.
This table shows examples of available report sizes:
Report Size
A3-SMALL
A3-SMALL-MANU-
AL
A4-LANDSCAPE
Margin
Bot-
Top tom
Foot Length Width Font
Double Wide
User Font 2
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 1
Small (17.1
cpi)
Large (10 cpi)
Large (10 cpi)
A4-LARGE
A4-LARGE-MANU-
AL
A4-MIDDLE
A4-MIDDLE-MANU- 5
AL
A4-SMALL
A4-SMALL-MANU-
AL
- 1
- 1
- 1
- 1
- 1
- 1
- 1
- 1
Middle (12
cpi)
Middle (12
cpi)
Small (17.1
cpi)
Small (17.1
cpi)
For more information on the previous report size parameters, see the Size, Margin, and Font field groups.
Note: The value you enter in this field will have influence on the report's Size, Margin, and Font fields. For
these fields, the selected report size determines the default values and enforces certain constraints.
External Design Present
If this check box is selected, the report has one of these external designs:
- Microsoft SQL Server Reporting Services (SSRS) report design
- Infor Reporting design
A hyperlink to the corresponding additional file is displayed. Click this hyperlink to view the additional file.
For SSRS, you can edit the report design in Microsoft Business Intelligence Development Studio (BIDS). For
more information, see these guides:
- Infor Enterprise Server Plug-in for Microsoft SSRS Development Guide
- Infor Enterprise Server Plug-in for Microsoft SSRS Administration Guide
For Infor Reporting, you can edit the report design in Report Studio. For more information, see these guides:
- Infor Enterprise Server Connector for Infor Reporting Development Guide
- Infor Enterprise Server Connector for Infor Reporting Administration Guide
Font
Report
The font of the report, which is a default for all report layouts. Fonts can be defined in the printer information
files of the used printer.
Allowed values:
To specify a value, select a font from the drop-down list. This list provides all predefined fonts in the
development repository of the connected LN server.
For example, you can choose one of the following fonts:
- Large (10 cpi)
- Small (17.1 cpi)
- Middle (12 cpi)
- Double Wide
- Near Letter Quality
- Italic
- Superscript
Fixed Device Font
If this check box is selected, the specified font cannot be changed when selecting the device at runtime. It
is possible to specify different fonts for each layout in the Different Font fields on the Layouts tab of the
report editor.
If this check box is cleared, it is possible to select another font for the report when you select a device in the
Select Device (ttstpsplopen) session. Each layout is printed with the same font. By default, the report font
is used.
Size
Length
The total page length, including top and bottom margin. If this value is -1, the report can be printed on paper
types with different page length.
Allowed values:
Whole number in the range from 1 to 999.
Value 0 is not allowed.
Value -1 indicates the page length is dependent on the used paper type.
Width
The page width of the report excluding the left margin. The page width is used to set the default width for
new report layouts. It is used for calculating the number of columns of a multi-column layout.
Allowed values:
Whole number in the range from 1 to 255 (value 0 is not allowed).
Nr. of Multi Column
The number of adjacent columns.
This is useful for printing labels, such as addresses of customers.
If the number of columns is 0, the report generator computes how many columns fit on one line.
Allowed values:
Whole number in the range from 0 to 99. Value 0 indicates a calculated number of columns.
Repeat Expression
An expression which is evaluated at runtime. The result is a numeric value, indicating the number of times
each layout on the report will be printed.
Example:
The result of the expression is 2. The report layout will be printed 2 times.
Allowed values:
The expression is an ASCII text with a maximum length of 30 characters.
If you use variables in the repeat expression, these variables must be input fields of the report. See the Input
Fields tab of the report editor.
Margin
Top
The number of blank lines at the top of each report page.
Allowed values:
Whole number in the range from 0 to 99.
Bottom
The number of blank lines printed at the bottom of each report page. These lines are printed just after the
footer section.
Allowed values:
Whole number in the range from 0 to 99.
Left
The number of blank spaces at the beginning of each report line. This left margin is added to the left margin
specified in your report script.
Allowed values:
Whole number in the range from 0 to 99.
Foot
The number of lines allocated for the footer. If the value is -1, the footer margin is calculated by the report
writer.
Note: When a number of different footer layouts of different sizes are executed on conditions at runtime, it
is difficult for the report writer to calculate the footer margin. In this situation, you have to specify a number
of lines for this margin.
Allowed values:
Whole number in the range from 1 to 99.
Value 0 is not allowed.
Value -1 indicates a calculated footer margin.
Linked Libraries
This list contains the records of all libraries linked to the report script of the current report.
Sorting
- To sort the libraries by position, name, or description, click the corresponding column header.
- When you sort by position, the sort mode is always ascending. When you sort by name or description,
click the involved column header to toggle between ascending and descending sort mode.
- When you sort by name or description, the Up and Down commands are disabled.
Add / remove libraries, change linking order
You can only perform the following actions if you sort the libraries by position.
- To add a library, click Add. Then, press Ctrl+Space in the Name field and select a library from the select
dialog box.
- To remove a library, right-click a library and, on the shortcut menu, select Remove.
- To change the linking order of the libraries, move them up or down the list.
Note: To edit a library, click the icon behind the library name.
Pos
The library sequence number (Position). This field indicates the linking order of the libraries.
This field is read-only. It is filled automatically when you link a library.
Name
The name of the library.
Allowed values:
To specify this attribute, press Ctrl+Space and select a library from the select dialog box.
Description
The description of the library.
Allowed values:
This field is read-only. LN Studio automatically fills in the library description after you specified the Name
of the library.
Script
Create Script
Click this button to create an initial report script for the report.
To view or edit the new report script, close the Report Editor, start the Report Editor again, and go to the
Source tab.
Remove Script
Click this button to remove a report script from the report.
View Debug Script
Click this link to open the debug script in the debug text editor. In this script, you can set breakpoints for the
debug process.
See Using breakpoints on page 68.
The debug script is generated automatically based on the report layout and the report script, if present.
### Input Fields tab

Use this tab to maintain the input fields of the report.
The input fields are used to specify the table fields or program scripts whose values must appear in the report.
All variables used in the report must be defined as input fields.
Note: The variables in the program script must be declared as 'extern' on the program script from which the
report is called.
The tab displays a list of all the input fields of the current report.
In the Input Fields list, you can add or remove input fields and change their sort mode. You can insert all
fields of a table definition using the Copy Fields from DD command.
To determine the sort sequence, change the order of the input fields by moving them up or down the list.
When changing the field order, the following constraints prevail:
- You can only change the sort sequence of the sorted input fields (with the sort mode equal to Presorted,
Ascending or Descending).
- The options to change the field order are disabled for non-sorted fields (with the sort mode equal to No
sorting).
- Sorted fields always precede non-sorted fields.
For more information, see Input Field shortcut menu on page 197.
Add and remove input fields
To add an input field:
1 Click Add. Alternatively, right-click in the Input Fields list and, on the shortcut menu, select Add.
2 Specify the Field Name of the new input field. Specify either the name of an external variable of the report
script, or the name of a table field. To select a table field, press Ctrl+Space. In the select dialog box,
choose a table and a field.
3 Specify the Depth (only non-table fields).
4 Specify the field Domain (only non-table fields). Press Ctrl+Space and select a domain from the
development repository.
5 When you finished adding input fields, refresh the Input Fields list, so the new fields are displayed at the
appropriate positions. Right-click in the Input Fields list and, on the shortcut menu, select Refresh.
For details, see the field help.
To remove an input field, right-click an input field and, on the shortcut menu, select Remove. Then, right-click
in the Input Fields list and, on the shortcut menu, select Refresh.
Sort mode
The icon in front of the field name indicates the sort mode of the input field. The following icons are used:
No sorting
Ascending
Descending
Presorted
If at least one input field of a report has sort mode Ascending or Descending, the report will sort the sent data
before printing it. If you are sure the sent data is presorted, use sort mode Presorted, because the sort by the
report is time-consuming.
Sorted fields must have a Depth of 0 or 1, and non-sorted fields can have greater depth values. If you change
the Depth of a sorted field to a value greater than 1, the sort mode of the field automatically changes to No
sorting. This means that the sorted field becomes a non-sorted field.
Note: Only input variables, with sort mode unequal to No sorting, can be used as sorted fields in a report
layout of type Before.field or After.field.
Sort sequence
The position of a field in the Input Fields list determines the sort sequence. The field at the top of the list has
sort sequence 1, the second field has sort sequence 2, and so on.
When you print a report, the sent data is sorted first on the input field with sort sequence 1, then on the input
field with sort sequence 2, and so on.
For example, if you want to sort addresses first by city and then by street, place city at the top of the list (sort
sequence 1) and street on the second position in the list (sort sequence 2).
To move fields up and down the list, use Up and Down.
> [!NOTE]
- You can only move fields with sort mode Ascending, Descending, or Presorted. Non-sorted fields have
sort sequence 99 and are always displayed at the bottom of the list.
- The sort sequence number is not displayed in the Input Fields list. To view this number, go to the editor's
TDE Documentation tab. If this tab is not displayed, enable the corresponding preference setting in the
Preferences - Multipage dialog box and restart the Report Editor.
Input Fields
Field Name
The name of the variable sent by the program script to the report. This variable can be a table field (like
maitm001.item). It can be a variable defined in your program script. This variable must be a global defined
variable, type 'extern'.
Allowed values:
In the report editor, this field is read-only. You can only set the field name when you add a new input field.
For details, see the Add command in the Input Field shortcut menu.
Depth
When the report input variable is an array, this field contains the depth of the array. If the report input variable
is a table field, you cannot change its depth.
If the depth of a field is greater than 1, the field cannot be a sorted field (with sort mode equal to Ascending,
Descending or Presorted).
Allowed values:
If the input field is a table field, the depth of the field is determined by the table definition. Therefore, for
table fields, you cannot change the depth of the field and the depth value is read-only.
If the input field is not a table field and defined as a variable in the report script, you can change its depth to
any whole number in the range of 0 - 99.
> [!NOTE]
- You cannot change the depth of a table field.
- Field depths greater than 1 only apply to non-sorted input fields.
Therefore, for input fields with a depth greater than 1, the Sort Mode command is not available. When
you set the depth of a sorted field to a value greater than 1, the sort mode of this input field automatically
changes to No sorting, and the field becomes a non-sorted field.
Domain
The domain of the report input field.
Only applicable for non-table fields.
Allowed values:
For non-table fields, specify a Domain for the new input field. Select one of the domains available on the
current LN server. Press Ctrl+Space and select a domain from the development repository.
For table fields, the Domain of the field is determined by the table definition. You cannot change this field
domain here.
Note: To edit the domain, click the icon behind the domain name.
Input Field shortcut menu
Add
Adds a new input field record to the Input Fields list.
See Add and remove input fields on page 195.
Remove
Removes the selected input field record from the Input Fields list.
Up
Moves the selected input field up one position in the sort sequence (and in the Input Fields list). This command
only applies to input fields with a sort mode equal to Presorted, Descending, or Ascending.
Down
Moves the selected input field down one position in the sort sequence (and in the Input Fields list). This
command only applies to input fields with a sort mode equal to Presorted, Descending, or Ascending.
Refresh
Refreshes the Input Fields list, so new fields are displayed at the appropriate positions and have the correct
sort sequence assigned. Use this command after you add or remove fields.
Copy Fields from DD
Inserts all table fields of the selected table definition. This table definition must be available on the current
LN server.
This command opens a dialog box that shows all table definitions of the current package. To navigate through
the table definitions available on the server, use the browse and search facilities of the dialog box. To insert
all fields of a table in the Input Fields field, select a table definition and click OK.
No / Ascending / Descending / Presorted
Sets the sort mode of the selected input field.
This command does not apply to input fields with a Depth greater than 1. Such depth fields are always
non-sorted (with sort mode equal to No sorting).
### Layouts tab

Use this tab to display the layouts of a report. Through the layout shortcut menu commands, you can perform
these actions:
- Add or remove layouts.
- Edit the selected layout.
- Edit all layouts simultaneously.
- Copy a layout from another report.
- View the selected layout.
For more information on the Layout commands, see Layout shortcut menu on page 201.
The tab displays a list of all layouts, by their name, used by the report.
Here, you can remove, add/edit layouts, and copy a layout from another report. If you add a layout type that
already exists, ensure the sequence number of the new layout is different from sequence number of the
existing layouts.
For more information about previous layout operations, see Add and remove layouts on page 198.
The Layouts list displays the following layout attributes:
- Layout Type
- Field Name
- No
- Output Expression
Add and remove layouts
To add a layout:
1 Click Add. Alternatively, press Alt+A or right-click in the Layouts list and select Add.
2 Specify the properties of the new layout. See the field help.
3 When you finished adding layouts, refresh the Layouts list, so the new layouts are displayed at the
appropriate positions. Right-click in the Layouts list and, on the shortcut menu, select Refresh.
To remove a layout:
1 Right-click a layout and select Remove. Alternatively, select a layout and press Alt+DEL.
2 Right-click in the Layouts list and select Refresh.
Layouts
Layout Type
The layout type.
Note: You can select a layout type from the list. When you select a layout type that is already used, specify
a sequence number different from the numbers of the used layouts.
Allowed values:
A report can contain the following layout types:
Layouts of this type are printed once at the beginning of the report. Use this layout to present
information about the report. For example, the title page of the report.
Header layouts are printed at the top of every page.
Before.report
Header
Before.field You can define this layout for each input field for which a sort mode is defined. Each time
the value of the sorted input field changes, this layout is printed before the Detail lines. In
this way the records are grouped.
If a group of records spans more than one page, the Before.field layout is repeated at the
top of the new page (following the header).
To suppress automatic printing at the top of every page, use lattr.break as an output expression. lattr.break is a predefined variable that contains the value 1 (true) when the sort
field changes. When you use this output expression, the layout is only printed when the input
variable is changed.
To define multiple grouping levels in a report:
1 On the Input Fields tab, define a Sort Mode and a Sort Seq. for each input field by which
the records must be grouped.
2 Define a Before.field for each of these sort fields.
An example of multiple grouping levels is to group Purchase Order records first by buyer,
and then by buy-from business partner.
The order of sorting and grouping depends on the sort sequence that was specified. This is
the sequence of the fields in the Input Fields list.
Detail layouts are used for the individual records included in the body of the report. They
are printed every time data is sent to the report.
You can define this layout for each input field for which a Sort Mode is defined in the Input
Fields tab. Each time the value of the sorted input field changes, the layout is printed after
the detail lines. In this layout, the presorted input field still contains the old value.
Among other things, this layout can be used to print totals for a particular group of detail
lines.
Footer layouts are printed at the bottom of each page.
This layout is used to print this information:
- Titles
- Page numbers
- Page totals
After.report This layout is only printed at the end of the report, and after all other layouts. If this layout
does not fill a complete page, the footer layout is printed at the bottom of the page, where
the After.report layout(s) is printed.
Detail
After.field
Footer
Note: The Field Name field is applicable only if you select Before.field or After.field layouts.
Field Name
The name of an input field used to activate Before.field and After.field layouts. When the field value changes,
the layout is printed.
Note: Select a field from the list.
Allowed values:
You can only specify fields, which are defined as a sorted input field in the Input Fields tab of the report
editor.
The Field Name attribute only applies to Before.field and After.field layouts.
No.
The sequence number of the layout.
You can define more than one layout per Layout/Fieldname combination. The layouts of the same
Layout/Fieldname are printed in the order of the sequence number of the layouts.
There are two reasons to define more than 1 layout per Layout/Fieldname combination:
- The maximum size of a layout is 22 lines. If your layout needs more lines, make a second layout of the
same type with a higher sequence number.
- If a particular layout must be printed under certain conditions and another layout under other conditions,
define more than one layout with different output conditions.
- If the report already uses the previously specified layout type with the same sequence number, LN Studio
issues the following warning:
Record not unique.
Note: You can only add a layout type that already exists in the current report if the sequence number of the
new layout differs from that of the existing layouts.
Output Expression
An expression which is evaluated at runtime. The result is always true or false. The expression syntax is equal
to the 3GL syntax. When a layout must be printed, the system evaluates the output condition of the layout.
If the result is true, the layout is printed.
Example:
Print result
Layout is always printed.
Layout is never printed.
Layout is printed if variable print.detail is 1 or 2.
Layout is printed if field tdsls041.cprj is not empty.
Output Expression
print.detail = 1 or print.detail =
strip$(tdsls041.cprj) <> ""
Allowed values:
The variables used in the output expression must be defined as input fields for the report.
Allowed values:
The default value is 1. Therefore, the expression is always true and LN will print the layout (if not prevented
by other controls).
Format
Different Font
The font in which the layout is printed.
Note: This field only applies to a report that can have different fonts. You can only specify another font if you
previously selected Fixed Device Font on the Overview tab of the Report Editor.
Allowed values:
These fonts can be defined in the printer information files of the printer being used.
To specify a value for this field, select a font from the drop-down list.
For example, you can choose one of these fonts:
- Large (10 cpi)
- Small (17.1 cpi)
- Middle (12 cpi)
- Double Wide
- Near Letter Quality
- Italic
- Superscript
Extra Need
This number indicates how many extra lines are required for the layout on the same page.
Before printing a layout, the report writer calculates the free space at the current page. If the layout does
not fit on the same page, the layout is printed on a new page. If the value of this field is 0, only the number
of lines of the layout itself is taken into account. With this field you can increase the number of extra free
lines for the layout. This can be useful if you want to print at least 2 detail layouts on the same page together
with a Before.field layout.
Note: This field does not apply to the Header and the Footer layout types.
Allowed values:
A whole number in the range 1-99.
Multi columns
This field indicates whether the report layout must be printed in more than one column or not.
The number of columns depends on the size of the layout and the paper width. Change the layout size with
the command <Esc>[S] in the report layout editor.
Allowed values:
Select one of the following values from the drop-down list:
- None
- Vertical Order
- Horizontal Order
New Page
If this check box is selected, the report layout is printed on a new page. Skipping to a new page always causes
printing of present Header, Footer and Before.field layout types. If the current line is at the top of the page,
the page command is ignored.
Note: This field does not apply to Header and Footer layouts.
Number of Columns
The number of characters or positions per line.
Allowed values:
This display field is read-only. This number is calculated automatically.
Number of Rows
The number of lines of the report layout.
Allowed values:
This display field is read-only. This number is calculated automatically.
Layout shortcut menu
Add (Alt+A)
Adds a new layout record to the Layouts grid.
See Add and remove layouts on page 198.
Remove (Alt+DEL)
Removes the selected layout record from the Layouts grid.
See Add and remove layouts on page 198.
Refresh
Refreshes the list of layouts. Use this command after you added or removed a layout.
Copy
Copies the selected layouts. You can paste the copies in the list of layouts in the current report, or in another
report.
Paste
Pastes copies of report layouts in the list of layouts.
Edit Layout
Opens the selected layout in an ASCII oriented report layout editor (ottadvformedit) of LN. See the online
Help of LN.
Edit All Layouts (Alt+Y)
Opens all layouts in an ASCII oriented report layout editor (ottadvformedit) of LN. See the online Help of LN.
Copy from Other Layout
Copies a layout from another report available in the development repository of the current LN server.
The command starts the Copy from other layouts dialog. In this dialog, choose a report and select one of
the layouts of this report.
This is helpful if you repeatedly use the same elaborate layouts, such as with complex expressions or formats.
### Source tab

Use this tab to view and edit the source code of the report's report script. The tab consists of a script editor,
which forms an integral part of the report editor.
See Script Editor on page 267.
This tab is only displayed, if a report script is linked to the report.
### Documentation tab

Use this tab to enter the report's release notes and technical documentation.
Release Notes
Use this field to specify the release notes of the report.
Technical Documentation
Use this field to specify the technical documentation of the report.
### TDE Documentation tab

Use this tab to view an XML tree with the technical information on the report's Technical Data Entity.
This optional tab is displayed depending on the multipage editor preferences.
See Multipage Editors on page 150.
## Session Editor

Use this editor to maintain the properties of a session.
Sessions are the basic functional elements of LN applications and used to perform actions or tasks.
### Overview tab

Use this tab to specify the general properties for the session.
General Information
Session
The session name that uniquely identifies the session. The name must start with the package code and
module code to which the session belongs.
Label Code
The name of the label that contains the session's description.
To edit or view the label in the Label Editor, click the hyperlink.
Description
The session's description, displayed in the title bar of the session's window at runtime.
Allowed values:
This field is read-only, because the description originates from a label. To edit this label, click Label Code.
Main Table
The session's main table.
Allowed values:
To select a main table, click Browse.
To edit or view the table in the Table Editor, click the hyperlink.
Session Status
The development status of the session.
Allowed values:
Developing
Testing
The session is being programmed.
The session is going through software testing.
Finished
The session is fully programmed and tested.
Synchronized Dialog
The name of an overview session's details session. The details session starts when a user double clicks a
record in the overview session.
Allowed values:
To select a details session, click Browse.
To edit or view the details session in the Session Editor, click the hyperlink.
Main Session
If this check box is selected, the session is a main session and can be placed in a browser menu.
If this check box is cleared, the session is a subsession and cannot be placed in a browser menu. Users can
only start the session through an overview session, or by a specific form command.
InContext Model
The name of the InContext model for this session.
To open the InContext model in the Session Model Editor, click the hyperlink.
If no InContext model exists for the session, click the hyperlink to generate a model. The Session Model
Editor is started.
Related topics:
- InContext Modeling on page 73
- Infor Enterprise Server InContext Modeling Development Guide
- The online help of the Session Model Editor
Table Indices and View Fields
Table Indices and View Fields
Use this field to indicate which indices of the main table are used in the session.
The field displays a tree structure in which the nodes are represented by check boxes. The tree structure lists
all indices of the session and, for each index, the session fields used for this index. By selecting or clearing
check boxes, you indicate which index applies and which index fields are displayed as View fields.
The top level Index check boxes denote the available indices. Select an index check box to indicate this index
is applicable for the session. If this check box is selected, you can activate the index at run time through the
Sort by command in the session's View menu.
The subordinate View check boxes indicate which fields of a selected index are displayed on the form as
view fields. When you select a particular index field as view field, the preceding index fields are displayed as
view fields.
Click Up and Down to move indices up and down the list. The sequence of the indices in the list determines
the order in which indices are displayed when you activate the Sort by command at runtime. The index at
the top of the list is the session's start index.
Session Behavior
Start Command
The session's Start Command.
Specify the default start command or one of the standard commands available to the session (see Standard
Commands field). Alternatively, indicate that the session will not have a start command.
Allowed values:
To specify this field, select a start command from the drop-down list. You can select on of the following
values:
The session uses the default start command that is defined for the session type
concerned.
No command is carried out when the user starts the session.
One of the session's standard commands, as displayed in the Standard Commands
field.
Default Start Command
No Start Command
<Standard Command>
Session Type
Specifies the session's type.
Allowed values:
For overview and details sessions (when not started in read-only mode), in which users can
edit fields.
Type 4 session.
Type 4 session.
Maintain session type, except that users cannot edit fields in an overview session. Users
can edit fields in a details session.
Update session that produces a report.
Print
button is not generated.
Type 4 session.
Type 4 session.
Maintain
Update
Print
Display
Update +
This session type behaves in the same way as a Print session, but at runtime the Preview
Graph
Conversion
Window Type
Specifies the session's window type.
Allowed values:
Modeless window with Deprecated
menu
Deprecated
menu
A modal secondary window, to display or to edit data.
The window is not movable and does not contain a title.
Deprecated
Starts a details window for a details session, and an overview window for an
overview session. If a user zooms to the session, a browse list starts for the session.
Modal window with
Dialog
No Window
Synchronized dialog
List Window (default
value)
Wizard
Parameter
Multi Main Table
A wizard window starts for the session. A wizard window usually consists of a
sequence of dialog boxes in which you must enter the required details, and
through which you can move forwards and backwards.
LN contains various sessions with a wizard window, for example:
- Export Language Dependent Data to XML - Wizard (ttadv8910m000) and
- Import Language-Dependent Data from XML - Wizard (ttadv8920m000)
A parameter window starts for the session.
LN contains various sessions with a parameter window, for example
- Infor Data Navigator Server - Parameters (ttgfd4124m000) and
- ART Parameters (ttaad6102s000)
A Multi Main Table window starts for the session. Use this window type for Multi
Main Table (MMT) sessions.
An MMT session is a combination of multiple sessions, each having their own
main table, and is used to present data with a typical parent-child structure. For
example: a Sales Order and the related Sales Order Lines.
The window of an MMT session consists of 2 parts:
- The upper part shows parent information. For example, a Sales Order.
- The lower part shows the child information. For example, the related Sales
Order Lines.
Note: The child satellite sessions of a MMT session are maintained on the
Satellite Sessions tab of the session editor.
Reports in several languages
If this check box is selected, you can print the session's reports in languages other than the runtime language.
> [!NOTE]
- Dependent on software delivery (see the Import- / Export functions module). You can only print reports
in the languages you select in the Languages to Deliver by Language (ttiex0101m000) session.
- You can manage multilingual report printing in the session's UI script.
Standard Commands
Use this field to enable / disable the standard commands of a session.
Note: Click St. Command set to start a dialog where you can select a standard command set for the session.
The commands of the selected command set are displayed in this field.
The field displays a tree structure in which the nodes are represented by check boxes. The tree structure lists
all standard menus for sessions and the standard commands for each menu. Select or clear check boxes to
indicate which standard commands and associated menus are used.
The top level Menu check boxes denote the standard menus. Select a menu check box to select all standard
commands of this menu. Clear a menu check box to clear all commands of the menu. The menu check box
shows a greyed out check mark if some commands of the menu apply and some do not.
The subordinate Command check boxes indicate which standard commands are used for the session. For
every standard command a check box is available. Select a check box to enable the command at runtime.
Clear a check box to disable the command at runtime. The command preferences set in this field can be
overruled by the program script, DAL script, or the user authorization settings.
BFlows
List of BFlows that are linked to the session.
To add a BFlow using the Create a New Infor LN Software Component wizard, click the Add button next
to the grid.
### Script tab

Use this tab to specify properties of the session's UI script and to link libraries to the session.
To edit or view the UI script, go to the Source tab.
General Information
Standard Script
The session's standard script type.
Allowed values:
No standard script is used. You must specify a UI script in the UI Script field.
If you change the Standard Script from 'Type 1/2/3' or 'Type 4' to value 'No', the
editor will automatically generate a script name.
The session is based on a main table and uses a standard script.
ble)
The session is not based on a main table, but uses a standard script
ble)
No
Type 1/2/3 (With M.Ta-
Type 4 (Without M.Ta-
> [!NOTE]
- If you specify a standard script, you cannot specify a UI script.
- When you specify a non-standard script (value 'No'), the editor creates a session reference that can be
used as an alias for the session's script.
Allowed values:
No
UI Script
The name of the program script.
A script is identified by its unique name, which is the combination of the package code, the module code,
and a script code.
The name and description of the script generally corresponds with the name and description of the session,
with the exception of existing sessions with an anomalous name. When you add a script to a script-less
session, the session editor will automatically generate a script (skeleton) with a name and description derived
from the associated session.
Example:
LN Manufacturing
Product Configuration
Package Code:
Module Code :
ti
pcf
Script Code :
Maintain Features
The total identification of the program script is: tipcf0110
Session reference
The session that owns the UI script of the current session. Click Browse and select the session from the list.
UI script ownership
Each session, which does not use a standard script, is linked to a UI script. Each UI script is owned by a session.
A UI script can be used by multiple sessions, but has only one owner. For example, sessions tetst0101m000
and tetst0101s000 both use the UI script tetst0101. Session tetst0101m000 is the owner of the script. For
both sessions, the following properties apply:
Session reference
tetst0101m000
tetst0101m000
Session
tetst0101m000
tetst0101s000
UI Script
tetst0101
tetst0101
> [!NOTE]
- You can only edit a UI script via the session that owns the script.
- When you create a new session with a UI script, LN Studio automatically assigns the new session as the
owner of the new script.
- If a script is not owned by a session, use the Check and Convert UI-Script Ownership (ttadv2930m000)
session to assign a session as the owner of the script.
If a script is already owned by a session, you can use this session to assign a different session as the
owner of the script.
To change the session reference
When you change the session reference, the UI Script field is automatically updated and filled with the script
code of the referenced session. This referenced session must be a script owner.
In the Session reference field, you can specify the code of the current session itself. If you do this, a new,
unique, script is assigned to the session. The new script is a copy of the script that belongs to the previously
referenced session. The code of the new script is identical to the code of the current session.
If the Session reference field is filled with the code of the current session, you cannot change the session
reference, because this would leave the script without an owner.
Expire / Unexpire sessions
A session can only be expired if there is no reference to it from another not-expired session.
A session cannot be unexpired if it has a session reference to an expired session.
Script Type
Specifies the use or nature of the session's program script.
- You can only edit a UI script via the session that owns the script.
- When you create a new session with a UI script, LN Studio automatically assigns the new session as the
owner of the new script.
- If a script is not owned by a session, use the Check and Convert UI-Script Ownership (ttadv2930m000)
session to assign a session as the owner of the script.
If a script is already owned by a session, you can use this session to assign a different session as the
owner of the script.
This field only applies if the session does not use a standard script, which implies that the Standard Script
field is set to 'No'.
For sessions without standard scripts, you can use the following script types:
A 4GL user interface script is used for display and maintain sessions. The
script is called by the 4GL engine (standard program) on certain events.
A 4GL user interface script is used for print and processing sessions. The
script is called by the 4GL engine (standard program) on certain events.
A 3GL script has no interaction with the 4GL engine (standard program).
Therefore, all logic of the program must be included in this script.
Examples of 3GL scripts are the well-known General Table
(ttaad4100/ttaad4500) sessions.
UI Script with Database handling
UI Script for Print/Processing
Sessions
3GL (Without 4GL Engine)
Compile Flags
The compile flag.
In (3GL and 4GL) sources, use compile flags to compile a part of the source depending on certain conditions.
This is called conditional compiling. For more information on conditional compiling and other compile
options, see the "Preprocessor" and "Compiler" sections of the Infor ES Programmers Guide (Infor Customer
Portal KB2924522).
Example:
| Compile Flag: -DMYTEST | Source ... #if MYTEST message(Some debug information) #endif ...

You can specify several compile flags separated by a space " ". For example:
Compile Flags: -DMYTEST -DVERSION_1 -DVERSION3.0
Note: The preprocessor only works during compilation of a 3GL source. This is because the standard generator
std_gen6.2 does not have a preprocessor pass. Therefore, you cannot use 4GL events in a #if, #ifdef or #ifndef.
Tools Interface Version
The Tools Interface Version (TIV) number of the script/library.
This is used to guarantee backward compatibility and is related to a particular version of the porting set, the
Enterprise Server and the 4GL Tools. For example, the TIV number for Enterprise Server 7, delivered together
with LN 6.1 FP1, is 1010. When you insert a new library, the TIV is automatically set to the highest supported
TIV number.
Setting a TIV number for each object can result in the behavior of these objects being different. This can
occur for incompatible features executed with different versions of the porting set or the LN 4GL Engine.
For example, the "set.synchronized.dialog" function was changed in TIV 1000. Therefore objects in which
this function is used, show different behavior for different TIVs:
- If the object's TIV is less than 1000, a synchronized dialog is started when a record is inserted or duplicated
in an editable grid.
- If the object's TIV is 1000, no synchronized dialog is started when a record is inserted or duplicated: the
new record is entered directly in the grid.
For details about the TIV, see the Infor ES Programmers Guide (Infor Customer Portal KB2924522).
License
Product ID Source
The product ID for which a license is needed to compile the object. If the field is empty, no license is needed
to compile the object.
Note: This field only applies to internal Infor development systems. For other development environments,
this field is not available.
Allowed values:
To select a product ID, click Browse.
Product ID Object
The product ID for which a license is needed to run the object. If the field is empty, no license is needed to
run the object.
Note: This field only applies to internal Infor development systems. For other development environments,
this field is not available.
Allowed values:
To select a product ID, click Browse.
Linked Libraries
This list contains the records of all libraries linked to the UI script of the current session.
Sorting
- To sort the libraries by position, name, or description, click the corresponding column header.
- When you sort by position, the sort mode is always ascending. When you sort by name or description,
click the involved column header to toggle between ascending and descending sort mode.
- When you sort by name or description, the Up and Down commands are disabled.
Add / remove libraries, change linking order
You can only perform the following actions if you sort the libraries by position.
- To add a library, click Add. Then, press CTRL+SPACE in the Name field and select a library from the select
dialog box.
- To remove a library, right-click a library and, on the shortcut menu, select Remove.
- To change the linking order of the libraries, move them up or down the list.
Note: To edit a library, click the icon behind the library name.
Pos
The library sequence number (Position). This field indicates the linking order of the libraries.
This field is read-only. It is filled automatically when you link a library.
Name
The name of the library.
Allowed values:
To specify this attribute, press CTRL+SPACE and select a library from the select dialog box.
Description
The description of the library.
Allowed values:
This field is read-only. LN Studio automatically fills in the library description after you specified the Name
of the library.
Documentation
Release Notes
Use this field to specify the release notes of the UI script.
Technical Documentation
Use this field to specify the technical documentation of the UI script.
### Source tab

Use this tab to view and edit the source code of the session's UI script. The tab consists of a script editor,
which forms an integral part of the session editor.
See Script Editor on page 267.
This tab is only displayed, if the source code of the UI script is available.
### User Interface tab

Use this tab to specify the form properties, link reports and charts to the session, and specify text fields.
Form
Edit/View Form
To edit or view the form in the Dynamic Form Editor (DFE), click the Edit/View Form hyperlink.
Label of Object
You can enter a label name in this field. At runtime, the label is visible in the pull-down menu of the session
if the session belongs to a multi-main table session.
Allowed values:
To specify this field, click Browse and select a label name from select dialog box.
Customization prohibited
If this check box is selected, , the customize form functionality in a details session and the customize visibility,
ordering and width of columns functionality in an overview session is disabled if the session is started from
Web UI.
Default Button
Command Type
Select the command type of the session's default button.
Allowed values:
The default button is disabled.
Not Applicable
Standard Command
Form Command
The default button starts a standard command.
The default button starts a form command.
Default Button
Select a command for the session's default command button. The default command button is the command
LN carries out when a user presses the Enter key whilst using the session. The default command button is
always the first button in the list of command buttons included on a session's form.
Allowed values:
Session's default command button is disabled.
One of the session's Standard Commands.
mand
One of the session's Form Commands.
Not Applicable
If Command Type is Standard Com-
If Command Type is Form Command
## Dynamic index switching

Select the session's dynamic index switching options.
You can only enable dynamic index switching if the current session has a Main Table. For sessions without
a main table, disable dynamic index switching. To do this, select value 'No'.
Allowed values:
When a user chooses a new index, the view fields and session layout do not
change. Select this value if the session does not have a main table.
The session restarts when a user chooses a new index, which alters the view
fields displayed above the session's grid.
The session restarts when a user chooses any new index.
No
Restart when view-fields
differ
Always restart
Related topics:
- Dynamic index switching on page 234
- Dynamic session
- Integrated session
Show name of index
If this check box is selected, the session's title bar displays the current index for overview sessions with
dynamic index switching implemented.
The check box is disabled if Dynamic Index Switching has value ‘No’.
Workflow / Web UI
Workflow Enabled
Use this field to specify whether the session can run in a Workflow environment.
Allowed values:
Select one of the following values from the drop-down list. Only three values of the list have a meaning, as
indicated in the table below.
Value
Not checked
Single / Redoable
Single / Not Redoable
Container / Redoable
Container / Not Redoable
Single / Container / Redoable
Single / Container/ Not Redoable
Not Workflow Enabled
Description
The session has not been checked in a Workflow environment
The session has been checked in a Workflow environment and executed
successfully
Not used
Not used
Not used
Not used
Not used
The session has been checked in a Workflow environment but failed
Web UI Enabled
If this check box is selected, you can successfully run this session in a Web UI environment.
Reports
List of all reports linked to the current session. The reports are listed by report group.
You can add or remove reports:
- To add a report to a session, click Add. The Select a Report dialog box starts. Click Browse and choose
a report. Then, specify a report group number and click OK.
See the online help of the Select a Report dialog box.
- To remove a report from a session, right-click the report and select Remove.
You can drag and drop reports from one report group to another.
To change the sequence of the reports in a report group, move them up or down the group list.
Charts
List of all charts linked to the current session. The charts are listed by chart group.
You can add or remove charts:
- To add a chart to a session, click Add. The Select a Chart dialog box starts. Click Browse and choose a
chart. Then, specify a chart group number and click OK.
See the online help of the Select a Chart dialog box.
- To remove a chart from a session, right-click the chart and, on the shortcut menu, select Remove.
You can drag and drop charts from one chart group to another.
To change the sequence of the charts in a chart group, move them up or down the group list.
Text Fields
List of all text fields of the current session (text fields are table fields of data type text).
You can add or remove text fields.
To add a text field to a session:
1 Click Add.
2 In the Name field in the grid, press CTRL+SPACE to start a dialog where you can select text fields.
3 Select the desired text field and click OK. The text field is displayed in the grid.
4 Complete one of these steps:
- Clear the Writable check box, so users can only read the text.
- Select the Writable check box, so users can also edit the text.
The text authorizations by text group, defined in the Text manager module, always have priority over
the authorizations you define in this grid. For example, a user is not authorized to change texts in text
group ABC. Therefore, even if this check box is selected, he cannot edit a text that belongs to text group
ABC.
To remove a text field from a session, right-click the text field and, on the shortcut menu, select Remove.
To change the sequence of the text fields, move them up or down the list. The sequence in the Session editor
corresponds with the order in which the text fields are displayed in the session at runtime.
### Form Definition tab

> [!NOTE]
- To use this tab, Enterprise Server 10.5.2 is required.
- You can only use this tab to customize forms for LN 10.5 or later. To customize forms for older LN versions,
you must use the Infor LN Dynamic Form Editor. See the Dynamic Form Editor documentation.
Use this tab to maintain the form of the session. The tab consists of these sections:
- Overview
This section shows the form's session, group and field elements. If you select an element in the tree, the
corresponding element details are displayed in the Details section.
The tree supports cut/copy/paste and drag/drop functionality.
You can expand or collapse all nodes of the tree by clicking the icons above the tree. Type in the filter
text box to only display elements with names that contain the entered text and elements with child
elements that have names that contain the entered text.
Select Add Table Fields on the shortcut menu to open the Table Fields view. To add an element to the
form, drag and drop an element from another form or from the Table Fields view, or use the shortcut
menu of the tree.
- Documentation
This section shows the technical documentation and the release notes of the element selected in the
Overview section.
- Details
This section shows the details of the element selected in the Overview section.
Session Properties
General
Use this dialog box to maintain the properties of the session.
Overview Session
If this check box is selected, the form can be displayed as an overview session.
Details Session
If this check box is selected, the form can be displayed as a details session.
Rich view
This setting only applies to the view area of an overview session.
If this check box is selected, the form's view has more features. A rich view can contain group boxes, field
buttons, and group boxes beside each other.
If this check box is cleared, the form's view does not contain groups.
We recommend that you select this check box in these situations:
- If the layout of the form differs from what you expected.
- If you create a form for a new session.
Subgroups on New Page (Details)
If this check box is selected, all subgroups of the main group start on a new page on a details session. This
option does not apply to repeating groups.
Subgroups on New Page (Overview)
If this check box is selected, all subgroups of the main group start on a new page on an overview session.
This option does not apply to repeating groups.
If this check box is selected and the layout of the form differs from what you expected, then also select the
Rich view check box.
Group Properties
General
Group Number
The group's number in the program script.
Label Code
Type or select the code of the label that you want to use as the group box header.
Group Description
The group's label as displayed on a group box.
Tab Description
The group's label as displayed on a tab.
Alignment
Default
If this check box is selected, the fields in the first column are positioned on the same x-position as those fields
in groups with the same alignment, or with Dependent alignment. For the subsequent columns only the
fields within a group are aligned with each other.
Dependent on Other Groups
If this check box is selected, the fields in all columns in all groups with the same alignment are aligned with
each other. For the first column the groups with the default alignment are also taken into account.
Independent
If this check box is selected, the fields in all columns of that group are aligned with each other. Other groups
are not taken into account
Next to other Group
If this check box is selected, the group is displayed next to another group. If you select the Subgroups next
to each other check box for the parent field, you can create columns of groups.
Subgroups next to each other
The number of subgroups that must be displayed next to each other. Only child groups for which the Next
to other Group check box is selected are placed next to each other. Ensure that the child groups that are
placed next to each other do not have subgroups.
Options
Details Session
If this check box is selected, the group is displayed in the details session.
Overview Session
If this check box is selected, the group is displayed in the overview session.
Repeating Group
If this check box is selected, the group is displayed on all tabs where the parent group is displayed at runtime.
Only the first subgroup of a parent group can be repeated on the form's tabs. Ensure that the repeating group
has no subgroup.
Button Group on Dashboard
If this check box is selected, the group is displayed as a button group in Web UI. Therefore, in Web UI, only
check boxes with a form command linked to it are displayed. The check boxes and buttons in this group will
also get a different appearance. The check box is displayed as an icon, the button is displayed as a hyperlink.
Show Group Box
If this check box is selected, the group is displayed in a group box. You must specify a label for the group in
the Label Code field. If you select this check box for both the parent-group and a subgroup, only the parent
group has a group box.
First Checkbox on Group Box
If this check box is selected, and if the Show Group box check box is selected, a check box is displayed as
the first field in the group box. The fields in the group box are automatically enabled or disabled when the
check box on the group box is selected or cleared.
Selection Group
If this check box is selected, the group is handled as a selection group. The group may become disabled if
this session is started from another session in which the user already made a selection. The printing/processing
is then performed based on the selection the user made in the parent. For this you must do some programming.
See the Infor ES Programmers Guide (Infor Customer Portal KB2924522), function sel.use.parent.selection.
If this check box is selected, a new field is displayed in the form definition. In this field the user indicates
whether the selection of the parent or a selection range is used. The new field is displayed above the group.
Note: This field is displayed if you edit a print or processing session.
Table of Parent Session
Indicate the main table of the parent session for which this session can handle the selection.
Note: This field is displayed if Selection Group is selected.
Field Properties
General
Use this tab to specify the form field's general data.
Note: You can only change a domain for a non-table field.
Field Type
The form field type.
This table shows the available options:
Option
Label
Display
Input
Display on Demand
Workflow Status Field
Description
The field is only used as a label on the form.
Normal display field, input not allowed.
Normal input field.
Display is only possible on this form field if the LN
4GL function display <field name> is used in the
program script.
Special field type reserved for the ION Workflow integration. This type of field can only be generated
through the Workflow Status Field command on
the Insert menu. You cannot add such a field manually.
Input on a form field also depends on the input expression. A form field can be a temporary display field if
attr.input is set to false in the before.input section of the field in your UI script.
Field Name
The name of the form field. You can use a table field or a non-table field. The domain and data type of the
table field are automatically filled for a table field. A non-table field can only be used if it is defined in the UI
script of the session for which the form is created. The program variable must be defined with the keyword
extern. The domain of the variable must be equal to the domain defined in the form. A domain and its data
type are not automatically filled for a non-table field. If you use a field without a domain, you can specify
label.only.
Element
If the specified field is an array, it specifies the element number of the table field., Use the Multi Currency
check box on the Miscellaneous tab to indicate that the field is a multi currency field. Do not specify -1 in
the Element field as an element number to indicate that the field is a multi currency field.
Domain
The domain. You can select the domain manually, or zoom to the Browse domains dialog to make a selection.
Note: You cannot modify the domain of table fields.
Segmented
If this check box is selected, the field is a segmented field. A segmented field is logically divided into chunks
called segments. This check box is read-only.
Initial Form Field Value
If the Form Field check box is selected, you can define an initial value in the field next to the Form Field
check box for a new record. If the Form Field check box is cleared, the initial value of the table field is used.
If the Form Field check box is cleared, and the field is not a table field, the value of the previous record is
used if the end user creates a new record in the session.
Mandatory Input
If this check box is selected, input on this form field is mandatory at runtime.
> [!NOTE]
- If the data type of the form field is byte, integer, long, or float, the value of the field at runtime must not
be 0, even if in the domain 0 is defined as a legal character.
- If the table field is already mandatory, this check box is selected and cannot be cleared.
Linked Form Command
The form command that is linked to the field. This field shows the code of the object it executes. If no form
command is linked to the field, the field is empty.
Field Sequence Number
The sequence number of the field. This is the number that is used when linking a form command to the field.
Besides, the sequence number also determines the tab order.
UUID
The Universally Unique Identifier (UUID) of the field. The UUID uniquely identifies the field on the form and
is used by the session personalization functionality in Web UI.
The UUID is generated automatically and cannot be changed.
Note: This field is only displayed if you use Enterprise Server 8.5.1 or later.
Label
Use this tab to specify the form field's label data.
If the appropriate check boxes are selected in the Session Properties, Group Properties, and Field Properties
dialog boxes, the form field is displayed in a details session or an overview session.
If the field is an option set, the descriptions of the enumerates are used in the details session. On the overview
session the field is displayed as a listbox.
Label
The label code. You can insert a label manually, or zoom to the Browse labels dialog.
Details
Position
The position of the label in relation to the field in the details session. This table shows the available options:
Description
The label and field are placed side by side. The label
is right aligned.
The label and field are placed side-by-side. The label
is left aligned.
You can only select this option for label-only fields.
The label is positioned with the controls of other
fields in the group.
Option
Before (right aligned)
Before
Above
Length
The length of the label in a details session or an overview session. The length of the label is used as a selection
criterion. A label is selected within the reserved length. If no such label is found, the shortest possible label
that is longer than the reserved length is selected. If the label's length is 0, the label is not displayed in a
details session.
Height
The height of the label in a details session or in an overview session. If no label is found with the specified
number of lines, a label with additional lines is used.
Overview
Link Label Length to Field Length
If this check box is selected, the length of the label is linked to the length of the form field in a grid.
Length
The length of the label in the grid of an overview session.
Note: The length of the label is used as a selection criterion. A label is selected within the reserved length.
If no such label is found, the shortest possible label that is longer than the reserved length is selected. If the
label's length is 0, the label is not displayed in the grid of an overview session. If the label's length is smaller
than the width of the column, the column's width is used to select a label.
Height
The height of the label in the grid of an overview session.
Note: The height of the label is used as a selection criterion for a label. If no label is found with the specified
number of lines, a label with additional lines is used.
Position
Use this tab to specify the form field's position on the form.
If the appropriate check boxes are selected in the Session Properties, Group Properties, and Field Properties
dialog boxes, the form field is displayed in a details session or an overview session.
Details Session
If this check box is selected, the form field is displayed in the details session at runtime.
Overview Session
If this check box is selected, the form field is displayed in an overview session at runtime.
Note: A dependent child field can be removed at runtime without removing its parent field. For example, as
a result of authorization limitations.
Allowed in Grid
If this check box is selected, the form field can be displayed in the grid. If this check box is cleared, the form
field is not displayed in the grid.
View Field
If this check box is selected, the current form field is a view field displayed above the grid when an overview
session is started. If the Dependent on Parent Field check box is selected, the View Field property is not
relevant, because its value is the same as the value of its parent field. So a dependent field is displayed in
the view, when its parent also is displayed in the view; otherwise the dependent field is displayed in the grid,
when the overview session is started.
Occurrence Independent
Select this check box if the value of the current form field is not dependent on the actual occurrence. This
only applies for view fields that are not part of the main table and are specified as a view field in the session
editor.
Dependent on Parent Field
If this check box is selected, the current form field is dependent on another field. That other field can be a
parent field or, if the parent is not a field, the field above the current form field. If the other field is displayed,
the current form field is displayed behind or below the field, depending on the relation between the two
fields.
Note: You can remove a dependent child field at runtime without removing its parent field. For example, as
a result of authorization limitations.
Child Fields Behind
If this check box is selected, the child field is displayed immediately behind its parent field.
Note: If the child field is not positioned immediately behind the current field, the child field is aligned with
other child fields in groups with the same alignment.
Behind Enum constant
If the parent of the current form field is an option set, specify the radio button behind which the field must
appear.
Note: Do not use structures of more than one row behind an option set.
Hidden (Details)
If this check box is selected, the form field is invisible in the details session at runtime.
Users can make the field visible through the Personalize Form command.
Administrators can centrally maintain these personalizations through the Session Personalizations
(ttadv9100m000) session.
Hidden (Overview)
If this check box is selected, the form field is invisible in an overview session at runtime.
Users can make the field visible through the Personalize Form command.
Administrators can centrally maintain these personalizations through the Session Personalizations
(ttadv9100m000) session.
Display
Use this tab to specify form field's display data.
Minimum Input Length
The minimum number of characters that must be used for input on the form field.
Display Height
You can specify a display height in this field if the field has a domain of type text.
Data Alignment
Type or select the alignment of the data within a non-grid-field. In the grid, for numeric fields the field
alignment is linked to the domain. The alignment of date fields is always linked to the display format. Other
types of fields are always linked to the domain.
Maximum Input Length
The maximum number of characters that must be used for input on the form field.
According to Domain
If this check box is selected, the value is linked to the domain. To specify another value, clear this check box
and specify a value in the field.
Maximum Display Length
The maximum number of characters that can be displayed in the form field.
According to Domain
If this check box is selected, the value is linked to the domain. To specify another value, clear this check box
and specify a value in the field.
Display Format
You can specify a display format in this field.
According to Domain
If this check box is selected, the value is linked to the domain. To specify another value, clear this check box
and specify a value in the field.
Miscellaneous
Use this tab to specify the form field's miscellaneous data.
Input/Reference Expression
The input condition or reference expression of the form field.
Input condition: The input condition determines the condition for which input on the input field is allowed.
For example, if the input condition is price > 0, the input is only allowed if the value of the price variable is
greater than 0.
Reference expression: The reference field or reference path can be used if a table field from a table other
than the main table is used. This can be used if the main table refers twice to a reference table.
Examples:
- tdsls000.item1 (reference field)
- tdsls000.item2, tiitm001.item (reference path)
> [!NOTE]
1 Declare the variables that are used on these fields with the keyword extern in the UI script.
2 You can also set attr.input to false in the before.input section of the field in your UI script.
3 The input changes the field into a display field and it overrules the input expression.
Language/Generic Unit Expression
This field has two functions:
1 If the data type of the form field is Date or String, the field can contain an expression that defines the
language for which the date must be displayed.
2 If the form field has a display format %A <currency format> and the data type Double or Float, a currency
can be displayed on the form field. This field can contain an expression that defines the currency code
for which the amount is displayed.
Note: This field can only be used if the data type of the form field is Float, Double, Date, or UTC.
Start Position String
The start position of the string in the form field. You can only specify a start position for a form field with the
String data type.
Message
The message code that is displayed on the bottom line of the dialog box. You can insert the message code
manually, or zoom to the Browse messages dialog to make a selection
Echo Field
If this check box is selected, the value of the form field is displayed on the form.
Synchronized Field
If this check box is selected, the current form field's input on the client is synchronized with the server.
Typically, in page mode, the client interacts with the server for each page to reduce network transactions.
If necessary, you can use this option to ensure that the client interacts with the server for this field instead
of waiting for the page's end.
Multiple Currency Field
If this check box is selected, you can use the form field for more than one currency, such as US$ or Euro. As
a result, the element number is set to -1.
Zoom
Use this tab to specify the form field's zoom data.
Zoom
Specifies if the form field is a zoom field and, if so, where it zooms to.
These options are available:
- No
- Session
- Menu
Zoom To
The menu or session code that can be activated from this form field. You can specify a menu or session
manually, or zoom to the Browse menus dialog or to the Browse sessions dialog to make a selection.
If this field is filled with a session code, in Web UI auto-complete is enabled on the form field.
If the zoom functionality has been scripted, we recommend that you leave this field blank.
If auto-complete does not make much sense, because it will show a lot of entries that are actually not valid
in the specific situation, you can switch auto-complete off for the form field by using the fields.autocomplete
function.
Return Field
The name of the table field in the zoom process whose value is returned to the form field in the main process.
You can specify a table field manually, or zoom to the Browse Table Fields dialog to make a selection.
Start Index of Zoom Session
If the current form field zooms to a session, you can specify in this field the index with which the zoom session
starts.
Description Field
If a table field has a reference to another table, you can specify in this field which field from the reference
table must be used as a search description. For example, for a form field that shows an item code, the user
would like to type (part of) the description of that item instead of the code. In this field, you can specify the
table field that contains that description.
In Web UI auto-complete also shows the description in the suggestion list. The look-up returns items that
match by description, besides the ones that match by code.
Note: This option is only valid for (multibyte)string fields.
Appearance
Use this tab to specify how the form fields with data type Enumerate or String are displayed on the form.
Note: The data in this dialog box only applies to form fields that have a domain of data type Enumerate or
String.
Enumerate
Check Box
If this option is selected, the form field with data type Enumerate is displayed as a check box. You can select
this option if there are only two enumerate values in the domain of this field.
Constant value for 'Yes'
If the form field is displayed as a check box, specify the value that represents the checked value.
List Box
If this option is selected, the form field with data type Enumerate is displayed as a list box.
Option Set
If this option is selected, the form field with data type Enumerate is displayed as an option set.
Automatic enable and disable children
If this check box is selected, and the parent field is an option set, the child fields of the parent field are
automatically enabled and disabled when the option is selected or cleared.
String
Normal String
If this option is selected, the form field with data type String is displayed as a normal field.
List box
If this option is selected, the form field with data type String is displayed as a drop-down list box.
Combo box
If this option is selected, the form field with data type String is displayed as a drop-down combo box.
URL Area
If this option is selected, the form field with data type String is displayed as an embedded URL Area. The URL
itself is defined by the 4GL application script and can be dynamically based on business functionality.
> [!NOTE]
- The URL area option is available for the form field type Display.
- The URL area cannot be part of a grid. Within an Overview session the URL area is part of the view area,
analogous to an Image field.
- The display width and height of the URL area field must be defined to set the runtime dimensions. Default
width: 40, height: 5.
- To show the URL area on the form, you can use the get.bi.server.location() 4GL function to load the
URL. For details, see the Infor ES Programmers Guide (Infor Customer Portal KB2924522).
- Minimal requirements:
- Application VRC TIV level 2020
- LN UI version 11.2.2
Long
A form field with data type Long can be displayed as a normal field or as a color field. In a color field, users
can select a color from a pre-configured palette.
Normal
If this option is selected, the form field is displayed as a normal field.
Color Field
If this option is selected, the form field is displayed as a color field. The selected color and its hex code are
displayed in the trigger area.
Color Field (swatch only)
If this option is selected, the form field is displayed as a color field. The selected color is displayed in the
trigger area.
Duration (Days and Time)
If this option is selected, the form field is displayed as a time duration field, consisting of both a days and a
time segment.
Note: This field is displayed if you use Enterprise Server 10.5.2 or later.
Duration (Time Only)
If this option is selected, the form field is displayed as a time duration field, consisting of only a time segment.
Note: This field is displayed if you use Enterprise Server 10.5.2 or later.
### Form Commands tab

Use this tab to maintain the form commands for the session.
All Form Commands
List of all form commands of the current session. The tree structure of the list mirrors the menu hierarchy of
the commands.
A form command can have activation types Function, Session, Business Method, or Menu. Therefore, the
command can invoke these types of activation objects. LN Studio uses the following icons to denote these
activation types:
Function
Session
Business Method
Menu
In the All Form Commands field, you can add and remove form commands:
- To add a form command to a session, click Add. The Create a New Form Command wizard starts. Specify
the properties for the new form command and click Finish.
See the online help of the Create a New Form Command wizard.
- To remove a form command from a session, right-click the form command and, on the shortcut menu,
select Remove.
The tree structure of the displayed form commands mirrors the menu hierarchy of the form commands in
the runtime session. Form commands of type menu can have child nodes, which must be commands of another
activation type. Menu commands cannot contain child items of type menu command. A command that does
not activate a menu cannot have child nodes. The Session editor only supports one level of submenus.
Therefore, a menu command can only have child nodes and cannot have grandchild nodes.
To change the menu structure, drag and drop a form command from one location to a menu command or
to the root of the tree structure. In the latter case, the command appears, at runtime, directly under the
session's appropriate menu.
To change the sequence of the form commands in a menu, move the commands up or down the command
list of a specific menu.
Form Command Properties
Activation
Activation Type
Activation Type specifies what your form command activates. You can select the activation types from the
drop-down list. The used type names are self explanatory.
Allowed values:
- Function
- Session
- Business Method
- Menu
Function/Session/Business Method/Menu
The name of the function, session, business method, or menu that the form command activates.
Allowed values:
- A session or menu available in the development repository of the connected LN server. To select a session
or a menu, click Browse.
To open the selected menu or session in the corresponding editor, click the Menu or Session hyperlink.
- An external function in the session's UI script. You can select a function from the drop-down list.
To view or edit the selected function in the script editor, click the Function hyperlink.
- A business method in the session's UI script, or DAL script. You must type in the code of the business
method.
Command Type
Command Type specifies where the form command appears on the session's form. You can select the
following command types from the drop-down list:
Allowed values:
Form For all of the session's form tabs, the form command appears on the form's appropriate menu, and/or
as a button on the form.
appropriate menu when a user selects the tab that includes the group you define in the Group/Field Number
field. Sequence NumberGroup/Field Number
Group Number / Field Number
This field specifies the group to which the form command belongs, or the sequence number of the field linked
to the form command. Whether this field specifies a group or a sequence number depends on the value you
entered as the Command Type: Group or Field.
This field only applies to form commands of type 'Group' or 'Field'. The field is disabled for the other form
command types ('Form' and 'Print').
The field has a dynamic name derived from the command type: Group Number or Field Number.
For form commands of Command Type Group, select the group to which the form command belongs. The
form command only appears in the session's appropriate menu when the user selects the group's tab.
For form commands of Command Type Field, select the field behind which the form command appears as
a field button.
The pull down list shows the numbers and label codes of the available groups or fields.
Allowed values:
To specify this field, select a value from the drop-down list.
Category
The form command category used by Infor LN UI. The category determines the pull-down menu in which the
command is displayed.
Allowed values:
The command is displayed in the session's Action menu.
The command is displayed in the session's Reference menu.
ence
The command is displayed in the session's Views menu.
The command is displayed in an additional pull-down menu, which is specific to the session.
category, you must select one default command. The description of this default command is
displayed on the special category's menu button.
Specify a short description in the Short Description field. If you leave the Short Description
field empty, the Long description is displayed on the menu button, so the button becomes too
large.
Action
Refer-
View
Special
Use the Special 1 and Special 2 categories to group frequently used commands. Per special
Special
Note: The category is only used by LN UI. If the session runs in another UI, the category is ignored.
Form commands in a menu must have the same category as the menu.
Default Command
Use this check box to define the form command as the default command for the session, or for a command
category in the session.
You can select this check box in these situations:
- If the command has Command Type Print.
- If the command belongs to the Special 1 or Special 2 category.
If this check box is selected, the command is the default command of its category. If the session runs in
LN UI, the description of the default command is displayed on the category's menu button. See the
example.
Example - default command for a category
This table shows an example:
Catego- Default Command
Yes
No
No
Session/Function/Business
Method
exec.user.1
Long description
Activate Job
ry
Special
exec.user.2
Queue Job
Special
exec.user.3
Block Job
Special
Session/Function/Business
Method
exec.user.4
Long description
Cancel Job
Catego- Default Command
No
ry
Special
The commands of the Special 1 category are displayed in the Activate Job pull-down menu.
Note: You can specify one default command per special category.
The default command is only used by LN UI. If the session runs in another UI, the default command is ignored.
Display
Label Code
The code of the form command's label.
To edit or view the label in the label editor, click the Label Name hyperlink.
Allowed values:
To specify this field, click Browse and select a label name from select dialog box.
Description
The description of the form command's label, as specified in Label Name.
Allowed values:
This field is read-only. LN Studio automatically fills in the label description after you specified the Label
Name.
Shortcut Key
The form command's shortcut key. This property does not apply to form commands that invoke a menu.
Select the form command's shortcut key from the drop-down list.
Allowed values:
The value for Shortcut Key is one of the following:
- "Not applicable"
- A key combination that conforms to the following syntax: CTRL+F1- CTRL+F12, or CTRL+SHIFT+A- CTRL+SHIFT+Z
Add Ellipses to Label
If this check box is selected, an ellipsis (...) follows the form command's label. Use ellipses to indicate the
form command opens a dialog box.
Suppression of Dialog Allowed
If this check box is selected, users can suppress the dialog box, which is started by the form command, at
runtime. The dialog box is suppressed if user defaults are defined and quick flow is activated. If the dialog
box is suppressed, the corresponding default command is executed.
This check box is only available if the Add Ellipses to Label check box is selected.
Separator
If this check box is selected, Enterprise Server inserts a line in the menu under the form command. Use these
lines to create separate groups of form commands in the menu.
Availability
Authorization Group
The authorization level users need to carry out the form command. All commands with an authorization
group higher than the user’s authorization for the session are removed from the appropriate menu.
Note: For form commands of type Menu, you must specify Authorization Group Display.
Example:
A user is authorized to view and print records in a session. The authorization group for that session is
'Print/Display'. All form commands with authorization groups 'Full Authorization'
(Delete/Insert/Modify/Print/Display), 'Insert/Modify/Print/Display' and 'Modify/Print/Display' are removed
from the appropriate menu.
Allowed values:
- Display
- Print/Display
- Modify/Print/Display
- Modify/Print/Display
- Insert/Modify/Print/Display
- Full Authorization
Choose the authorization group of a form command according to the following guidelines:
Authorization Group
gives access to functionality, where a delete action should Full Authorization
be possible.
gives access to functionality, where an insert action should Insert/Modify/Print/Display
gives access to functionality, where a modify action should Modify/Print/Display
be possible, but no insert or delete action is needed.
Display
no print, modify, insert, or delete actions are needed.
gives access to report functionality, which also provides an Full Authorization
option for the end-user to delete data (or executes a delete
action in the script).
gives access to report functionality, which also provides an Insert/Modify/Print/Disoption for the end-user to insert data, but not to delete (or play
executes an insert action in the script).
gives access to report functionality, which also provides an Modify/Print/Display
option for the end-user to modify data, but not to insert or
delete (or executes a modify action in the script).
gives access to report functionality, which prints data, but Print/Display
does not provide an option to modify, insert or delete data.
Command Type
Form, Field or
Group
Form, Field or
Group
Form, Field or
Group
Form, Field or
Group
Print
If this form command…
be possible, but no delete action is needed.
gives access to functionality, where data is displayed, but
Print
Print
Print
Note: Define authorizations in the Authorization Management System module, and link these to a user on
the Authorizations tab of the User Data (ttaad2500m000) details session.
Command Availability
The availability of the form command.
Note: This field does not apply to form commands of type menu.
Allowed values:
Authorized users can activate the form command. The programming function disable.command overrules this option.
One Record Select- Authorized users can only activate the form command when they have selected one
record in the overview session's grid. The programming function disable.command
overrules this option. This option overrules the enable.command programming
function.
Authorized users can only activate the form command when they have selected one
or more records in the overview session's grid. The programming function disable.command overrules this option. This option overrules the enable.command programming
function.
Users cannot execute the form command. The programming function enable.command overrules this option.
Always
ed
Records Selected
Never
Show as Button in Dialog or Browse Session
If this check box is selected, the form command displays as a field button on the session's form.
Show in Menu bar of Details window
If this check box is selected, the form command is shown on the details session's appropriate menu.
Note: Programming functions are available to create an application toolbar that includes a session's form
commands.
Initial hidden
If this check box is selected, the form command is initially not displayed in the session. At runtime, you can
make the form command visible through the Personalize Session Menus or Personalize Toolbar option.
The initially hidden commands are displayed as a menu option in the Hidden panel of the Personalize
Session Menus dialog box, just like the other hidden menu options.
Initial hidden when added to Toolbar
If this check box is selected, the session does not display the form command if the form command appears
as an icon on the toolbar.
Execution
Before Execution
Question
When the user tries to execute the form command, Enterprise Server prompts the user with the question
whose name you enter in this field. This field does not apply to form commands of type menu. If the field is
left empty, no question is asked.
Allowed values:
To specify this field, click Browse and select a question from the select dialog box.
Answer
To carry out form commands, a user must give the answer you enter in this field when prompted by Enterprise
Server with the question in the Question field. This restriction only applies if the Question field has been
specified. This field does not apply to form commands that invoke a menu.
Allowed values:
To specify this field, select a answer from the drop-down list. This list contains all answers available for the
selected question.
Multi Session execute
For an overview session, when a user executes a form command with multiple records selected in the grid,
if in this field you select:
Once, LN only carries out the form command for the first record selected in the grid.
For every occurrence, LN carries out the form command for every record selected in the grid.
Allowed values:
Form command is only carried out for the first record selected in the grid.
Form command is carried out for every record selected.
rence
Once
For every occur-
Save data
If this check box is selected, when a user activates the form command, LN saves the session's data before
carrying out the form command. This option does not apply to form commands of type menu.
If this check box is cleared, when a user activates the form command, LN carries out the form command
without saving the session's data.
Execution
Start mode Session
Select the mode of the session the form command starts.
Note: This field only applies to form commands of type Session.
Allowed values:
- Modal
- Modeless
- Synchronized Child
- Modal Overview
- Not applicable
Kind of Session
Select the type of session the form command starts from the options.
Note: This field only applies to form commands of type Session.
Allowed values:
- Overview Window
- Details Window
- Not applicable
After Execution
Refresh Parent
If this check box is selected, when users execute the form command in a session, the data affected by the
form command automatically updates in any related sessions.
If this check box is cleared, users must manually save the changes after they execute the form command for
the changes to update in any related sessions.
### Satellite Sessions tab

If the session is a multi-main table (MMT) controller session, use this tab to maintain the MMT satellites for
the session.
The fields of this tab are only enabled for sessions that have Window Type Multi Main Table specified and
Session Type Maintain.
An MMT session is a combination of multiple sessions, each having their own main table. It is used to present
data with a typical parent-child structure. For example, a Sales Order and the related Sales Order Lines.
The window of an MMT session consists of two parts:
- The multi-main table controller session is a maintain session for the main entity, such as a Sales Order.
The form of this session determines the upper part of the session.
- The lower part displays satellite sessions with child information, such as Sales Order Lines. At runtime,
the satellite sessions are shown as tabs.
See Multi Main Table sessions on page 235.
All Satellite Sessions
This field contains the records of all satellite sessions linked to the current multi-main table (MMT) controller
session. Only a MMT controller session can have satellite sessions.
The satellite sessions are child sessions of the MMT controller session, such as the Order Lines session is a
satellite session of the Order Header session.
The satellite session records show two attributes:
- The Session attribute (the session's name)
- The Description attribute
To add a satellite session:
1 Click Add.
2 In the Session field in the grid, press CTRL+SPACE to start a dialog where you can select satellite sessions.
3 Select the desired satellite session and click OK. The satellite session is displayed in the grid.
You can only select sessions that have the List Window window type.
4 Select the satellite session in the grid and define the field mapping.
To remove a satellite session record, select a record and, on the shortcut menu, select Remove.
To change the order of the satellite sessions, move them up or down the list.
Name
The name of the satellite session.
Allowed values:
Press CTRL+SPACE and select a name from the select dialog. This dialog shows the names of all available
sessions.
Description
The description of the satellite session.
Allowed values:
This field is read-only. LN Studio automatically fills in the satellite session description after you specified the
Name of the satellite session.
Field Mapping
This field contains the field mapping records which map the fields of the multi-main table (MMT) controller
session with the corresponding fields of its child satellite sessions. The records define a mapping for the
satellite session marked in the All Satellite Sessions field.
The field mapping records consist of two attributes:
- The Field in MMT Session attribute, which specifies the name of the field in the parent MMT session
- The Field in Satellite Session attribute, which specifies the name of the corresponding field of the
satellite session
For example, the Order Number field of an Order Header session (MMT session) corresponds with Order
Number field of its child Order Lines sessions (satellite session).
To add a field mapping record, click Add and select the desired field names.
To remove a field mapping record, right-click a record and select Remove.
Note: The field mapping records define a mapping between the parent MMT session and one of its satellite
sessions. You can compare such a field mapping with a foreign key of a record that points to the primary key
of a referenced record. Similarly, the Field in Satellite Session field of the satellite session forms a pointer
to the Field in MMT Session identification field of the main MMT session.
Field in MMT Session
The name of the field of the multi-main table (MMT) controller session.
Usually, the field of the main MMT session you specify here corresponds with the identification of the involved
session records (business objects).
Allowed values:
To specify this attribute, select a field name from the drop-down list. This list contains the names of all
available fields of the MMT controller session.
Field in Satellite Session
The name of the field of the satellite session.
Usually, the field of the satellite session you specify here corresponds with the identification field of the main
MMT session.
Allowed values:
To specify this attribute, select a field name from the drop-down list. This list contains the names of all the
fields of the satellite session that is marked in All Satellite Sessions field.
### Documentation tab

Use this tab to enter the session's release notes and technical documentation.
Release Notes
Use this field to specify the release notes of the session.
Technical Documentation
Use this field to specify the technical documentation of the session
### TDE Documentation tab

Use this tab to view an XML tree with the technical information on the session's Technical Data Entity.
This optional tab is displayed depending on the multipage editor preferences.
See Multipage Editors on page 150.
## Dynamic index switching

If an overview session's standard command set has the Sort by option selected, users can select different
indices by which the records in the grid are sorted. The user selects an index from the View menu's Sort by
submenu. When a user selects a new index, the view fields above an overview session's grid and the field
order in the grid do not change.
Dynamic index switching allows you to configure session indices, so when a user selects a new index from
the Sort by submenu, the view fields above the grid and the field order in the grid can change.
You can only implement dynamic index switching for sessions whose standard command set includes the
Sort by option in the Form Option Sets (ttadv3120s000) session.
Implementing dynamic index switching
To implement dynamic index switching for an overview session:
1 On the User Interface tab of the LN Studio Session Editor, select the appropriate session's Dynamic
Index Switching option.
2 On the Overview tab of the Session Editor, specify the session's Table Indices and View fields settings.
Selecting dynamic index switching options
1 To start the Session Editor, double-click a session in the Activity Explorer.
2 On the User Interface tab of the Session Editor, select either of the following Dynamic index switching
check boxes:
- Restart when view fields differ. If switching indices results in the view fields above the grid changing,
Enterprise Server restarts the session.
- Always restart. Users can switch indices in the Overview session, which always restarts the session.
Note: You can only select the previous Dynamic index switching check boxes if your session is integrated.
For non-integrated sessions, use the predefined "dynamic.index.switching" variable in the before.program
section of the session's program script:
- dynamic.index.switching = -1 has the same effect as selecting the Restart when view-fields differ
check box.
- dynamic.index.switching = -2 has the same effect as selecting the Always restart check box .
3 To show the current index in the overview session's title bar, select the Show name of index check box.
Specifying index and view field settings
1 On the Overview tab of the Session Editor, select the session's indices for which you want to implement
dynamic index switching.
2 For every index check box you select, specify the order the indices are displayed on the session's Sort
by submenu and indicate the index fields that must be displayed as view fields.
a In the Table Indices and View fields field, determine the order the indices are displayed on the
session's Sort by submenu. To do this, use the Up and Down buttons to rearrange the sequence of
indices. The first entry in the list is the session's default index.
b In the Table Indices and View fields field, indicate which index fields must be displayed as view
fields above the overview session's grid. To do this, select the check boxes for the desired index
fields. When you select a particular index field as view field, the preceding index fields are displayed
as view fields.
Note: The Field Properties dialog box of the Session Editor's Form Definition tab contains the
View Field check box. If this check box is selected for a field, the field is always displayed as a view
field in the overview session, regardless of your Dynamic Index Switching settings. If you want a field
to be excluded as a view field for certain indices, clear the View Field check box for that field in the
Field Properties dialog box of the Session Editor's Form Definition tab.
## Multi Main Table sessions

A Multi Main Table (MMT) session is a combination of multiple sessions, each having their own main table.
MMT sessions are designed to present data with a typical parent-child structure, such as the following:
- Sales Order and the related Sales Order Lines
- Financial Business Partner group and the related Ledger accounts and Control accounts
- Work Order and the related Work Order activity lines, Work Order material resources, Work Order other
resources, Work Order measurements, Work Order Hours accounting
Although this data is distributed among several main-tables in the system, it can all be presented and edited
from within a single parent-child session.
This enables users to enter their data fast and to have a good overview of their work.
A typical parent-child session has two areas:
- The upper part contains information and functionality about the parent.
- The lower part contains one or more lists that show data about the various types of children.
Parent data and child data can be edited inside the session, which makes the sessions extremely powerful
for data entry. A parent-child session gives the user a complete overview of all important data related to the
object.
This figure shows an example of a parent-child session:
Sample parent-child sessions
Parent-child MMT sessions are available in various LN packages, such as the following:
Package
Manufacturing
Manufacturing
Order Management
Order Management
Service
Service
Service
Service
Session
Production Order
Generic Item – Structure
Sales Order – Lines
Sales Order Line – Deliveries
Service Order – Lines
Service Order Activity – Lines
Maintenance Sales Order
Work Order – Lines
Package
Finance
Finance
Finance
Finance
Finance
Finance
Quality Management
Quality Management
Object Data Management
Object Data Management
Tools
Tools
Session
Mapping Scheme
Ledger Mapping
Dimension Mapping
Financial Business Partner Group (Accounts Receivable)
Financial Business Partner Group (Accounts Payable)
Invoice-Source Relation
Inspection Orders – Easy Entry
Item – Storage Inspection
Document Revisions – Easy Entry
Change Proposal – Easy Entry
## Table definitions

Business Objects
Header and satellites
A parent-child MMT session is an integration of multiple sessions into one single session. It consists of the
following:
- A header session: This is the upper part of the MMT session window. It contains information and
functionality about the parent, such as the Service Order, see the previous figure. The header is a single
occurrence session.
- One or more satellites, displayed as tabs, containing data and functionality for the various types of
children, such as for the activities, estimated materials and labor. Each satellite is a separate session
linked to the MMT header session. All satellites are multi occurrence sessions.
The header and satellites can also run stand-alone.
This diagram shows the structure of an MMT session:
The header and lines in an MMT session are automatically synchronized. When you select a particular record
in the header area, the corresponding lines are automatically displayed in the satellites. There is no
synchronization between the satellites themselves.
A satellite tab only contains a grid. Additional fields outside the grid, such as view fields, are only displayed
when the satellite runs stand-alone.
Example
When the Order Lines session runs stand-alone, the Order Number is displayed as a view field above the grid.
When the session runs as a satellite in the Order MMT session, the satellite tab only displays the grid.
Developer guidelines
This section describes the prerequisites, possible issues, and the procedure for creating an initial MMT
header-lines session.
Prerequisites
You can only create an MMT header-lines session if the following conditions are met:
- There is a clear header-lines relation. Enterprise Server only supports synchronization if each satellite is
directly related to its header. For example, Sales Order Lines are directly related to the Sales Order Header
through the Order Number field.
- No synchronization is required between the satellites.
- The header has a single-occurrence representation. If not, it should be created.
- All satellite sessions you want to define have multi-occurrence representations. If not, they should first
be created.
Possible issues
Before you start creating an MMT header-lines session, identify the development effort required to solve the
following possible issues:
The header of the header-lines session contains the Duplicate and Delete standard comcopy/delete mands. In an initial MMT session, these actions only execute on the header.
Functionality to automatically copy or remove the corresponding lines when a header is
copied or removed must be programmed separately. You can re-use existing code to do this.
An implicit save means that a session and its contents are saved without a user action.
Therefore, the user performs a manual "Save" action, such as clicking Save on the tool bar
or selecting the Save menu item.
In an MMT header-lines session, all data within each separate session is saved on each focus
change from satellite to satellite, from header to satellite, or the other way around. For example, if a sales order is inserted and you switch the focus from the header to one of the
satellites, the header is saved. To indicate a save is being executed, a save icon appears in
the lower right part of the session window.
If you modify data after the last implicit or explicit save and then close the session, you are
prompted whether the changes must be saved. If you select No, this undoes the changes after
the last implicit or explicit save. When programming, be aware of this behavior. It can cause
unreferenced data in the database, such as an order header without lines. You might consider
programming a way to remove this data directly when it is generated, or to build a session
that cleans the database of these unreferenced entries.
Deep
Implicit
saves
Creating an initial MMT session
1 Create an MMT header session.
a Start the Create a New Infor LN Software Component wizard. Select File > New > New LN
Component.
b On the first page of the wizard, specify the LN Studio activity in which you create the new component
and the Component Type. The component type must be Session. To continue, click Next.
c On the second page of the wizard, provide the new session with a valid Name. Use the code of an
existing package and module and a new session number not already in use.
d On the second page of the wizard, fill in the other session properties as follows:
- Select the Multi Main Table Window Type.
- For the MMT header session, specify a Details Session as Synchronized Dialog. For example,
specify the Order Header details session as synchronized dialog for the Order MMT header
session. Users can start this session through the Details command in the MMT header session.
- In the Label of Object field, select the label to be used in the header session's menu items.
See Label of object on page 241.
e To create the session and exit the wizard, click Finish.
2 Customize the MMT header session.
a Edit the form of the MMT header session. Only include fields that are required for entering a new
record. All other relevant properties are specified in the Synchronized Dialog in a separate window.
b Ensure the MMT session fits into Web UI. Web UI supports 1024x768, but because the sessions are
hosted within Web UI, they should be smaller. Try your session in Web UI to see if it fits. To maximize
a session within Web UI, press ALT+F11. This allows you to see the full session screen.
c The fields specified in the dynamic form of the MMT header session are displayed in the upper part
of the MMT session, above the satellite tabs. By default, these fields should be read-only. They should
only be accessible when a new record is inserted in the header session. To achieve this, use 'add.set'
in the program script.
To edit forms, use the Session Editor's Form Definition tab.
See Form Definition tab on page 214.
For details on program scripts, see the Infor ES Programmers Guide (Infor Customer Portal KB2924522).
3 Define the Label of Object for each satellite.
Edit the properties of each satellite session in the Session Editor. In the Label of Object field, select the
label to be used in the satellite's tab description and menu items.
See Label of object on page 241.
4 Link satellites to the MMT Header session.
To link the desired satellites to the new MMT header session:
a Open the MMT header session in the Session Editor.
b Go to the Satellite Sessions tab and specify the satellites to be linked.
You can only link sessions that have the List Window window type.
Per satellite, enter the field relations used to synchronize the MMT header session with the satellite
session. To enter a field relation, specify the name of the relevant field in the header's main table,
followed by the name of the corresponding field in the main table of the satellite. For example, specify
the Order Number field from the Order Headers table and the Order Number field from the Order
Lines table.
5 Create or modify program scripts and DAL scripts.
The MMT header session and satellite sessions are separate sessions. Therefore you must define a program
script (UI script) for each of them, and optionally modify the DAL scripts of the corresponding tables.
Other session components, such as Reports, Text fields and Indices must be defined per session.
When a satellite tab is activated for the first time, the corresponding session is started and its
startup-sections, before.program, after.form.read, init.group.1, are called.
The program script of the satellite session can run in two modes:
This is the ‘normal’ mode; used when the session is executed as stand-alone session.
mode
This is the special MMT mode. Use the is.mmt.satellite() statement to check whether
a session is running as an MMT satellite session. You can program different behavior
for the satellite mode if required.
Stand-alone
Satellite mode
In the satellite mode you can perform the following actions:
Hide certain form fields since they are not relevant in the satellite mode. However,
there is only one form for both modes. You must define all fields you want to use in
either one of them, in the form.
Hide fields
Enable/disable
satellite
Hide/unhide satellite
Enable or disable a satellite within an MMT session in a particular case. The tab of a
disabled satellite is still visible in the MMT session, but cannot be selected or accessed.
To disable a satellite, use the disable.satellite() function. To enable it, use enabl
e.satellite(). Call these functions from the global after.form.read section in the
header session's program script.
Hide a particular satellite using the satellite.invisible() function. With this, you
can still make the satellite visible at runtime. For example, you can check authorizations and hide/unhide satellites for specific users. You cannot hide/unhide satellites
dynamically based on the availability of data in a satellite.
For details on program scripts and DAL, see the Infor ES Programmers Guide (Infor Customer Portal
KB2924522).
Label of object
MMT header sessions and satellite sessions have a Label of Object. This label contains a generic description
of the object within the session.
Label for Header session
For a Header session, define a single label. Note the following:
- The text should be a singular noun, such as "Purchase Order" for the Purchase Order MMT header session.
- The Context of Label must be Session, Table or Report Description.
The Label of Object is used in the Header session's menu-items to make clear on what object the
menu-item-command executes. For example, the menu-item for inserting a new record in the Purchase Order
MMT header session is called New Purchase Order, instead of New.
Labels for satellite sessions
For a satellite session, you can create two labels with the same label code. One label is used in the satellite's
menus, the other as the satellite's tab description.
Menu items
For the label used in the satellite's menu-items, note the following:
- The text must be a singular noun, such as "Order Line" for the Purchase Order Lines satellite session.
- The Context of Label must be Session, Table or Report Description.
This label makes clear on what object the menu-item-command executes. For example, the menu-item for
inserting a new record in the Purchase Order Lines satellite session is called New Order Line instead of New.
Tab description
By default, the session-description of the satellite is shown on the tab. When this description is not suitable,
create a new label with these properties:
- The label code must be identical to the code of the other Label of Object.
- The text must be a plural noun, such as "Order Lines" for the Purchase Order Lines satellite session.
- The Context of Label must be General Use.
Defining the label of object
For both MMT header sessions and satellite sessions, define the Label of Object. This label contains a generic
description of the object within the session.
To define a Label of Object for a session:
1 Create a label.
See Creating a label on page 103 and Label of object on page 241.
2 Link the label to the session: in the Label of Object field in the Session Editor, specify the label.
See Creating an initial MMT session on page 239.
## Session Model Editor

Use this editor to modify an InContext model for a session.
Several sections in this editor are similar to sections in the Table InContext Model Editor.
See Table InContext Model Editor on page 262.
### Session tab

Use this tab to maintain the overall data of the InContext model.
General Information
Session
The session name and description.
To edit or view the session in the Session Editor, click the hyperlink.
Main table
The name and description of the session's main table, if applicable.
To edit or view the table in the Table Editor, click the hyperlink.
(Re)generate
Click this link to (re)generate the InContext model. The session model is regenerated based on the table
model of the session’s main table. Note that manual changes to this session model may be lost.
Alternatively, you can (re)generate the model through the (Re)generate Implementation Model
(tticm1210m000) session.
Hooks
Include Hook/Declaration Hook/Function Hook
Click these links to open the corresponding hooks in the source viewer in the Hook section.
Library
Library
The model's library.
To edit or view the library in the Library Editor, click the hyperlink.
(Re)generate
Click this link to (re)generate the library.
Hook
Source viewer panel
This section is similar to the Hook section in the Table Editor.
See Table Editor on page 244.
### Context Messages tab

Use this tab to specify context messages and the corresponding mappings and hooks.
General Information
Session
The session name and description.
To edit or view the session in the Session Editor, click the hyperlink.
Main table
The name and description of the session's main table, if applicable.
To edit or view the table in the Table Editor, click the hyperlink.
Context Messages
Context Messages grid
This section is similar to the Context Messages section in the Table Model Editor.
See Table InContext Model Editor on page 262.
These are the differences compared to the Table Model Editor:
- You can create more than one context message of the same type.
- The table column is empty for manually created context messages.
- The hidden column has only two options: true or false.
For context messages with the 'hidden' element set to true, a strikethrough font is used.
Mapping
Mapping grid
This section is similar to the Mapping section in the Table Model Editor.
See Table InContext Model Editor on page 262.
Hook
Source viewer panel
This section is similar to the Hook sections in the Table Model Editor.
See Table InContext Model Editor on page 262.
Besides table fields, you can also use all form fields in the hooks.
### TDE Documentation tab

Use this tab to view an XML tree with the technical information on the session model's Technical Data Entity.
This optional tab is displayed depending on the multipage editor preferences.
See Multipage Editors on page 150.
## Table Editor

Use this editor to define and maintain table definitions and the corresponding DAL scripts.
Tables are data structures used to store data that consists of a list of records, with each entry identified by a
unique key and containing a set of related values. A table contains a number of table fields that belong to a
specific domain.
Table definitions describe the record fields and the field domains. A table definition shows the following
properties:
Table
Label Name
Description
Update Ref. Message
Delete Ref. Message
Relation Type
Table Fields
Table Indices
Table Script
The name of the table.
The name of the label that contains the description of the table.
The description of the table.
The message that appears when you change a record referenced by other records.
The message that appears when you delete a record referenced by other records.
How table fields are mutually dependent.
The record attributes.
The index fields and their sequence.
The Data Access Layer (DAL) script that applies to this table. A DAL script is used to
authorize data access and to ensure data integrity.
See Table definitions on page 257.
Note: If you are not authorized to change the data model, you can only edit the table's DAL script. See the
descriptions of the Script and Source tabs.
### Overview tab

Use this tab to maintain the overall data of a table definition.
General Information
Table
The name of the table, used as table identification code.
A table is uniquely identified by the combination of package code, module code, and table code.
Allowed values:
The table name is read-only. You can only specify a table name when you create a new table definition.
Afterwards, you cannot change this name anymore.
Table names must have the following format: <package code><module code><table number>
(tools)
(application development)
(sequence number of table)
Package Code
Module Code
Table number
2 letters
3 letters
3-digit number
tt
adv
Label Name
The name of the label that contains the table description.
To open the label in the Label Editor, click the hyperlink.
Allowed values:
The label name is read-only. You can only specify a label name when you create a new table definition.
Afterwards, you cannot change this name.
Description
The description of the table.
Allowed values:
The description is read-only, because the description text is stored in a label.
To change the description, click the Label Name hyperlink and edit the label in the Label Editor.
Update Ref. Message
The code of the message which appears if a user tries to change the primary key of a record referred to by
another table.
To open the message in the Message Editor, click the hyperlink.
Example:
Table pkitm001, Item table, is linked to Update Reference Message pkitmt0001. This message contains the
following text:
Item code cannot be changed, item is in use.
Table pksls041, Sales order line, refers to the Item table by its item code. If a user tries to change an item
code in the item table, which is used in a sales order line, LN displays the defined reference message.
Delete Ref. Message
The code of the message, which appears if a user tries to delete a record referred to by another table.
To open the message in the Message Editor, click the hyperlink.
Example:
Table pkitm001, Item table, is linked to Delete Reference Message pkitmt0001. This message contains the
following text:
Item code cannot be deleted, item is in use.
Table pksls041, Sales order line, refers to the item table by its item code. If a user tries to delete an item code
in the item table, which is used in a sales order line, LN displays the defined reference message.
Relation Type
The relation type for the fields in this table.
Note: This indication is important for delayed lock facilities in the bshell. If you use a delayed lock, two users
can change one record at the same time. However, they cannot change the same fields or the fields that are
related to each other.
Allowed values:
Select one of the following relation types:
All fields of the record are independent. When a user edits a field, another user can
edit other fields of the record.
All fields of a record depend on other fields of this record. When a user edits a field, all
fields are locked so other users cannot edit the record.
You can define groups of related fields. Some fields of a record depend on other fields
of this record and some fields are independent. When a user edits a field, the related
fields are locked. The other fields can be edited by other users.
No relations
All Fields
Specified Relations
InContext Model
The name of the InContext model that describes which fields are required for the context messages for this
table.
To open the InContext model in the Table InContext Model Editor, click the hyperlink.
If no InContext model exists for the table, click the hyperlink to generate a model. The Table InContext
Model Editor is started.
Related topics:
- InContext Modeling on page 73
- Infor Enterprise Server InContext Modeling Development Guide
- Table InContext Model Editor on page 262
Field Relationships
This section contains the Field-Group records. This indicates which table fields belong to which field groups.
Fields can be arranged into groups to indicate their mutual relationships.
To add a Field-Group record, click Add and specify a group and a field.
To remove a record, right-click a record and select Remove.
Note: This section is only displayed if the Relation Type is Specified Relations.
Group
The identification of a group of related fields.
Allowed values:
A number in the range 0-9999.
Name
The name of the field, which is related to other fields with the same group number.
Allowed values:
Select a field from the list.
Description
The description of the field.
The description is read-only. It is filled automatically when you select a field.
Runtime
Convert: Convert Tables to Runtime
This link is only available if the table is checked in.
Click this link to convert domains and tables to the runtime data dictionary:
- For LN servers with Enterprise Server 10.5 or later, the Convert to Runtime dialog box is started.
- For LN servers with older Enterprise Server versions, the Convert to Runtime Data Dictionary
(ttadv5215m000) session is started.
You must be authorized to run this session.
Note: In the Convert to Runtime dialog box or the Convert to Runtime Data Dictionary (ttadv5215m000)
session, select the package combination that contains the Project VRC of your current Software Project.
Domains and tables in all Activities linked to the software project are converted. Therefore, not only tables in
your own Activity VRC are converted, but changed tables in activity VRCs of other developers are also converted.
Read the online help of the dialog box or session before you start the conversion.
Create: Create Tables
This link is only available if the table is checked in.
Click this link to create this table for a range of companies:
- For LN servers with Enterprise Server 10.5 or later, the Create Tables dialog box is started.
- For LN servers with older Enterprise Server versions, the Create Tables (ttaad4230m000) session is
started.
You must be authorized to run this session.
### Fields tab

Use this tab to maintain the table fields of the table definition and perform these actions:
- Specify the field name and field number of the table field. The field name must be unique in the current
table.
- Specify whether the field is combined. For example, is there a combination of two or more fields of the
same table?
- You must specify a domain that specifies the data type, legal values, validation check, display format
and so on.
- Specify the label data for the field, the initial value, the mandatory input, and whether it is a repeating
field.
- Specify a relation to another table, insert check, delete, and update mode and specify whether the field
is active.
All Table Fields
List of all table fields.
In the All Table Fields list, you can perform these actions:
- Add or remove table fields.
- To add a field, click Add and enter the basic field properties in the grid. Then, enter the remaining
properties in the Table Field Properties field group.
- To remove a field, right-click a field and select Remove.
- To change the field sequence of the table, click Up and Down to move fields up and down the list.
- Link child fields to parent fields. To link a child field to its parent (combined) field, drag the child field
on the parent field and release the mouse button. The parent and child fields are displayed as a tree
structure.
- Copy fields to an index in the Indices tab, or copy fields from the current table to another table. To copy
fields to another table, select the fields, right-click, and select Copy. Then, right-click a field in the All
Table Fields list of the other table and select one of these commands:
- Paste as Fields: The fields are added below the selected field.
- Paste as Children: You can only select this command if the selected field is a combined field. The
fields are added as child fields of the combined field.
Name
The name of the field.
You can only enter a field name when you add a field. For existing fields, the name is read-only.
Label
The code of the label that is used as a description of the table field. Press CTRL+SPACE and select a label
from the select dialog box.
To open the label in the Label Editor, click the label icon.
For new table fields, the label is generated when you save the table.
Description
The description of the field.
You can only enter a description when you add a field. LN Studio stores the description in a label.
Allowed values:
For existing fields, the Description field is read-only, because the description text is stored in a label.
To change the description, click the label icon behind the Label field and edit the label in the Label Editor.
Domain
The domain of the table field. Press CTRL+SPACE and select a domain from the select dialog box.
Click the domain icon to open the domain in the Domain Editor.
Hooks
Click the Hooks icon to view a list of hooks that are defined for this field in the table's DAL script.
Table Field Properties
Column
Name
The name of the field that can be used in forms, reports, and scripts in this way: <table name>.<field name>
Allowed values:
The field name is an ASCII text with a maximum length of 8 characters. The field name must be unique in the
table.
Field names are usually abbreviated by leaving out syllables or vowels in the description of a particular
property, such as dscr for description or cnty for country.
Example table : pksls040 (package - module - table number) field name: orno
Label Name
The name of the label that is used as a description of the table field.
To start a dialog where you can select another label, click Browse.
To open the label in the Label Editor, click the hyperlink.
Description
The description of the table field, as defined by a label with the same name as the table field. If a label in a
form, report, or menu has the same name as the table field, this description replaces the label.
Note: A percentage symbol % in the label description forces a line break in the label in the form, report, or
menu.
Allowed values:
The description is read-only, because the description text is stored in a label.
To change the description, click the Label Name hyperlink and edit the label in the Label Editor.
Combined Field
If this check box is selected, the field is combined. A combined field consists of two or more normal fields,
not combined fields.
- A combined field can be used for references and indices.
- To add a child field to a combined field, go to the All Table Fields field group and drag the child field on
the combined field.
Mandatory Input
If this check box is selected, input in this field by the user is mandatory.
If the field has the byte, integer, long, float or double data type, mandatory input means the value of the field
must be unequal to 0. Mandatory input is an addition to the domain definition of the field and has precedence
over what is defined as the range of the domain. If the user tries to make a field empty while input is mandatory,
Enterprise Server gives range message of the domain.
Example
(datatype long)
Allowed range on the field
0 - 999999
1 - 999999
Field:
Range
$$ IN [0, 999999]
$$ IN [0, 999999]
Employee number
Mandatory input
no
yes
$$ IN [1, 999999]
$$ IN [1, 999999]
no
yes
0 - 999999 (0=empty)
1 - 999999
Elements
The depth of a repeating field.
If you specify a value greater than 1, the field is repeating. A repeating field occurs multiple times in the table
with the same name and characteristics. Identification of an element is performed using a sequence number.
Example: The Help Topics table contains these fields:
Elements
Field name
Help Topic Code
Topic Title
Topic Keywords
"Topic Keywords" is a repeating field of 4 levels. In the Help Topics table, you can define four key words for
each Help Topic Code.
Note: You can only specify the depth when you add a field. You cannot change the depth of existing fields.
Allowed values:
A number in the range 0-99.
To indicate the field is not repeating, enter 0.
To indicate the number of elements for a repeating field, specify a value greater than 1.
Domain Name
The name of the domain of the table field.
To open the domain in the Domain Editor, click the hyperlink.
Allowed values:
Select a domain from the field's drop-down list. The list contains all domains available on the current LN
server.
Data Type
The data type of the domain.
Allowed values:
This field is read-only. The data type is determined by the specified domain.
Length
The length of the domain.
Allowed values:
This field is read-only. The length is determined by the specified domain.
Generate Unique Default Value
This check box indicates whether a unique value must be generated for the selected table field during
reconfiguration of the table.
If you select this check box:
- The Default Value field becomes disabled, showing no content.
- In the database, the value "$__unique" is stored as the "Initial Value".
- The value "$__unique" is used to start a bdbreconfig. It generates a unique ID for the selected field.
If this check box is cleared (default value):
- The Default Value field becomes enabled.
- The default value for Default Value is empty. You can manually specify a default value.
- The value of Default Value is stored in the database.
Default Value
If a user adds a record to the table, this is the initial value for the field.
If the Generate Unique Default Value check box is cleared, you must specify a default value.
If the Generate Unique Default Value check box is selected, this field is read-only. The default value is
determined by the specified domain.
Field Dependency Editor
This link is only available if the table has a DAL 2 script and the table is checked out.
Click this link to start the Field Dependency Editor. This editor enables you to view and modify the field
dependencies defined in the table's DAL 2 script. For details on DAL (2) scripts and field dependencies, see
the Infor ES Programmers Guide (Infor Customer Portal KB2924522).
Reference
Reference Table
The related table to which this field refers.
> [!NOTE]
The reference table is also known as the parent table.
To open the reference table in the Table Editor, click the hyperlink.
Allowed values:
To start a dialog where you can select a reference table, click Browse.
Reference Mode
Indicates whether the referenced field must exist in the reference table. The reference field is the field referred
to by the current field.
Allowed values:
Select one of these reference modes:
The foreign key value (the reference record) must exist in the reference table.
Same as Mandatory, but the foreign key value can be empty.
empty
The foreign key value is not checked against the reference table.
The field does not refer to a field of another table.
Mandatory
Mandatory unless
Not mandatory
Not Applicable
Reference Message
The message code which LN gives, if you enter a value in an input field in the form, where no related record
in the reference table is present.
Note: The reference message is only relevant if the reference mode is mandatory, or mandatory unless
empty.
To open the reference message in the Message Editor, click the hyperlink.
Allowed values:
To start a dialog where you can select a reference message, click Browse.
Delete Mode
The action to be taken by LN if a referenced record in the reference table is deleted.
Select a delete mode from the drop-down list.
Allowed values:
All children that refer to the parent are deleted.
Note: If the reference does not identify the relation
this can result in the automatic deletion of many
records. For example if the relation between the
parent and child is not one-to-one but one-to-many.
Deletion of the parent is restricted if any child refers
to the parent. A reference counter is checked, which
indicates how many children refer to the parent.
With each database action this counter is checked
and updated, if necessary.
Deletion of the parent is restricted if any child refers
to the parent.
If the parent has been deleted, no check or action
is performed on the child occurrences which refer
to the parent. In that case the referential integrity
of the database cannot be guaranteed.
The field(s) of the child, which refer(s) to the parent
that has been deleted, are made empty (spaces or
zero value).
Child will be deleted
Restricted (with counter)
Lookup (Restricted)
No check
Nullifies
Update Mode
The action to be taken by LN if the primary key of a referenced record in the reference table is changed.
Select an update mode from the drop-down list.
Allowed values:
All children that refer to the parent are updated.
Note: If the reference does not identify the relation
this may result in the automatic update of many
records. For example if the relation between the
parent and the child is not one-to-one but one-tomany.
Any change of the primary key fields of the parent
is not allowed if any child refers to this record. A
reference counter is checked, which indicates how
many children refer to the parent. With each
database action this counter is checked and updated, if necessary.
Child will be updated
Restricted (with counter)
Lookup (Restricted)
No check
Nullifies
Any change of the primary key fields of the parent
is not allowed if any child refers to this record.
If the parent is changed, no check or action is performed on the child records which refer to the parent. In that case the referential integrity of the
database cannot be guaranteed.
The field(s) of the child, which refer(s) to the updated parent record, are made empty (spaces or zero
values).
Inter-Company via Field
Clear this check box if the reference table is located in the same company as the current table.
Select this check box if the reference table is located in a different company. If this check box is selected,
you must specify the table field that contains the company number where the reference table is located.
Example:
The Shipping Warehouse (whinh220.cwar) field in the Outbound Order Lines (whinh220) table refers to the
Warehouses (whwmd200) table.
The Warehouses (whwmd200) table is located in a different company.
The Ship-from Company (comp) field in the Outbound Order Lines (whinh220) table contains the company
number where the Warehouses (whwmd200) table is located.
This reference information is specified for the Shipping Warehouse (whinh220.cwar) field in the Outbound
Order Lines (whinh220) table:
- Reference Table: whwmd200
- Inter-Company via Field: Yes comp
Technical Doc.
Use this field to specify the technical documentation of the table field.
Release Notes
Use this field to specify the release notes of the table field.
### Indices tab

Use this tab to maintain the table indices and index fields of the table definition.
You can perform these actions:
- Add indices and index fields:
- To add an index, click Add Index and enter the index properties in the grid. See the field help.
- To add an index field, select an index in the grid and click Add Child. Then, in the Name field, select
the desired field from the list.
Alternatively, right-click a field in the Fields tab and select Copy. Then, go back to the Indices tab,
right-click an index and select Paste.
- Remove indices and index fields. To remove an index or index field, right-click the index or field and select
Remove.
- To determine the index sequence, use the Up and Down buttons to move the index records up or down
the list. The index numbers change correspondingly. The index with number 1 is the primary key.
All Table Indices
All table indices. Each index is represented by a record.
Name
The number of the index or the name of the index field.
Note:  The index with number 1 is the primary key.
Description
The description of the index or index field.
You can only enter a description when you add an index. LN Studio stores the index description in a label.
Label
The label that contains the description of the index.
This field is read-only.
To open the label in the Label Editor, click the label icon.
Note: For new indices, the label is generated when you save the table.
This field does not apply to index fields.
Active
If this check box is selected, the index is active. The primary index (index number 1) is always active.
Note: This information is not used in the data dictionary or the database layer.
This field does not apply to index fields.
Unique
If this check box is selected, the index is unique. Therefore, different records must have different values in
the index parts.
If this check box is cleared, different records can have the same values in the index parts. These are called
duplicate records.
Note: This field does not apply to index fields.
### Script tab

Use this tab to specify the properties of the table's DAL script. You can also link libraries to the table.
Data Access Layers (DALs) are program scripts to guarantee data integrity. The DAL script considers for all
types of dependencies, various business rules, specific constraints and so on.
For more information on DALs and the availability of two versions of these scripts, see Data Access Layer (DAL)
on page 258.
To edit or view the DAL script, go to the Source tab.
For more information on the LN Studio Script editor, see Script Editor on page 267.
For more information about the script properties, see the Script tab of the session editor.
General Information
Script Type
The type of program script used for this table. The script type is DAL or DAL2.
Allowed values:
Select one of the following options:
Data Access Layer that contains the Business Logic related to a table. The DAL is called by
the 4GL engine on certain events. Since version 2 of DAL is available, you are advised to
use DAL (version 2) scripts.
Data Access Layer that contains the Business Logic related to a table. The DAL is called by
the 4GL engine on certain events. DAL (version 2) is more integrated with the Business Data
Entity (BDE) interfaces and the integration software.
No DAL script is used for this table.
ble
DAL
DAL (version
2)
Not Applica-
DAL
The name and description of the DAL script.
Usually, a script is uniquely identified by the package code, module code, and script code. The code of a DAL
script corresponds with the name of the table for which the script is used.
Compile Flags
The compile flag.
For details, see the Script tab of the Session Editor.
Tools Interface Version
The Tools Interface Version (TIV) number of the script/library.
For details, see the Script tab of the Session Editor.
License
Product ID Source
The product ID for which a license is needed to compile the object. If the field is empty, no license is needed
to compile the object.
Note: This field only applies to internal Infor development systems. For other development environments,
this field is not available.
Allowed values:
To enter a product ID, click Browse and select an ID from the select dialog box.
Product ID Object
The product ID for which a license is needed to run the object. If the field is empty, no license is needed to
run the object.
Note: This field only applies to internal Infor development systems. For other development environments,
this field is not available.
Allowed values:
To enter a product ID, click Browse and select an ID from the select dialog box.
Linked Libraries
This list contains the records of all libraries linked to the DAL script of the current table.
Sorting
- To sort the libraries by position, name, or description, click the corresponding column header.
- When you sort by position, the sort mode is always ascending. When you sort by name or description,
click the involved column header to toggle between ascending and descending sort mode.
- When you sort by name or description, the Up and Down commands are disabled.
Add / remove libraries, change linking order
You can only perform the following actions if you sort the libraries by position.
- To add a library, click Add. Then, press CTRL+SPACE in the Name field and select a library from the select
dialog box.
- To remove a library, right-click a library and select Remove.
- To change the linking order of the libraries, move them up or down the list.
Note: To edit a library, click the icon behind the library name.
Pos
The library sequence number (Position). This field indicates the linking order of the libraries.
This field is read-only. It is filled automatically when you link a library.
Name
The name of the library.
Allowed values:
To specify this attribute, press CTRL+SPACE and select a library from the select dialog box.
Description
The description of the library.
Allowed values:
This field is read-only. LN Studio automatically fills in the library description after you specified the Name
of the library.
Documentation
Release Notes
Use this field to specify the release notes of the table's DAL script.
Technical Documentation
Use this field to specify the technical documentation of the table's DAL script.
### Source tab

Use this tab to view and edit the source code of the DAL script of the table. The tab consists of a script editor,
which forms an integral part of the table editor.
See Script Editor on page 267.
This tab is only displayed, if the source code of the DAL script is available.
### Documentation tab

Use this tab to enter the table definition's release notes and technical documentation.
Release Notes
Use this field to specify the release notes of the table definition.
Technical Documentation
Use this field to specify the technical documentation of the table definition
### TDE Documentation tab

Use this tab to view an XML tree with the technical information on the table's Technical Data Entity.
This optional tab is displayed depending on the multipage editor preferences.
See Multipage Editors on page 150.
## Table definitions

Table Definitions define a structure to the data. The table code and name are attributes of a table. A table is
a collection of data, arranged in rows (records) and columns (fields).
This diagram shows a table data example:
Fields, domains and indices
A table has fields. Table fields store individual pieces of data such as a customer name, the quantity of an
item ordered, or the date a journal entry was made.
Table fields are linked to domains. Domains are components that define common information about data
such as the following:
- The data type, such as a character type for customer name, a number type for quantity, and a date type
for journal date
- Valid ranges
- Special characteristics such as capitalization rules
Domains ensure consistent data types for similar table fields.
This diagram shows a table fields and domains example:
A table must have at least one index. An index consists of one or more table fields used to sort and search
records in the table. The first index is always the Primary key, the unique identification for a record in a table.
Related Tables and References
The table may have a related table. A related table means that a field in the table refers to the key field of
another table. Therefore, data can have relationships: customers can have orders; inventory stores items in
warehouses; and employees work in a department. To create diagrams from these defined relationships, use
a tool in the Enterprise Modeler.
Creating table definitions
Create table definitions in the Create a New Infor LN Software Component wizard and the Table Editor.
See Creating a table on page 111.
## Data Access Layer (DAL)

The Data Access Layer allows developers to describe rules about data. A DAL is linked to a table, not a session.
Therefore, anytime the table is accessed, the DAL is used. Therefore, different sessions can update a table
and the same rules apply in the same way. In addition, integration capabilities use the DAL to ensure updates
occur in the same way.
Data Access Layer scripts implement the business rules of the application to ensure the logical integrity of
the database. DAL scripts are a Library software component aligned with a specific table. These scripts are
compiled into objects. When a session performs an action on a table, the DAL for the table is loaded.
In LN, two types of Data Access Layer scripts exist: DAL 1 and DAL 2.
Business Rules
A business rule is a statement that defines, or constrains, some aspect or operation of the business. It is
intended to control or influence the behavior of the business operations. Business rules are logical integrity
rules, and differ from database oriented referential integrity rules.
Business Rules - example
Business rules in a purchasing system could be as follows:
- An item can be ordered only from its supplier
- When the gross weight and net weight for an item are the same, there is no packaging
- The supplier provides the arrival date of a purchase order after the order is entered into the system.
- Items cannot be removed if there is stock on-hand
- The item on-order quantity is increased when an order for the item is entered
- The item on-hand quantity is increased, and the on-order quantity decreased, when an order arrives
Referential Integrity Rules - example
In contrast, integrity rules in a purchasing system could be as follows:
- An item must exist for it to be ordered
- If an item has a supplier, the system must know the supplier
- Items can not be deleted if the item record is used elsewhere in the system
Business rules are implemented as hooks. A hook is a pre-defined function name you create in a Data Access
Layer script. The 4GL engine will call this function as it executes user interface and database related actions
on the table the DAL is written for.
Business rules fall into categories that determine how the business rule is implemented in the DAL.
The categories, depending on the type of DAL script, are as follows:
- Property or Field hooks
- Object Hooks
- Field Dependencies
- Business Methods
DAL 1
DAL 1 scripts were introduced in Infor Baan 5.0. A DAL 1 script contains database logic such as logical integrity
rules, but it usually does not contain all business logic for the table it belongs to. Very often, business logic
is spread across the DAL 1 script and the UI scripts.
Most UI scripts still contain business logic to do the following:
- Make fields read-only.
- Determine which enum constants can be selected in an enumerated field.
- Update a field after a change to a related field.
Therefore, it is difficult to use the DAL 1 scripts for integrations via the LN Business Adapter software: the
business logic in the UI scripts is skipped if another application connects to an LN table. Therefore, this logic
must be rebuilt in the Business Object Interfaces (BOIs) that provide the connection. If you change the business
logic in the UI scripts, you must also adapt the corresponding BOIs.
A DAL 1 script can contain the following types of hooks:
Object hooks. These hooks operate on the row or record as a whole unit. Object hooks determine if operations on a row are allowed, and specify additional operations that should be performed
based on an operation of the row.
Examples of object hooks are as follows:
- Delete the additional employee data in the People package when an employee is
deleted.
- When a sales order line is saved, create a history record of the sales order line.
- Update the item inventory when a planned stock transaction is created.
These hooks operate at a field level, and are used to verify valid values and calculate default
values for table fields.
Examples of property hooks are as follows:
- Validity check that the Quotation expiration date should be after the Quotation entry
date.
- When adding an employee, the language of the company is the default for the employee’s language.
Property
hooks.
For details on DAL 1 scripts, see "Data Access Layer" in the Infor ES Programmers Guide (Infor Customer Portal
KB2924522).
Creating DAL 1 scripts
Create and edit DAL 1 scripts in the Table Editor. For DAL 1 scripts, the script type is "DAL".
DAL 2
DAL 2 scripts are introduced in LN. A DAL 2 script contains all business logic related to a particular table. The
UI scripts of the sessions operating on the table only contain UI logic.
DAL 2 scripts are suited for integrations via the LN Business Adapter software. Other applications can connect
to LN tables through Business Objects. The business logic in the table's DAL 2 script is executed automatically.
To build an integration, you do not need to rebuild this business logic in the BOIs that provide the interface.
Various predefined Business Objects, that can be used for integration purposes, are delivered with LN. DAL
2 scripts are only available for tables used in these business objects. For the remaining tables, DAL 1 scripts
are available. For details on business objects and integration technology, see the LN Business Adapter
documentation.
In DAL 2 various new hooks are introduced. A DAL 2 script can contain the following:
Object hooks
Field hooks
Business method
hooks.
These hooks are identical to the object hooks in DAL 1 scripts.
These hooks contain the business logic for table fields and can contain logic to do
the following:
- Verify valid values on a table field (logical integrity rules).
- Make a field read-only. For example, the contact field of the Business Partner
is not a required entry, and is a display field in the UI when the Business Partner
is created.
- Make a field invisible.
- Automatically update a field, after a related field was changed. See "Field Dependencies".
- Make input on a field mandatory.
- Hide a particular enumerated constant from an enum list.
These hooks disable/enable and hide specific form commands of type "business
method".
For details on DAL 2 scripts, see "DAL 2 Overview" in the Infor ES Programmers Guide (Infor Customer Portal
KB2924522).
Field dependencies
In DAL 2 scripts, you can define field dependencies used to determine default values. when these field
dependencies are defined, dependent fields update themselves when the fields they depend on are updated.
The field updates are defined in the DAL as a field hook.
Dependencies are also used to update the User Interface. The 4GL Engine uses these field dependencies to
disable and enable fields, and determine enum values.
Examples of field dependencies are as follows:
- The packing field of the Item is yes if the gross weight and net weight of the item are different. A field
dependency is defined so the packing field is updated if the gross or net weight fields change.
- An item without a gross weight cannot have a net weight and packing. A field dependency is defined so
the net weight and packing fields are disabled if the gross weight is zero.
Business methods
Business Methods are operations on a row or set of rows within a table. A business method is a function that
performs a task that involves manipulating or checking one or more tables in the database.
Sessions, object hooks, or property hooks from another table’s DAL can call a business method. See the Infor
ES Programmers Guide (Infor Customer Portal KB2924522).
Examples of business methods are as follows:
- The sales order line session can remove an order line. The object hook for deleting the sales order line
calls a business method to also remove the unpaid commissions.
- In the Purchase Order session, check if it is allowed to change a purchase order header based on the
purchase order status and the business partner status.
- If a purchase order issues components, the object hook for the purchase order line calls a business method
to issue the components for the purchase order. The business method inserts items of the bill of material
into a purchase order components table.
## Table InContext Model Editor

Use this editor to modify an InContext model for a table.
### Table tab

Use this tab to maintain the overall data of the InContext model.
General Information
Table
The table name and description.
To edit or view the session in the Session Editor, click the hyperlink.
Dependent InContext Models
This link shows the dependent Table and Session Models in separate view below the editor. You can use that
view to refactor dependent models.
See Dependent InContext Models view on page 316.
(Re)generate
Click this link to (re)generate the InContext model. The table model is regenerated based on the InContext
Reference model of the session’s main table. Context messages are derived from the main table or inherited
from the tables referenced by the main table. This regeneration process will update table references and
context messages that were added or removed from the InContext Reference model. Note that manual
changes to this table model may be lost.
Alternatively, you can (re)generate the model through the (Re)generate Implementation Model
(tticm1210m000) session.
Drillback
Drillback session
The session that is started when the business object is referenced and must be displayed.
To edit or view the session in the Session Editor, click the hyperlink.
Click Browse to view all sessions where the main table is the same as the table of the current model.
From Enterprise Server version 10.3 you can define the session code through a hook. To add a hook, click
the Hook link. To remove a hook, clear the hook code. The hook must return a String.
Mode
Indicates whether the drillback session will start as single or multi occurrence session, assuming that the
session supports the selected mode. Default value is Single Occ.
From Enterprise Server version 10.3 you can define the mode through a hook. This hook must return either
SINGLE_OCC or MULTI_OCC.
Index
The index the drillback session will start with.
From Enterprise Server version 10.3 you can define the index through a hook. This hook must return a Long.
If the session code is specified using a hook, the index must also be specified through a hook.
If you leave this field blank, the default index, 1, is used.
Referenced Tables
Referenced Tables grid
The grid shows all referenced tables from the model. If a hidden element is present in the model and has the
value 'true', a strikethrough font is used. The descriptions are read from the server. If the same table occurs
multiple times as referenced table, the sequence number element is used to make the descriptions unique.
The 'hidden' check box toggles the 'hidden' element of the referenced table.
The grid synchronizes with the Table Reference section.
To create a row in the grid and add a referenced table, click Add. This field supports code completion. The
table is validated and the description is added. These default settings are generated for the table reference:
- Reference type: where
- Mandatory: false
- Field mapping: all primary key fields of the referenced table that are also present as fields in the current
model table.
To remove a table from the grid, right-click the table and select Remove. This is only possible for referenced
tables that are not present in the active Reference Model.
Include Hook/Declaration Hook/Function Hook
Click these links to open the corresponding hooks in the source viewer in the Hook section.
Table Reference
Type
The reference type.
The TableRead Hook hyperlink is only active in case of Type 'hook'. If the Type is changed, the Mappings are
generated following the rules.
Mandatory
If this check box is selected, the referenced table must be present.
Field Mapping grid
This mapping defines how the current table is related to the referenced table. The From fields must exist in
the current table. The To fields must exist in the referenced table.
To create a row in the grid and add a mapping, click Add. Code completion is possible on both, From and
To fields.
To remove a mapping from the grid, right-click the mapping and select Remove.
Use the Up and Down buttons to change the position of the mapping, although this does not have any impact.
Hook
Source viewer panel
Use this viewer to edit the selected hook.
This editor supports all LN Studio Script Editor features, such as code completion, text hover tool-tips, open
declaration, and syntax highlighting.
See Script Editor on page 267.
In the hooks, you can use all table fields from the current table and all referenced tables.
Click the Previous hyperlink to move to the previous hook in the model.
Click Next to move to the next hook in the model.
Click Compile to generate a source with the three generic hooks (Include, Declaration and Function) and a
wrapper around the current hook. The Include and Declaration hooks themselves are compiled solely.
### Context Messages tab

Use this tab to specify context messages and the corresponding mappings and hooks.
General Information
Table
The table name and description.
To edit or view the session in the Session Editor, click the hyperlink.
Context Messages
Context Messages grid
The grid shows the context messages from the model.
The Hidden column can have these values:
- No: the context message is sent for this table and is also available for the tables that refer to this table.
- Current level: the context message will not be sent for this table, but is available for the tables that
refer to this table.
- Child level: the context message is sent for this table but is not available for the tables that refer to this
table.
- All: the context message is not sent for this table and is not available for the tables that refer to this
table.
For context messages with the 'hidden' element set to true, a strikethrough font is used.
Click Add to add a context message to the grid. Only messages that are present in tagencontextmessages.xml
are allowed. Code completion is supported. For context messages that are added manually, you cannot
specify the table and sequence number.
To remove a context message from the grid, right-click the message and select Remove. This is only possible
for context messages that are not present in the active Reference Model.
The Refresh button performs these actions:
- Refresh the context messages for all referenced tables.
Read the context messages from the referenced model.
- Compare them to the present ones related to that table.
- Add/delete if required.
- Change only the context messages that are not manually changed.
- This refresh is also executed on save if a referenced table has been added. You must confirm this; the
save will not be performed if you do not choose to refresh. If this referenced table has a table model,
the context messages are copied from this model. If there is no model, the context messages are copied
from the reference model. Note that the sequence number makes the context message unique if the
same context message is linked to the same table multiple times.
The grid synchronizes with the Mapping section.
- 
Mapping
Mapping grid
This editable grid shows the Mapping elements from the model.
This table shows the functionality required for the columns in the grid:
Col-
Description
These values come from the model; they are the placeholders in the XML template of the context
message.
The type of mapping. This table shows the possible values for this column:
Description
The placeholder can be replaced directly with the value of the field.
There is no mapping; the element that refers to this mapping in the XML template of the
context message is skipped when the message is constructed.
A hook will calculate the value for the placeholder. Selecting the row automatically loads
the hook into the hook editor.
A function is called; the return value of the function is used for the substitution.
tion
umn
Target
Type
Type
field
none
hook
func-
Source The possible values for this column depend on the type of mapping specified in the Type column.
This table shows the possible values for the Source column:
Type of map-
Value for Source column
A table field from the current table
Empty
Empty
A function from the Infor ES Programmers Guide (Infor Customer Portal
KB2924522), Functions hook, or from a library that has been linked to the
model by “pragma used dll” in the Include hook.
ping
field
none
hook
function
Condition Hook/Before Mappings Hook/After Mappings Hook
Click these links to open the corresponding hooks in the source viewer in the Hook section.
Hook
Source viewer panel
This section is similar to the Hook section on the Tables page.
The Inherit check box indicates whether the hook type is 'inherit' or 'override':
- If you select this check box, the current hook is deleted and the corresponding hook from the referenced
table is displayed. The hook editor is read-only.
- If you clear this check box, the hook is copied and can be edited. The new hook overrides the logic of
the inherited hook.
If there is no hook to inherit, the Inherit check box is disabled.
### TDE Documentation tab

Use this tab to view an XML tree with the technical information on the table model's Technical Data Entity.
This optional tab is displayed depending on the multipage editor preferences.
See Multipage Editors on page 150.
