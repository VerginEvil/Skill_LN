# rprt_open()

## Syntax:
`function long rprt_open( )`

## Description
This is a short version of [brp.open()](brp.open.md). It has the same effect as:
brp.open( spool.report, spool.device, 1 )
That is, it prints the current report to the default device. The predefined variables *spool.report* and *spool.device* store the names of the current report and default device respectively.

## Return values
> 0 an ID for the activated report
0 report could not be activated
-1 spooler could not be opened

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:

- TIVLevel >= 2120 and In a not trusted process

## Example
```

if rprt_open() <= 0 then     | Opens spooler and report
      return
endif
.....
<store report values>
rprt_send()
rprt_close()
```

## Related topics
- [Reports overview and synopsis](overview_and_synopsis.md)

- [Spooling overview and synopsis](../functions_spooling/overview_and_synopsis.md)
