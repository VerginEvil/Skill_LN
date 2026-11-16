# cmf.sendMail()

## Syntax:
`#include <bic_cmf>`
`function long cmf.sendMail( string sender, string subject, string recipients.to(,), long num.recipients.to, string recipients.cc(,), long num.recipients.cc, string recipients.bcc(,), long num.recipients.bcc, string body, string body.mime, string attachments(,), string attachment.mimes(,), long num.attachments, [ string service ] )`

## Description
Convenience function to send a mail to one or more recipients, with the possibility to add attachments to the mail.
Note: the sender and the recipients can be specified in the following ways:

- *User name**<**mail address**>*: e.g. "John Doe <jdoe@acme.com>"; this value is split into a user name ("John Doe") and a mail address (jdoe@acme.com).

- *Mail address only*: e.g. "jdoe@acme.com"; the mail address is also used as the user name; note that any value of 8 characters or less, is interpreted as an LN user code, even if it contains the '@' sign. So a value like "a@b.com" is not interpreted as a mail address, but as an LN user code. Use the 'User name <mail address>' format to prevent any ambiguities.

- *LN user code*: e.g. "jdoe"; the mail address and user name are resolved using the CMF address book.

## Arguments
| | | |
|---|---|---|
| `string` | `sender` |  The sender of the mail.  |
| `string` | `subject` |  The subject of the mail.  |
| `string` | `recipients.to(,)` |  An array of recipients; these will be set in the mail's 'to' list.  |
| `long` | `num.recipients.to` |  The number of 'to' recipients; can be 0.  |
| `string` | `recipients.cc(,)` |  An array of recipients; these will be set in the mail's 'cc' list.  |
| `long` | `num.recipients.cc` |  The number of 'cc' recipients; can be 0.  |
| `string` | `recipients.bcc(,)` |  An array of recipients; these will be set in the mail's 'bcc' list.  |
| `long` | `num.recipients.bcc` |  The number of 'bcc' recipients; can be 0.  |
| `string` | `body` |  The path to the file which must be used as the body of the mail.  |
| `string` | `body.mime` |  The mime type of the body.  |
| `string` | `attachments(,)` |  An array of paths to attachment files.  |
| `string` | `attachment.mimes(,)` |  An array of mime types of the attachment files.  |
| `long` | `num.attachments` |  The number of attachments; can be 0.  |
| `[ string` | `service ]` |  The eMessage connector service to be used to send the mail. If not specified (or empty), service SMTP will be used. Available with KB3641113 / LNCE 2025.12.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| <> 0 | Failed to send mail; a message is set via [dal.set.error.message()](../functions_message_handling/dal.set.error.message.md) |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2370.

## Example
```

string	to.list(100,3)
string	cc.list(100,2)
string	bcc.list(100,1)
string	att.list(100,2)
string	att.mime.list(30,2)
long	result

to.list(1,1) = "jsmith"                                        |* LN user
to.list(1,2) = "jane78@gmail.com"                              |* mail address only
to.list(1,3) = "Paul M. Gibson <paul.m.gibson@acme.com>"       |* user name and mail address

cc.list(1,1) = "sales.office.atlanta@acme.com"
cc.list(1,2) = "Ben Winston <ben.winston@acme.com>"

bcc.list(1,1) = "kc23@gmail.com"

att.list(1,1) = path.combine(bse.appdata.dir$(), "invoice.pdf")
att.list(1,2) = path.combine(bse.appdata.dir$(), "readme.txt")

att.mime.list(1,1) = "application/pdf"
att.mime.list(1,2) = "text/plain"

result = cmf.sendMail(
                "donotreply@acme.com",                         |* sender
                "Your invoice with number 123456",             |* subject
                to.list,                                       |* 'to' recipients
                3,                                             |* number of 'to' recipients
                cc.list,                                       |* 'cc' recipients
                2,                                             |* number of 'cc' recipients
                bcc.list,                                      |* 'bcc' recipients
                1,                                             |* number of 'bcc' recipients
                path.combine(bse.appdata.dir$(), "body.htm"),  |* path to file used as the body
                "text/html",                                   |* body mime type
                att.list,                                      |* paths to attachment files
                att.mime.list,                                 |* mime types of attachments
                2)                                             |* number of attachments

if result = 0 then
        |* success
else
        |* error; DAL error message has been set
endif
```

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)
