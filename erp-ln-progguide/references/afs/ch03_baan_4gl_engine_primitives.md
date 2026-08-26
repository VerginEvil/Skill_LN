# Chapter 3 Baan 4GL engine primitives

In most AFS functions in which a session is mentioned as a parameter, the session is starts automatically if the session is not already running. Functions that require that the session already be started return an error if no function is called before the started session. For more information, refer to Chapter 4, “Special issues.” This implies that all subsequent function calls for the same session to be sent to the same session instance.

The sessions that the AFS starts must be 4GL sessions. You cannot run 3GL sessions without a form and a script of type 3GL (Without Std.Prog) with the AFS.

## Get Field Value from session

**Syntax**

```baan
void stpapi.get.field (string session, string field, ref string value, [long
element])
```

**Arguments**

- *session:*  Name of the session on which this command is executed.

- *field*: Name of the field whose value is desired.

- *value* : Upon return, this parameter contains the string representation of the current value of the field specified in *field*. For fields that contain enum or set values, the string representation of the numeric value is returned, not the text description of this value. Date and UTC fields are not converted, so the Baan 3GL internal long values are returned as string. Normal numeric values are also returned as string (for example, -123.45), no conversion based on display formats or language dependent format is performed.

- *element*  : Array element whose value is to be returned in the case of arrays or repeating fields.

**Description**

This returns the current value of a particular field from a specified running Infor ERP session. If the field is available in the field buffer, the value is taken from there. Otherwise, the value is extracted directly from the session. For information on the stpapi.* functions that cause the field buffer to be updated, see Chapter 4, “Special issues.”

**Return Values**

None.

**Example**

```baan
stpapi.put.field("dtfsa1101s000", "dtfsa100.seno", str$(i.seno))
retval = stpapi.find("dtfsa1101s000", error.msg)
if retval = 1 then
stpapi.get.field("dtfsa1101s000" , "dtfsa100.name", o.name)  st papi.get.field("dtfsa1101s000",
"balance", o.balance)
endif
```

**Explanation**

In the dtfsa1101s000 session, the record with key i.seno is searched. The values of the fields dtfsa100.name , which is the table field on the form, andbalance, which is the calculated field on the form, are retrieved from the session.

**Usage Notes**

Function in dll created by creatdll:

```baan
Function extern domain <domain-name> <fs-name>.get.<field-descr>()
```

ERP Baan5.x and ERP Enterprise (LN) only: If the AFS calls a synchronized session (multi- occurrence/single-occurrence) the fields must be taken from the session in which the field resides. This implies that if a field must be fetched from the single-occurrence dialog box, a synchronize call must have been performed (see stpapi.synchronize.dialog()).

For segmented fields, the get.field function must be performed on the separated segments. A get function on the segmented field itself will not work.

**Example**

```baan
retval = stpapi.find("dtfsa2500m000", error.msg)
if retval = 1 then
stpapi.get.field("dtfsa2500m000", "d tfsa200.segm.segment.1", “1”)
stpapi.get.field("dtfsa2500m000", "d tfsa200.segm.segment.2", “2”)
endif
```

## Set Field Value in session

**Syntax**

```baan
void stpapi.put.field(string session, string field, string value, [long
element])
```

**Arguments**

- *session* : Name of the session this command is executed on.

- *field*: Name of the field whose value is desired.

- *value* : The value of the field specified in*field*is set to the contents of this parameter. Any necessary type conversion is performed, however, Date and UTC fields must be placed in the internal Baan 3GL format. Enum fields must be put in the internal byte value. Examples: str$(date.num()), str$(-123.45), str$(etol(tcyesno.yes)).

- *element*  : Array element whose value is to be set in the case of arrays or repeating fields.

**Description**

This sets the current value of a particular field in a specified running Infor ERP session. If the field is available in the field buffer, the value is placed in the field until the value is processed by the field loop in the session. For more information, refer to Chapter 4, “Special issues.” If the field is not available in the field buffer, the field value is directly sent to the session with the put.var function.

Note that no field sections in the script are run during the put.field call, therefore, no validation is performed. These sections are called when all fields are processed for an insert or update call.

**Return Values**

None.

**Example**

```baan
stpapi.put.field("dtfsa1201s000", "seno.f", str$(i.seno))
stpapi.put.field("dtfsa1201s000", "seno.t", str$(i.seno))
stpapi.put.field("dtfsa1201s000", "proc.date", str$(date.num()))
stpapi.put.field("dtfsa1201s000", "do.update", str$(etol(dtyesno.no)))
stpapi.continue.process("dtfsa1201s000", error.msg)
```

**Explanation**

For a processing session, the input fields are sent to the session, and the continue process function of the session is run.

**Usage Notes**

Function in dll created by creatdll:

```baan
Function extern void <fs-name>.put..<field-descr>(const domain <domain-name>
value)
```

The case and alignment of the passed string values is not relevant. The AFS automatically converts the value to the correct domain.

ERP Baan 5.x and ERP Enterprise (LN)) only: If fields are sent to a single-occurrence session, which is synchronized with a multi-occurrence session, the values must be put after a stpapi.synchronize.dialog() call is issued to the multi-occurrence session, because otherwise the single-occurrence session is activated without a link to the multi-occurrence session. For segmented fields, the put.field function must be performed on the separated segments. A put function on the segmented field itself will not work.

**Example**

