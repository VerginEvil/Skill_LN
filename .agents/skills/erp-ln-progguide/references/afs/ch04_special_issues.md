# Chapter 4 Special issues

## To start application sessions

The application session starts when the first AFS call for that session runs. However, a number of functions return an error message if they are the first function call for a specific session:

**One or more stpapi.put.field() calls must have been**

stpapi.insert()                     performed.

stpapi.update()                   A record must be current, so a stpapi.find() must have been performed.

stpapi.delete()                   A record must be current, so a stpapi.find() must have been performed.

stpapi.save() A stpapi.insert(), stpapi.update() must have been performed.

stpapi.recover() A stpapi.insert(), stpapi.update() must have been performed.

stpapi.continue.process() The session parameters must have been filled.

## Field buffer

## Field loop

During insert and update calls and also continue.process, print.data, and form.command calls on type 4 forms, the field loop of the 4GL-Engine is executed.

All fields on all forms are processed. For these fields, the 4GL-sections are executed. Between the sections before.input and before.checks, the value is extracted from the field buffer when the value is filled by a stpapi.put.field() call. To find out whether the field is put, another array is used; this array contains an entry for each field, which indicates whether the field is put. This array is initialized after each stpapi.* function call, which caused the session to use the values (for example, stpapi.insert()).

## Field buffer as input

The following AFS functions cause the 4GL-Engine to take the values from the field buffer:

Function                            Remark

stpapi.insert()

stpapi.update()

stpapi.find() Only key fields

stpapi.change.view() Only view fields

stpapi.continue.process()         Only in a form of type 4, for other form  types the record must be made current (with a find or browse function)

stpapi.print.report()             Only in a form of type 4, for other form  types the record must be made current (with a find or browse function)

stpapi.application.option()       Only in a form of type 4, for other form  types the record must be made current (with a find or browse function)

stpapi.zoom.option()              Only in a form of type 4, for other form  types the record must be made current (with a find or browse function)

stpapi.form.command()             Only in a form of type 4, for other form  types the record must be made current (with a find or browse function)

For the form fields, the field loop is run, as described in “Field loop,” in this chapter. Messages from the field checks, or messages raised during the processing, are returned.

## Field buffer as output

The following AFS functions cause the 4GL-Engine to update the values in the field buffer:

Function                            Remark

stpapi.insert()                   Field buffer is updated wi th the values written to the database (for example, the determined order number overwrites the input value, which only contained a series number)

stpapi.update()                   Field buffer is updated wi th the values written to the database (for example, the determined order number overwrites the input value, which only contained a series number)

stpapi.save()                     Field buffer is updated wi th the values written to the database (for example, the determined order number overwrites the input value, which only contained a series number)

stpapi.recover() Restor es the old values

stpapi.find() The field buffer is updated  with the values of the record, which is made Current. Function                            Remark

stpapi.browse.set() The field buffer is updated with the values of the record, which is made Current.

stpapi.browse.view() By default, the first set of the view is returned, but the application session can react differently on the view events; the field buffer is updated with the values of the current record in the session

stpapi.synchronize.dialog() The field buffer of the single-occurrence session is updated (only of Modify and Display) with the values of the current record of the single-occurrence session

## Message handling

## Introduction

One of the main issues of using the AFS is modifying the Infor ERP database through the business logic of the sessions. Validations performed in the session scripts must also be performed when AFS runs the session.

In case of incorrect data, error messages are returned through the AFS to the calling program. This section describes this message handling.

## Functions

The following Baan 4GL functions can raise messages:

- void message( string mess _str(.) [, arg, ...] )

- void mess( string messcode(14), long mode [, arg, ...] )

- void set.input.error( string messcode(14) [, arg, ...] )

- void dal.set.error.message( string mess.or.code [, arg ...])2

- void skip.io( string mesg(14) [, ...] )

- void abort.io( string mesg(14) [, ...] )

All messages given by these functions are returned by the AFS; however, messages raised by mess() or message() are treated as warning, except when followed by set.input.error(), skip.io(), abort.io(), or choice.again().

Baan 5.x and 6.1 only If the functions set.input.error(), skip.io(), and abort.io() are called with an empty argument and without a mess() or message() call before, an error message is generated. The same applies to the input.again() function.

