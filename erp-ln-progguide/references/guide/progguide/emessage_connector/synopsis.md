# eMessage Connector synopsis
Functions are categorized into the following:
- Message object general functions
- Message object identification functions
- Message object delivery settings functions
- Message object recipient functions
- Message object attachment functions
- Task object functions
- Appointment object functions
- Miscellaneous

## Message object general functions
| | | |
|---|---|---|
| `long` | [cmf.sendMail()](cmf.sendmail.md) | `(string sender, string subject, string recipients.to(,), long num.recipients.to, string recipients.cc(,), long num.recipients.cc, string recipients.bcc(,), long num.recipients.bcc, string body, string body.mime, string attachments(,), long num.attachments)` |
| `long` | [cmf.create()](cmf.create.md) | `( )` |
| `long` | [cmf.destroy()](cmf.destroy.md) | `(long mid)` |
| `long` | [cmf.send()](cmf.send.md) | `(long mid, string service(15))` |
| `long` | [cmf.receive()](cmf.receive.md) | `(ref long mid, domain ttcmf.prov service, long block)` |
| `long` | [cmf.startService()](cmf.startservice.md) | `(string service(15), long mode, [string address(13)])` |
| `long` | [cmf.stopService()](cmf.stopservice.md) | `(string service(15), long mode)` |
| `long` | [cmf.addObjectToMessage()](cmf.addobjecttomessage.md) | `(long oid, long mid, string class(100))` |

## Message object identification functions
| | | |
|---|---|---|
| `long` | [cmf.setClass()](cmf.setclass.md) | `(long mid, string class)` |
| `long` | [cmf.getClass()](cmf.getclass.md) | `(long mid, ref string class)` |
| `long` | [cmf.setMessageId()](cmf.setmessageid.md) | `(long mid, string messageId)` |
| `long` | [cmf.getMessageId()](cmf.getmessageid.md) | `(long mid, ref string messageId)` |
| `long` | [cmf.getCreateTime()](cmf.getcreatetime.md) | `(long mid, ref domain ttutc createtime)` |
| `long` | [cmf.setSubject()](cmf.setsubject.md) | `(long mid, string subject)` |
| `long` | [cmf.getSubject()](cmf.getsubject.md) | `(long mid, ref string subject)` |
| `long` | [cmf.setTemplate()](cmf.settemplate.md) | `(long mid, string template)` |
| `long` | [cmf.getTemplate()](cmf.gettemplate.md) | `(long mid, ref string template)` |
| `long` | [cmf.setChargeCode()](cmf.setchargecode.md) | `(long mid, string chargecode)` |
| `long` | [cmf.getChargeCode()](cmf.getchargecode.md) | `(long mid, ref string chargecode)` |
| `long` | [cmf.setCategories()](cmf.setcategories.md) | `(long mid, string categories)` |
| `long` | [cmf.getCategories()](cmf.getcategories.md) | `(long mid, ref string categories)` |

## Message object delivery functions
| | | |
|---|---|---|
| `long` | [cmf.setPriority()](cmf.setpriority.md) | `(long mid, enum priority)` |
| `long` | [cmf.getPriority()](cmf.getpriority.md) | `(long mid, ref enum priority)` |
| `long` | [cmf.setSensitivity()](cmf.setsensitivity.md) | `(long mid, enum sensitivity)` |
| `long` | [cmf.getSensitivity()](cmf.getsensitivity.md) | `(long mid, ref enum sensitivity)` |
| `long` | [cmf.setStartTime()](cmf.setstarttime.md) | `(long mid, domain ttutc starttime)` |
| `long` | [cmf.getStartTime()](cmf.getstarttime.md) | `(long mid, ref domain ttutc starttime)` |
| `long` | [cmf.setExpiry()](cmf.setexpiry.md) | `(long mid, domain ttutc expiry)` |
| `long` | [cmf.getExpiry()](cmf.getexpiry.md) | `(long mid, ref domain ttutc expiry)` |
| `long` | [cmf.setFollowupFlag()](cmf.setfollowupflag.md) | `(long mid)` |
| `long` | [cmf.getFollowupFlag()](cmf.getfollowupflag.md) | `(long mid)` |
| `long` | [cmf.setDueDate()](cmf.setduedate.md) | `(long mid, domain ttutc duedate)` |
| `long` | [cmf.getDueDate()](cmf.getduedate.md) | `(long mid, ref domain ttutc duedate)` |
| `long` | [cmf.setNotification()](cmf.setnotification.md) | `(long mid, enum notification)` |
| `long` | [cmf.getNotification()](cmf.getnotification.md) | `(long mid, ref enum notification)` |
| `long` | [cmf.setDisplay()](cmf.setdisplay.md) | `(long mid, enum display)` |
| `long` | [cmf.getDisplay()](cmf.getdisplay.md) | `(long mid, ref enum display)` |

