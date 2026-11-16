# Process Change Manager Code Examples
The most common use of the Process Change Manager is to trigger other sessions to refresh the data on the screen. This can be achieved by registering observer sessions to a certain table. E.g. if updates are done in an Order Header table, then any session that registered itself for this table will be notified, by means of a BMS message. The examples below show how this can be done in both 4GL and 3GL code.

## Subject sessions
In this example a subject session is a session should notify other sessions after it performs updates on a database table.
In case the subject session is a 4GL session and the session performs the choice UPDATE.DB (either via the Save in the UI or by calling `execute(UPDATE.DB)` in the UI script), other sessions will automatically be notified. But in case the maintable is updated directly in the UI script or via a DLL function, then this session itself is responsible for notifying any observer sessions. This can be achieved by calling [prcm.notify()](prcm.notify.md) after a commit.transaction() has been done.
Note  Do not call [prcm.notify()](prcm.notify.md) for the maintable in the *after.update.db.commit* section or the [after.commit.transaction()](../functions_dal/after.commit.transaction.md) hook of the DAL of the maintable, as this interferes with the automatic notification of the [4GL engine](../glossary/glossary.md#fourgl_engine).
3GL sessions have to take care of notifying other sessions themselves. In general this should be done after a commit.transaction() is done.

## Example
The UI script contains a form command that sets a status field of maintable tisfc001:
```

function extern set.status()
{
    db.retry.point()

    select  tisfc001.*
    from    tisfc001 for update
    where   tisfc001._index1 = {:...}
    as set with 1 rows
    selectdo
        ...
        dal.update("tisfc001", ttisfc001, retval, true, db.retry)
    endselect

    commit.transaction()

    prcm.notify("tisfc001")
}
```

## Observer sessions
In this example an Observer session is a session that is interested in updates done in certain database tables. It wants to be notified about such updates, so that it can take an appropriate action, like refreshing data on the screen.

## Registering
Sessions show their interest in changes in subject sessions by calling [prcm.register()](prcm.register.md).
4GL sessions do this by calling prcm.register() in the *before.program* section of the UI script:
```

before.program:
    prcm.register("tisfc001")
    prcm.register("tisfc005")
```
3GL sessions can do this by calling prcm.notify() at start up of the session (somewhere before entering the main event loop).

## Handling notifications
When a session is notified, it has to handle the notification. A 4GL session does this as follows:
(In this case the session wants to refresh its data on the screen when updates are done on the tables tisfc001 or tisfc005)
```

choice.bms:
on.choice:
    if prcm.bms.is.notification() then
        on case prcm.get.subject()
        case "tisfc001": |* An update is done on table tisfc001
        case "tisfc005": |* An update is done on table tisfc005
            |* Refresh all data on the screen
            refresh.all.occs()
            break
        endcase
    endif
```
See [refresh.all.occs()](../functions_form_and_form_field_operations/refresh.all.occs.md) for more information about refreshing data on the screen.
A 3GL session has to implement its own event loop:
```

function main()
{
    long event(EVTMAXSIZE)

    prcm.register("tisfc001")

    ...

    while true
        next.event(event)
        on case evt.type(event)
        case EVTBUCKETMESSAGE:
            if prcm.bms.is.notification(evt.bms.command(event)) then
                on case prcm.get.subject()
                case "tisfc001": |* An update is done on table tisfc001
                    ...
                endcase
            endif
            break
        ...
        endcase
        ...
    endwhile

    ...
}
```

## Related topics
- [Process Change Manager overview](overview.md)

- [Process Change Manager synopsis](synopsis.md)
