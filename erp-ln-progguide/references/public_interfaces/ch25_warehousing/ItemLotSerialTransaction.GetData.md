# ItemLotSerialTransaction.GetData

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ItemLotSerialTransaction
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1128-1128

```baan
DLL:   whextltcapi
This function is available from 2023.02 (KB2275936).
Syntax: long ItemLotSerialTransaction.GetData(
domain  whltc.tord       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcitem           iItem,
domain  tcclot           iLot,
domain  tcibd.sern       iSerial,
domain  tctrns.date      iTransactionDate,
domain  tcyesno          iDirectDelivery,
ref     domain  tcedm.revi       oRevision,
ref     domain  tccom.bpid       oBusinessPartner,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function reads order line related data for items
which are lot controlled or serialized and for which
lot/serial tracking applies.
The following fields are retrieved:
- Revision (Engineering Item Revision)
- Business Partner
If possible, the Business Partner is retrieved from the
Item, Lot and Serial Transactions (whltc310) for the item, lot
and/or serial passed. If not found, it is determined from the
Ship-from Code (for receipt transactions) or Ship-to Code (for
issue transactions) of the warehousing order (history).
The Revision is read from the inbound/outbound warehouse
order line (history) tables.
Pre:    n.a.
Post:   n.a.
Input:  iOrderOrigin            - Order Origin used in the LTC Module
(mandatory)
iOrderNumber            - Order Number (mandatory)
iOrderLine              - Order Line (mandatory)
iItem                   - Item (mandatory)
iLot                    - Lot
iSerial                 - Serial Number
iTransactionDate        - Transaction Date (UTC Date/Time)
iDirectDelivery         - Direct Delivery Y/N (mandatory)
Output: oRevision               - Engineering Item Revision
oBusinessPartner        - Business Partner
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK
<> 0: error
```
