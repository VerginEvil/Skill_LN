# Character-based windows - overview and synopsis

## Overview
*Deprecated.* This API is only supported for character-based windows and its usage is therefore deprecated. You do not use these functions to handle graphical windows.
Note  The functions for sending data and instructions to the screen or printer all return a string that you can print by calling the *print()* function or that you can use in a string expression. When you use *print()* with these functions, only the internal screen is updated. You must call [refresh()](refresh.md) to update the terminal screen.

## Synopsis
```

string
```
```

void
```
```

string
```
```

string
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

string
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

void
```
```

string
```
```

string
```
```

string
```
```

string
```
```

string
```
```

string
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

string
```
```

string
```
```

string
```
```

void
```
```

string
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

long
```
```

void
```
```

string
```
```

string
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
```

string
```
```

void
```
```

void
```
| | | |
|---|---|---|
|  | [bg$()](bg.md) | `( long color )` |
|  | [box()](box.md) | `( long box_x, long box_y, long box_width, long box_height, long mode )` |
|  | [bs$()](bs.md) | `( [num_expr] )` |
|  | [cf$()](cf.md) | `( num_expr )` |
|  | [change.window()](change.window.md) | `( long wind_id )` |
|  | [cl.screen()](cl.screen.md) | `( long column, long row, long no_of_cols, long no_of_rows )` |
|  | [cp$()](cp.md) | `( long column, long row )` |
|  | [cr$()](cr.md) | `( )` |
|  | [cs$()](cs.md) | `( [num_expr] )` |
|  | [current.window()](current.window.md) | `( )` |
|  | [data.input()](data.input.md) | `( string options(.), ref string result(.), string default(.) [, ref long event(EVTMAXSIZE), ref long char_value )` |
|  | [del.window()](del.window.md) | `( long wind_id )` |
|  | [delch$()](delch.md) | `( num_expr )` |
|  | [deleteln$()](deleteln.md) | `( num_expr )` |
|  | [el$()](el.md) | `( )` |
|  | [es$()](es.md) | `( )` |
|  | [ff$()](ff.md) | `( )` |
|  | [fg$()](fg.md) | `( long color )` |
|  | [first.window()](first.window.md) | `( long wind_id )` |
|  | [fs$()](fs.md) | `( [num_expr] )` |
|  | [get.col()](get.col.md) | `( )` |
|  | [get.cp()](get.cp.md) | `( ref long x, ref long y )` |
|  | [get.row()](get.row.md) | `( )` |
|  | [get.window.attrs()](get.window.attrs.md) | `( long wind_id, ref long attrs(WINMAXSIZE) )` |
|  | [insch$()](insch.md) | `( string_expr )` |
|  | [insertln$()](insertln.md) | `( string_expr )` |
|  | [keyin$()](keyin.md) | `( [99] )` |
|  | [last.window()](last.window.md) | `( long wind_id )` |
|  | [lf$()](lf.md) | `( [num_expr] )` |
|  | [map.window()](map.window.md) | `( long wind_id )` |
|  | [mark.handler()](mark.handler.md) | `( ref long mark.table() )` |
|  | [move.window()](move.window.md) | `( long col, long row )` |
|  | [new.window()](newwindow.md) | `( long height, long width, long row, long col )` |
|  | [no.scroll()](no.scroll.md) | `( long wind_id )` |
|  | [pc$()](pc.md) | `( num_expr )` |
|  | [pf$()](pf.md) | `( num_expr )` |
|  | [refresh()](refresh.md) | `( [long wind_id] )` |
|  | [set.refresh.rate()](set.refresh.rate.md) | `( [long wind_id] )` |
|  | [resize.window()](resize.window.md) | `( long width, long height )` |
|  | [scroll()](scroll.md) | `( long wind_id )` |
|  | [set.bg.color()](setbgcolor.md) | `( long wind_id, long color )` |
|  | [set.fg.color()](set.fg.color.md) | `( long wind_id, long color )` |
|  | [sf$()](sf.md) | `( num_expr )` |
|  | [sub.window()](sub.window.md) | `( long parent_wind, long height, long width, long row, long col )` |
|  | [tab$()](tab.md) | `( num_expr )` |
|  | [unmap.window()](unmapwindow.md) | `( long wind_id )` |
|  | [wrebuild()](wrebuild.md) | `( long mode )` |
