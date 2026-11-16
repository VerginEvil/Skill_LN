# Lot.Generate

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Lot
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1115-1116

```baan
DLL:   whextltcapi
This function is available from 2023.09 (KB2303855).
Syntax: long Lot.Generate(
domain  tcitem           iItem,
domain  whltc.olot       iLotOrigin,
domain  tcsite           iSite,
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrder,
domain  tcwset           iOrderSet,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  tcuef.effn       iEffectivityUnit,
domain  tcedm.revi       iRevision,
domain  whltc.ltbp       iBusinessPartnerLot,
domain  tcmcs.cmnf       iManufacturer,
domain  whltc.cert       iCertificateNumber,
domain  tcclot           iOriginalLot,
ref     domain  tcclot           oLot,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface can be used to generate new lot codes.
Based on the lot mask setup, the mask can require the order
information for which the lot code is to be generated, which can
be provided as input to this function (iOrderOrigin, iOrder,
iOrderSet).
When the iLotOrigin is Purchase, the iShipFromBusinessPartner
must be provided as a lot with this origin requires the
reference to the Ship-From Business Partner.
Pre:    db.retry.point()
Post:   abort/commit transaction
Input:  iItem                   - Mandatory
iLotOrigin              - Mandatory, possible values are:
whltc.olot.maint - Maintenance
whltc.olot.prod - Production
whltc.olot.purch - Purchase
iSite                   - Optional
iOrderOrigin            - Optional
iOrder                  - Optional
iOrderSet               - Optional
iShipFromBusinessPartner - Conditionally Mandatory; When the
iLotOrigin is Purchase, this field is
mandatory.
iEffectivityUnit        - Optional
iRevision               - Optional
iBusinessPartnerLot     - Optional
iManufacturer           - Optional
iCertificateNumber      - Optional
iOriginalLot            - Optional
Output: oLot                    - Generated lot
oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0       - Success
<> 0    - Error
```