If a choice.again() is called without a mess() or message() call before it, a Command cancelled warning is generated.

An error is returned in the argument of most stpapi.* functions, warnings can only be retrieved by the function stpapi.get.mess.code().

## Message array

Messages raised by the session are kept in an array, with a maximum of 20 messages. If more than 20 messages are raised, the twenty-first message will be: “More than 20 messages raised by the session, other messages are lost.”

The function stpapi.get.mess.code() gives access to this array. The array has two fields: error code and error text.

The error code can be empty for messages raised by the function message(). In the first call to this function, the last message is returned, then the previous one, etc..

Example of message array:

Code                                      Text

dtfsas0002 Price must be filled

dtfsas0001 Note: Insufficient inventory

In this example, the session first raised a warning, in the check.input of the quantity field, with only a mess() function. In the check.input of thePricefield set.input.error(dtfsas0002) was called, or mess(dtfsas0002, 1) followed by set.input.error(“”). The string “Price must be filled” is also returned in the error argument of the stpapi.insert() call.

If the message array only contains the warning dtfsas0001, no string is returned in the error argument of the stpapi.insert().

For information on how to handle the message array, refer to the example code in Chapter 3, "Baan 4GL engine primitives.”

Before each stpapi.* call, the array is cleaned up, except stpapi.put.field(), stpapi.get.field() and stpapi.get.mess.code().

## Generated error messages

In some situations an error can occur while no error message appears:

- set.input.error, skip.io or abort.io are call ed without a message code and no message or mess function is called before. For skip.io and abort.io, a default message exists in the 4GL-Engine; this one is returned. For set.input.error, no default error message exists, and the error Input cancelled on field …… is returned.

- Input.again is called without a preceding mess age or mess function call, and the error Input cancelled on field …… is returned.

- Choice.again is called without an error message set before. As the AFS does not know whether this function is called before or after the processing, no error message is generated. A warning Command cancelled is written to the message array.

Consider the following examples:

```baan
choice.cont.process: choice.cont.process:
on.choice:  on.choice:
processing()  if some.condition then
choice.again()      choice.again()
else
processing()
endif
```

In the first example, processing is performed, while in the second no processing is performed. The AFS cannot see the difference. In both situations, the warning Command cancelled is written to the message array and the error message argument of the stpapi.continue.process() or stpapi.form.command() remains empty.

## Again Choice.again()

When a choice.again() function is used in the application session, and a message is raised before, the error message argument of stpapi.continue.process() and stpapi.form.command() is filled. However, this will not always imply that an actual error occurred.

Consider the following example:

```baan
choice.cont.process:
on.choice:
processing()
message(“Ready”)
choice.again()
```

In this case, the error message argument is filled with Ready.

To handle this correctly in the calling programs, the programmer must know what happens in the session. If you cannot find out whether the session is run as desired, you must change the application session. Refer to Chapter 5, "Guidelines for Baan 4GL application sessions,” for more details.

## Form commands

Form commands of type Function can also raise messages. Usually, a message is given and a return statement ends the function. In this case, the AFS treats this as warnings, and the stpapi.form.command() call does not return the error message directly. If a choice.again() ends the function, the stpapi.form.command() call returns the error message directly.

## Messages from AFS and 4GL-Engine

The AFS itself can give several messages, for example, if functions are called in the incorrect order. Message codes are not assigned to all of these messages, therefore, the returned string of the function stpapi.get.mess.code() is empty. Because these messages can change, you must no longer parse these strings.

## Multi-occurrence/Single-occurrence

ERP Baan 5.x and 6.1 only: For most inserts and updates in Infor ERP, a combination of a multi- occurrence and single-occurrence sessions are used. The programmer is responsible to get the sessions in a synchronized state. This is not done automatically for better performance and because the AFS cannot determine whether the editable dialog box or the read-only dialog box must be opened.

With the normal interface, synchronizing the multi-occurrence and single-occurrence session is an asynchronous process, so the processes do not wait until the other is synchronized. The AFS, however, waits until the synchronization is ready.

The sequence of the stpapi.* calls is as many of the same actions performed with the user interface as possible to carry out actions on a combination of a multi-occurrence and single-occurrence session.

Synchronization is necessary to:

- Insert records.

- Update records.

- Run a form command of the single-occurrence session.

