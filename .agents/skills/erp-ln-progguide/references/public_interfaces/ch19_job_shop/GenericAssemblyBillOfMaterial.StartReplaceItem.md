# GenericAssemblyBillOfMaterial.StartReplaceItem

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for GenericAssemblyBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 836-837

```baan
DLL:   tiextpcfapi
This function is available from 2026.10 (KB3684746).
Syntax: long GenericAssemblyBillOfMaterial.StartReplaceItem(
long             iStartMode,
domain  tcsite           iSite,
domain  tcitem           iItemToBeReplaced,
domain  tcitem           iReplacementItem,
domain  tiutcs           iCheckDate,
domain  tiutcs           iValidFromDate,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the session Replace Item in Generic
Assembly BOM (tipcf3218m100). Use this session to replace the
item in the generic assembly bill of material (BOM).
Note that the session can only be started if
- The Configurations by Site field is set to Active or
In Preparation in Implemented Software Components.
- Assembly checkbox is selected in Implemented Software
Components.
- Product Configurator checkbox is selected in Implemented
Software Components.
Pre:    NA
Post:   NA
Input:  iStartMode -
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
iItemToBeReplaced       - Item to be Replaced (Mandatory). If
filled, this should be present in
Items (tcibd0501m0000).
iReplacementItem        - Replacement Item (Optional). If
filled, this should be present in
Items (tcibd0501m0000).
iCheckDate              - Check Date (Mandatory).
iValidFromDate          - Valid From Date (Mandatory).
iProcessingOptionSet    - A Processing Option Set can be created
via a call to
ProcessingOptionSet.Create(). If 0,
then user default/session default
values are applied (Optional).
Processing Options have a direct relationship with the form
fields on session Replace Item in Generic Assembly Bills of
Material (tipcf3218m100) and are not explained in further
detail here.Please refer to the session help for additional
information. Replace Item in Generic Assembly Bills of Material
options which are not available as Processing Options will get
defaulted in accordance with the session logic.
NAME                    TYPE                    DEFAULT
ProductFrom             domain  tcitem          explained below
ProductTo               domain  tcitem          explained below
UseUpInventory          domain  tcyesno         explained below
RetainOriginalItem      domain  tcyesno         explained below
RetainValidFromDate     domain  tcyesno         explained below
ActualVersions          domain  tcyesno         explained below
Default Values:
*From                   - If the input variable field i* is
given, it will be used as the default
value, otherwise it will be defaulted
with blank.
*To                     - If the "*From" field is provided then
"*To" field will be defaulted with
"*From" field, otherwise the "*To"
fields will be defaulted to their
maximum domain value.
UseUpInventory          - Use Up Inventory (Optional). Default
the value to tcyesno.no.
RetainOriginalItem      - Retain Original Item (Optional).
Default the value to tcyesno.no.
RetainValidFromDate     - Retain Valid From Date (Optional).
Default the value to tcyesno.no.
ActualVersions          - Actual Versions (Optional). Default
the value to tcyesno.yes.
Note:
RetainValidFromDate     - Retain Valid From Date (Mandatory).
This is always tcyesno.no if
RetainOriginalItem is tcyesno.yes.
Output: oExceptionMessage       - The last error message found during
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