```baan
stpapi.put.field("dtfsa2500m000", "dtfsa200.segm.segment.1", “1”)
stpapi.put.field("dtfsa2500m000", "dtfsa200.segm.segment.2", “2”)
stpapi.put.field("dtfsa2500m000”, “dtfsa200.int”, “1”)
stpapi.insert("dtfsa2500m000", error.msg)
```

## Clear All fields

**Syntax**

```baan
void stpapi.clear(string session)
```

**Arguments**

*Session*            Name of the session this command is executed on.

**Description**

This function fills in an ‘empty’ value (unset) for all input fields of the form.

**Example**

```baan
stpapi.clear(“dtfsa1101s000”)
stpapi.put.field("dtfsa1101s000", "dtfsa101.seno", str$(i.seno)) stpapi.put.field("dtfsa1101s000", "dtfsa101.name", name)
retval1 = stpapi.insert("dtfsa1101s000", true, error.msg)
if not retval1 then
retval2 = stpapi.recover("dtfsa1101s000", recover.msg)
endif
```

**Explanation**

Before you perform the put.field actions, you first empty all fields using the clear function.

**Usage Notes**

Function in dll created by creatdll:

```baan
Function extern void <fs-name>.clear()
```

**Note**

In early versions of Functionserver, you required this stpapi.clear function to clear the put field buffers. The newer versions will, after an action such as insert automatically, reset the put field buffers.

## Insert Record in session

**Syntax**

```baan
long stpapi.insert (string session, long do.save, ref string err.mesg)
```

**Arguments**

- *Session*  : Name of the session on which this command is run.

- *do.save:*Flag that specifies whether a database commit must take place within this function. If *do.save*  is set to 1, the update.db choice section of the session will be run before this function returns. If  *do.save*is set to 0, update.db is not run. In this case, a stpapi.save() function must be called afterwards to update the database.

- *err.mesg*  : This parameter contains the text of  the error message if the function cannot complete normally.

**Description**

This inserts the current record of the specified session into the database. The values of the fields in the session must be set before calling this function.

**Return Values**

0 Record not inserted or save failed:   *err.mesg*is filled with the reason.

1 Record inserted:     *err.mesg*is empty

**Example**

```baan
stpapi.put.field("dtfsa1101s000", "dtfsa101.seno", str$(i.seno)) stpapi.put.field("dtfsa1101s000", "dtfsa101.name", name)
retval1 = stpapi.insert("dtfsa1101s000", true, error.msg)
if not retval1 then
retval2 = stpapi.recover("dtfsa1101s000", recover.msg)
endif
```

**Explanation**

The fields to be filled in the table are sent to the session and the insert function is called.

**Usage Notes**

Function in dll created by creatdll:

```baan
Function extern long <fs-name>.insert(long do.update, ref string error))
```

If*err.mesg*is filled, stpapi.recover() must be called before any other stpapi.* commands are issued to this session, or the record can be inserted into the database because the stpapi.end.session() call will perform an update.db action. These error messages can occur:

- Session not available.

- Command disabled; no insert is possible in the current state of the session.

- Editable synchronized dialog box not started (ERP Baan 5.x and ERP Enterprise (LN) only).

- Any error message from the session.

Only use this function with ‘do.save’ 0 if the calling program must distinguish between errors raised by the insert (for example, check.inputs) and the save (for example, skip.io’s in before.write). Do not use it to buffer inserts, because inserts will not be buffered, because the next stpapi.insert() call will run an update.db for the previously inserted record.

If a record is inserted with a type 3 form, the function stpapi.change.view() must be called to set the correct key field values.

ERP Baan 5.x and ERP Enterprise (LN) only: If a record must be inserted with a synchronized single-occurrence dialog box, the dialog box must be synchronized before the first put.field function is called, because otherwise the field buffer is not present. The stpapi.insert() call must be issued to the multi-occurrence session, but the stpapi.put.field() calls to the single-occurrence session. For multi-occurrence sessions of type 3, make sure you call the stpapi.change.view() before the synchronization.

## Update Record in session

**Syntax**

```baan
long stpapi.update(string session, long do.save, ref string err.mesg)
```

**Arguments**

- *session* : Name of the session this command is executed on.

- *do.save:*Flag that specifies whether a database commit must take place within this function. If *do.save*  is set to 1, the update.db choice section of the session runs before this function returns. If   *do.save*is set to 0, update.db does not run. In this case, a stpapi.save() function must be called afterwards to update the database.

- *err.mesg*  : This parameter contains the text of the error message if the function cannot complete normally.

**Description**

This updates the current record of the specified session. The values of the fields in the session must be set before calling this function.

**Return Values**

0 Record not updated or save failed:    *err.mesg*is filled with the reason 1 Record updated:      *err.mesg*is empty

**Example**

```baan
stpapi.put.field("dtfsa1101s000", "dtfsa101.seno", str$(i.seno))
ret = stpapi.find("dtfsa1101s000", error.msg)
if ret = 1 then
stpapi.put.field("dtfsa1101s000", "dtfsa101.name", name)
retval1 = stpapi.update("dtfsa1101s000", true, error.msg)
if not retval1 then
retval2 = stpapi.recover("dtfsa1101s000", recover.msg)
endif
endif
```

**Explanation**

The record to be updated is searched in the session and its name field is updated.

**USAGE NOTES**

Function in dll created by creatdll:

```baan
Function extern long <fs-name>.update(long do.update, ref string error)
```

A record must be current in the session (for example, by a stpapi.find() call), otherwise, the results are unpredictable.

If*err.mesg*is filled, stpapi.recover() must be called before any other stpapi.* commands are issued to this session, otherwise, the record can be updated in the database, because the stpapi.end.session() call performs an update.db action.

