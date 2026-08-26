# tdext.sls0005.validate.received.customer.order.during.processing

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ReceivedCustomerOrderProcess
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2199-2200

```baan
Syntax: long tdext.sls0005.validate.received.customer.order.during.processing(
domain  tcorno           i.received.customer.order,
domain  tdsls.obty       i.received.customer.order.document.type,
domain  tdwcom           i.received.customer.order.origin,
domain  tcproc.actn      i.process.action,
domain  tcyesno          i.change.order,
domain  tcmcs.st30m      i.customer.order.number mb,
domain  tccom.bpid       i.sold.to.bp,
domain  tccwoc           i.sales.office )
Usage:        Expl:   This function executes customer defined validations during
processing the given Received Customer Order. To indicate that
the validation failed, the extension must put an error                      -message
on the stack and return a non                      -zero value. In that case, the
error will be logged in the message log, and the system
continues with the next Received Customer Order (if any).
Pre:    Not Applicable.
Post:   Not Applicable.
Input:  i.received.customer.order
-                                               Received Customer Order
i.received.customer.order.document.type
-                                               Received Customer Order Document Type.
Possible value(s):
* tdsls.obty.order (Sales Order)
i.received.customer.order.origin
-                                               Received Customer Order Origin.
Possible values:
* tdwcom.edi (EDI)
* tdwcom.bod (BOD)
* tdwcom.manual (Manual)
i.process.action                              - Process Action.
Possible values:
* tcproc.actn.create (Create)
* tcproc.actn.update (Update)
* tcproc.actn.cancel (Cancel)
* tcproc.actn.not.applicable (Not
Applicable)
i.change.order                                - Change Order (Yes/No)
i.customer.order.number                       - Customer Order
i.sold.to.bp                                  - Sold-to Business Partner (Mandatory)
i.sales.office                                - Sales Office
Output: Not Applicable
Return: 0                                     - Validation was successful.
<> 0                                          - The extension indicates that the given
Received Customer Order is not valid.
An error message has been
put on the stack by the extension.
LN will skip this Received Customer
Order.
```

## Process Extensions for ReminderAdvice

The following process extension(s) is/are available: ReminderAdvice.SkipPrintReminderAdvice
