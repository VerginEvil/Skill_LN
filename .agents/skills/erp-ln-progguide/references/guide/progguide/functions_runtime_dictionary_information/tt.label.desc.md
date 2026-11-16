# tt.label.desc()

## Syntax:
`function string tt.label.desc( string label_code(19), domain ttadv.cont label_context, ref string desc )`

## Description
This returns information of the specified label. It is returned, and optionally also stored in the *desc* argument. (The optional argument is only present for backward compatibility.)

## Arguments
| | | |
|---|---|---|
| `string` | `label_code(19)` |  The label code, including the package code.  |
| `domain ttadv.cont` | `label_context` |  The label's context. The possible values are: ttadv.cont.general: General Use (for labels on forms and reports) ttadv.cont.description: Session, Table or Report Descriptions ttadv.cont.enumerate: Enumerate descriptions ttadv.cont.indices: Index descriptions ttadv.cont.charts: Chart descriptions ttadv.cont.menus: Menu and menu field descriptions ttadv.cont.ch.opt: Chart Application Option descriptions ttadv.cont.bus.obj: Business Object descriptions ttadv.cont.sub.func: Subfunction descriptions ttadv.cont.form.cmd: Form Command descriptions ttadv.cont.external: Descriptions for External Use ttadv.cont.form.casc.menu: Cascading item on button descriptions  |
| `ref string` | `desc` |  This returns the longest description (in the user's current language) of the specified label.  |

## Return values
The description is returned.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