- Retrieve data from the si ngle-occurrence session.

The following sections describe each of these actions in more detail and provide examples for each action.

## To insert records

To insert a record, you must start both the multi-occurrence session must be started and also the editable single-occurrence dialog box. The values for the new record must be sent to the single- occurrence session. The stpapi.insert() call is sent to the multi-occurrence session, the stpapi.recover() is sent to the single-occurrence session.

To insert records in a type 3 multi-occurrence session (with view), the view must first be set.

Example type 2, multi-occurrence:

```baan
ret = stpapi.synchronize.dialog("dtfsa1501m000", "add", error.msg)
if ret then
stpapi.put.field("dtfsa1101s000", "dtfsa101.seno", str$(new.seno)
stpapi.put.field("dtfsa1101s000", "dtfsa101.name", new.name)
ret = stpapi.insert("dtfsa1501m000", true, error.msg)
if not ret then
ret = stpapi.recover("dtfsa1101s000", error.msg)
endif
endif
stpapi.end.session("dtfsa1501m000", error.msg)
```

**Explanation**

By calling the stpapi.synchronize.dialog() function, the multi-occurrence and single-occurrence sessions are both started. The fields are filled for the single-occurrence session. The insert is sent to the multi-occurrence session (theAddbutton is there). If the insert fails, the recover must be performed on the single-occurrence session (where theRevertbutton resides). The synchronized dialog box is killed when the multi-occurrence session is ended.

Example type 3, multi-occurrence:

```baan
stpapi.put.field("dtfsa1502m000", "dtfsa102.seno", str$(i.seno)
ret = stpapi.change.view("dtfsa1502m000", error.msg)
if ret = 1 then
ret = stpapi.synchronize.dialog("dtfsa1502m000", "add", error.msg)
if ret then
stpapi.put.field("dtfsa1102s000", "dtfsa102.pono", str$(new.pono)
stpapi.put.field("dtfsa1102s000", "dtfsa102.name", new.name)
ret = stpapi.insert("dtfsa1502m000", true, error.msg)
if not ret then
ret = stpapi.recover("dtfsa1102s000", error.msg)
endif
endif
stpapi.end.session("dtfsa1502m000", error.msg)
```

**Explanation**

Similar to the previous example, however, a stpapi.change.view() must be called to fill theViewfield. During the synchronization, the view fields are copied to the single-occurrence session.

## To update records

To update a record, the multi-occurrence session must be started and also the editable single- occurrence dialog box. The values for the new record must be sent to the single-occurrence session. The stpapi.update() call is sent to the multi-occurrence session, and the stpapi.recover() is sent to the single-occurrence session.

No difference exists between type 2 and type 3 multi-occurrence sessions, in both situations the record must be searched in the multi-occurrence session.

**Example**

```baan
stpapi.put.field("dtfsa1501m000", "dtfsa101.seno", str$(i.seno)
ret = stpapi.find("dtfsa1501m000", error.msg)
if ret = 1 then
ret = stpapi.synchronize.dialog("dtfsa1501m000", "modify", error.msg)
if ret then
stpapi.put.field("dtfsa1101s000", "dtfsa101.name", new.name)
ret = stpapi.update("dtfsa1501m000", true, error.msg)
if not ret then
ret = stpapi.recover("dtfsa1101s000", error.msg)
endif
endif
stpapi.end.session("dtfsa1501m000", error.msg)
```

**Explanation**

The record to be modified is searched in the multi-occurrence session. The single-occurrence session is synchronized and the field is updated.

## To run form commands

To run form commands of a synchronized single-occurrence session, the dialog box must also be synchronized if the correct record is found in the multi-occurrence session. The mode of the synchronized dialog box depends on the availability of the command in edit- and/or read-only mode.

Note that for form commands on the multi-occurrence session, no special action is necessary.

**Example**

```baan
stpapi.put.field("dtfsa1501m000", "dtfsa101.seno", str$(i.seno)
ret = stpapi.find("dtfsa1501m000", error.msg)
if ret = 1 then
ret = stpapi.synchronize.dialog("dtfsa1501m000", "modify", error.msg)
if ret then
stpapi.form.command("dtfsa1101s000", 5, "some.function", error.msg)
endif
endif
stpapi.end.session("dtfsa1501m000", error.msg)
```