## Message object recipient functions
| | | |
|---|---|---|
| `long` | [cmf.createRecipient()](cmf.createrecipient.md) | `(long mid, enum role)` |
| `long` | [cmf.getNextRecipient()](cmf.getnextrecipient.md) | `(long mid, ref enum role, long previous)` |
| `long` | [cmf.setRecipientName()](cmf.setrecipientname.md) | `(long recipient, string name)` |
| `long` | [cmf.getRecipientName()](cmf.getrecipientname.md) | `(long recipient, ref string name)` |
| `long` | [cmf.setRecipientAddress()](cmf.setrecipientaddress.md) | `(long recipient, string address)` |
| `long` | [cmf.getRecipientAddress()](cmf.getrecipientaddress.md) | `(long recipient, ref string address)` |
| `long` | [cmf.setRecipientType()](cmf.setrecipienttype.md) | `(long recipient, string type)` |
| `long` | [cmf.getRecipientType()](cmf.getrecipienttype.md) | `(long recipient, ref string type)` |
| `long` | [cmf.setRecipientResponsibility()](cmf.setrecipientresponsibility.md) | `(long recipient, string responsibility)` |
| `long` | [cmf.getRecipientResponsibility()](cmf.getrecipientresponsibility.md) | `(long recipient, ref string responsibility)` |
| `long` | [cmf.setRecipientReasoncode()](cmf.setrecipientreasoncode.md) | `(long recipient, long reasoncode)` |
| `long` | [cmf.getRecipientReasoncode()](cmf.getrecipientreasoncode.md) | `(long recipient, ref long reasoncode)` |
| `long` | [cmf.setRecipientReasonstring()](cmf.setrecipientreasonstring.md) | `(long recipient, string reasonstring(100))` |
| `long` | [cmf.getRecipientReasonstring()](cmf.getrecipientreasonstring.md) | `(long recipient, ref string reasonstring)` |

## Message object attachment functions
| | | |
|---|---|---|
| `long` | [cmf.createAttachment()](cmf.createattachment.md) | `(long mid)` |
| `long` | [cmf.getNextAttachment()](cmf.getnextattachment.md) | `(long mid, long previous)` |
| `long` | [cmf.copyAttachment()](cmf.copyattachment.md) | `(long attachment.id, oid)` |
| `long` | [cmf.setAttachmentBody()](cmf.setattachmentbody.md) | `(long attachment, enum ttyeno body)` |
| `long` | [cmf.getAttachmentBody()](cmf.getattachmentbody.md) | `(long attachment, enum ttyeno body)` |
| `long` | [cmf.setAttachmentMIME()](cmf.setattachmentmime.md) | `(long attachment, string mime)` |
| `long` | [cmf.getAttachmentMime()](cmf.getattachmentmime.md) | `(long attachment, ref string mime)` |
| `long` | [cmf.setAttachmentFilename()](cmf.setattachmentfilename.md) | `(long attachment, string filename [, string displayname])` |
| `long` | [cmf.getAttachmentFilename()](cmf.getattachmentfilename.md) | `(long attachment, ref string filename, ref string displayname)` |
| `long` | [cmf.setAttachmentPosition()](cmf.setattachmentposition.md) | `(long attachment, string position(10))` |
| `long` | [cmf.getAttachmentPosition()](cmf.getattachmentposition.md) | `(long attachment, ref string position)` |

## Task object functions
| | | |
|---|---|---|
| `long` | [cmf.createTask()](cmf.createtask.md) | `( )` |
| `long` | [cmf.setTaskSubject()](cmf.settasksubject.md) | `(long tid, string subject)` |
| `long` | [cmf.getTaskSubject()](cmf.gettasksubject.md) | `(long tid, ref string subject)` |
| `long` | [cmf.setTaskPriority()](cmf.settaskpriority.md) | `(long tid, enum priority)` |
| `long` | [cmf.getTaskPriority()](cmf.gettaskpriority.md) | `(long tid, ref enum priority)` |
| `long` | [cmf.setTaskStartdate()](cmf.settaskstartdate.md) | `(long tid, domain ttutc startdate)` |
| `long` | [cmf.getTaskStartdate()](cmf.gettaskstartdate.md) | `(long tid, ref domain ttutc startdate)` |
| `long` | [cmf.setTaskDuedate()](cmf.settaskduedate.md) | `(long tid, domain ttutc duedate)` |
| `long` | [cmf.getTaskDuedate()](cmf.gettaskduedate.md) | `(long tid, ref domain ttutc duedate)` |
| `long` | [cmf.setTaskReminderTime()](cmf.settaskremindertime.md) | `(long tid, domain ttutc remindertime)` |
| `long` | [cmf.getTaskReminderTime()](cmf.gettaskremindertime.md) | `(long tid, ref domain ttutc remindertime)` |
| `long` | [cmf.setTaskTotalwork()](cmf.settasktotalwork.md) | `(long tid, string totalwork)` |
| `long` | [cmf.getTaskTotalwork()](cmf.gettasktotalwork.md) | `(long tid, ref string totalwork)` |

