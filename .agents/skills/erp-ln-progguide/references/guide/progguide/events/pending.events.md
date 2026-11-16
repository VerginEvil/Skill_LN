# pending.events()

## Syntax:
`function long pending.events( )`

## Description
This returns the number of events present in the event queue of the process group. Note that including the function in an empty loop uses a lot of processor time. For example:
```

while pending.events() = 0
       ...
endwhile
```

## Return values
> 0 number of events in event queue
0 empty queue

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long event
if pending.events() > 0 then
                next.event( event )
else
                ....
endif
```

## Related topics
- [Events overview](overview.md)

- [Events synopsis](synopsis.md)

- [Event types](event_types.md)

- [Event array parameters](event_array_parameters.md)

- [Events sample program](sample_program.md)
