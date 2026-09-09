# Common.GetParameters

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 112-113

```baan
DLL:   tcextcomapi
This function is available from 2019.08 (KB2074177).
Syntax: long Common.GetParameters(
domain  tcncmp           iCompany,
domain  tctabl.c         iTableCode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function reads one or more parameters from a standard LN
parameter table.
Note that this function uses variable arguments, for input and
output. Data is retrieved via name value pairs: the field
mnemonic and the field value.
Several parameter-fields are stored as arrays. Individual elements
of these parameter-fields can be retrieved by adding the element
number to the field-mnemonic. Example: "qipo(28)", "mvst(2)".
Example: When the 'Minimal Picks' and 'Quarantine Inventory
Available for Planning by Origin' are needed from the
Inventory Handling parameters, the call of
this public interface is as follows:
if Common.GetParameters(
|* Fixed arguments:
company,                --> input
"whinh000",             --> input
exception.message,      --> output
exception.id,           --> output
|* Variable arguments:
"minp",                 --> input
minimal.picks,          --> output
"qipo(1)",              --> input
l.qipo(1),              --> output
"qipo(2)",              --> input
l.qipo(2),              --> output
"qipo(3)",              --> input
l.qipo(3)) <> 0 then    --> output
|* Error, do something
Exception.Delete(exception.id)
endif
Pre:    None
Post:   None
Input:
iCompany          - Company: Mandatory
Note: for reading "tccom000" always the current
company is taken.
iTableCode        - Code of the parameter table: Mandatory.
Example: "tpctm000"
...               - The field mnemonic of the required parameters.
Output:
oExceptionMessage - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID      - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
...               - The value of the required parameters.
Return: 0                 - Parameter(s) read.
<> 0              - Error occurred.
```
