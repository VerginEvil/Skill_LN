# Sales.StartProcessProFormaInvoices

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for Sales
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 286-288

```baan
DLL:   tdextslsapi
This function is available from 2023.05 (KB2290270).
Syntax: long Sales.StartProcessProFormaInvoices(
long             iStartMode,
boolean          iIgnoreSelectionFields,
domain  tcyesno          iProcessOrders,
domain  tcyesno          iProcessInstallments,
domain  tcyesno          iProcessSchedules,
domain  tcorno           iFromSalesOrder,
domain  tcorno           iFromSalesSchedule,
domain  tccotp           iFromSalesOrderType,
domain  tccwoc           iFromSalesOffice,
domain  tccom.bpid       iFromSoldToBusinessPartner,
domain  tccom.bpid       iFromShipToBusinessPartner,
domain  tccom.bpid       iFromInvoiceToBusinessPartner,
domain  tcrefs           iFromShipmentReference mb,
domain  tcorno           iToSalesOrder,
domain  tcorno           iToSalesSchedule,
domain  tccotp           iToSalesOrderType,
domain  tccwoc           iToSalesOffice,
domain  tccom.bpid       iToSoldToBusinessPartner,
domain  tccom.bpid       iToShipToBusinessPartner,
domain  tccom.bpid       iToInvoiceToBusinessPartner,
domain  tcrefs           iToShipmentReference mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the session Process Pro Forma
Invoices (tdsls4248m000).
Input:  iStartMode
Not Used.
iIgnoreSelectionFields
If true, From/To selection fields will not be
filled in the session.
iProcessOrders
Process orders, must be Yes or No.
iProcessInstallments
Process installments, must be Yes or No.
iProcessSchedules
Process schedules, must be Yes or No.
iFromSalesOrder
From Sales Order selection field is filled with this
value. (when iIgnoreSelectionFields is false)
iFromSalesSchedule
From Sales Schedule selection field is filled with this
value. (when iIgnoreSelectionFields is false)
iFromSalesOrderType
From Sales Order Type selection field is filled with this
value. (when iIgnoreSelectionFields is false)
iFromSalesOffice
From Sales Office selection field is filled with this
value. (when iIgnoreSelectionFields is false)
iFromSoldToBusinessPartner
From Sold-to Business Partner selection field is filled
with this value. (when iIgnoreSelectionFields is false)
iFromShipToBusinessPartner
From Ship-to Business Partner selection field is filled
with this value. (when iIgnoreSelectionFields is false)
iFromInvoiceToBusinessPartner
From Invoice-to Business Partner selection field is
filled with this value. (when iIgnoreSelectionFields
is false)
iFromShipmentReference
From Shipment Reference selection field is filled with
this value. (when iIgnoreSelectionFields is false)
iToSalesOrder
To Sales Order selection field is filled with this
value. (when iIgnoreSelectionFields is false)
iToSalesSchedule
To Sales Schedule selection field is filled with this
value. (when iIgnoreSelectionFields is false)
iToSalesOrderType
To Sales Order Type selection field is filled with this
value. (when iIgnoreSelectionFields is false)
iToSalesOffice
To Sales Office selection field is filled with this
value. (when iIgnoreSelectionFields is false)
iToSoldToBusinessPartner
To Sold-to Business Partner selection field is filled
with this value. (when iIgnoreSelectionFields is false)
iToShipToBusinessPartner
To Ship-to Business Partner selection field is filled
with this value. (when iIgnoreSelectionFields is false)
iToInvoiceToBusinessPartner
To Invoice-to Business Partner selection field is
filled with this value. (when iIgnoreSelectionFields
is false)
iToShipmentReference
To Shipment Reference selection field is filled with
this value. (when iIgnoreSelectionFields is false)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error.
```
