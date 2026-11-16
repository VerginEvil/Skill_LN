# Exception.GetMessage

> Chapter: Chapter 2 Public Interfaces for Extensibility
>
> Group: Public Interfaces for Exception
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 81-82

```baan
DLL:   tcextextapi
Syntax: Exception.GetMessage(
long             iExceptionID,
long             iMessageIndex,
ref     domain  tcmcs.s999m      oMessageDescription mb )
Usage:        Expl:   This function reads message description from all messages in
the XML identified by iExceptionID for a certain index.
Pre:    iExceptionID should refer to an Exception.
Post:   None
Input:
iExceptionID    - the exception id.
iMessageIndex   - the index for the message to be returned.
iMessageIndex should be greater than zero and
less than the number of messages.
Output:
oMessageDescription - The found message.
Return: None
```