These error messages can occur:

- Command disabled: No update is possible in the current state of the session.

- Editable synchronized dialog box not started (ERP Baan 5.x and ERP Enterprise (LN) only).

- Any error message from the session.

Only use this function with do.save 0 if the calling program must distinguish between errors raised by the update (for example, check.inputs) and the save, for example, skip.io’s in before.rewrite. Do not use it to buffer updates, because updates will not be buffered since the next stpapi.find() call to make another record current will execute an update.db for the previously updated record.

ERP Baan 5.x and ERP Enterprise (LN) only: If a record must be updated with a synchronized single-occurrence dialog box, the dialog box must be synchronized before the first put.field function is called, otherwise, the field buffer is not present. The stpapi.update() call must be issued to the multi-occurrence session, but the stpapi.put.field() calls to the single-occurrence session.

## Delete Record from session

**Syntax**

```baan
long stpapi.delete(string session, long do.save, ref string err.mesg)
```

**Arguments**

- *session* : Name of the session this command is executed on.

- *do.save:*This option must be true. Do.save = false is not supported for stpapi.delete. The option is in the function for compatibility reasons but the function will act as do.save = true.

- *err.mesg*  : This parameter contains the text of  the error message if the function cannot complete normally.

**Description**

This deletes the current record of the specified session in the database.

**RETURN VALUES**

0 Record not deleted or save failed:   *err.mesg*is filled with the reason.

1 Record deleted:     *err.mesg*is empty.

**Example**

```baan
stpapi.put.field("dtfsa1101s000", "dtfsa101.seno", str$(i.seno))
ret = stpapi.find("dtfsa1101s000", error.msg)
if ret = 1 then
retval1 = stpapi.delete("dtfsa1101s000", true, error.msg)
if not retval1 then
retval2 = stpapi.recover("dtfsa1101s000", recover.msg)
endif
endif
```

**Explanation**

The record to be deleted is searched in the session and then deleted.

**Usage Notes**

Function in dll created by creatdll:

```baan
Function extern long <fs-name>.delete(long do.update, ref string error)
```

A record must be current in the session (for example, by a stpapi.find() call), otherwise, the results are unpredictable.

If*err.mesg*is filled, stpapi.recover() must be called before any other stpapi.* commands are issued to this session. Otherwise, the record can be deleted in the database, because the stpapi.end.session() call will perform an update.db action. These error messages can occur:

- Command disabled: No update is possible in the current state of the session.

- Any error message from the session.

ERP Baan 5.x and ERP Enterprise (LN) only: If a multi-occurrence session is used with a synchronized dialog box, the delete action must be sent to the multi-occurrence session.

## Save Session Updates to database

**Syntax**

```baan
long stpapi.save(string session, ref string err.mesg)
```

**Arguments**

- *session* : Name of the session on which this command is run.

- *err.mesg*  : This parameter will contain the text of the error message if the function cannot complete normally.

**Description**

This runs the choice section update.db of the specified session. Note that the same effect can be achieved by issuing any of the following functions:

- stpapi.insert()

- stpapi.update()

with the   *do.save*parameter set to 1.

**Return Values**

0 Record not saved:      *err.mesg*is filled with the reason.

1 Record saved:      *err.mesg*is empty.

**Example**

```baan
stpapi.put.field("dtfsa1101s000", "dtfsa101.seno", str$(i.seno))
ret = stpapi.find("dtfsa1101s000", error.msg)
if ret = 1 then
stpapi.put.field("dtfsa1101s000", "dtfsa101.name", name)
retval1 = stpapi.update(" dtfsa1101s000", false, error.msg)
if retval1 then
retval2 = stpapi.save("dtfsa1101s000", false, error.msg) endif
if not retval1 or not retval2 then
retval3 = stpapi.recover("dtfsa1101s000", recover.msg)
endif
endif
```

**Explanation**

The record to be updated is searched in the session and its name field is updated. The update function is called without running update.db directly. The record is saved to the database with the save function.

**Usage Notes**

Function in dll created by creatdll:

```baan
Function extern long <fs-name>.save(ref string error)
```

If*err.mesg*is filled, stpapi.recover() must be called before any other stpapi.* commands are issued to this session, otherwise, the record can be updated in the database as the stpapi.end.session() call will perform an update.db action.

These error messages can occur:

- Command disabled: No update.db is possibl e in the current state of the session.

- Any error message from the session.

ERP Baan 5.x and ERP Enterprise (LN) only: If a record must be saved with a synchronized single- occurrence dialog box, the stpapi.save() call must be issued to the single-occurrence session.

Use the stpapi.insert(), and stpapi.update() calls with the do.save flag set to True, as this is better for performance. Buffering inserts or updates and saving one time will not work, as subsequent stpapi.* function calls will call update.db implicitly. In case of errors, the calling program does not know whether the update.db of the previous record failed, or that the current record is rejected due to field values.

## Recover Session updates

**Syntax**

```baan
long stpapi.recover(string session, ref string err.mesg)
```

**Arguments**

- *session* : Name of the session this command is executed on.

- *err.mesg*  : This parameter will contain the text of the error message if the function cannot complete normally.

**Description**

This runs the choice section recover.set in the specified session.

**Return Values**

0 Record not recovered:     *err.mesg*is filled with the reason. 1 Record recovered:      *err.mesg*is empty.

**Example**

