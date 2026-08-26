# ExchangeScheme.RegularImport

> Chapter: Chapter 49 Public Interfaces for Exchange
>
> Group: Public Interfaces for ExchangeScheme
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1930-1932

```baan
DLL:   daextxchapi
This function is available from     2024.03 (KB2321682  ).
Syntax: long ExchangeScheme.RegularImport(
domain  daxch.cxch       iExchangeScheme,
domain  daxch.redo       iProcessingType,
domain  daxch.yesno      iReprocessRecordsRejectedDueToErrors,
domain  daxch.yesno      iReprocessRecordsRejectedDueToConditions,
domain  daxch.yesno      iOverruleBatchCompany,
domain  daxch.comp       iBatchCompany,
domain  daxch.yesno      iReallyQuitOnStopCondition,
domain  daxch.yesno      iIgnoreBatchesToImport,
domain  daxch.yesno      iUncompressASCIIFiles,
ref             long             oRunNumber,
ref             long             oTryNumber,
ref     domain  daxch.yesno      oProcessStoppedDueToStopCondition,
ref             string           oExceptionMessage(),
ref             long             oExceptionId )
Usage:        Expl:   This function does a regular import of the given
ExchangeScheme.
Based on session "Import Data (on a Regular Basis)" (daxch0224m000)
Pre:    NA
Post:
Input:
iExchangeScheme                               - Exchange Scheme code: Mandatory
iProcessingType                               - The processing type of the import
procedure: Mandatory
Allowed values
daxch.redo.new       1 (New run)
daxch.redo.restart   2 (Restart Previous run)
daxch.redo.reprocess 3 (Reprocess rejected records)
daxch.redo.continue  4 (Continue interrupted run)
iReprocessRecordsRejectedDueToErrors
daxch.yesno.yes = 1
daxch.yesno.no  = 2
-                                               records that are rejected due to
errors in the previous import run are
processed again: Mandatory
-                                               This option has only influence when
iProcessingType = daxch.redo.reprocess
iReprocessRecordsRejectedDueToConditions
daxch.yesno.yes = 1
daxch.yesno.no  = 2
-                                               records that are rejected due to
conditions in the previous run are
processed again: Mandatory
-                                               This option has only influence when
iProcessingType = daxch.redo.reprocess
iOverruleBatchCompany
daxch.yesno.yes = 1
daxch.yesno.no  = 2
-                                               batch companies that are defined in
the Batches (daxch0104m000) session
are overruled: Mandatory
iBatchCompany                                 - The LN company that is used instead
of the batch company.
-                                               This option has only influence when
iOverruleBatchCompany = daxch.yesno.yes
iReallyQuitOnStopCondition
daxch.yesno.yes = 1
daxch.yesno.no  = 2
-                                               yes: an import program cannot continue
if it is stopped.
-                                               no: the exchange process will not stop
if a stop condition returns true
iIgnoreBatchesToImport
daxch.yesno.yes = 1
daxch.yesno.no  = 2
-                                               yes: the batches in the exchange scheme
are ignored during the import procedure.
-                                               no: the batches in the exchange scheme
are not ignored
iUncompressASCIIFiles
daxch.yesno.yes = 1
daxch.yesno.no  = 2
-                                               yes: compressed ASCII files are restored
to their original format before the
import procedure
-                                               no: ASCII file may not be compressed
Output:
oRunNumber                                    - The run number of the exchange scheme
that is imported or redone
oTryNumber                                    - The Try number of the executed run.
oProcessStoppedDueToStopCondition
-                                               Yes the Import was stopped due to a
stop condition
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - The Exchange Scheme is imported
or process stopped due to stop condition
<> 0                                          - Execution stopped. Exchange scheme,
batch or sequence does not exist
```

## Public Interfaces for ExchangeLogBatchLineLevel

The following functions are available: ExchangeLogBatchLineLevel.StartOverview
