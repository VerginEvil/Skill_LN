# Call.TransferToPlannedActivity

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for Call
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1373-1373

```baan
DLL:   tsextclmapi
This function is available from     2025.09 (KB3614353  ).
Syntax: long Call.TransferToPlannedActivity(
domain  tcorno           iCall,
ref     domain  tcyesno          oCallIsBlocked,
ref     domain  tcorno           oPlannedActivity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to transfer a Call to a new Planned Activity.
Note that the Master Routing or the Required Activity must be
set on the Call.
Before transferring the call, based on the blocking settings
defined in the Call Management parameters, it is checked if the
call must be blocked. When the call is set to blocked, the call
cannot be transferred and output argument oCallIsBlocked
will be set to Yes.
Pre:                  -
Post:   This function sets a retry              -point and will commit and/or abort
the transaction.
Input:  iCall
Call Number: Mandatory
================================================================
Output: oCallIsBlocked
Indicates if the Call is set to blocked.
If the Call is blocked, the Call will not be
transferred.
oPlannedActivity
The Planned Activity that the Call was transferred to.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0    :  Transfer successful or Call is Blocked
<> 0 :  Error occurred
```