```baan
stpapi.put.field("dtfsa1101s000", "dtfsa101.seno", str$(i.seno))
ret = stpapi.find("dtfsa1101s000", error.msg)
if ret = 1 then
stpapi.put.field("dtfsa1101s000", "dtfsa101.name", name)
retval1 = stpapi.update(" dtfsa1101s000", false, error.msg)
if retval1 then
retval2 = stpapi.save("dtfsa1101s000", false, error.msg)
endif
if not retval1 or not retval2 then
retval3 = stpapi.recover("dtfsa1101s000", recover.msg)
endif
endif
```

**Explanation**

The record to be updated is searched in the session and the record’s name field is updated. The update function is called without running update.db directly. The record is saved to the database using the save function.

**Usage Notes**

Function in dll created by creatdll:

```baan
Function extern long <fs-name>.recover(ref string error)
```

If*err.mesg*is filled, you must call stpapi.end.session()before you issue any other commands to this session.

The error messages returned can be:

- Command disabled: No update is possible in the current state of the session.

- Any error message from the session.

ERP Baan 5.x and ERP Enterprise (LN) only: If a record must be recovered using a synchronized single-occurrence dialog box, the stpapi.recover() call must be issued to the single-occurrence session.

Use the stpapi.insert(), stpapi.update(), and stpapi.delete() calls with the do.save flag set to True, because this setting is more favorable to performance. Buffering inserts or updates and saving one time will provide problems in case records are rejected, because subsequent calls will call update.db implicitly. The calling program does not know then which records failed.

## Set Current Record for session

**Syntax**

```baan
long stpapi.find(string session [, ref string err.mesg])
```

**Arguments**

- *session* : Name of the session on which this command runs.

- *err.mesg*  : This parameter contains the text of the error message if the function cannot complete normally.

**Description**

This finds the record in the session that corresponds with the current values of the session’s key fields and makes the record current. The key field values must be set before calling this function.

The function is         similar to the def.find function in Baan Windows.

**Return Values**

0 No record found: Empty table or error occurred and    *err.mesg*is filled.

1 Record found:      *err.mesg*is empty.

2 A record different from the one requested was found:   *err.mesg*is empty.

**Example**

```baan
stpapi.put.field("dtfsa1101s000", "dtfsa101.seno", str$(i.seno))
ret = stpapi.find("dtfsa1101s000", error.msg)
if ret <> 1 then
message("Record not found")
endif
```

**Explanation**

The key field for the session is put and the record is made current.

**Usage Notes**

Function in dll created by creatdll:

```baan
Function extern long <fs-name>.find([string error(500)])
```

The behavior is the same as a find action through BW:

- If no record exists, no record is shown: Return value 0

- If the record is found, the reco rd is selected: Return value 1

- If the record cannot be found, the next record is selected: Return value 2

- If no record exists, no records are shown: Return value 0

The error messages returned can be:

- Any error message from the session given during the find action.

## Mark Current Record for session

**Syntax**

```baan
long stpapi.mark(string session [, ref string err.mesg])
```

**Arguments**

- *session:* Name of the session this command is executed on.

- *err.mesg*  : This parameter will contain the text of the error message if the function cannot complete normally.

**Description**

This marks the record in the session, which is made current by the stpapi.find() or one of the stpapi.browse.set() functions.

**Return Values**

0 Record is not marked:     *err.mesg*is filled

1 Record marked:      *err.mesg*is empty

**Example**

```baan
stpapi.put.field("dtfsa1501m000", "dtfsa101.seno", str$(i.seno))
ret = stpapi.find("dtfsa1501m000", error.msg)
if ret <> 1 then
message("Record not found")
else
ret = stpapi.mark("dtfsa1501m000", error.msg)
if ret then
stpapi.form.command("dtfsa1501m000", 5, "do.something",
error.msg)
endif
endif
```

**Explanation**

Because the form command needs a record to be marked, the found record is marked before the form command is called.

**Usage Notes**

Function in dll created by creatdll:

```baan
Function extern long <fs-name>.mark([string error(500)])
```

A record must be current in the session, for example, by a stpapi.find() call, otherwise, the results are unpredictable.

These error messages can occur:

- Any error message from the session given during the mark action.

Only one record can be marked.

## Browse Session records

**Syntax**

```baan
long stpapi.browse.set(string session, string option [, ref string err.mesg])
```

**Arguments**

- *session* : Name of the session this command is executed on.

- *option*: This parameter indicates what type of browse action is required. The possible values are first.set, next.set, prev.set, and last.set that correspond with the browse actions first record, next record, previous record, and last record respectively.

- *err.mesg*  : This parameter will contain the text of the error message if the function cannot complete normally.

**Description**

This performs the specified browse action against the indicated session. The resulting record is set as current.

**Return Values**

0 No record found: Empty table, no next or previous record or error occurred and    *err.mesg*is filled.

1 Record found:      *err.mesg*is empty

**Example**

```baan
ret = stpapi.browse.set("dtfsa1101s000", "first.set", error.msg)
while ret
stpapi.get.field("dtfs a1101s000", "dtfsa100.name", o.name)
stpapi.get.field("dtfsa1101s000", "balance", o.balance)
rprt_send()
ret = stpapi.browse.set("dtfsa1101s000", "next.set", error.msg)
endwhile
```

**Explanation**

This piece of code browses through all records of a session and prints the fields.

**Usage Notes**

Functions in dll created by creatdll:

```baan
Function extern long <fs-name>.first([string error(500)])
Function extern long <fs-name>.next([string error(500)])
Function extern long <fs-name>.previous([string error(500)])
Function extern long <fs-name>.last([string error(500)])
```

