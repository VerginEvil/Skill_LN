# tt.reports()

## Syntax:
`function void tt.reports( const string i.session.code, ref long o.nr.reports, ref long o.rprt.group(), ref long o.rprt.nr(), ref string o.rprt.code(,), ref boolean o.is.standard() )`

## Description
This returns all reports defined for a session.

## Arguments
| | | |
|---|---|---|
| `const string` | `i.session.code` |  The session code.  |
| `ref long` | `o.nr.reports` |  This returns the number of reports (standard + custom) defined for the session.  |
| `ref long` | `o.rprt.group()` |  This returns report group numbers (array).  |
| `ref long` | `o.rprt.nr()` |  This returns the sequence numbers within the group, standard reports first (array)  |
| `ref string` | `o.rprt.code(,)` |  This returns the report codes, including 'r' prefix (array)  |
| `ref boolean` | `o.is.standard()` |  This returns if a report is standard (true = standard, false = custom) (array)  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2381.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
