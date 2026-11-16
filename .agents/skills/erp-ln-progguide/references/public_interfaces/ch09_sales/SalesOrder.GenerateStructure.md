# SalesOrder.GenerateStructure

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 323-326

```baan
DLL:   tdextslsapi
This function is available from 2024.12 (KB3538863).
Syntax: long SalesOrder.GenerateStructure(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
long             iProcessingOptionSet,
ref             boolean          oStructureGenerated,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl. : This function generates the project (PCS) structure or product
structure for the items of all lines of a sales order or for the
item of a specific order line.
The execution of automatic order steps is not started. Function
SalesOrderLine.StartAutomaticProcessing can be used for this.
Pre:    Caller must set a retry-point by default.
When the Processing Option "ConsiderMaterialPricing" is set to
Yes (tcyesno.yes), the transaction management is done by the
function itself, setting a retry-point is not needed.
See also Processing Option "ConsiderMaterialPricing" below for
more information.
Post:   Caller must commit/abort the transaction by default.
When the Processing Option "ConsiderMaterialPricing" is set to
Yes (tcyesno.yes), the transaction management is done by the
function itself, commit or abort is not needed.
See also Processing Option "ConsiderMaterialPricing" below for
more information.
Input:  iSalesOrder             - Sales order (Mandatory)
iSalesOrderLine         - Sales order line (Optional)
If 0, a structure is generated for
all order lines if applicable.
If not 0, a structure is generated
only for the specified order line.
iProcessingOptionSet    - Processing Option Set (Optional).
If 0, the default values for the
settings and option fields of session
'Generate (Project PCS) Structure'
(tdsls4244m000) are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Processing Options have a direct relationship with the form fields
available in the Selection and Options groups of session 'Generate
(Project PCS) Structure'. Please refer to the session help for additional
information on these fields.
Session option "Print to predefined Device" is not available, because
printing is not supported using this function.
Any options which are not available as Processing Options will get
defaulted in accordance with the logic of session 'Generate (Project PCS)
Structure'.
Supported Processing Options and their defaults:
NAME                                    TYPE                    DEFAULT
ConsiderMaterialPricing                 domain tcyesno          tcyesno.no
GenerationMethod                        domain tccpge           tccpge.eto
ProjectSeries                           domain tcseri           ""
InitialProjectStatus                    domain tcpsts           tcpsts.active
CreateProjectPerSalesOrder              domain tcyesno          tcyesno.yes
EquateProjectWithSalesOrder             domain tcyesno          tcyesno.yes
CheckStandardItemInventory              domain tcyesno          tcyesno.yes
IgnoreWarehouseFromBOM                  domain tcyesno          tcyesno.no
CreateOrderLinesForPhantom              domain tcyesno          tcyesno.no
GenerateProjectPartsForCostServiceItems domain tcyesno          tcyesno.no
GenerateProjectPartsForAllOrders        domain tcyesno          tcyesno.no
Some notes on options:
- ConsiderMaterialPricing
This option is not available on the session. Normally session
'Generate (Project PCS) Structure' updates material pricing content
for applicable items when the concept "Material Pricing" is used
(concept "Material Pricing" reads Yes in session 'Implemented Software
Components', tccom0500m000/tccom0100s000). The logic that updates
material pricing content has its own transaction management. This
forces the logic of generating a project or product structure to also
use its own transaction management.
Function SalesOrder.GenerateStructure uses the available logic of
session 'Generate (Project PCS) Structure' and so, transaction
management controlled by the caller is normally not possible. This
restricts the use of the function.
Therefore option "ConsiderMaterialPricing" has been added. The option
can have 2 values:
No (tcyesno.no, the default value if it is not specified)
- the logic for Material Pricing is skipped
- the caller must use its own transaction management
Yes (tcyesno.yes)
- the logic for Material Pricing is executed when applicable
- the caller cannot use its own transaction management
- GenerationMethod
Valid values:
- tccpge.eto (Engineer-to-Order)
- tccpge.sto (Standard-to-Order)
- InitialProjectStatus
Valid values:
- tcpsts.free (Free)
- tcpsts.simulation (Simulated)
- tcpsts.active (Active)
- CreateProjectPerSalesOrder
This option can be overruled by the setting of Sales Order Parameter
"Link Installments to Projects". If this parameter reads Yes, the option
is ignored and the system  will generate one project per Sales Order.
Not all combinations of options are possible:
- CreateProjectPerSalesOrder
If this option is set to No, the value of option
EquateProjectWithSalesOrder must be set to No.
The system will correct the value of EquateProjectWithSalesOrder
if needed.
- EquateProjectWithSalesOrder
If this option is set to No, it is mandatory to provide a valid
series with option ProjectSeries. If the ProjectSeries is not
provided or it does not exist, the function cannot continue and
returns an error.
- CreateOrderLinesForPhantom
If this option is set to No, the value of option
IgnoreWarehouseFromBOM must be set to No. The system will correct
the value of option IgnoreWarehouseFromBOM if needed.
Examples:
1) Caller uses default Processing Options. So Processing Option
"ConsiderMaterialPricing" is No (the default).
Update of material pricing content is skipped, and the caller must
handle the transaction management.
domain  tcorno          sales.order
domain  tcpono          sales.order.line
boolean         structure.generated
boolean         process.stopped
domain  tcmcs.str132    exception.message
long            exception.id
long            processing.option.set
long            ret.val
sales.order = "SLS000101"
sales.order.line = 0
processing.option.set = 0
db.retry.point()
ret.val  = SalesOrder.GenerateStructure(
sales.order,
sales.order.line,
processing.option.set,
structure.generated,    |* ref
exception.message,      |* ref
exception.id)           |* ref
if ret.val = 0 then
commit.transaction()
else
abort.transaction()
endif
2) Caller wants Material Pricing to be updated. Processing Option
"ConsiderMaterialPricing" must be set to Yes, meaning transaction
management is done by function  ProcessingOptionSet.Create.
domain  tcorno          sales.order
domain  tcpono          sales.order.line
boolean         structure.generated
boolean         process.stopped
domain  tcmcs.str132    exception.message
long            exception.id
long            processing.option.set
long            ret.val
sales.order = "MPR000101"
sales.order.line = 0
ret.val = ProcessingOptionSet.Create(
processing.option.set,  |* ref
exception.message,      |* ref
exception.id,           |* ref
|* Options to be set:
"ConsiderMaterialPricing",
tcyesno.yes)
if ret.val = 0 then
ret.val  = SalesOrder.GenerateStructure(
sales.order,
sales.order.line,
processing.option.set,
structure.generated,    |* ref
exception.message,      |* ref
exception.id)           |* ref
endif
if processing.option.set <> 0 then
ret.val = ProcessingOptionSet.Delete(
processing.option.set)  |* ref
endif
Output:
oStructureGenerated     - True:  A structure has been generated
- False: No structure has been generated
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - No error occurred
<> 0                    - An error occurred
```
