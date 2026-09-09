# OCM.SkipObjectApproval

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for OCM
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2108-2110

```baan
Skips sending the Workflow (WFDA) BOD to ION and immediately approve the object.
This process extension is available from 2026.10 (KB3697600).
To implement this process extension, you can use the information below:
Usage:        Process Extension OCM.SkipObjectApproval can be used to skip sending
the Workflow Document Authorization (WFDA) BOD to ION when an object is
submitted for approval. When the extension returns 'true', the object is
NOT sent to ION; instead it is immediately checked-in (approved) within
the same transaction. When the extension returns 'false' (or is not
implemented), the standard flow runs and the WFDA BOD is sent to ION.
This allows customers to conditionally bypass ION approval for scenarios
where approval is not required, while keeping the standard ION flow
for all other cases.
Objects/sessions where this Process Extension applies:
- All WFDA (Object Change Management) enabled objects that are submitted
for approval, such as Purchase Requisitions (REQ), Purchase Orders (PO)
and Sales Orders (SO), and any process that triggers their submit.
Fields that are available to be used in this Process Extension:
- All fields of the root table of the object being submitted (the root
table is current). For example tdpur400 for a Purchase Order, tdsls400
for a Sales Order, tdpur200 for a Purchase Requisition.
External (context) variables that are available to be used in this
Process Extension (they describe the current workflow scenario):
- proc_ext_ocm_toid        [ type: string ] - Typed Object ID of the
object being submitted.
- proc_ext_ocm_object_type [ type: string ] - Object type, e.g. "TDPO".
- proc_ext_ocm_root_table  [ type: string ] - Root table, e.g.
"tdpur400".
- proc_ext_ocm_action      [ type: string ] - Object action, e.g.
"APPROV".
- proc_ext_ocm_old_status  [ type: long ]   - The previous (checked-in)
value of the application
status field (rcd_prst),
as an enum value converted
to long. Use ltoe() to
compare against an enum
domain value.
Note: tables and external variables must also be declared in the
Process Extension (Declarations hook).
Pseudocode:
Below you can find an example that skips ION for some objects based on
conditions.
Hook: Declarations
table   ttdpur400       |* Purchase Orders
table   ttdsls400       |* Sales Orders
table   ttdpur200       |* Purchase Requisition
extern  domain ttocm.toid       proc_ext_ocm_toid
extern  domain ttocm.otyp       proc_ext_ocm_object_type
extern  domain ttst08           proc_ext_ocm_root_table
extern  string                  proc_ext_ocm_action(20)
extern  long                    proc_ext_ocm_old_status
Hook: ext.skip
function extern boolean ext.skip()
{
on case proc_ext_ocm_root_table
case "tdpur400":                       |* Purchase Order
|* Skip ION if the order is already approved before.
if proc_ext_ocm_object_type = "TDPO" and
proc_ext_ocm_action      = "APPROV" and
ltoe(proc_ext_ocm_old_status) = tdpur.hdst.approved and
not isspace(proc_ext_ocm_toid) then
return(true)                  |* skip ION, approve
directly
endif
break
case "tdsls400":                       |* Sales Order
|* Skip ION only if a CDF field is Set.
if proc_ext_ocm_object_type = "TDSO" and
tdsls400.cdf_skip = tcyesno.yes then
return(true)
endif
break
case "tdpur200":                       |* Purchase Requisition
|* Skip ION based on advanced logic in TX.
if proc_ext_ocm_object_type = "TDREQ" and
tx.skip.requisition.allowed(
proc_ext_ocm_toid,
proc_ext_ocm_root_table,
proc_ext_ocm_action,
proc_ext_ocm_old_status) then
return(true)         |* TX dll confirmed to skip
endif
break
default:
break
endcase
return(false)
}
```
