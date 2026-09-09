# rbhp.set.session()

## Syntax:
`#pragma used dll "ottstprbhp"`
`function void rbhp.set.session( const string session.code, long mode, long company, [ long session.index ] )`

## Description
Set the session to be started, the mode of this session, the company number in which this session and the start index of the session. This function can only be called by either the application function: tcint.dll0001.drill.back() or the tools function icm.drillback() of the tticmdll0002 library.

## Arguments
| | | |
|---|---|---|
| `const string` | `session.code` |  The code of the session that must be started  |
| `long` | `mode` |  SINGLE_OCC The session is started as a single-occurrence (details) session. MULTI_OCC The session is started as a multi occurrence (overview) session. MULTI_OCC+MODAL The session is started as a multi occurrence in zoom mode.  |
| `long` | `company` |  The company number in which the session must be started.  |
| `[ long` | `session.index ]` |  Optional argument specifying the initial index of the started session.  |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Role Based Home Pages overview](overview.md)

- [Role Based Home Pages synopsis](synopsis.md)
