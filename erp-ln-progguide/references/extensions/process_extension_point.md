# Process extension point

A process extension is used to implement additional functionality in the LN application.

Use process extensions when changing the behavior of the LN application cannot be achieved with other extension types such as table extensions and session extensions. Ensure that those process extensions are prepared in the standard LN application.

Examples:

- LN data based on custom specific selection criteria. Skip printing or processing of

- Define your own criteria for composing invoices.

For the available Process Extensions, see the Infor LN Public Interfaces & Process Extensions Reference Guide (Infor Customer Portal KB2003722).

That guide describes also the procedure how to request new extendable processes in the LN standard application.

For the Process extension point there are two extension types:

- Process

- Custom Field

This diagram shows the position of the Process extension: Optional
LN Functionality Process
Extension
Session
Extension4GL engine
LN tables
Screen

The LN standard application calls the process extension, if implemented. If the process extension requires additional information from the end user, the fields must be added to the session extension. For example information about new ranges for printing data. Session Optional LN Screen Extension LN Extension 4GL Functionality Process engine tables

## Process

The hooks you can define on Process level are supporting hooks for the hooks on Component level.

Additionally to those hooks you must implement the functions specifically for this process extension.

This table shows the standard available hooks:

Name Signature

Declarations

Functions

Examples of functions to be implemented, dependent of the process extension type: • `ext.skip` • `tfext.cmg0001.define.custom.receipt.elements`

How to implement the process extension implementation specific functions, see the Infor LN Public Interfaces & Process Extensions Reference Guide (Infor Customer Portal KB2003722).

## Declarations hook

Use this hook to declare tables and variables that must be globally available in all hooks of the extension.

The references to include files and DLLs that are used by the extension must be coded in this hook with `#include` and `#pragma`.

Example:

```baan
#include        <bic_tt>
table   txprc000          |* Price Parameters
#pragma used dll "otxprcdll0000"
```

## Functions hook

Use this hook to code (common) functions to use in the other hooks of the Process extension.

This helps you in reusing code and to keep the other hooks small and clear.

Example:

```baan
function boolean own.pricing.implemented()
{
txprcdll0000.read.parameter()
return(txprc000.impl = tcyesno.yes)
}
```

## Custom field

Use a Custom Field extension type if your implementation of the process extension requires additional input on the session’s screen.

To have them available on the screen, you must add the custom field in the session extension. See Custom Field in Session Extension point.

These are the available properties:

- Name

- Label

- Description

- Domain

This table shows the available hooks:

| Name | Signature |
|---|---|
| Calculate Initial Value | `void <field name>. calculate.default.value()` |

## Name property

The Name property is used for the variable name.

`ext.` is the prefix of the property. The maximum length of a variable name is 17, including the prefix. Use this variable name as the name in the hooks.

## Label property

Use this property if the field description must be displayed in different languages.

You can select an existing label or create a new label in the Extensions package. A label can have descriptions in different languages and multiple length variants.

See the Infor LN Studio Application Development Guide.

The Label property cannot be filled if the Description property is used.

## Discription property

The Description is displayed before the field.

If the descriptions must be available in multiple languages, based on user language, do not use the Description property. Link a label to the field with the Label property. The Description property cannot be specified if the Label property is used.

## Domain property

The Domain property is required to define the data type of the Custom Field.

You can select an existing domain or create a new domain in the Extensions package. The Domain property is read only for Custom Fields that are inherited from a process extension.

See the Infor LN Studio Application Development Guide.

## Calculate initial value hook

Use this hook to set the initial value of the custom field.

If the custom field is not added to a session extension or this hook is not implemented for the field in the session extension, this hook is used.

Example:

```baan
function extern void ext.colr.t.calculate.default.value()
{
ext.colr.t = "ZZZZZZZZZZ" }
```

## Functions

In the hooks of a process extension you can use all trusted functions to do string manipulation, calculations, comparisons, etc.

See Trusted / Untrusted concept on page 155.

Embedded SQL and the `sql.*` functions are available to read data from the LN database.

Calling (own) DLL functions is also possible.

## Limitations and restrictions

These are the limitations and restrictions:

- Transactions By default, transactions are not supported in process extensions. If for a specific process extension, it is allowed, this is documented for that process extension. See the Infor LN Public Interfaces & Process Extensions Reference Guide (Infor Customer Portal KB2003722).

- UI Whether the UI is available depends on the type of process extension. See the Infor LN Public Interfaces & Process Extensions Reference Guide (Infor Customer Portal KB2003722)
