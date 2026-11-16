# Reports overview and synopsis

## Overview
Use these functions to activate reports and send data to them. Note that the *rprt.** functions are short versions of the *brp.** functions.

## Synopsis
```

void
```
```

long
```
```

long
```
```

long
```
```

long
```
```

void
```
```

long
```
```

void
```
```

void
```
| | | |
|---|---|---|
|  | [brp.close()](brp.close.md) | `( long brp_id )` |
|  | [brp.open()](brp.open.md) | `( string rep_name(16), string device(14), long mode )` |
|  | [brp.open.language()](brp.open.language.md) | `( string rep_name(16), string lang, string device(14), long mode )` |
|  | [brp.ready()](brp.ready.md) | `( long brp_id )` |
|  | [choice.report()](choice.report.md) | `( ref string reportname(15) )` |
|  | [rprt_close()](rprt_close.md) | `( [ long mess_flag ] )` |
|  | [rprt_open()](rprt_open.md) | `( )` |
|  | [rprt_send()](rprt_send.md) | `( )` |
|  | [set.spool.main.report()](set.spool.main.report.md) | `( const string rep_name )` |

## Related topics
- [Spooling overview and synopsis](../functions_spooling/overview_and_synopsis.md)
