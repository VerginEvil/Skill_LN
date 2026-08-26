# Object identifications (preprocessor)
The compiler always places a default identification in an object, but you can include you own if you wish. You can use the UNIX command *what* to write all object lines that begin with '@(#)' on standard output.
The default identification has the following contents:
```

#ident "@(#)<source name>, YY/MM/DD, [HH/MM], From ${logname}"
```
To set you own identification use the following statement:
```

#ident "@(#)Identification of object"
```
For example:
```

#ident "@(#)<progname>, YY/MM/DD [HH/MM], version, author"
```

## Related topics
- [3GL programming language features: overview](overview.md)
- [Preprocessor](preprocessor.md)
