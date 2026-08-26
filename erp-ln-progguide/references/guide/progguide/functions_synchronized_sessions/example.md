# Child synchronization sample program
```

  declaration:
    long   field.proc
  before.program:
    field.proc = 0
    ...

  function extern field.process()       | called by Form Command
  {
    if field.proc then
          synchronize.with.child( field.proc )
    endif
    | field.proc is a reference variable that is set to zero when
    | child cannot be found
    if not field.proc then
          field.proc = start.synchronized.child ( "ttadv4127m000",
              "ttadv420.vers", "ttadv422.vers",
              "ttadv420.rele", "ttadv422.rele",
              "ttadv420.cust", "ttadv422.cust",
              "ttadv420.cpac", "ttadv422.cpac",
              "ttadv420.cmod", "ttadv422.cmod",
              "ttadv420.flno", "ttadv422.flno" )
    endif
  }
```

## Related topics
- [Synchronized sessions overview](overview.md)
- [Synchronized sessions synopsis](synopsis.md)
