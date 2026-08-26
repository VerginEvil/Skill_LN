# Exception.NumberOfMessages

> Chapter: Chapter 2 Public Interfaces for Extensibility
>
> Group: Public Interfaces for Exception
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 81-82

```baan
DLL:   tcextextapi
Syntax: long Exception.NumberOfMessages(
long             iExceptionID )
Usage:        Expl:   This function determines the number if messages that have been
stored in the XML where iExceptionID refers to.
Pre:    iExceptionID should refer to a valid XML with the structure
as described above.
Post:   None
Input:
iExceptionID                          - the exception id that points to the XML.
Output:
None
Return: The number of found messages. If iExceptionID does not refers
to a valid XML the return value is 0.
```

## Public Interfaces for ProcessingOptionSet

The following functions are available: ProcessingOptionSet.CheckOptionNames ProcessingOptionSet.Create ProcessingOptionSet.Delete ProcessingOptionSet.Read
