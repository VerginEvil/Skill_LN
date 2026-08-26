# Variables (based) overview and synopsis

## Overview
Use the *at.base()* functions to base one variable (the *based_variable*) on another variable or value (the *basic_variable* or *basic_value*). The *based_variable* then uses the same memory area as the *basic_variable* or *basic_value*.
The *based_variable* must be of the same type as the *basic_variable* or *basic_value*. The possible types are string, string array, long array, and double array.
The *based_variable* must be declared as BASED.
The *basic_variable* must be declared as EXTERN.
If the *basic_variable* is declared as CONST or the *basic_value* is not suitable as a reference argument, then the *based_variable* must be declared as CONST.

## Synopsis
```

long
```
```

long
```
| | | |
|---|---|---|
|  | [at.base](at.base1.md) | `(<ref|const> <type> basic_value [, long position, ...], <ref|const> <type> based_variable [, long length, ...])` |
|  | [at.base](at.base2.md) | `(long process_id, string basic_variable_name, void unused [, long position, ...], <ref|const> <type> based_variable [, long length, ...])` |
