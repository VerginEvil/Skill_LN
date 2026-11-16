# ExchangeScheme.NonRegularImport

> Chapter: Chapter 49 Public Interfaces for Exchange
>
> Group: Public Interfaces for ExchangeScheme
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1947-1948

```baan
DLL:   daextxchapi
This function is available from 2024.03 (KB2321682).
Syntax: long ExchangeScheme.NonRegularImport(
domain  daxch.cxch       iExchangeScheme,
domain  daxch.cbat       iBatchFrom,
domain  daxch.cbat       iBatchTo,
domain  daxch.pint       iBatchSequenceNumberFrom,
domain  daxch.pint       iBatchSequenceNumberTo,
domain  daxch.redo       iProcessingType,
domain  daxch.yesno      iReprocessRecordsRejectedDueToErrors,
domain  daxch.yesno      iReprocessRecordsRejectedDueToConditions,
domain  daxch.yesno      iOverruleBatchCompany,
domain  daxch.comp       iBatchCompany,
domain  daxch.yesno      iReallyQuitOnStopCondition,
ref             long             oRunNumber,
ref             long             oTryNumber,
ref     domain  daxch.yesno      oProcessStoppedDueToStopCondition,
ref             string           oExceptionMessage(),
ref             long             oExceptionId )
Usage:        Expl:   This function does a non regular import of the given
ExchangeScheme.
Based on session "Import Data (on a Non Regular Basis)" (daxch0223m000)
Pre:    NA
Post:
Input:
iExchangeScheme         - Exchange Scheme code: Mandatory
iBatchFrom              - Batch From:
iBatchTo                - Batch To: Mandatory
iBatchSequenceNumberFrom- Sequence Number From of the batch.
iBatchSequenceNumberTo  - Sequence Number To of the batch.
Mandatory
iProcessingType         - The processing type of the import
procedure: Mandatory
Allowed values
daxch.redo.new       1 (New run)
daxch.redo.restart   2 (Restart Previous run)
daxch.redo.reprocess 3 (Reprocess rejected records)
daxch.redo.continue  4 (Continue interrupted run)
iReprocessRecordsRejectedDueToErrors
daxch.yesno.yes = 1
daxch.yesno.no  = 2
- records that are rejected due to
errors in the previous import run are
processed again: Mandatory
- This option has only influence when
iProcessingType = daxch.redo.reprocess
iReprocessRecordsRejectedDueToConditions
daxch.yesno.yes = 1
daxch.yesno.no  = 2
- records that are rejected due to
conditions in the previous run are
processed again: Mandatory
- This option has only influence when
iProcessingType = daxch.redo.reprocess
iOverruleBatchCompany
daxch.yesno.yes = 1
daxch.yesno.no  = 2
- batch companies that are defined in
the Batches (daxch0104m000) session
are overruled: Mandatory
iBatchCompany           - The LN company that is used instead
of the batch company.
- This option has only influence when
iOverruleBatchCompany = daxch.yesno.yes
iReallyQuitOnStopCondition
daxch.yesno.yes = 1
daxch.yesno.no  = 2
- yes: an import program cannot continue
if it is stopped.
- no: the exchange process will not stop
if a stop condition returns true
Output:
oRunNumber              - The run number of the exchange scheme
that is imported or redone
oTryNumber              - The Try number of the executed run.
oProcessStoppedDueToStopCondition
- Yes the Import was stopped due to a
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
stop condition
Return: 0                       - The Exchange Scheme is imported
or process stopped due to stop condition
<> 0                    - Execution stopped. Exchange scheme,
batch or sequence does not exist
```
