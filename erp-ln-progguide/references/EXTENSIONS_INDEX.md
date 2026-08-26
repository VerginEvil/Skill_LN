# Infor LN Extensions Development Guide (10.8)

Full text of *Infor LN Extensions Development Guide* (162 pages, edition 01062026),
converted to Markdown. Covers the LN Extension Modeler and all extension points for
customizing standard LN components without touching core software ("last-mile" development).

Source PDF: `Infor LN Extensions Development Guide 108 (01062026).pdf`.

## Chapters

| File | Content |
|---|---|
| `extensions/about_this_guide.md` | Scope, audience |
| `extensions/introduction.md` | Extensibility concept, types (Personalize/Tailor/Extend/Integrate), supported LN versions, licensing |
| `extensions/personalization.md` | User personalization features |
| `extensions/customer_defined_fields.md` | CDF types, configuration, PMC export/import, ttadv4291m000/ttadv4292m000, limitations |
| `extensions/extension_modeler.md` | Extension Modeler (ttext1500m000), cloud readiness, getting started, activity context, scripts, history, activation/deactivation |
| `extensions/domain_extension_point.md` | Domain extension, extended string length |
| `extensions/table_extension_point.md` | Table hooks (declarations/functions/before.open.object.set/set.object.defaults/method.is.allowed/before+after.save.object/before+after.destroy.object), CDF logic hooks (is.applicable/is.mandatory/is.readonly/is.derived/make.valid/is.valid/update), standard field logic, custom index, calculated fields, User Exit DLL |
| `extensions/report_extension_point.md` | Report hooks (write row, get alternative report), table selection, datasets (LN Report Designer), calculated fields, text line filters |
| `extensions/session_extension_point.md` | Session extension: before.context.send, table selection, secondary tables, linked reports, CDF/standard/custom field hooks (when.field.changes, check.input, zoom hooks), custom/calculated fields, standard+custom form commands, context messages, events |
| `extensions/bod_bde_extension_point.md` | BOD/BDE extension: Add Calculated Fields hook macros (addValue, addAmountValue, addCodeValue, addMasterDataReferenceValue, addQuantityValue, addDescription, addEffectiveTimePeriod, addXML), Process Inbound User Area hook macros (getFirstProperty ... getUserAreaParent), CC-library |
| `extensions/odata_rest_api_extension_point.md` | OData REST API entity type extension, CDFs |
| `extensions/menu_extension_point.md` | Menu extension: standard/custom menu items, is.visible hook |
| `extensions/process_extension_point.md` | Process extension: custom fields, calculate initial value |
| `extensions/extension_debugging.md` | Debug Workbench, breakpoints/watchpoints, debugging from LN Studio |
| `extensions/new_component_development_ln_studio.md` | New components (tables/domains/sessions) in Infor LN Studio |
| `extensions/governance.md` | Trusted/untrusted concept, performance governors, file system governors, best practices (database, standard components) |
| `extensions/extension_deployment.md` | Exporting/importing extensions |

## Quick orientation

- **Hook signature pattern**: `function extern <type> <hook-name>(args)` coded inside an
  extension of a specific table/session/report; error signaling via
  `dal.set.error.message("@...")`, return `DALHOOKERROR` / false / nonzero as documented per hook.
- **Extension scripts** run under VRC; created/maintained in Extension Modeler
  (`ttext1500m000`) or Infor LN Studio; activated/deactivated per company/activity.
- **CDF naming**: `<table>.cdf_<name>` e.g. `tdsls400.cdf_blck`; logic hooks are named
  `<constantname>.is.mandatory()`, `.make.valid()` etc.
- **BOD UserArea macros** only work directly inside the hook (not in called functions).

Background for DAL semantics (return values, `dal.set.error.message()`,
`with.old.object.values.do()`) lives in the main programmer's guide:
`references/FUNCTION_INDEX.md` (functions_dal) and `guide/progguide/`.