For next.set and prev.set a record must be current in the session (for example, by a stpapi.find() call), otherwise the results are unpredictable.

These error messages can occur:

- Any error message from the session given during the browse action.

## Set Current View for session

**Syntax**

```baan
long stpapi.change.view(string session [, ref string err.mesg])
```

**Arguments**

- *session* : Name of the session on which this command is run.

- *err.mesg*  : This parameter will contain the text of the error message if the function cannot complete normally.

**Description**

This sets the current view for sessions with forms of type 3 (multiple occurrence plus view). The field values of the view fields must be set prior to calling this function.

The function is similar to the def.find function in Baan Windows.

**Return Values**

0 Empty view found or error occurred and     *err.mesg*is filled

1 View found:     *err.mesg*is empty

2 Another view found:     *err.mesg*is empty

**Example**

```baan
stpapi.put.field("dtfsa1501m000", "dtfsa101.seno", str$(i.seno))
ret = stpapi.change.view("dtfsa1501m000", error.msg)
if not ret then
message(error.msg)
endif
```

**Explanation**

The View field in the session is changed to the given key.

**Usage Notes**

Functions in dll created by creatdll:

```baan
Function extern long <fs-name>.set.view([string error(500)])
```

The behavior is the same as a find/new group action through BW:

- If no records exist, no record is shown: Return value 0

- If at least one record in the view exists, the firs t record in that view is selected: Return value 1

- If the view cannot be set due to either authorizati ons or application logic, the first record in the next view is selected: Return value 2

- If no next group is found, no records are shown: Return value 0.

The error messages returned can be:

- Any error message from the session given during the browse action.

Before you can insert a record on a type 3 form, the view must have been changed to the desired key fields.

## Browse Session Views

**Syntax**

```baan
long stpapi.browse.view(string session, string option [, ref string
err.mesg])
```

**Arguments**

- *session* : Name of the session this command is executed on.

- *option*: This parameter indicates what type of browse action is required. The possible values are:

- first.view: Corresponds to t he first view browse action.

- next.view: Corresponds to the next view browse action.

- prev.view: Corresponds to the previous view browse action.

- last.view: Corresponds to t he last view browse action.

- *err.mesg*  : This parameter will contain the text of the error message if the function cannot complete normally.

**Description**

This runs the specified browse action against the indicated session. The first record of the view being read is set as Current.

**Return Values**

0 No view found or error occurred and    *err.mesg*is filled

1 View found:     *err.mesg*is empty

**Example**

```baan
stpapi.put.field("dtfsa1501m000", "dtfsa101.seno", str$(i.seno))
ret = stpapi.change.view("dtfsa1501m000", error.msg)
if ret then
ret = stpapi.browse.view("dtfsa1501m000", "prev.view", error.msg)
if ret then
message("View before " & str$(i.seno) & " found")
endif
```

**Explanation**

A check is performed whether a view is present before a given view.

**Usage Notes**

Functions in dll created by creatdll:

```baan
Function extern long <fs-name>.first.view([string error(500)])
Function extern long <fs-name>.next.view([string error(500)])
Function extern long <fs-name>.previous.view([string error(500)])
Function extern long <fs-name>.last.view([string error(500)])
```

These error messages can occur:

- Any error message from the session given during the browse action.

## Synchronize Multi-occurrence and Single-occurrence sessions

**Syntax**

```baan
long stpapi.synchronize.dialog(string session, string mode, ref string
err.mesg)
```

**Arguments**

- *session* : Name of the multi-occurrence session on which this command runs.

- *mode:*   The mode in which the synchronized dialog box must be started. The possible values are:

- Add: The dialog box starts and is synchronized in Edit mode. View fields are sent from the multi-occurrence session to the single-occurrence session. Use this mode before a stpapi.insert() call.

- Modify: The dialog box starts and is synchro nized in Edit mode. Use this mode before a stpapi.update() call.

- Display: The dialog box starts in Display mode.

- “ ”: No dialog box is synchronized. Fo r future use when multi-occurrence and single- occurrence sessions have the same code, focus is set to the multi-occurrence session.

- *err.mesg*  : This parameter will contain the text of the error message if the function cannot complete normally.

**Description**

This function synchronizes a multi-occurrence session with the session’s registered synchronized dialog box. Depending on the mode, the session with the editable window is synchronized or the read-only window.

**Return Values**

0 Sessions could not be synchronized:     *err.mesg*is filled.

1 Sessions are synchronized:     *err.mesg*is empty.

**Example**

```baan
stpapi.put.field("dtfsa1501m000", "dtfsa101.seno", str$(i.seno))
ret = stpapi.find("dtfsa1501m000", error.msg)
if ret then
ret = stpapi.synchronize.dialog("dtfsa1501m000", "modify", error.msg)
if ret then
stpapi.put.field("dtfsa1101s000", "dtfsa101.name", new.name)
ret = stpapi .update("dtfsa1501m000", true, error.msg)
endif
endif
```

**Explanation**

The record is searched in the multi-occurrence session. When found, the synchronized dialog box is started, the field changed, and the record updated.

**Usage Notes**

Functions in dll created by creatdll:

```baan
Function extern long <fs-name>.synchronize.dialog(string mode, ref string
error)
```

This function is for ERP Baan 5.x and ERP Enterprise (LN) only.

The error messages returned can be:

- Command disabled; no insert/update is possibl e in the current state of the session.

- Session has no synchronized dialog box.

