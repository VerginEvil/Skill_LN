# Menu extension point

A Menu extension is used to add additional menu items or to hide standard menu items.

For example:

- Have a sub menu with all own developed sessions in the Extensions package on the main menu.

- Hide some sessions you do not use.

- Overrule standard menu item descriptions.

For the Menu extension point there are three extension types:

- Menu

- Standard Menu Item

- Custom Menu Item

This diagram shows the position of the Menu extension:

## Menu

The hooks you can define on Menu level are supporting hooks for the hooks on Component level.

This table shows the available hooks: Name Signature

Declarations

Functions

## Declarations hook

Use this hook to declare tables and variables that must be globally available in all hooks of the extension. Also, the references to include files and DLLs that are used by the extension must be coded in this hook with `#include` and `#pragma`.

Example:

```baan
#include        <bic_tt>
table   txprc000          |* Price Parameters
#pragma used dll "otxprcdll0000"
```

## Functions hook

Use this hook to code (common) functions to use in the other hooks of the Menu extension. This helps you in reusing code and to keep the other hooks small and clear.

Example:

```baan
function boolean own.pricing.implemented()
{
txprcdll0000.read.parameter()
return(txprc000.impl = tcyesno.yes)
}
```

## Standard Menu Item

With the properties and hooks defined for the extension type Standard Menu Item, you can overrule the standard menu item description or make it (conditionally) invisible for the end user.

This table shows the available properties:

Name

Overwrite Description

Description Label

Description This table shows the available hooks:

| Name | Signature |
|---|---|
| Is Visible | `boolean       <type>.<name>.is.visible()` |

## Overwrite Description property

If you select this property, you can overwrite the standard description of the menu item, which is the sub menu description, the session description or the query description. In this case, you must either specify the `Description Label` property or the `Description` property.

## Description Label property

Use this property to have different descriptions for users that are working in different languages. You can select an existing label, or create a new label in the Extensions package. The label used must have the context `General use`. A label can have descriptions in different languages and multiple length variants; for the menu item the longest one is shown at runtime.

See the Infor LN Studio Application Development Guide.

You cannot specify the `Description Label` property if the `Description` property is used.

## Description property

Use this property if your menu item description is not language dependent.

The Description is read-only in case the `Overwrite Description` property is not checked or the `Description` `Label` property is filled. In those cases, the Description shows the description that is used when the menu is displayed at runtime.

## Is Visible hook

Use this hook to remove the standard menu item from the menu.

Example:

```baan
function boolean menu.tcemm00005001.is.visible()
{
|* Use this hook to remove the menu item from the
|* menu. You can do that based on conditions. To
|* remove it, let the function return the value
|* false.
select  txcom001.*
from    txcom001
where   txcom001.user = :logname$
and  tccom001.shem = tcyesno.yes
as set with 1 rows
selectdo
return(true)
endselect
return(false)
}
```

## Custom Menu Item

With the properties and hooks defined for the extension type Custom Menu Item, you can (conditionally) add menu items to standard menus.

This table shows the available properties:

Name

Type

Code

Overwrite Description

Description Label

Description

Process Info

This table shows the available hooks:

| Name | Signature |
|---|---|
| Is Visible | `boolean         <type>.<name>.is.visible()` |

## Type property

Choose the Type of the Custom Menu Item.

This table shows the available Types:

| Type | Description |
|---|---|
| Session | The Custom Menu Item is a session. |
| Menu | The Custom Menu Item is a sub menu. |
| Query | The Custom Menu Item is an SQL Query, |

## Code property

The code of the Session, Menu of Query. Sessions and menus can be standard sessions or menus, or own developed sessions or menus in the Extension package. Queries are always own developed queries.

## Overwrite Description property

If you select this property, you can overwrite the standard description of the menu item, which is the sub menu description, the session description or the query description. In this case, you must either specify the `Description Label` property or the `Description` property.

## Description Label property

Use this property to have different descriptions for users that are working in different languages. You can select an existing label, or create a new label in the Extensions package. The label used must have the context ‘General use’. A label can have descriptions in different languages and multiple length variants; for the menu item the longest one is shown at runtime.

See the Infor LN Studio Application Development Guide.

You cannot specify the `Description Label` property if the `Description` property is used.

## Description property

Use this property if your menu item description is not language dependent.

The Description is read-only in case the `Overwrite Description` property is not checked or the `Description` `Label` property is filled. In those cases, the Description shows the description that is used when the menu is displayed at runtime.

## Process Info property

Use this property to pass (static) information from the menu to the session. This only makes sense for own developed sessions, because the standard sessions do not retrieve this information.

## Is Visible hook

Use this hook to add the custom menu item conditionally to the menu. Example:

```baan
function boolean session.txprc5500m000.is.visible()
{
|* Use this hook to remove the menu item from the
|* menu. You can do that based on conditions. To
|* remove it, let the function return the value
|* false.
return(own.pricing.implemented())
|* This function is available in the Functions hook
}
```

## Functions

In the hooks of a Menu extension you can use all trusted functions to do string manipulation, calculations, comparisons, etc.

See Trusted / Untrusted concept on page 155.

Embedded SQL and the `sql.*` functions are available to read data from the LN database.

Calling (own) DLL functions is also possible.

## Limitations and restrictions

- Transactions Transactions in a Menu extension are not supported.

- UI

A Menu extension has no access to the UI. You cannot start sessions or reports, or display messages.

- Top menu The top menu which is displayed in LN UI can be extended. However, if you add a session directly to this top menu, a sub menu is automatically added. The Xi-style does not allow individual sessions in the top menu.

- Testing menu extensions Menu extensions can be tested after the Activity Context is set. If a menu is opened already, you must restart LN UI, set the Activity Context and open the menu. For the top menu, you must commit the extension before you see the changes. After KB 1884185 is installed, you can refresh the menu (including the top menu) from the Extension Modeler.
