# ProjectCostPegTransfer.Generate

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProjectCostPegTransfer
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1100-1102

```baan
DLL:   whextinhapi
This function is available from 2023.05 (KB2286749).
Syntax: long ProjectCostPegTransfer.Generate(
domain  tcseri           iSeries,
domain  tccwar           iWarehouse,
domain  tcitem           iItem,
domain  tcuef.effn       iEffectivityUnit,
domain  tcowns           iOwnership,
domain  tccprj           iFromProject,
domain  tcpdm.cspa       iFromElement,
domain  tcpdm.cact       iFromActivity,
domain  tccprj           iToProject,
domain  tcpdm.cspa       iToElement,
domain  tcpdm.cact       iToActivity,
domain  whinh.cptt       iTransferType,
domain  tcqiv1           iQuantity,
domain  tcdate           iRequirementDate,
domain  tccdis           iReason,
domain  tcyesno          iDirectProcess,
ref     domain  tcorno           oProjectCostPegTransfer,
ref     domain  tcpono           oProjectCostPegTransferLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function generates a Project Cost Peg Transfer header and
line. Optionally, the cost peg transfer can be processed
directly.
Only allowed when the Project Pegging concept is enabled in
Implemented Software Components (tccom0500m000).
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iSeries
Series used to generate the Project Cost Peg Transfer.
Must exist for the Number Group defined for Project
Cost Peg Transfers in Inventory Handling Parameters.
If left empty, the series defined in the User Profiles,
Warehouse Settings by Site or Inventory Handling
Parameters are used
iWarehouse (mandatory)
The warehouse where the project cost peg is transferred
iItem (mandatory)
The item of the project cost peg transfer line
iEffectivityUnit
The Effectivity Unit. Only applicable if the item is
lot controlled (in inventory).
iOwnership (mandatory)
The ownership of the project pegged inventory to be
transferred
Only value Company Owned or Customer Owned is allowed.
In case of Customer Owned, the owner of the iFromProject
(or iToProject) is put on the cost peg transfer line.
iFromProject
The Project from which the cost pegs are transferred.
iFromElement
The Element linked to the iFromProject.
Is mandatory if cost control level by element is active
for the iFromProject
iFromActivity
The Activity linked to the iFromProject
Is mandatory if cost control level by activity is active
for the iFromProject
iToProject
The Project to which the project cost peg is transferred
Is mandatory if the iItem is mandatory pegged
iToElement
The Element linked to the iToProject
Is mandatory if cost control level by element is active
for the iToProject
iToActivity
The Activity linked to the iToProject
Is mandatory if cost control level by activity is active
for the iToProject
iTransferType   (mandatory)
The project cost peg transfer type. Allowed values:
- Permanent:
The loaning project is compensated for the cost of the
material. New demand orders are created to replenish it
- Borrow/Loan:
The borrowing project must pay back the borrowed
inventory to the lending project before the next
billing cycle.
No cost is transferred between the projects.
This value is only allowed if:
- iOwnership is Company Owned and
- Both iFromProject as iToProject is filled and
- Manual Borrow/Loan Transfers are allowed according to
the Project Pegging Parameters (tcpeg0100m000)
iQuantity (mandatory)
The quantity to be transferred (in inventory unit)
iRequirementDate
The date on which the target peg requires the goods.
If left empty, the current date is used.
iReason (mandatory)
The reason code of the project cost peg transfer.
Must be of type 'Cost Peg Transfer'
iDirectProcess (mandatory)
Directly process the generated cost peg transfer(Yes/No)
Output: oProjectCostPegTransfer
The generated project cost peg transfer number
oProjectCostPegTransferLine
The generated project cost peg transfer line
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0: OK
<> 0: Error
```
