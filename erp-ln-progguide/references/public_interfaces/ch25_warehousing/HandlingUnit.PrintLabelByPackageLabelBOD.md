# HandlingUnit.PrintLabelByPackageLabelBOD

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1043-1044

```baan
DLL:   whextwmdapi
This function is available from     2021.04 (KB2182068  ).
Syntax: long HandlingUnit.PrintLabelByPackageLabelBOD(
domain  tclabl           iLabelLayout,
domain  tcmcs.long       iNumberOfCopies,
ref     domain  whhuid           iHandlingUnitArray() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will publish the PackageLabelBOD for the
handling units that are passed in the iHandlingUnitArray().
For each handling unit the handling unit structure is searched
for labeled handling units. For each handling unit passed, the
PackageLabelBOD will be published.
For example:
Handling unit structure contains a pallet, with 2 crates and
4 boxes per crate. The pallets and crates are labeled.
If the following handling unit structure is present
HU0001                       - Pallet
-                         HU0002 - Crate
-                            HU0003 - BOX
-                            HU0004 - BOX
-                            HU0005 - BOX
-                            HU0006 - BOX
-                         HU0007 - Crate
-                            HU0008 - BOX
-                            HU0009 - BOX
-                            HU0010 - BOX
-                            HU0011 - BOX
When this function is called with handling unit HU0001, the
following labels will be printed via the PackageLabelBOD:
HU0001, HU0002, HU0007;
When this function is called with handling unit HU0002, the
following labels will be printed via the PackageLabelBOD:
HU0002;
When this function is called with handling unit HU0003, there
will be no PackageLabelBOD, because handling unit HU0003 is
not labeled.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iLabelLayout                          - Label Layout
iNumberOfCopies                               - Number of copies; By default 1 label
is printed per labeled handling unit,
so passing this variable as 1 will
mean 2 labels are printed, the
original one and a copy. Maximum value
is 99.
iHandlingUnitArray                            - Array of handling units for which
labels must be printed; Mandatory
Output: N.a.
Return: 0               - Success
<> 0                       - Error
```
