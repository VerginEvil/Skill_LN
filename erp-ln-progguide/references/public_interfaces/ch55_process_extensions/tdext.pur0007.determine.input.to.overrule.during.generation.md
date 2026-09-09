# tdext.pur0007.determine.input.to.overrule.during.generation

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseOrderGenerate
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2203-2206

```baan
Syntax: long tdext.pur0007.determine.input.to.overrule.during.generation(
const           long             i.input.option.set,
ref             long             o.overruled.input.option.set )
Usage:        Expl:   Use this process-extension to customize the logic used during
purchase order line generation. Use it to overrule specific
input before the purchase order line is created.
Scope:
The extension is invoked for all generation origins (different
callers) and runs early in the generation process.
How it works (high-level)
A request to generate a purchase order line can originate from
multiple sources. Regardless of origin, the same core generation
function is called with source-specific input.
Inside the core generation function, several preparatory steps
run before any purchase order or purchase order line is created:
* Input is normalized and validated.
* Default values for multiple fields are calculated from the
input and context.
* The process-extension (this hook) is invoked to allow
overrides of a small, pre-defined set of input.
* After the extension returns, defaulting and any subsequent
steps proceed using the final input values provided by the
extension.
When the extension is invoked
The extension is executed at an early stage of the generation
function. Because it runs early, values returned by the
extension will be used by later defaulting logic and can
therefore influence how other fields are derived.
Input that can be overruled
The list of input variables that can be overruled is given below.
Be aware, that if an option-set is returned with an unsupported
option, then LN will not overrule any input. Instead, standard
logic for generating the purchase order line will be applied.
Supported Processing Options for o.overruled.input.option.set:
NAME                    TYPE
"tdpur400.ccon"         domain  tcemno
"tdpur400.plnr"         domain  tcemno
Pseudocode:
Below an example is given:
|* Read the context
ret = ProcessingOptionSet.Read(
i.input.option.set,
my.exception.message1,
my.exception.id1,
|* option name                  option-variable                 option
default
"PurchaseOrderOrigin",          purchase.order.origin,          empty,
"SourceGeneratingProcess",      source.generating.process,      0,
"BuyFromBusinessPartner",       buy.from.bp,                    "",
"ShipFromBusinessPartner",      ship.from.bp,                   "",
"PurchaseOffice",               purchase.office,                "",
"Item",                         item,                           "",
"Buyer",                        buyer,                          "",
"Planner",                      planner,                        "")
if <some.condition> then
|* No overruling
return(0)
endif
|* Fill o.overruled.input.option.set to overrule the
|* given input below.
return(ProcessingOptionSet.Create(
o.overruled.input.option.set,           |* ref
my.exception.message1,                  |* ref
my.exception.id1,                       |* ref
"tdpur400.ccon",        "Johnson",
"tdpur400.plnr",        "Smith"))
Pre:    N.A.
Post:   N.A.
Input:  i.input.option.set      - An Option-Set that contains several
attributes regarding the purchase
order/purchase order line that is
about to be created.
The contents of a Processing Option
Set can be read via a call to
ProcessingOptionSet.Read()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Supported Processing Options and their type:
NAME                            TYPE
PurchaseOrderOrigin             domain  tdpur.corg
SourceGeneratingProcess                 long
BuyFromBusinessPartner          domain  tccom.bpid
ShipFromBusinessPartner         domain  tccom.bpid
PurchaseOffice                  domain  tccwoc
Item                            domain  tcitem
Buyer                           domain  tcemno
Planner                         domain  tcemno
Explanation for some of the supported Processing Options:
PurchaseOrderOrigin
- The Purchase Order Origin from / for
which the purchase order is generated.
SourceGeneratingProcess
- Indicates the source process from /
for which the purchase order is
generated and where an order header
can be created.
Possible Values:
0           Undefined - Use
PurchaseOrderOrigin
to determine the source
process
1           Sales Order Components
(Kitting)
2           Return Rejected
The following generation sources can be affected by the process
extension. These processes are either identified by the origin
(PurchaseOrderOrigin) or by the value of
i.source.generating.process.
Source Process                  Value of PurchaseOrderOrigin
- Unexpected Warehouse Receipts         tdpur.corg.wh.receipt
- RFQ                                   tdpur.corg.inquiries
- Subcontracting Purchase Order         tdpur.corg.subc.pur.order
- Subcontracting Purchase Schedule      tdpur.corg.subc.pur.sched
- Production                            tdpur.corg.sfc
- Planning                              tdpur.corg.mrp
- Purchase Payment (Pay on Use)         tdpur.corg.payment
- Price Calculation                     tdpur.corg.price.calc
- Sales                                 tdpur.corg.sls
- Warehousing                           tdpur.corg.inv
- Contract Delivery Scheme              tdpur.corg.contracts
- Service Material Cost Lines           tdpur.corg.sma
- Maintenance Work Order                tdpur.corg.wcs
- Price Calculator                      tdpur.corg.price.calc
- Assembly                              tdpur.corg.asc
- List items                            tdpur.corg.manual
- Net Prices per Buy-from Business      tdpur.corg.manual
Partner
- Copy BOM                              tdpur.corg.manual
- Project (PRP Orders)                  tdpur.corg.project
- Requisition                           tdpur.corg.requisition
- Orders generated through external     tdpur.corg.manual
integrations: BOD/BDE/...
Source Process                  Value of SourceGeneratingProcess
- Sales Order Components (Kitting)      1
- Return Rejected                       2
BuyFromBusinessPartner  - Buy-from Business Partner
ShipFromBusinessPartner - Ship-from Business Partner
PurchaseOffice          - Purchase Office
Item                    - Item
Buyer                   - Buyer
Planner                 - Planner
output:
o.overruled.input.option.set
- Processing Option Set. If 0, then no
overruling of input will be done.
Standard LN logic will be executed.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
The Processing Option Set must be
created as a list of key-value pairs.
Supported options are listed above.
If an option-set is returned with an
unsupported option, then LN will not
overrule any input. Instead, standard
logic for generating the purchase order
line will be applied.
Return: 0                       - Success
<> 0                    - When an error occurs.
The standard logic for generating the
purchase order line will be applied.
```
