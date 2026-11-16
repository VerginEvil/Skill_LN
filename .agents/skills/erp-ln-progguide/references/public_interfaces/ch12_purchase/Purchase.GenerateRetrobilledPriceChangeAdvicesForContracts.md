# Purchase.GenerateRetrobilledPriceChangeAdvicesForContracts

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for Purchase
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 399-400

```baan
DLL:   tdextpurapi
This function is available from 2019.12 (KB2079838).
Syntax: long Purchase.GenerateRetrobilledPriceChangeAdvicesForContracts(
domain  tccono           iPurchaseContract,
domain  tccono           iChangeRequest,
domain  tcorno           iAdviceNumber,
domain  tcyesno          iGenerateForOrders,
domain  tcyesno          iGenerateForSchedules,
domain  tcyesno          iShowProgressIndicator,
ref     domain  tcorno           oAdviceNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will generate Retro-Billed Advices* and Advice Lines
based on the given input parameters. The price change is
calculated from the given Contract (that has the newest prices
and discounts) against the Orders and/or Schedules that have
a link to that Contract.
* If the given Advice Number (iAdviceNumber) is a series, then
a new Advice header will be created based upon that series.
If it is an existing Advice, then the given Advice will be used.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iPurchaseContract       -  Purchase Contract: Mandatory
iChangeRequest          -  Contains the change request
number that initiated the
price change.
Must be empty when the price
change was not initiated by
a change request.
iAdviceNumber           -  Advice Number
Can be a series or an Advice ID.
iGenerateForOrders      -  Yes/No
Indicates if Retro Billed advices
must be generated for orders.
iGenerateForSchedules   -  Yes/No
Indicates if Retro Billed advices
must be generated for schedules
iShowProgressIndicator  -  Yes/No
Indicates if showing the
progress indicator is allowed.
Yes: If applicable, the progress
indicator is shown.
No:  The progress indicator
will not be shown.
Output
oAdviceNumber           -  Generated Advice Number
oExceptionMessage       - The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Function was executed successfull.
Price change advices may have been
generated.
<> 0                    - An error occurred during the execution
of the function.
```
