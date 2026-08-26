# Memory operations overview and synopsis

## Overview
Use these functions to perform various memory operations. For example:
- to allocate and deallocate memory at run time
- to retrieve the structure and size of an array
- to compare the values in two memory spaces
- to copy data from one memory space to another
- to set the content of a memory space.

## Synopsis
| | | |
|---|---|---|
| `long` | [alloc.mem](alloc.mem.md) | `( ref variable, long dim1 [, long dim2, ...] )` |
| `long` | [array.get.size.in.bytes](array.get.size.in.bytes.md) | `( void var )` |
| `void` | [array.info](array.info.md) | `( void var, ref long nr.dims, ref long dim.array(4) )` |
| `long` | [cmp.mem](cmp.mem.md) | `( var1, var2 [, long count] )` |
| `void` | [copy.mem](copy.mem.md) | `( ref destination, source [, long count] )` |
| `void` | [free.mem](free.mem.md) | `( variable )` |
| `long` | [get.size.in.bytes](get.size.in.bytes.md) | `( void var )` |
| `long` | [set.mem](set.mem.md) | `( ref destination, source [, long count] )` |
