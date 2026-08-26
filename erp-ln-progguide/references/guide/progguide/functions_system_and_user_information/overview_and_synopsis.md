# System and user information overview and synopsis

## Overview
Use these functions to retrieve system and user information.

## Synopsis
| | | |
|---|---|---|
| `string` | [bse.appdata.dir$](bse.appdata.dir.md) | `()` |
| `string` | [bse.dir$](bse.dir.md) | `()` |
| `string` | [bse.release$](bse.release.md) | `()` |
| `string` | [bse.tmp.dir$](bse.tmp.dir.md) | `()` |
| `long` | [current.display](current.display.md) | `()` |
| `long` | [get.bw.hostname](get.bw.hostname.md) | `( ref string hostname )` |
| `string` | [get.bw.ip.address](get.bw.ip.address.md) | `()` |
| `long` | [get.bw.username](get.bw.username.md) | `( ref string username )` |
| `long` | [get.display.data](get.display.data.md) | `( ref long server_data(SRVMAXSIZE) )` |
| `string` | [getenv$](getenv.md) | `( string env_var(256) )` |
| `long` | [get.long.byte.count](get.long.byte.count.md) | `()` |
| `string` | [get.os.user](get.os.user.md) | `()` |
| `string` | [get.resource$](get.resource.md) | `( string resource_name(256) )` |
| `long` | [get.ui.mode](get.ui.mode.md) | `()` |
| `long` | [get.utc.byte.count](get.utc.byte.count.md) | `()` |
| `boolean` | [group.exists](group.exists.md) | `( const string groupname )` |
| `string` | [hostname$](hostname.md) | `( [boolean getcanonicalname] )` |
| `boolean` | [is.administrator](is.administrator.md) | `()` |
| `long` | [ostype](ostype.md) | `()` |
| `long` | [setenv](setenv.md) | `( string env_var(256), string env_value(1024) )` |
| `boolean` | [user.exists](user.exists.md) | `( const string username )` |
