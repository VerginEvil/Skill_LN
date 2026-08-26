# prcm.get.aspect()

## Syntax:
`function observer processes can call prcm.get.aspect( )`

## Description
Returns the last decoded aspect of the subject that did a notification.

## Return values
The last decoded aspect as string.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Preconditions
- The bms message that was sent to the observer process is expected to be a PRCM notification. This can be tested by calling function [prcm.bms.is.notification()](prcm.bms.is.notification.md). In other words, [prcm.bms.is.notification()](prcm.bms.is.notification.md) must have been called before calling prcm.get.aspect() and it should have returned TRUE.

## Explanation
Subjects can notify observers (i.e. other processes) about certain aspects. Only if an observer registered itself for a combination of subject and aspect, the observer is notified.
Suppose a process wants to notify other processes about delete and insert actions on table fmfoc200. This process can call [prcm.notify()](prcm.notify.md) ("fmfoc200", "delete") to inform processes about a delete action and [prcm.notify()](prcm.notify.md) ("fmfoc200", "insert") to inform processes about an insert action. The 2nd argument in this call defines the aspect.
Observer processes can call prcm.get.aspect() to test for this aspect:
```

before.program:
    |* Register for the delete aspect of the fmfoc200 subject
    prcm.register("fmfoc200", "delete")
    |* Register for the insert aspect of the fmfoc200 subject
    prcm.register("fmfoc200", "insert")
    |* Register for any change of the fmlbd300 subject
    prcm.register("fmlbd300")

choice.bms:
on.choice:
    if prcm.bms.is.notification() then
        on case prcm.get.subject()
        case "fmfoc200":
            on case prcm.get.aspect()
            case "delete":
                |* React on the delete
                break
            case "insert":
                |* React on the insert
                break
            endcase
        case "fmlbd300":
            ...
        endcase
    endif
```

## Related topics
- [Process Change Manager overview](overview.md)
- [Process Change Manager synopsis](synopsis.md)
- [Process Change Manager Code Examples](examples.md)
