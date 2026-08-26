# DLL functions (executing) overview and synopsis

## Overview
Use these functions to execute functions in a dynamic link library (DLL) at runtime. For an overview of dynamic link libraries and runtime dynamic linking, see [Dynamic-link libraries](../dynamic_link_libraries/overview.md).

## Synopsis
| | | |
|---|---|---|
| `long` | [exec_dll_function()](exec_dll_function.md) | `( string dll_name, string function_name [, ref void return_value, arg, ...] )` |
| `long` | [exec_function()](exec_function.md) | `( long dll_id, long func_id [, ref void return_value, arg, ...] )` |
| `long` | [get_function()](get_function.md) | `( long dll_id, string function_name )` |
| `long` | [load_dll()](load_dll.md) | `( string dll_name [, long overload ] )` |
| `long` | [parse_and_exec_function()](parse_and_exec_function.md) | `( string dll_name, string function_call [, ref void return_value, ref string return_call() ] )` |
