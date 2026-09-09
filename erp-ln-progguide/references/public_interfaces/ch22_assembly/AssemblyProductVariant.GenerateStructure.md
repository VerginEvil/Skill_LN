# AssemblyProductVariant.GenerateStructure

> Chapter: Chapter 22 Public Interfaces for Assembly
>
> Group: Public Interfaces for AssemblyProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 873-875

```baan
DLL:   tiextascapi
This function is available from 2026.06 (KB3652287).
Syntax: long AssemblyProductVariant.GenerateStructure(
domain  tccpva           iProductVariant,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface generates product variant structure
for a Product Variant (assembly). This function interface
mirrors the behaviour of Generate Product Variants
Structures (tiapl3210m000).
Transaction management is handled in this function.
Pre:    N.A.
Post:   N.A.
Input:  iProductVariant         Product Variant(Assembly)
iProcessingOptionSet    Processing Option Set (Optional).
If 0, then user default/session
default values are applied.
A Processing Option Set can be created
via call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete().
Either Product Variant or one of the
selection ranges in Processing Option
set must be set to generate the product
variant structure in the limited range.
Note: In case, neither Product Variant
nor the Process option set is provided,
then the process will generate the
product variant structure for full range.
Processing Options have a direct relationship with the form fields
on session Generate Product Variants Structures (tiapl3210m000) except
configuration date range and are not explained in further detail here.
Please refer to the session help for additional information.
Configuration Date available in Product Variants (Assembly) will be used
for the given selection range.
Generate Product Variants Structures options which are not available
as Processing Options will get defaulted in accordance with the session
logic.
NAME                            TYPE                    DEFAULT
ProductVariantFrom              domain tccpva           0
ProductVariantTo                domain tccpva           explained below
RollOffAssemblyLineFrom         domain tiasln           ""
RollOffAssemblyLineTo           domain tiasln           explained below
ConfigurableItemFrom            domain tcitem           ""
ConfigurableItemTo              domain tcitem           explained below
ConfigurationDateFrom           domain tiutcs           0
ConfigurationDateTo             domain tiutcs           explained below
PrintReport                     domain tcyesno          tcyesno.no
PrintingDevice                  domain tcmcs.str14      ""
PrintingFileoutPathAndName      domain tcmcs.str100     ""
Default values:
ProductVariantFrom - If the input variable field iProductVariantFrom is
given, it will be used as the default value,
otherwise it will be defaulted with 0.
RollOffAssemblyLineFrom - If the input variable field iRollOffLineFrom
is given, it will be used as the default
value, otherwise it will be defaulted with
blank.
ConfigurableItemFrom - If the input variable field iConfigurableItemFrom
is given, it will be used as the default value,
otherwise it will be defaulted with blank
ConfigurationDateFrom - If the input variable field
iConfigurationDateFrom is given, it will be used
as the default value, otherwise it will be
defaulted with 0.
*To -   If the "*From" field is provided then "*To"
field will be defaulted with "*From" field,
otherwise the "*To" fields will be defaulted to
their maximum domain value (ZZZZZZZZ or 9999999 or max. date)
If PrintReport is tcyesno.yes, then the error(s) will be printed
in the report. If it is tcyesno.no, then error(s) will be logged in
Message log.
Output:
oExceptionMessage
- The last error message found during the execution of
public interface. If multiple error messages are found,
by using "oExceptionID", messages can be retrieved.
oExceptionID
- An ID that refers to the exception information. Use
"Exception" related functions to retrieve related
information.
Return: 0, Function succesful, product variant structures are generated
<>0, Error occurred during product variant structure generation.
```
