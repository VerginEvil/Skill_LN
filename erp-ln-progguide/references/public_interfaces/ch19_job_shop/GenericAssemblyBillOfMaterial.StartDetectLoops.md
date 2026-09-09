# GenericAssemblyBillOfMaterial.StartDetectLoops

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for GenericAssemblyBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 834-836

```baan
DLL:   tiextpcfapi
This function is available from 2026.10 (KB3684744).
Syntax: long GenericAssemblyBillOfMaterial.StartDetectLoops(
long             iStartMode,
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tibmrv           iVersion,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the session Detect Loops in Generic
Assembly Structures(tipcf3218m000). This session detects loops
in Generic Assembly Structures for specified Product/Product
range (version controlled).
Note that the session can only be started if the parameter
'Job Shop by Site' is 'In Preparation' or 'Active'.
Pre:    N.A.
Post:   N.A.
Input:  iStartMode              -
Specifies the start mode for the session.
Possible values are:
MODAL           - The parent session is blocked until
the child session exits, the session
will be started as a zoom session.
MODELESS_ALWAYS - Parent and child are parallel sessions
that can be manipulated
simultaneously, even if the session is
a Dialog.
iSite                   - Site (Optional). If value entered,
then Site must exist in Sites.
iProduct                - Product (Optional). If value entered,
then Product must exist in Configurable
Item - Assembly Line.
iVersion                - Version of the Product(Optional).
iProcessingOptionSet    - A Processing Option Set can be created
via a call to
ProcessingOptionSet.Create(). If 0,
then user default/session default
values are applied (Optional).
Processing Options have a direct relationship with the form
fields on session Detect Loops in Generic Assembly
Structures(tipcf3218m000) and are not explained in further detail
here. Please refer to the session help for additional
information. Detect Loops in Generic Assembly Structures options
which are not available as Processing Options will get defaulted
in accordance with the session logic.
NAME                     TYPE                   DEFAULT
Site                     domain tcsite          explained below
ProductFrom              domain tcitem          explained below
ProductTo                domain tcitem          explained below
VersionFrom              domain tibmrv          explained below
VersionTo                domain tibmrv          explained below
CheckForLoopsAgainstDate domain tcyesno         explained below
ReferenceDate            domain tcdate          explained below
StopAtFirstLoop          domain tcyesno         explained below
PrintVerifiedStructures  domain tcyesno         explained below
Default Values:
Site                    - If the input variable field "iSite" is
given, it will be used as the default
value, otherwise it will be defaulted
from User Profile.
*From                   - If the input variable field i* is
given, it will be used as the default
value, otherwise it will be defaulted
with blank.
*To                     - If the "*From" field is provided then
"*To" field will be defaulted with
"*From" field, otherwise the "*To"
fields will be defaulted to their
maximum domain value.
CheckForLoopsAgainstDate- Defaulted to tcyesno.no. If set to
tcyesno.yes LN performs loop detection
validation against the date entered in
the "Reference Date" field.
ReferenceDate           - Defaulted to current date and time.
StopAtFirstLoop         - Defaulted to tcyesno.no.
PrintVerifiedStructures - Defaulted to tcyesno.no.
Note:                     The "Reference Date" field is only
editable when
CheckForLoopsAgainstDate = tcyesno.yes.
Output:
oExceptionMessage       - The last error message found during
the execution of public interface. If
multiple error messages are found, by
using "oExceptionID", messages can be
retrieved.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started.
<> 0                    - Otherwise.
```
