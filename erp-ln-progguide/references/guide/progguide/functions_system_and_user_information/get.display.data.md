# get.display.data()

## Syntax:
`function long get.display.data( ref long server_data(SRVMAXSIZE) )`

## Description
This retrieves information about the display server. It stores the information in the array *server_data*. The predefined constant SRVMAXSIZE indicates the maximum size of the array.
You can retrieve the information using a set of predefined variables:
| | |
|---|---|
| Information | Variable |
| Server type |  typesrv.type(server_data) DSNOSERVER DSBX DSBA DSBW  |
| Display width | srv.display.width(server_data) |
| Display height | srv.display.height(server_data) |
| Display width in millimeters | srv.display.width.mm(server_data) |
| Display height in millimeters | srv.display.height.mm(server_data) |
| Number of colors | srv.display.colors(server_data) |
| Microsoft operating system |  srv.display.os.type(server_data) DSBW_WIN_311 DSBW_WIN_NT DSBW_WIN_95 NT4  |

## Arguments
| | | |
|---|---|---|
| `ref long` | `server_data(SRVMAXSIZE)` |  |

## Context
This function is implemented in the porting set and can be used in all script types.
Note  The above variables are valid only after a call to *get.display.data()*.

## Related topics
- [System and user information overview and synopsis](overview_and_synopsis.md)