You must use this function to get the multi-occurrence session synchronized with the session’s connected single-occurrence dialog box. You must call this function before an insert or update call. In addition, you must call this function before you run a Form command on the single-occurrence session, because the editable and display variants can have various sets of form commands. To retrieve data from the single-occurrence dialog box, you must also run the synchronization.

## Send Start processing command to session

**Syntax**

```baan
void stpapi.continue.process(string session, ref string err.mesg)
```

**Arguments**

- *session* : Name of the session on which this command runs.

- *err.mesg*  : This parameter contains the text of the error message if the function cannot complete normally.

**Description**

This causes the choice option cont.process to be executed in the specified session.

**Return Values**

None.

**Example**

```baan
stpapi.put.field("dtfsa1201s000", "seno.f", str$(i.seno))
stpapi.put.field("dtfsa1201s000", "seno.t", str$(i.seno))
stpapi.put.field("dtfsa1201s000", "proc.date", str$(date.num()))
stpapi.put.field("dtfsa1201s000", "do.update", str$(etol(dtyesno.no)))
stpapi.continue.process("dtfsa1201s000", error.msg)
```

**Explanation**

For a processing session, the input fields are sent to the session, and the continue process function of the session runs.

**Usage Notes**

Functions in dll created by creatdll:

```baan
Function extern void <fs-name>.continue(ref string error)
```

This function is for ERP Baan IV only. For ERP Baan 5.x and ERP LN (6.x), use the stpapi.form.command()*.*

The error messages returned can be:

- Any error message from the session.

When a report is printed, the report specifications must have been set by stpapi.set.report().

## Set Session Report parameters

**Syntax**

```baan
void stpapi.set.report(string session, string reportname, string device, ref
string err.mesg)
```

**Arguments**

- *session* : Name of the session on which this command runs.

- *reportname:*  Valid Infor ERP report code for desired report.

- *device:* Valid Infor ERP device code for desired device.

- *err.mesg*  : This parameter contains the text of the error message if the function cannot complete normally.

**Description**

This selects the report to be printed and the device to be printed to if you call stpapi.print.report(), stpapi.continue.process(), or stpapi.form.command().

**Return Values**

None.

**Example**

```baan
stpapi.put.field("dtfsa1401m000", "seno.f", str$(i.seno))
stpapi.put.field("dtfsa1401m000", "seno.t", str$(i.seno))
stpapi.set.report("dtfsa1401m000", "rdtfsa140111000", pr.device, error.msg)
if isspace(error.msg) then
stpapi.continue.process("dtfsa1401m000", error.msg)
endif
```

**Explanation**

The specified session prints the given report.

**Usage Notes**

Functions in dll created by creatdll:

```baan
Function extern void <fs-name>.set.report(string reportname, string device,
ref string error)
```

The case and alignment of the passed string values is not relevant. The AFS automatically converts the value to the correct domain.

The error message that can be returned is for future use. Currently, no errors will be returned by the function. Errors about invalid reports or devices are returned by the subsequent stpapi.print.report(), stpapi.continue.process(), or stpapi.form.command() calls.

Some sessions determine the report to be printed based on the input on the form. If the report code is already known in the session when the report is opened, the value set in the AFS is ignored.

Only one report can be set. Therefore, sessions that print more than one report in one execution cannot be executed with the AFS.

To print the report to a file, use a write-file or rewrite file device. To print the data to another file then the default file for the device, you must also set the spool.fileout variable:

```baan
stpapi.put.field(“<sessioncode>”, “spool.fileout”, myfile)
```

## Send Print command to session

**Syntax**

```baan
void stpapi.print.report(string session, ref string err.mesg)
```

**Arguments**

- *session* : Name of the session this command is executed on.

- *err.mesg*  : This parameter will contain the text of the error message if the function cannot complete normally.

**Description**

This causes the choice option print.data to run in the specified session.

**Return Values**

None.

**Example**

```baan
stpapi.put.field("dtfsa1401m000", "seno.f", str$(i.seno))
stpapi.put.field("dtfsa1401m000", "seno.t", str$(i.seno))
stpapi.set.report("dtfsa1401m000", "rdtfsa140111000", pr.device, error.msg)
if isspace(error.msg) then
stpapi.print.report("dtfsa1401m000", error.msg)
endif
```

**Explanation**

For a print session, the input fields are sent to the session, and the print.data function of the session runs.

**Usage Notes**

Functions in dll created by creatdll:

```baan
Function extern void <fs-name>.print(ref string error)
```

This function is for ERP Baan IV only. For ERP Baan 5.x and ERP Enterprise (LN), use stpapi.form.command().

These error messages can occur:

- Report not found.

- Device not found.

- Any error message from the session.

The report specifications must have been set by stpapi.set.report().

## End session

**Syntax**

```baan
void stpapi.end.session(string session [, ref string err.mesg)
```

**Arguments**

*session*: Name of the session on which this command runs.

**Description**

This ends the specified session.

**Return Values**

None.

**Example**

```baan
stpapi.put.field("dtfsa1101s000", "dtfsa101.seno", str$(i.seno)) stpapi.put.field("dtfsa1101s000", "dtfsa101.name", name)
retval1 = stpapi.insert("dtfsa1101s000", true, error.msg)
if not retval1 then
retval2 = stpapi.recover("dtfsa1101s000", recover.msg)
endif
stpapi.end.session("dtfsa1101s000")
```

**Explanation**

A record is inserted in the session and the session is ended.

**Usage Notes**

Functions in dll created by creatdll:

```baan
Function extern void <fs-name>.end([string error(500)])
```

This error message can be:

