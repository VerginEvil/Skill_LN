# Chapter 5 Guidelines for Baan 4GL application sessions

This chapter provides several guidelines for Baan 4GL programmers, such as which constructions cannot be used in the program scripts, and when the session must be run through the AFS.

## Predefined variable api.mode

In 4GL scripts, the predefined variable api.mode is present to know whether the session is started by the AFS. If different behavior is required for sessions that run in API-mode and sessions with a normal user-interface, this variable must be used.

If the variable api.mode is used in a DLL, this variable must be declared in the dll as extern long, otherwise, this can cause compile errors.

If you start a subsession from the active session, this activated session also starts automatically in api.mode.

## Messages

As described in Chapter 4, “Special issues,” the message handling is very important. Because no user interface is present, nobody can see what happened exactly in the session. Functions such as set.input.error(), choice.again(), etc., which cause the session to cancel the requested action, can only be used if a message is given, or must not be called in api.mode.

**Examples**

```baan
choice.cont.process:
before.choice:
if reprint = tcyesno.no and delete = tcyesno.no then
choice.again()
endif
```

In this example, the AFS never knows that nothing is done, while a normal user can see that the hourglass disappears immediately. To solve this, a message must be given, at least in api.mode:

```baan
choice.cont.process:
before.choice:
if reprint = tcyesno.no and delete = tcyesno.no then
if api.mode then
mess("dtfsas0001", 1)
|* No processing option selected
endif
choice.again()
endif
```

An exception applies for choice.again(). Occasionally you must bypass the behavior of a session:

```baan
choice.zoom:
before.choice:
if dtfsa001.type = dttype.normal then
zoom.to$("dtfsa1500m000", z.session, "", "", 0)
choice.again()
endif
```

In this situation, the message Command cancelled is generated, and as a result, the AFS-user must ignore the message Command cancelled.

In some cases, messages are returned to the AFS that contain information only. If this message is followed by a choice.again(), the AFS treats this as an error:

```baan
choice.cont.process:
on.choice:
do.all.processing()
mess("dtfsas0002", 1)
choice.again()
```

Preferably, use the following code:

```baan
choice.cont.process:
on.choice:
do.all.processing()
if not api.mode then
mess("dtfsas0002", 1)
endif
choice.again()
```

## Choice.again()

Only use choice.again() to stop the current choice section. Choice.again() used in field sections stops the field loop if records are inserted or updated by the AFS, so fields following on the same form and subsequent forms are not filled with the values from the field buffer.

## Execute(…)

To help the end users, a choice sometimes starts automatically, for example, starting the add.set when no records are present. If the session runs in api.mode, starting choices automatically can result in undesired results.

**Example**

```baan
form.1:
init.form:
execute(find.data)
if filled.occ = = then
execute(add.set)
endif
```

Preferably, use the following code:

```baan
form.1:
init.form:
if not api.mode then
execute(find.data)
if filled.occ = = then
execute(add.set)
endif
endif
```

## Hidden functionality

The AFS cannot reach functionality that is only accessible through zooming on field level. For example, if you click a zoom button for a field, a menu appears to maintain or display records. If no separate main session exists to maintain these records, no new record can be entered through the AFS.

## Commands

If the session has more than one form, keep the form commands (standard and form specific) the same. AFS does not have a notion of current form.
