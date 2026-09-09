# GenericAssemblyBillOfMaterial.StartValidate

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for GenericAssemblyBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 837-839

```baan
DLL:   tiextpcfapi
This function is available from 2026.10 (KB3684742).
Syntax: long GenericAssemblyBillOfMaterial.StartValidate(
long             iStartMode,
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tibmrv           iVersion,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the session Validate Generic
Assembly BOM (tipcf3217m100). This session validates the
multi-site Generic Assembly Bill of Material (BOM) for specified
Product/Product range (version controlled).
Note that the session can only be started if the parameter
'Job Shop by Site' is 'In Preparation' or 'Active'.
Input:  iStartMode              -
Specifies the start mode for the session.
Possible values are:
MODAL           - The parent session is blocked until
the child session exits. The session
will be started as a zoom session.
MODELESS_ALWAYS - Parent and child are parallel sessions
that can be manipulated
simultaneously, even if the session is
a Dialog.
iSite                   - Site (Optional). If value entered,
then Site must exist in Sites.
iProduct                - Product (Optional). If value entered,
then Product must exist in
Configurable Item - Assembly Line.
iVersion                - Version of the Product(Optional).
iProcessingOptionSet    - A Processing Option Set can be created
via a call to
ProcessingOptionSet.Create(). If 0,
then user default/session default
values are applied (Optional).
Processing Options have a direct relationship with the form
fields on session Validate Generic Assembly BOM (tipcf3217m100)
and are not explained in further detail here.Please refer to the
session help for additional information. Validate Generic
Assembly BOM options which are not available as Processing
Options will get defaulted in accordance with the session logic.
NAME                    TYPE                    DEFAULT
Site                    domain  tcsite          explained below
ProductFrom             domain  tcitem          explained below
ToProduct               domain  tcitem          explained below
VersionFrom             domain  tibmrv          explained below
VersionTo               domain  tibmrv          explained below
ValidateUseUp           domain  tcyesno         explained below
ThresholdQuantity       domain  tcqiv1          explained below
RemoveUseUpItems        domain  tcyesno         explained below
PrintValidBOMs          domain  tcyesno         explained below
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
ValidateUseUp           - Defaulted to tcyesno.no. If set to
tcyesno.yes, LN checks for the use-up
material and whether the last allowed
order date is set correctly.
ThresholdQuantity       - Defaulted to 0.0000. The redundancy
threshold of the use-up inventory. If
the inventory is less than the
specified threshold, or is zero, the
use-up material is defined as
redundant.
RemoveUseUpItems        - Defaulted to tcyesno.no. If set to
tcyesno.yes, the application removes
the use-up material with no stock from
the generic assembly bill of material.
PrintValidBOMs          - Defaulted to tcyesno.no. If set to
tcyesno.yes, LN prints only the
generic assembly bill of materials
that are valid.
Note:
ThresholdQuantity       - Threshold Quantity value can be given
only if ValidateUseUp = tcyesno.yes.
Negative quantity is not allowed for
this field.
RemoveUseUpItems        - Remove Use Up Items value can be given
only if ValidateUseUp = tcyesno.yes.
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
Return: 0                       - Session Started
<> 0                    - Otherwise
```
