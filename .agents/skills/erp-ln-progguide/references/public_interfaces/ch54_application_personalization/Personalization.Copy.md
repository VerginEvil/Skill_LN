# Personalization.Copy

> Chapter: Chapter 54 Public Interfaces for Application Personalization
>
> Group: Public Interfaces for Personalization
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1963-1965

```baan
DLL:   ttextadvapi
This function is available from 2026.07 (KB3680922).
Syntax: long Personalization.Copy(
domain  ttadv.culv       iFromPersonalizationLevel,
domain  ttadv.udrc       iFromPersonalizationFor,
domain  ttadv.culve      iToPersonalizationLevel,
domain  ttadv.udrc       iToPersonalizationFor,
domain  ttyeno           iCopyAllPersonalizations,
domain  ttadv.ptyp       iPersonalizationType,
domain  ttadv.cpac       iPackage,
domain  ttadv.cmod       iModule,
domain  ttadv.csmr       iSessionMenuReport,
domain  ttadv.vaid       iReportVariant,
domain  ttadv.parm       iMenuSequence,
domain  ttyeno           iCopySessionPersonalizations,
domain  ttyeno           iCopyFilters,
domain  ttyeno           iCopyConditionalFormatting,
domain  ttyeno           iCopyMenus,
domain  ttyeno           iCopyReports,
domain  ttyeno           iOverwriteUserPersonalizations,
long             iProcessingOptionSet,
ref             string           oExceptionMessage() mb,
ref             long             oExceptionID )
Usage:        Expl:   This function copies all Personalizations, Conditional Formats
and Filters to these levels:
- User
- Role
- Enterprise Modeler role
- Company
Existing Session Personalizations will be overwritten.
See session Copy Personalizations (ttadv9250m000) for more information.
Pre:    There should be no open database transaction before calling
this public interface.
Post:   Changes are committed to the database.
Input:
iFromPersonalizationLevel       - Source Level. Mandatory
User/Role/Company
iFromPersonalizationFor         - Source Personalization for.
Mandatory
iToPersonalizationLevel         - Target Level. Mandatory
/User/Pers.Role/EM Role/Company
iToPersonalizationFor           - Target Personalization for.
Mandatory
iCopyAllPersonalizations        - Copies all Personalizations
(Sessions, Menus and Reports)
of the Source to the Target.
If one copy failed the copyAll
will continue with the rest.
Mandatory
Use these arguments to copy a specific Source Personalization to
the Target:
iPersonalizationType            - Personalization Type Session,
Menu or Report.
Mandatory if
iCopyAllPersonalizations is No
iPackage                        - Package
Mandatory if
iCopyAllPersonalizations is No
iModule                         - Module
Mandatory if
iCopyAllPersonalizations is No
iSessionMenuReport              - Session, Menu or Report code
Mandatory if
iCopyAllPersonalizations is No
iReportVariant                  - Report Variant of a Report
iMenuSequence                   - Sequence Number of Parallel
Menus
Include or exclude these Personalizations from the given Source,
when copying to the Target:
iCopySessionPersonalizations    - Copy Session Personalizations.
Mandatory
iCopyFilters                    - Copy the Filters. Mandatory
iCopyConditionalFormatting      - Copy Conditional Formats.
Mandatory
iCopyMenus                      - Copy Menu Personalizations.
Mandatory
iCopyReports                    - Copy Report Personalizations.
Mandatory
iOverwriteUserPersonalizations  - Overwrite the existing User
Personalizations when the
Target is Role or Company Level.
Mandatory
iProcessingOptionSet            - Not Used.
Output: oExceptionMessage       - A message if the return value is not equal
to 0. This message contains the root cause of
the method failure.
oExceptionID            - An ID that refers to all error information. Use
the functions in Exception to get the error
messages.
Return values:
0: Function is executed successfully
-1: Copy failed, as the target is checked out
-2: Delete Personalization failed with error
-3: Copy Session Personalization failed with error
-4: Remove User Level Personalizations by Range failed with error
-5: Copy Menu Personalization failed with error
-6: Copy Report Personalization failed with error
-7: Error during CopyAllPersonalizations
-12:Error with one of the arguments
```
