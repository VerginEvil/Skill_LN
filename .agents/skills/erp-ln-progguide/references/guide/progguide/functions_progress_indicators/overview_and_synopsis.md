# Progress indicators overview and synopsis

## Overview
A progress indicator provides feedback to the user on the progress of a lengthy operation. It consists of a rectangular bar that fills from left to right as the operation progresses, indicating the percentage of completion of the operation. It can also (or alternatively) display a series of text messages that describe the progress of the operation.
You can create progress indicators in both UI and DAL scripts.

## Synopsis
```

#include <bic_dam>
```
```
boolean
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
void
```
```
void
```
| | | |
|---|---|---|
|  | [progress.indicator.exists()](progress.indicator.exists.md) | `( )` |
|  | [create.progress.indicator()](create.progress.indicator.md) | `( string title() [, long mode] )` |
|  | [change.progress.indicator()](change.progress.indicator.md) | `( long percentage [, string message,...] )` |
|  | [change.progress.delay()](change.progress.delay.md) | `( long delay )` |
|  | [change.progress.title()](change.progress.title.md) | `( string title() )` |
|  | [destroy.progress.indicator()](destroy.progress.indicator.md) | `( )` |

## Related topics
- [Progress indicators sample program](example.md)