**Explanation**

The record for which the form command must be executed is searched in the multi-occurrence session. The single-occurrence session is synchronized and the form command is executed.

## To retrieve data from a synchronized dialog box

Required data that is not present in the multi-occurrence session must be retrieved from the synchronized dialog box.

**Example**

```baan
stpapi.put.field("dtfsa1501m000", "dtfsa101.seno", str$(i.seno))
ret = stpapi.find("dtfsa1501m000", error.msg)
if ret = 1 then
ret = stpapi.synchronize.dialog("dtfsa1501m000", "display", error.msg)
if ret then
stpapi.get.field("dtfsa1101s000", 5, "balance", balance)
endif
endif
stpapi.end.session("dtfsa1501m000", error.msg)
```

**Explanation**

The record to be modified is searched in the multi-occurrence session. The single-occurrence session is synchronized and the form command is executed.

## Multi-Main table sessions

MMT sessions are not supported by Application Function Server. However since ES8.7 Solution 1016219 there is support for MMT sessions in Application Function Server Available.

**Example**

```baan
stpapi.put.field("tebmemmtcontr", "tebme004.index", “String1”)
ret = stpapi.find(("tebmemmtcontr", error.msg)
ret = stpapi.browse.set("tebme0113m000", "first.set", error.msg)
stpapi.get.field(("tebme0113m000", "tebme013.string", value)
stpapi.put.field(("tebmemmtcontr", "tebme004.index", "String2")
ret = stpapi.find(("tebmemmtcontr", error.msg)
ret = stpapi.browse.set("tebme0113m000", "first.set", error.msg)
stpapi.get.field(("tebme0113m000", "tebme013.string", value)
stpapi.end.session("tebmemmtcontr",  error.msg)
```

**Explanation**

The controller is started by the first stpapi.put.field on the controller (tebmemmtcontr). The satellites are not started. The satellite session is started by the first command on the satellite session (tebme0113m000). The satellite session is started as a satellite of the just started controller.

To get the data from the satellite the Field Buffers need to be filled. See the topic Field Buffer in this chapter. In this case they are filled by the command stpapi.browse.set.

When the controller moved to another record (In the example done by a stpapi.find on the controller) the record buffers in the satellite are not updated. To get the new record buffers, again a command must be executed as described in the topic Field Buffers.

## Debugging

When you test programs that use the AFS, errors can be in various places:

- The AFS is used incorrectly.

- The used Baan 4GL applicat ion session is not well suited for use by the AFS.

- An error can exist in the communica tion between the AFS and the 4GL-Engine.

Normal debugging of the AFS-using script and/or the Baan 4GL application session is not always possible, or does not give the appropriate information to solve the problem. For this reason, extra logging facilities are present to help the developers to solve problems.

This logging can be activated by setting the environment variable AFSLOG to a non-blank value:

- For ba: ba6.1 -set AFSLOG=1 or AFSLOG=1 ba6.1

- For bw: -set AFSLOG=1 in theCommandfield

During the execution of the AFS-using program, the results of the communication between the AFS and the 4GL-Engine are written to a log file afs.log in the user’s home directory.

Example of logging:

```baan
LOGGING STARTED
2001-07-17
15->get.fields
15<-get.fields...
16->get.fields
16<-get.fields...
15->syncadd
15<-syncadd^A0
>dtfsa0101s000 put.field:dtfsa001.seno 3334
>dtfsa0101s000 put.field:dtfsa001.name name
>dtfsa0101s000 put.field:dtfsa001.date 730630
>dtfsa0101s000 put.field:dtfsa001.yeno 1
>dtfsa0101s000 put.field:dtfsa001.mult 3334
>dtfsa0101s000 enum.answer dtfsa0001:2
16->enum.answer^Adtfsa0001^A2
16<-enum.answer^A0
>dtfsa0501m000 insert
16->add.set+save
16<-add.set+save^A0^A0
<dtfsa0501m000
>dtfsa0501m000 end.session
15->end.program
15<-end.program^A0
```

In this logging, you can see the AFS functions, which the calling program calls, how the functions are translated to the internal protocol between the AFS and the 4GL-Engine, and what the 4GL-Engine returns.

## Text management

The AFS does not support text management.
