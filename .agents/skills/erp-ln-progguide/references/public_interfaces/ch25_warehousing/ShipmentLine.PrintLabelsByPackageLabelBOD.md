# ShipmentLine.PrintLabelsByPackageLabelBOD

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1175-1176

```baan
DLL:   whextinhapi
This function is available from 2021.07 (KB2196280).
Syntax: long ShipmentLine.PrintLabelsByPackageLabelBOD(
domain  whinh.shpm       iShipment,
domain  tcpono           iShipmentLine,
domain  tclabl           iLabelLayout,
domain  tcmcs.long       iNumberOfCopies,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will publish the PackageLabelBOD for the
handling units that are linked to the iShipment and
iShipmentLine. For each top level handling unit the
PackageLabelBOD will be published.
Pre:    - There should be no pending logical transaction before calling
this function.
- Handling Units should be present for the iShipment and
iShipmentLine
- PackageLabelBOD should be implemented.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iShipment               - Shipment; Mandatory
iShipmentLine           - Shipment Line; Mandatory
iLabelLayout            - Label Layout; Optional
iNumberOfCopies         - Number of copies; By default 1 label
is printed per labeled handling unit,
so passing this variable as 1 will
mean 2 labels are printed, the
original one and a copy. Maximum value
is 99.
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
