# ProjectContractDeliverable.CalculatePlannedDeliveryOrReceiptDate

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectContractDeliverable
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1708-1709

```baan
DLL:   tpextpdmapi
This function is available from 2024.08 (KB2329987).
Syntax: long ProjectContractDeliverable.CalculatePlannedDeliveryOrReceiptDate(
domain  tccono           iContract,
domain  tpctm.cnln       iContractLine,
domain  tppdm.tdel       iTypeOfDeliverable,
domain  tcyesno          iReturnDeliverable,
domain  tccprj           iProject,
domain  tcitem           iItem,
domain  tcsite           iSite,
domain  tccwar           iWarehouse,
domain  tccrte           iRoute,
domain  tccfrw           iCarrier,
domain  tcmcs.serv       iServiceLevel,
domain  tccdec           iTermsOfDelivery,
domain  tcptpa           iPointOfTitlePassage,
domain  tccom.cadr       iShipToAddress,
domain  tccshp           iShipToBusinessPartner,
domain  tcdate           iPlannedDeliveryDate,
domain  tcdate           iPlannedReceiptDate,
ref     domain  tcdate           oPlannedDeliveryDate,
ref     domain  tcdate           oPlannedReceiptDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionId )
Usage:        Expl:   This function determines the planned delivery
date or the planned receipt date.
If the planned delivery date is zero, it will be
calculated backwards from the planned receipt date.
If the planned receipt date is zero, it will be
calculated forward from the planned delivery date.
Pre:    Not Applicable
Post:   Not Applicable
Input:  iContract               - Contract.
mandatory, if iProject is empty
optional, if iProject is provided
iContractLine           - Contract Line.
mandatory, if iProject is empty
optional, if iProject is provided
iTypeOfDeliverable      - Type of Delivery. Mandatory
iReturnDeliverable      - Return Deliverable(Yes/No). Mandatory
iProject                - Project code linked to contract
deliverable line. Optional
iItem                   - Item. Mandatory
iSite                   - Site. Optional
iWarehouse              - Warehouse. Mandatory
iRoute                  - The Route linked to the contract
deliverable. Optional
iCarrier                - Carrier for the contract
deliverable. Optional
iServiceLevel           - Service Level. Optional
iTermsOfDelivery        - Delivery terms for the contract
deliverable. Optional
iPointOfTitlePassage    - The Point of title passage for the
contract deliverable. Optional
iShipToAddress          - Address code of the ship to
business partner. Optional
iShipToBusinessPartner  - Ship to Business Partner. Mandatory
iPlannedDeliveryDate    - Planned Delivery Date. Optional
iPlannedReceiptDate     - Planned Receipt Date. Optional
Output: oPlannedDeliveryDate    - Planned Delivery Date
oPlannedReceiptDate     - Planned Receipt Date
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       - Planned Receipt date, Planned Delivery date determined
<> 0    - Planned Receipt date, Planned Delivery date not determined
```
