# DataAuthorization.DocumentFilter

> Chapter: Chapter 34 Public Interfaces for Authorization and Security
>
> Group: Public Interfaces for DataAuthorization
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1750-1755

```baan
DLL:   tcextsecapi
This function is available from     2020.11 (KB2158660  ).
Syntax: long DataAuthorization.DocumentFilter(
domain  tcsec.auth.doc   iDocumentType,
const           string           iMainTableDocumentField(),
const           string           iMainTableCompanyField(),
ref             string           oDocumentFilter(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function creates a filter that can be used in sessions to
filter out records for which the user is not authorized
according to applied rules set up in the Authorization and
Security module in Common.
By applying the filter, only records for which the user has
authorization are visible. Being authorized means that the
authorization level must be View, Use or Modify for the document
defined by the main table of the session, e.g. a PCS Project,
Sales Order or a Contract.
The filter is created for the given Document Type (iDocumentType)
and main table document field (iMainTableDocumentField), and must
be added to the standard SQL query of the session using the
query.extend.where function.
Document Types supported:
iDocumentType                   Description
-----------------------------------------------------------
Contract
tcsec.auth.doc.contract         Contract
Project
tcsec.auth.doc.project          Project
Procurement Documents
tcsec.auth.doc.requisition      Requisition
tcsec.auth.doc.rfq              Request for Quotation
tcsec.auth.doc.purch.order      Purchase Order          *1
tcsec.auth.doc.purch.contract   Purchase Contract
tcsec.auth.doc.pur.price.book   Purchase Price Book
tcsec.auth.doc.trgt.price.book  Target Price Book
Sales Documents
tcsec.auth.doc.opportunity      Opportunity
tcsec.auth.doc.sls.quote        Sales Quote
tcsec.auth.doc.customer.order   Received Customer Order
tcsec.auth.doc.sls.order        Sales Order
tcsec.auth.doc.sls.contract     Sales Contract
tcsec.auth.doc.sls.price.book   Price Book
tcsec.auth.doc.sls.catalog      Sales Catalog
Production
tcsec.auth.doc.work.center      Work Center
tcsec.auth.doc.work.cell        Work Cell
tcsec.auth.doc.pcs.project      Project (PCS)
Service Documents
tcsec.auth.doc.service.contrct  Service Contract
tcsec.auth.doc.contract.quote   Contract Quote
tcsec.auth.doc.srv.order.quote  Service Order Quote
tcsec.auth.doc.mnt.sls.quote    Service Quote
tcsec.auth.doc.quote.request    Quote Request
tcsec.auth.doc.service.call     Service Call
tcsec.auth.doc.service.order    Service Order
tcsec.auth.doc.mnt.sls.order    Maintenance Sales Order
tcsec.auth.doc.work.order       Work Order
tcsec.auth.doc.customer.claim   Customer Claim
tcsec.auth.doc.supplier.claim   Supplier Claim
tcsec.auth.doc.installtn.group  Installation Group
Warehouses
tcsec.auth.doc.warehouse        Warehouse
Items
tcsec.auth.doc.item             Item
Business Partners
tcsec.auth.doc.bus.partner      Business Partner
Invoice Documents
tcsec.auth.doc.man.sls.invoice  Manual Sales Invoice
Financial Documents
tcsec.auth.doc.transactn.type   Transaction Type
tcsec.auth.doc.ledger.account   Ledger Account
tcsec.auth.doc.gl.code          General Ledger code
tcsec.auth.doc.bank.relation    Bank Relation
tcsec.auth.doc.budget           Budget (FBS)
tcsec.auth.doc.fin.statement    Financial Statement
Input argument iMainTableCompanyField
Argument iMainTableCompanyField can be used to specify a
company field of the main table in the filter. This company
field holds the actual company where the Document exists. This
can be another (logistic) company or the current company.
If iMainTableCompanyField is not specified, only Documents of
the current company are considered.
Input argument iMainTableCompanyField is optional, with one
exception: it is mandatory for for Document Type "Manual Sales
Invoice".
Also, the argument is only supported for a subset of Document
Types.
Supported Document Types for argument iMainTableCompanyField:
iDocumentType                   Description
-----------------------------------------------------------
Project
tcsec.auth.doc.project          Project
Production
tcsec.auth.doc.work.center      Work Center
tcsec.auth.doc.work.cell        Work Cell
tcsec.auth.doc.pcs.project      Project (PCS)
Service Documents
tcsec.auth.doc.service.contrct  Service Contract
tcsec.auth.doc.contract.quote   Contract Quote
tcsec.auth.doc.srv.order.quote  Service Order Quote
tcsec.auth.doc.mnt.sls.quote    Service Quote
tcsec.auth.doc.quote.request    Quote Request
tcsec.auth.doc.service.call     Service Call
tcsec.auth.doc.service.order    Service Order
tcsec.auth.doc.mnt.sls.order    Maintenance Sales Order
tcsec.auth.doc.work.order       Work Order
tcsec.auth.doc.customer.claim   Customer Claim
tcsec.auth.doc.supplier.claim   Supplier Claim
tcsec.auth.doc.installtn.group  Installation Group
Warehouses
tcsec.auth.doc.warehouse        Warehouse
Items
tcsec.auth.doc.item             Item
Invoice Documents
tcsec.auth.doc.man.sls.invoice  Manual Sales Invoice
Note: mandatory
Financial Documents
tcsec.auth.doc.transactn.type   Transaction Type
tcsec.auth.doc.ledger.account   Ledger Account
tcsec.auth.doc.gl.code          General Ledger code
tcsec.auth.doc.bank.relation    Bank Relation
tcsec.auth.doc.budget           Budget (FBS)
tcsec.auth.doc.fin.statement    Financial Statement
Usage examples:
Example without company field:
string          document.filter(4096)
domain  tcmcs.s999m     exception.message
long            exception.id
#pragma used dll        "otcextsecapi"
if DataAuthorization.DocumentFilter(
|* Document Type: Project
tcsec.auth.doc.project,
|* Main table field name holding the
|* Project
"tppdm600.cprj",
|* No main table field for company
|* specified
"",
|* Return argument with the filter
document.filter,
|* Return arguments with error
|* information if applicable
exception.message,
exception.id) = 0 then
|* No errors: apply the filter
query.extend.where(
document.filter,
EXTEND_APPEND)
else
|* Handle the returned error(s)
endif
Example with company field:
if DataAuthorization.DocumentFilter(
tcsec.auth.doc.warehouse,
"whwmd241.cwar",
"whwmd241.ncmp",
document.filter,
exception.message,
exception.id) = 0 then
|* No errors: apply the filter
query.extend.where(
document.filter,
EXTEND_APPEND)
else
|* Handle the returned error(s)
endif
*1 The functionality of purchase order authorization by
purchase office (see authorization and security parameters)
is not supported by this function.
Pre:    None
Post:   None
Input:  iDocumentType                         - Document Type: Mandatory
iMainTableDocumentField                       - The name of the main table field
containing the Document: Mandatory
Note: this argument must be filled
with a quoted string of the table
field name: e.g. "tipcs020.cprj".
iMainTableCompanyField                        - The name of the main table field
containing a Company: Optional, with
one exception: Mandatory for Document
Type "Manual Sales Invoice".
If set, the Company in the field is
used instead of the current company.
Note: the input of a company field
is not supported by all Document Types.
If supported this argument must be
filled with a quoted string of the
table field name: e.g. "whwmd241.ncmp"
else with an empty string: "".
Output: oDocumentFilter                       - A string containing a SQL filter
to filter records based on
authorization settings for the user.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Successful.
<> 0                                          - An error occurred.
```

## Chapter 35 Public Interfaces for Quality

## Management

## Public Interfaces for OrderInspection

The following functions are available: OrderInspection.Close OrderInspection.Complete OrderInspection.Process
