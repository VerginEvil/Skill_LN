# JobSession.ChangeInputValue

> Chapter: Chapter 50 Public Interfaces for Job Management
>
> Group: Public Interfaces for JobSession
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1935-1937

```baan
DLL:   ttextaadapi
This function is available from     2024.08 (KB3522710  ).
Syntax: long JobSession.ChangeInputValue(
const   domain  ttaad.cjob       iJob,
const   domain  ttaad.sequ       iSessionNumber,
const           string           iFieldName(),
const           string           iNewValue(),
const           boolean          iValidateField,
ref             string           oExceptionMessage() mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface changes one input value for a session in a job. To
change multiple values, the function must be called multiple times.
All types of variables are supported, including dates; however, dates
must be absolute dates. If dates are stored as a relative date, the
change will be ignored, or an error will be set (in case iValidateField
is 'true').
The new value must be cast to a string, so for non                      -string values, use the
str$() function.
Array fields can be handled as well. For string fields, a suffix
(1,<element>) for iFieldName is needed, for example "form.ccur(1,2)" for
the second element in the array. For non                      -string fields the suffix must be
(<element>), e.g. "form.qty(2)". Ensure there are no blanks and leading
zeros in the suffix.
Pre:    db.retry.point() must have been set.
Post:   abort.transaction() or commit.transaction() must be done.
Input:  iJob                                  - The Job for which the input value must be
changed. Mandatory.
iSessionNumber                                - The Session Number (not the Sequence Number!)
in the job for which the input value must
be changed. Mandatory.
iFieldName                                    - The Field Name in the session. Mandatory.
iNewValue                                     - New value for the form field in the job
session. Optional (empty value will clear the
form field).
iValidateField                                - Indicator whether a non-existing field or a
relative date must result in an error.
Otherwise they will be ignored. Mandatory
(true/false).
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

## Chapter 51 Public Interfaces for User Management

## Public Interfaces for User

The following functions are available: User.ConvertToRuntime
