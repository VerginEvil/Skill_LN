# ProcessingOptionSet.Create

> Chapter: Chapter 2 Public Interfaces for Extensibility
>
> Group: Public Interfaces for ProcessingOptionSet
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 83-84

```baan
DLL:   tcextextapi
This function is available from 2023.11 (KB2302509).
Syntax: long ProcessingOptionSet.Create(
ref             long             oProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   Create a Processing Option Set. The created Processing Option
Set can be used to control Public Interfaces that support this
functionality. Name/Value pairs must be given in the variable
arguments. Example flow for Item.Copy():
ret = ProcessingOptionSet.Create(
my.copy.item.processing.option.set,
my.exception.message1,
my.exception.id1,
"copyItemsBySiteAndItemsByOffice",      tcyesno.no,
"copyItemText",                         tcyesno.yes,
"copyReferenceDesignators",             tcyesno.no,
"targetItemDescription",  "This is the copied item",
"projectPartQuantity",                  751.12)
.
.
ret = Item.Copy(
source.item,
target.item,
my.copy.item.processing.option.set,
my.exception.message2,
my.exception.id2)
.
.
|* release memory
ret = ProcessingOptionSet.Delete(
my.copy.item.processing.option.set)
.
.
Pre:    -
Post:   Use ProcessingOptionSet.Delete() to release memory for the
allocated Processing Option Set.
Input:  Variable Arguments - repetition of pairs:
OptionName              - option name of type string
OptionValue             - option value, type as defined by
Public Interface usage.
Output: oProcessingOptionSet    - reference to the processing option set
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return:         0               - successfully created
<> 0            - failed.
```
