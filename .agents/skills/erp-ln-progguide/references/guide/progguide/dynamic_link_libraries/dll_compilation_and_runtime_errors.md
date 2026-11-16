# DLL compilation and runtime errors

## Compilation errors
A compilation error occurs when a function is not found in the specified DLLs or if there is an argument mismatch.

## Runtime errors
The following runtime error message is displayed when a script calls a function that has been removed from the DLL and only the DLL has been recompiled:
```

Dynamic Link Failure function %s
```
The following runtime error messages are displayed when a function's arguments are changed within a DLL without recompilation of programs that call the changed function:
```

Arg error <function name>(<argument name>) type ...
expected ...
```
or
```

Illegal number of args (%d) for function %s expected %d
```
To avoid runtime errors, it is advisable to recompile programs whenever you change the programmer's interface of a DLL that is linked to those programs.

## Related topics
- [Dynamic-link libraries](overview.md)
