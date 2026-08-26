# Item.GetOrderingData

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 172-173

```baan
DLL:   tcextibdapi
This function is available from     2019.03 (KB2043720  ).
Syntax: long Item.GetOrderingData(
domain  tcncmp           iLogisticCompany,
domain  tcitem           iItem,
domain  tcsite           iSite,
boolean          iForceRead,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   Retrieves data from Items - Ordering.
The required field is specified by the field menomonic,
the output value is filled in the output argument depending on
the data type.
This function is Multi Site aware, data is read from general
level or site level, depending on the input arguments Site
and implementation phase of Multi Site.
Note: this function uses variable arguments, for input and
output. Data is retrieved via value pairs: specify the field
and the field value.
Example: when item ordering warehouse and order interval are
needed, the function must be called as follows:
if Item.GetOrderingData(
|* Fixed arguments:
company,                                                            --    > input
item,                                                            --       > input
site,                                                            --       > input
force.read,                                                            -- > input
exception.message,                                                      --> output
exception.id,                                                           --> output
|* Variable arguments:
"cwar",                                                            --     > input
warehouse,                                                            --  > output
"oint",                                                            --     > input
order.interval) <> 0 then                                               --> output
|* Error, do something
Exception.Delete(exception.id)
endif
Pre:    None
Post:   None
Input:
iLogisticCompany                              - Logistic Company: Mandatory
iItem                         -               - Item: Mandatory
iSite                         -               - Site: Not Mandatory
iForceRead                                    - Option to force new query in stead of
using cached information.
...                                           - The field mnemonic of the required
field.
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
...                                           - The value of the required field.
Return: 0                                     - Data read.
<> 0                                          - Otherwise.
```