## Appointment object functions
| | | |
|---|---|---|
| `long` | [cmf.createAppointment()](cmf.createappointment.md) | `( [long mid] )` |
| `long` | [cmf.setAppointmentSubject()](cmf.setappointmentsubject.md) | `(long apid, string subject)` |
| `long` | [cmf.getAppointmentSubject()](cmf.getappointmentsubject.md) | `(long apid, ref string subject)` |
| `long` | [cmf.setAppointmentDescription()](cmf.setappointmentdescription.md) | `(long apid, string description)` |
| `long` | [cmf.getAppointmentDescription()](cmf.getappointmentdescription.md) | `(long apid, ref string description)` |
| `long` | [cmf.setAppointmentMethod()](cmf.setappointmentmethod.md) | `(long apid, domain ttcmf.mth method)` |
| `long` | [cmf.getAppointmentMethod()](cmf.getappointmentmethod.md) | `(long apid, ref domain ttcmf.mth method)` |
| `long` | [cmf.setAppointmentUUID()](cmf.setappointmentuuid.md) | `(long apid, string uuid)` |
| `long` | [cmf.getAppointmentUUID()](cmf.getappointmentuuid.md) | `(long apid, ref string uuid)` |
| `long` | [cmf.setAppointmentMeeting()](cmf.setappointmentmeeting.md) | `(long apid, enum meeting)` |
| `long` | [cmf.getAppointmentMeeting()](cmf.getappointmentmeeting.md) | `(long apid, ref enum meeting)` |
| `long` | [cmf.setAppointmentAlldayevent()](cmf.setappointmentalldayevent.md) | `(long apid, enum alldayevent)` |
| `long` | [cmf.getAppointmentAlldayevent()](cmf.getappointmentalldayevent.md) | `(long apid, ref enum alldayevent)` |
| `long` | [cmf.setAppointmentStarttime()](cmf.setappointmentstarttime.md) | `(long apid, domain ttutc starttime)` |
| `long` | [cmf.getAppointmentStarttime()](cmf.getappointmentstarttime.md) | `(long apid, ref domain ttutc starttime)` |
| `long` | [cmf.setAppointmentEndtime()](cmf.setappointmentendtime.md) | `(long apid, domain ttutc endtime)` |
| `long` | [cmf.getAppointmentEndtime()](cmf.getappointmentendtime.md) | `(long apid, ref domain ttutc endtime)` |
| `long` | [cmf.setAppointmentAlarm()](cmf.setappointmentalarm.md) | `(long apid, domain ttutc alarm)` |
| `long` | [cmf.getAppointmentAlarm()](cmf.getappointmentalarm.md) | `(long apid, ref domain ttutc alarm)` |
| `long` | [cmf.setAppointmentBusystatus()](cmf.setappointmentbusystatus.md) | `(long apid, enum busystatus)` |
| `long` | [cmf.getAppointmentBusystatus()](cmf.getappointmentbusystatus.md) | `(long apid, ref string busystatus)` |
| `long` | [cmf.setAppointmentLocation()](cmf.setappointmentlocation.md) | `(long apid, string location)` |
| `long` | [cmf.getAppointmentLocation()](cmf.getappointmentlocation.md) | `(long apid, ref string location)` |

## Miscellaneous
| | | |
|---|---|---|
| `long` | [cmf.messageDialog()](cmf.messagedialog.md) | `(long mode, long show, [long show.message])` |
| `long` | [cmf.getId()](cmf.getid.md) | `(domain ttcmf.cmes messageId, string service, domain ttcmf.mdir message.direction, ref string error_string())` |
| `long` | [cmf.isServiceEnabled()](cmf.isserviceenabled.md) | `(domain ttcmf.prov service)` |
| `long` | [cmf.enableService()](cmf.enableservice.md) | `(domain ttcmf.prov service, long enable)` |
| `long` | [cmf.resolveAddress()](cmf.resolveaddress.md) | `(ref domain ttcmf.catg category, ref domain ttcmf.catg key, ref domain ttcmf.defa addresstype, ref string address(), ref string message.str, [string name(100) mb, long use.default])` |

## Address List Object Functions
| | | |
|---|---|---|
| `long` | [cmf.createAddressList()](cmf.createaddresslist.md) | `()` |
| `long` | [cmf.addAddressEntry()](cmf.addaddressentry.md) | `(long aid, string role, string name, string address, string addresstype, [domain ttcmf.catg key, domain ttcmf.catg category])` |
| `long` | [cmf.getNextAddress()](cmf.getnextaddress.md) | `(long aid, long previous)` |
| `long` | [cmf.getAddressDetails()](cmf.getaddressdetails.md) | `(long entry_id, ref string category, ref string key, ref string role, ref string name, ref string address, ref string addresstype, ref long errorcode)` |
| `long` | [cmf.getAddressBookKey()](cmf.getaddressbookkey.md) | `(long entry.id, ref string key, ref string category)` |
| `long` | [cmf.updateAddressStatus()](cmf.updateaddressstatus.md) | `(long entry_id, long errorcode)` |
| `long` | [cmf.getService()](cmf.getservice.md) | `(enum addresstype, enum user_interaction, enum resolve, ref string service)` |
| `long` | [cmf.sendToPerson()](cmf.sendtoperson.md) | `(long mid, long aid, long display, long show.progress, ref string message_string() [,long convert, string filename1, string filename2, ...] )` |
| `void` | [cmf.stopAllServices()](cmf.stopallservices.md) | `()` |

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector examples](examples.md)
