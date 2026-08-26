# Processes overview and synopsis

## Overview
Use these functions for handling processes.

## Synopsis
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

string
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
```

void
```
```

void
```
```

string
```
```

long
```
| | | |
|---|---|---|
|  | [act.and.sleep()](act.and.sleep.md) | `( string procname(.) [, "arg1", "arg2" ...] )` |
|  | [activate()](activate.md) | `( string procname(.) [, "arg1", "arg2" ...] )` |
|  | [argc()](argc.md) | `( )` |
|  | [argv$()](argv.md) | `( num_expr )` |
|  | [bshell.pid()](bshell.pid.md) | `( )` |
|  | [kill()](kill.md) | `( long processno )` |
|  | [pstat()](pstat.md) | `( long pid, ref string progname, ref long info(PSMAXSIZE) )` |
|  | [reactivate()](reactivate.md) | `( long processno )` |
|  | [signal()](signal.md) | `( long type, long action )` |
|  | [sleep()](sleep.md) | `( long processno )` |
|  | [suspend()](suspend.md) | `( long msec )` |
|  | [wait()](wait.md) | `( ref long process_id, long option )` |
|  | [wait.and.activate()](wait.and.activate.md) | `( string procname(.) [, "arg1", "arg2", ...] )` |

## Related topics
- [Process groups overview](../functions_process_groups/overview.md)
- [Multitasking and the GUI](../multitasking/multitasking_and_the_gui.md)
