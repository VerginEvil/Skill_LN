# Governance

Build the extensions in a way that they are ready for the cloud. This means that upgradability is guaranteed, no infrastructure data is revealed, and other customers are not impacted by your extensions.

In Infor LN, you can use several mechanisms to govern your extensions whether they are ready for the cloud:

- Trusted / Untrusted concept

- Performance governors

- File system governors

- Best practices

If you do not develop with the Extensions ready for Cloud parameter switched on, the governors are not activated.

See Cloud readiness on page 23 why we do not recommend this.

In a multi-tenant cloud environment, the governers are always activated and cannot be switched off.

## Trusted / Untrusted concept

With the introduction of trusted functions, the LN infrastructure can restrict the extensions to break the general rules for cloud readiness.

Other software added by customers to the LN environment, such as Exchange scripts can also be restricted. Extensions are only allowed to call trusted functions. This applies to the 3GL and 4GL functions of LN ’s programming language, which are described in the Infor ES Programmers Guide (Infor Customer Portal KB2924522). It also applies to application functions in DLLs, which can be called by the extensions to retrieve and store data with LN’s application logic.

These functions are untrusted, and cannot be used within extensions:

- Functions that can harm the infrastructure if they are used in the incorrect way. Example: `run.prog()`

- Functions that reveal information about the infrastructure. Example: `hostname$()`

- Functions that are deprecated. Example: `cf$()`

- Functions that may disturb the flow of the standard application.

Example: `dal.get.error.message()`

- Functions that may use standard components and the interface of the standard components may break. Those functions are “conditionally trusted”, which means that they are allowed to be called, but not for standard components. Example: `wait.and.activate()` `wait.and.activate()` can be called for an own session in the tx-package, but not for a standard session. This also applies to the Application Function Server (stpapi.* functions). You can use AFS to start own sessions in the tx-package, but you cannot run standard LN sessions through AFS.

Functions in LN Application DLLs, even if declared as `extern`, are untrusted by default. A new specific trusted layer is available with functions that can be used by extensions. The trusted LN Application functions are called “Public Interfaces”.

For a coding example and the procedure how to request a new Public Interface, see the Infor LN Public Interfaces & Process Extensions Reference Guide (Infor Customer Portal KB2003722).

During compilation of an extension script or any other script in the Extensions (tx) package, messages are raised when untrusted functions are called.

This diagram shows the different layers with trusted and untrusted functions: LN Tools layer
(DAL/4GL/BOD/Report
Engines)
LN Runtime
(bshell)
Application layer
Extension layer
4
2
Extensions world
Standard world
Trusted function
Untrusted function
5
1
3

The explanation of the numbers:

1 An extension can call trusted functions in the LN Runtime layer, bshell functions, that are documented as trusted in the Infor ES Programmers Guide (Infor Customer Portal KB2924522). 2 The extension can also call a trusted function in the LN Tools layer; those are also documented as trusted in the Infor ES Programmers Guide (Infor Customer Portal KB2924522). 3 The extension can call trusted functions (Public Interfaces) in the application layer, that are documented in the help pages of LN Studio and the Extension Modeler. See the Infor LN Public Interfaces & Process Extensions Reference Guide (Infor Customer Portal KB2003722)

4 Untrusted standard functions cannot be called from the extensions. All functions in the extensions are untrusted, but those can be called by the extension itself. LN ools T layer Extensions (LN Runtime world world DAL/4GL/BOD/Report Standard 4 2 1 3 5 T Untrusted rusted Application Extension Engines) layer layer function function (bshell) 5 With the standard software, the distinction between trusted and untrusted is not considered.

## Performance governors

The goal of the performance governors is to restrict the impact your extensions can have on the infrastructure. This especially applies to the resource consumption.

Extensions are restricted in:

- Time spent (elapsed time)

- Amount of data written to the file system

- Future versions may have more restrictions

The counter starts each time the extension starts execution. It is reset when the extension stops execution. This implies that for example each hook in a table extension has its own scope regarding the governors.

The exact limits are set by the Infor Cloud team. If you develop extensions in an on-premises environment with the Extensions Ready for Cloud option selected, you can change the values in the `$BSE/lib/extensibil` `ity/config.<package combination>` file:

