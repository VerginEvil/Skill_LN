# BMS messages: sample programs

## Example 1
```

| process 1
ret = bms.send("do_action_1", 0, "tfgld1201s000", 0)

| background process "tfgld1201s000"
bms.add.mask("bms.shutdown")            | to detect the shutdown
event
                                        | which is sent by the
system
....
bucket = bms.receive$()
if bucket = "bms.shutdown" then
        end.process()           | contains del.window command
else
        if bucket = "do_action_1" then
                action_1()
        endif
endif
```

## Example 2
```

long    event(EVTMAXSIZE)
string  bms.ret(2048)

while true
        next.event(event)
        on case evt.type(event)
        case EVTBUCKETMESSAGE:
                bms.ret = bms.receive$()
                handle.bucket.message( bms.ret )
                break
        case EVTKEYPRESS:
                ....
        case EVTBUTTONPRESS:
                ....
        endcase
endwhile

function handle.bucket.message( const string bms.str() )
{
        string  key.of.record(100)

        on case bms.str
        case "first":
                key.of.record = get.first.record()
                bms.send(key.of.record, event, "",
evt.bms.sender(event))
                break
        case "last":
                key.of.record = get.last.record()
                bms.send(key.of.record, event, "",
evt.bms.sender(event))
                break
        case "next":
                key.of.record = get.next.record()
                bms.send(key.of.record, event, "",
evt.bms.sender(event))
                break
        case "prev":
                key.of.record = get.prev.record()
                bms.send(key.of.record, event, "",
evt.bms.sender(event))
                break
        endcase
}
```

## Related topics
- [Interprocess communication (OS level) overview](../functions_interprocess_communication_os_level/overview.md)

- [Interprocess communication (bshell) overview](overview.md)

- [Interprocess communication (bshell) synopsis](synopsis.md)
