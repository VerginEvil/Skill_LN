# PlannedPurchaseOrder.Transfer

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlannedPurchaseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 588-590

```baan
DLL:   cpextrrpapi
This function is available from 2024.11 (KB2331324).
Syntax: long PlannedPurchaseOrder.Transfer(
domain  cpcom.plnc       iScenario,
domain  cprrp.orno       iPlannedPurchaseOrder,
domain  tccotp           iPurchaseOrderType,
domain  tcseri           iPurchaseOrderSeries,
boolean          iGenerateRequestForQuotation,
domain  tcseri           iRequestForQuotationSeries,
domain  tcrfq.type       iRequestForQuotationType,
boolean          iRetainBuyer,
domain  tcyesno          iAddToExistingRequestForQuotation,
domain  tcqono           iExistingRequestForQuotation,
long             iProcessingOptions,
boolean          iTransferText,
ref     domain  tckoor           oCreatedOrderType,
ref     domain  cporno           oCreatedOrder,
ref     domain  tcpono           oCreatedOrderLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface transfers a Planned Purchase Order into a
Purchase Order or a Request for Quotation. This function makes
use of a Processing Option Set, which can be created via a call
to ProcessingOptionSet.Create(), and cleaned up after use, via a
call to ProcessingOptionSet.Delete().
Pre:    A db.retry.point should be set.
Post:   Commit or abort the transaction.
Input:  iScenario                       - The Planning Scenario
(Mandatory)
iPlannedPurchaseOrder           - The Planned Purchase Order to
be transferred (Mandatory).
iPurchaseOrderType              - The Purchase Order Type. If
the user does not provide a
value, then the value is
retrieved from the user
purchase profile (Optional).
iPurchaseOrderSeries            - The Purchase Order Series. If
the user does not provide a
value, then the value is
retrieved from the user
purchase profile (Optional).
iGenerateRequestForQuotation    - Control to generate a Request
for Quotation Instead of
generating a Purchase Order.
When no supplier is predefined
for the Planned Purchase Order,
a Request for Quotation may be
generated (Optional).
iRequestForQuotationSeries      - The Request for Quotation -
Order Series. If the user
does not provide a value, then
the value is retrieved
from the user purchase
profile (Optional).
iRequestForQuotationType        - The Request for Quotation -
Order Type. If the user
doesnot provide a value, then
the value is retrieved from
the user purchase profile
(Optional).
iRetainBuyer                    - Control to force that
generated order is linked to
the same Buyer (Optional).
iAddToExistingRequestForQuotation-Control to allow/force
addition to an existing
Request For Quotation
(Optional).
iExistingRequestForQuotation    - The Existing Request for
Quotation that is used when
adding to an existing
quotation (Optional).
iProcessingOptions              - Processing Option Set which
can be used to pass additional
parameters. This parameter is
optional, when zero (0) is
passed, the options get their
defined default values
(Optional).
NAME                            TYPE                    DEFAULT
Contract                        domain tccono           ""
ContractLine                    domain tcpono           0
ContractSequence                domain tcpono           0
ContractPurchaseOffice          domain tccwoc           ""
ContractIgnored                 domain tcyesno          tcyesno.no
Default values:
Contract                - If the contract is selected, it will be used
as the default value, otherwise it will be
defaulted with empty string.
ContractLine            - If the contract is selected,its Contract line
will be as the default value,otherwise it will
be defaulted with 0.
ContractSequence        - If the contract is selected, its sequence
number will be used as the default value,
otherwise it will be defaulted with 0.
ContractPurchaseOffice  - If the contract is selected, its contract
sequence number will be used as the default
value, otherwise it will be defaulted with
empty string.
ContractIgnored         - If the contract is selected, it will be used
as the default value, otherwise it will be
defaulted with tcyesno.no.
iTransferText                   - If true, the text of the
Planned Purchase Order will be
transferred. Default value is
false (Optional).
Output: oCreatedOrderType               - Transferred to Order Type,
possible values are Purchase
Order (tckoor.act.pur) or
Request for Quotation
(tckoor.pur.rfq).
oCreatedOrder                   - The Order that was created.
oCreatedOrderLine               - The Order Line number of the
created Order.
oExceptionMessage               - The last message if any
message is found. If more than
one message is found, these
are present in the
oExceptionID
oExceptionID                    - An ID that refers to the
exception information. Use the
functions in Exception to get
all relevant information.
Return:    0                            - Planned Order successfully
transferred.
<> 0                            - Otherwise.
```
