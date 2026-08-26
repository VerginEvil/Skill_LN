# LocationSearchEngine.CheckLocation

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for LocationSearchEngine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2081-2081

Allows to skip or replace a location advised by standard LN search engine. This process extension is available from 2025.04 ( KB3563599 ). Technical information for this process extension:

```baan
Usage:        With this Process Extension it is possible to perform additional
checks on the Location Search Engine, which is used when getting
available location to store the goods.
There are 2 extension points within the process extension, which can be
implemented individually:
The first one (whext.dll0015.overrule.location) will be called from the
standard prior to location constraints checks (multi              -item (lot),
capacity and other properties). This allows the extender to replace the
suggested warehouse location with any other suitable location of their
choice during the execution of the Location Search Engine.
If the location has failed the standard storage condition check,
the selection process will continue until a suitable location is found
or will stop if no available locations are detected.
The other extension point (whext.dll0015.skip.location) will be
called when the Standard LN Location Search Engine has selected the
suitable location and performed standard location availability checks.
Here the user will be able to skip the current location.
```

To implement this process extension, you need to implement the following method(s):