| Resource | Default | Remark |
|---|---|---|
| `governor_elapsed_time` | 5000 | Elapsed time in milliseconds. |
| `governor_write_file_quotum` | 5000000 | 5 Mb |

Increasing those resources to higher values than required by the Infor Cloud team results in extensions that are not ready for the cloud and may not run after they are moved to the cloud.

## File system governors

In cloud environments, the file system access is restricted. Cloud-ready extensions must comply with those restrictions.

Extensions are restricted to certain folders in the BSE. Outside those folders data cannot be read or written. The LN standard software can read outside those folders but can only write in a restricted number of folders. End users cannot choose all locations to put their files that are output of their sessions.

Extensions are also restricted in writing files with certain file extensions. For example, writing a file with a `.` `exe` file extension is not allowed.

If you develop extensions in an on-premises environment with the Extensions Ready for Cloud option switched on, you can change the values in the `$BSE/lib/extensibility/config.<package combination>` file:

| Resource | Default | Remark |
|---|---|---|
| `user_writable_dirs` Resource Default Remark | appdata, tmp | Within `$BSE`. |
| `not_trusted_object_accessible` | appdata, tmp | Within `$BSE`. |
| `forbidden_filename_extensions` | exe,vb*,com |  |

Adding folders or extensions to those resources results in extensions that are not ready for the cloud. These extensions may not run after they are moved to the cloud.

## Best practices

To reduce the risk that your extensions are not compatible with newer versions of LN, we recommend that you comply with the rules.

## Database

Queries

The LN development team has the responsibility to keep the data model compatible. Sometimes it is required to change indexes. We recommend that you do not refer to indexes, but to the fields directly. See these code examples:

- This syntax is incorrect because it refers to an index:

```baan
function extern void tdsls401.read()
{
select tdsls401.*
from   tdsls401
where  tdsls401._index1 = {:rep.orno, :rep.pono}
selectdo
endselect
}
```

- Instead, use this syntax, which refers to the fields directly:

```baan
function extern void tdsls401.read()
{
select tdsls401.*
from   tdsls401
where  tdsls401.orno = :rep.orno
and    tdsls401.pono = :rep.pono
selectdo
endselect
}
```

If Public Interfaces are available to read data from the database, use those instead of querying the database directly. Public Interfaces are not created to read data which can be retrieved by a simple query. If the approach is more complex, Public Interfaces can be present or can be requested. See these code examples:

- This syntax is incorrect because it queries the database directly and there is a Public Interface available:

```baan
function domain tcyesno read.apply.discount.parameter()
{
domain tcyesno apply.discount
select tssoc003.aomt:apply.discount
from   tssoc003
where  tssoc003.soff = :rep.soff
and    tssoc003.site = :rep.site
selectdo
selectempty
apply.discount = empty
endselect
return(apply.discount)
}
```

- Instead, use this syntax, which uses the Public Interface:

```baan
function domain tcyesno read.apply.discount.parameter ()
{
domain tcyesno apply.discount
long    ret
long    exceptionid
string  exception.message(1000) mb
if Service.GetServiceOrderSettings(
get.compnr(),
rep.soff,
rep.site,
false,
exception.message,
exception.id,
"aomt",
apply.discount) = 0 then
apply.discount = empty
Exception.Delete(exception.id)
endif
return(apply.discount)
}
```

Table definitions

If you create own tables in the Extensions (tx) package, use standard domains if you store copies of standard data in your tables. This ensures that your tables also are reconfigured if the standard tables are reconfigured after a domain change. For enumerated domains, new values can be added. Prepare your extension for possible new values.

Standard table updates

If you update standard tables, use the DAL. Always check the return values of the functions such as `dal.save.object()` and react accordingly.

## Standard components

Do not use standard components. Except for the LN PubIic Interfaces, the interfaces or functionality of other standard components can change.

## Other restrictions

Extensibility has validations built in to check also other things that might result in not cloud-ready extensions.

For example, you cannot run these actions:

- Infor Reporting or Microsoft SSRS reported designs for reports in the Extension (`tx`) package. Create

- LN tables. For `tx` -tables this Change Object Configuration Management (OCM) models for standard restriction does not apply.