- Any error message from the session.

Although sessions are started implicitly (when used for the first time, see Chapter 4, “Special issues”), you must end sessions explicitly.

If the session has activated another session (see also stpapi.handle.subprocess()), you must first end the subsession, because the main session might be waiting until the subsession ends. In this case, the main session cannot accept the protocol message to end.

## Execute session user option

**Syntax**

```baan
void stpapi.application.option(string session, long form, long option, ref
string err.mesg)
```

**Arguments**

- *session* : Name of the session on which this command runs.

- *Form:*Form number on which user option must be executed. User options, such as the commands on the      Specialmenu, are defined for each form.

- *option:* The option number to be run. User options appear as choice.user.x options in the Baan 4GL code where x is a number that ranges from 0 to 9. The value of x that corresponds to the option that you want to activate is provided as the value of this parameter.

- *err.mesg :*   This parameter contains the text of the error message if the function cannot complete normally.

**Description**

This runs the specified user option in the session.

**Return Values**

None.

**Example**

```baan
stpapi.put.field("dtfsa1501m000", "dtfsa101.seno", str$(i.seno))
ret = stpapi.find("dtfsa1501m000", error.msg)
if ret = 1 then
stpapi.application.option("dtfsa1501m000", 2, 3, error.msg)
endif
```

**Explanation**

For the record found, choice user.3 is run on the second form.

**Usage Notes**

Functions in dll created by creatdll:

```baan
Function extern void <fs-name>.<option description>(ref string error)
```

This function is for ERP Baan IV only. For ERP Baan 5.x and ERP Enterprise (LN), use stpapi.form.command().

This error message can be:

- Any error message from the session.

## Execute session zoom option

**Syntax**

```baan
void stpapi.zoom.option(string session, long form, string zoom.prog, ref
string err.mesg)
```

**Arguments**

- *Session*  : Name of the session on which this command runs.

- *Form:*Form number on which zoom must be executed. You must specify this form number, because some sessions depend on a particular form being active when you run the zoom.

- *zoom.prog:*  Infor ERP session for the zoom. This must be the same as the zoom session specified for the choice field of*form*. If the choice specifies a zoom to a menu, this session must be one of those listed on the menu.

- *err.mesg :*   This parameter contains the text of the error message if the function cannot complete normally.

**Description**

This performs a zoom in the specified session to the program given in*zoom.prog*.

**Return Values**

None.

**Example**

```baan
stpapi.put.field("dtfsa1501m000", "dtfsa101.seno", str$(i.seno))
ret = stpapi.find("dtfsa1501m000", error.msg)
if ret = 1 then
stpapi.handle.subproc("dtfsa1501m000", "dtfsa1201m000", "add")
stpapi.zoom.option("dtfsa1501m000", 2, "dtfsa1201m000", error.msg)
stpapi.continue.process("dtfsa1201m000", error.msg)
endif
```

**Explanation**

For the record found, the session dtfsa1201m000 is run, which is connected to theChoicefield or a menu choice of the menu connected to theChoicefield.

**Usage Notes**

This function is for ERP Baan IV only. For ERP Baan 5.x and ERP Enterprise (LN), use stpapi.form.command().

This error message can be:

- Any error message from the main session, which is set in before.choice of choice.zoom.

## Execute session form command

**Syntax**

```baan
void stpapi.form.command(string session, long command.type, string
command.prog, ref string err.mesg)
```

**Arguments**

- *Session*  : Name of the session on which this command runs.

- *command.type:*   The type of form command to be run. The following values apply:

- 2: Session

- 5: Function

- *command.prog:*    The code of the session or the name of the function to be run.

- *err.mesg*  : This parameter contains the text of the error message if the function cannot complete normally.

**Description**

This function causes the specified form command to run in the specified session.

**Return Values**

None.

**Example**

```baan
stpapi.put.field("dtfsa1501m000", "dtfsa101.seno", str$(i.seno))
ret = stpapi.find("dtfsa1501m000", error.msg)
if ret = 1 then
ret = stpapi.mark("dtfsa1501m000", error.msg)
if ret = 1 then
stpapi.form.command("dtfsa1501m000", 5, "calculate.vat",
error.msg)
endif
endif
```

**Explanation**

For the record found, the function calculate.vat is carried out.

**Usage Notes**

Functions in dll created by creatdll:

```baan
Function extern void <fs-name>.<form-command-desc>(ref string error)
```

This function is for Baan 5.x and ERP LN (6.x) only. For ERP Baan IV, use stpapi.continue.process(), stpapi.application.option(), or stpapi.zoom.option()*.* The error messages returned can be:

- Form command not found in session.

- Any error message from the session.

Whether an error message is returned in the function call depends on the way in which the call is coded in the session. See Chapter 4, “Special issues,” for more information.

The form command is searched in the session. If the command is found in one of the forms, the command is run.

If a report is printed, the report specifications must have been set by stpapi.set.report().

If the form command is of type Session, a stpapi.handle.subproc() call must first be issued.

## Specify actions for subsessions

**Syntax**

```baan
void stpapi.handle.subproc(string session, string sub.prog, string action)
```

**Arguments**

- *session* : Name of the session on which this command runs.

- *sub.prog:*  Infor ERP session code to which the action specified applies. This must be the session code of a valid subsession of the specified session or the menu code of a menu that can be started by the specified session.

- *Action:* The action to be taken when the subsession starts or which menu choice to be activated when the menu is activated.

Actions for subsessions:

- kill: Child process is killed as soon as the process starts

