# BOD.InterruptPublishing

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1675-1676

```baan
DLL:   tcextbodapi
This function is available from 2022.11 (KB2267552).
Syntax: long BOD.InterruptPublishing(
boolean          iAllBods,
domain  tcbod.name       iNoun,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function interrupts the publishing of all BODs or one
specified BOD in the current process. If parallel processing is
implemented, the BOD publishing will be interrupted in the parallel
processes as well.
For example: session Calculate Standard Cost publishes the
ItemMasterBOD for each item for which the cost price is updated.
If you don't need the ItemMasterBOD from this session, you can
call this function in the Before Command hook of the main
processing with iNoun = "ItemMasterCommonBOD". You can resume the
publishing by calling function BOD.ResumePublishing().
If a process can publish multiple BODs (e.g. SalesOrderBOD,
CustomerReturnBOD and ShipmentBOD) and you want to interrupt the
publishing of two BODs, you can call this function two times and
specify iAllBods as false and iNoun as the BOD for which the
publishing must be interrupted.
Pre:    N/A
Post:   Function BOD.ResumePublishing() must be called to resume the
publishing.
Output:
iAllBods                - true: The publishing of all BODs in the
current process is interrupted.
false: The publishing of the specified
BOD in the current process is interrupted.
iNoun                   - The (protected) Noun for which the
publishing must be interrupted.
Example: ItemMasterCommonBOD.
Mandatory if iAllBods is false. Not
needed / ignored if iAllBods is true.
oExceptionMessage       - A message if the return value is not equal
to 0. This message contains the root cause of
the request failure.
oExceptionID            - An ID that refers to all error information
if the return value is <> 0.
Use the functions in Exception to get
all relevant information.
Return:
0                       - The action to interrupt the publishing was
set successfully.
<> 0                    - The action to interrupt the publishing can
not be set.
```
