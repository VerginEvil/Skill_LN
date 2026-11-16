# dal.set.messages.on()

## Syntax:
`function void dal.set.messages.on( )`

## Description
Turns on [dal.set.error.message](dal.set.error.message.md).
To turn [dal.set.error.message](dal.set.error.message.md) off, use [dal.set.messages.off](dal.set.messages.off.md).

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  Multiple calls to dal.set.messages.off() require an equal number of calls to dal.set.message.on() in order to enable messages again

## Example of when to use dal.set.messages.on()
```

| BAD Example
function long b()
{
        dal.set.messages.off()
        if ... then
                dal.set.messages.on()
                return(DALHOOKERROR)
        endif
        return(0)
}

function a()
{
        | by default messages are on
        if b() = DALHOOKERROR then
                dal.set.error.message(...)
                | This is not ignored, because
                | dal.set.messages.on() was done in b(),
                | before it returned DALHOOKERROR
        else
                ...
                dal.set.error.message(...)
                | This is still ignored, as when b() returned 0,
                | dal.set.messages.on() was not called!
        endif
}

| Correct Example
function long b()
{
        dal.set.messages.off()
        if ... then
                dal.set.messages.on()
                return(DALHOOKERROR)
        endif
        dal.set.messages.on() | Added
        return(0)
}

function a()
{
        | by default messages are on
        if b() = DALHOOKERROR then
                dal.set.error.message(...)
                | This is not ignored, because
                | dal.set.messages.on() was done in b(),
                | before it returned DALHOOKERROR
        else
                ...
                dal.set.error.message(...)
                | Not ignored either
        endif
}
```

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
