# DataAuthorization.DocumentActionAllowed

> Chapter: Chapter 34 Public Interfaces for Authorization and Security
>
> Group: Public Interfaces for DataAuthorization
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1746-1750

```baan
DLL:   tcextsecapi
This function is available from     2020.11 (KB2158660  ).
Syntax: long DataAuthorization.DocumentActionAllowed(
domain  tcsec.auth.doc   iDocumentType,
domain  tcsec.docm       iDocument,
domain  tcncmp           iDocumentCompany,
const           string           iDocumentAction(),
boolean          iSkipActionNotAllowedMessage,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function checks if the user has authorization to perform
a given action for a specific document.
The authorization check is based on applied rules that have been
set up in the Authorization and Security module in Common.
Supported Document actions are:
iDocumentAction                 Description
-----------------------------------------------------------
"VIEW"                          Check if view is allowed
"USE"                           Check if use is allowed
"MODIFY"                        Check if modify is allowed
Supported Document Types:
iDocumentType                   Description
-----------------------------------------------------------
Contract
tcsec.auth.doc.contract         Contract
Project
tcsec.auth.doc.project          Project
Procurement Documents
tcsec.auth.doc.requisition      Requisition
tcsec.auth.doc.rfq              Request for Quotation
tcsec.auth.doc.purch.order      Purchase Order
tcsec.auth.doc.purch.contract   Purchase Contract
tcsec.auth.doc.pur.price.book   Purchse Price Book
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
Input argument iDocumentCompany
Argument iDocumentCompany can be used to specify a different
company than the current company.
The support for this input argument depends on both Document
Type and Document action, and is limited to below list.
A "V" means: supported for the combination of Document Type and
Action.
iDocumentAction
iDocumentType                   VIEW   USE   MODIFY
---------------------------------------------------
Project
tcsec.auth.doc.project            V     V
Production
tcsec.auth.doc.work.center        V     V
tcsec.auth.doc.work.cell          V     V
tcsec.auth.doc.pcs.project        V     V
Service Documents
tcsec.auth.doc.service.contrct    V     V
tcsec.auth.doc.contract.quote     V     V
tcsec.auth.doc.srv.order.quote    V     V
tcsec.auth.doc.mnt.sls.quote      V     V
tcsec.auth.doc.quote.request      V     V
tcsec.auth.doc.service.call       V     V
tcsec.auth.doc.service.order      V     V
tcsec.auth.doc.mnt.sls.order      V     V
tcsec.auth.doc.work.order         V     V
tcsec.auth.doc.customer.claim     V     V
tcsec.auth.doc.supplier.claim     V     V
tcsec.auth.doc.installtn.group    V     V
Warehouses
tcsec.auth.doc.warehouse          V
Items
tcsec.auth.doc.item               V
Invoice Documents
tcsec.auth.doc.man.sls.invoice    V     V       V
Financial Documents
tcsec.auth.doc.transactn.type     V     V
tcsec.auth.doc.ledger.account     V     V
tcsec.auth.doc.gl.code            V     V
tcsec.auth.doc.bank.relation      V     V
tcsec.auth.doc.budget             V     V
tcsec.auth.doc.fin.statement      V     V
Example:
To check if updating a PCS Project is allowed for the current
company.
domain  tcmcs.s999m     exception.message
long            exception.id
#pragma used dll        "otcextsecapi"
if DataAuthorization.DocumentActionAllowed(
|* Document Type: PCS Project
tcsec.auth.doc.pcs.project,
|* PCS Project to check
tipcs020.cprj,
|* Current company
get.compnr(),
|* Document action: Check Modify is
|* allowed
"MODIFY",
|* Skip the authorization error message
true,
|* Return arguments with error
|* information if applicable
exception.message,
exception.id) = 0 then
|* Update record or allow an action command
else
|* Handle the returned error(s)
endif
Pre:    None
Post:   None
Input:  iDocumentType                         - Document Type: Mandatory
iDocument                                     - Document code: Optional
Typically this argument is filled
with a Document number, e.g. a
Contract or Project.
If the Document is empty the action is
allowed (the function will return a
value 0).
iDocumentCompany                              - Document Company: Mandatory
The support for this input field
depends on the Document Type and
Document Action (see table above).
When not supported, the field value
must be set to the current company
(use function get.compnr()), else
the current or another company can
be specified. Company 0 is not
allowed.
iDocumentAction                               - The action that must be checked:
Mandatory
Possible actions: "VIEW", "USE and
"MODIFY".
iSkipActionNotAllowedMessage
-                                               Do not show an error message when
the Document Action is not allowed:
mandatory.
The purpose of this input argument is
to be able to suppress the error
message that is set when the user is
not allowed to perform the action.
This may be useful when printing or
processing Documents and the Documents
for which the user has no authorization
can just be skipped.
If the value is true the error message
not set. When false an error message
could be set and returned in output
argument oExceptionMessage.
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID. When input argument
iSkipActionNotAllowedMessage is set
to true, the returned message in this
argument is the authorization error
message.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - The specified Document action is allowed
<> 0                                          - An Error occurred or the user does not
have authorization for the action
specified.
```
