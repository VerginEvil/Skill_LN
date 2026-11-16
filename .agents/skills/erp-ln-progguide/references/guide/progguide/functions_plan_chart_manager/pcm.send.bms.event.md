# pcm.send.bms.event()

## Syntax:
`function void pcm.send.bms.event( long command, ref string arglist )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
Use this in a process started by [pcm.activate.session()](pcm.activate.session.md) in order to send an event back to the application that started the session.

## Arguments
| | | |
|---|---|---|
| `long` | `command` |  The command to be sent back to the application. The Chart Manager places this in the variable  |
| `ref string` | `arglist` |  The argument list. The application can retrieve this string by calling [bms.receive$()](../functions_interprocess_communication_bshell/bms.receive.md).  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Application
```

| handle events
while next.event(event)
        evt.bucket = bms.receive$()
        on case evt.bms.sender(event)
        case appl.pid:
                pcm.bucket = evt.bucket
                if pcm.bucket(1;1) = "0" then
                        item.f = pcm.bucket(2;16)
                        item.t = pcm.bucket(18;16)
                else
                        if pcm.bucket(1;1) = "1" then
                                cprj.f = pcm.bucket(2;6)
                                cprj.t = pcm.bucket(8;6)
                        endif
                endif
                pcm.refresh(plan_id)
                break
        case ...
                        ....
        endcase
          ....
endwhile

| start session
tt.session.desc("ppmod1000m000", desc)
appl.pid = pcm.activate.session("ppmod1000m000", desc)
```

## Other process
```

choice.cont.process:
before.choice:
        event.bucket(1;1) = "0"
        event.bucket(2;16) = item.f
        event.bucket(18;16) = item.t
        pcm.send.bms.event(0, event.bucket)

choice.end.program:
before.choice:
        event.bucket(1;1) = "1"
        event.bucket(2;6) = cprj.f
        event.bucket(8;6) = cprj.t
        pcm.send.bms.event(0, event.bucket)
```

## Related topics
- [Plan Chart Manager overview](overview.md)

- [Plan Chart Manager synopsis](synopsis.md)

- [Plan Chart Manager: example](example.md)
