# Job.Activate

> Chapter: Chapter 50 Public Interfaces for Job Management
>
> Group: Public Interfaces for Job
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1934-1935

```baan
DLL:   ttextaadapi
This function is available from     2025.11 (KB3634024  ).
Syntax: long Job.Activate(
const   domain  ttaad.cjob       iJob,
ref             string           oExceptionMessage() mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface activates a Job. The following rules apply for the
Job:
-                       Current user must have authorization for the Job.
-                       Job must have been defined with 'Use External Schedule'.
-                       Job must contain at least one active session.
-                       Job status must be 'Free'; this implies that it can be activated only
once, until the execution is ready.
The Job will be queued and picked up by the Job Scheduler as soon as
possible. Note that if the Job is not defined as 'Periodical', it can be
activated only once, because it will be deleted after the execution.
Pre:    db.retry.point() must have been set.
Post:   abort.transaction() or commit.transaction() must be done.
Input:  iJob                                  - The Job which must be activated. Mandatory.
Output: oExceptionMessage                     - A message if the return value is not equal
to 0. This message contains the root cause of
the of the method failure.
oExceptionID                                  - An ID that refers to all error information. Use
the functions in Exception to get the error
messages.
Return values:
0                                             - Function is executed successfully
<> 0                                          - Error(s) occurred
```

## Public Interfaces for JobSession

The following functions are available: JobSession.ChangeInputValue