- ignore: The child process is ignored, alt hough the parent will wait until the child ends.

- send: All future stpapi.* function calls that use the name of the parent act on the child instead of the parent.

- add: The child is added to the list of sessions curr ently under control. The child can, therefore, be controlled independently by issuing stpapi.* function directly against the child’s session name

Menu choice:

- Menu choice of the session to be started converted to a string

**Description**

This sets the action that is taken when the specified subsession is invoked from the specified session or the menu choice to be activated when the menu is invoked. Note that a stpapi.handle.subproc() must also be called for the session activated by the menu choice.

**Return Values**

None.

**Example**

```baan
stpapi.put.field("dtfsa1501m000", "dtfsa101.seno", str$(i.seno))
ret = stpapi.find("dtfsa1501m000", error.msg)
if ret = 1 then
stpapi.handle.subproc("dtfsa1501m000", "dtfsa1201m000", "add")
stpapi.zoom.option("dtfsa1501m000", 1, "dtfsa1201m000", error.msg)
stpapi.put.field("dtfsa1201m000", "dtfsa101.date", str$(date.num()))
stpapi.continue.process("dtfsa1201m000", error.msg)
stpapi.end.session("dtfsa1201m000")
endif
stpapi.end.session("dtfsa1501m000")
```

**Explanation**

For the record found, the session dtfsa1201m000 is run, which is connected to theChoicefield or a menu choice of the menu connected to theChoicefield. To also send messages to the subsession, the stpapi.handle.subproc() is called.

**Usage Notes**

Functions in dll created by creatdll:

```baan
Function extern void <fs-name>.handle.sub.process(string sub.process, string
action)
```

If the subprocesses are a session without form, you cannot communicate with the session through the AFS. In these cases, you cannot define the action for the subsessions of this process.

For this situation, you can define the action for the subprocesses of that session in the group session, which is the session where the pid is the same as the gid of this subsession in the process list. In addition, the intermediate session must be defined with action Ignore.

This function must always be called when the session starts a subprocess called through the AFS when the subprocess expects user interaction, such as filling fields or pressing buttons.

## Get Messages from session

**Syntax**

```baan
string stpapi.get.mess.code(string session [, ref string err.mesg])
```

**Arguments**

- *session* : Name of the session on which this command runs.

- *err.mesg:*Text of the message.

**Description**

This retrieves the messages generated by the indicated session as a result of an stpapi.* function call. The messages are returned in the opposite order as generated in the session. Messages generated by the AFS or 4GL-Engine are also returned. These messages are generated when the AFS is not used correctly by the programmer, for example, wrong order of function calls.

**Return Values**

String that contains code of error message or the empty string if no error message is found or only the error text is filled.

**Example**

```baan
stpapi.put.field("dtfsa1101s000", "dtfsa101.seno", str$(i.seno)) stpapi.put.field("dtfsa1101s000", "dtfsa101.name", name)
retval1 = stpapi.insert("dtfsa1101s000", true, error.msg)
if not retval1 then
while true
error.code = stpapi.get.mess.code("dtfsa1101s000", error.msg)
if isspace(error.msg) then
break
endif
rep.message = error.msg
rprt_send()
endwhile
retval2 = stpapi.recover("dtfsa1101s000", recover.msg)
endif
```

**Explanation**

A record is inserted. If an error occurred, all errors raised by the session are retrieved and printed.

**Usage Notes**

Functions in dll created by creatdll:

```baan
Function extern string <fs-name>
.get.last.message.code([string error(500)])
```

For more information, refer to Chapter 4, “Special issues.”

## Set answers to questions in session

**Syntax**

```baan
void stpapi.enum.answer(string session, string question, bset answer)
```

**Arguments**

- *session* : Name of the session on which this command runs.

- *question:* Infor ERP question code. This question code must be valid in the session, that is, the session must ask this question when the user interface is used.

- *answer:*  The enum or set answer to be supplied as answer to the question. This must be expressed as the enum value as opposed to the numeric equivalent for example, tcyesno.yes i.s.o. 1.

**Description**

This sets the answers to questions that occur while the session runs.

**Return Values**

None.

**Example**

```baan
stpapi.put.field("dtfsa1101s000", "dtfsa101.seno", str$(i.seno))
stpapi.put.field("dtfsa1101s000", "dtfsa101.name", new.name)
stpapi.enum.answer("dtfsa1101s000", "dtfsa1101a", tcyesno.yes)
ret = stpapi.insert("dtfsa1101s000", true, error.msg)
```

**Explanation**

The session prompts the user whether to continue if a record is already present with the same name. The default answer in the session is No, but you must continue.

**Usage Notes**

Functions in dll created by creatdll:

```baan
Function extern long <fs-name>.define.enum.answer(string question, bset
answer)
```

This function must only be used for questions for which the default answer in the session must be overruled.

If the same question is used more than once in the same session, you can define only one answer.

## Change Sort Order

**Syntax**

```baan
long stpapi.sort.by(string session, string sortorder, ref string err.mesg)
```

**Arguments**

- *session* : Name of the session this command is executed on.

- *sortorder*: The number of the sorting. This number is not the index number but the number in sequence as presented to the enduser.

- *err.mesg*  : This parameter will contain the text of the error message if the function does not complete normally.

**Description**

This function will change the sorting order of the specified session.

**Return Values**

0 Record not recovered: err.me sg is filled with the reason.

1 Record recovered: err.mesg is empty.

**Usage Notes**

ERP Baan IV and ERP Baan 5.0c and ERP Enterprise (LN) only.
