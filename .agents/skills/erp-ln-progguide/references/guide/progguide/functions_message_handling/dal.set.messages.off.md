# dal.set.messages.off()

## Syntax:
`function void dal.set.messages.off( )`

## Description
Turns off [dal.set.error.message()](dal.set.error.message.md). After calling dal.set.messages.off(), any calls to dal.set.error.message() are ignored.
To turn on [dal.set.error.message()](dal.set.error.message.md) again, use [dal.set.messages.on()](dal.set.messages.on.md).

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  Multiple calls to dal.set.messages.off() require an equal number of calls to dal.set.message.on() in order to enable messages again

## Example of when dal.set.error.message() is ignored
```

function a()
{
    dal.set.messages.off()      | messages are now off
    b()                         | call function b(), see below
    dal.set.error.message(...)  | will be ignored
    dal.set.messages.on()       | messages are now on
    dal.set.error.message(...)  | will set a message
}

function b()
{
    dal.set.messages.off()      | messages still off
    dal.set.error.message(...)  | will be ignored
    dal.set.messages.on()       | NOTE: messages still off!
                                | This is, because at this point,
                                | dal.set.messages.off() has been
                                | called 2 times, and
                                | dal.set.messages.on() only once.
    dal.set.error.message(...)  | will be ignored
}
```

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
