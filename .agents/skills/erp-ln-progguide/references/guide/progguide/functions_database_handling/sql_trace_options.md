# SQL trace options
It is possible to monitor whether the SQL compiler and optimizer are taking the right decisions. If the results indicate that the design is incorrect, the query must be changed. The optimizer can never emulate the programmer. The Infor Enterprise Server 3GL programming language therefore enables the programmer to instruct the computer what it has to do to a considerable degree of detail. You can define which index to use; also, a number of special (non-standard SQL) functions have been built in.
You can use the environment variable BAAN_SQL_TRACE to trace what happens inside the SQL processor. BAAN_SQL_TRACE is used to trace SQL processing in the client (that is, bshell), as well as in the server process (that is, the database driver). The methods involved are different for client and server.

## Client tracing
When BAAN_SQL_TRACE is set, the output from the client process is written to stderr. To keep this information, you must call the bshell with the options "-keeplog" and "-logfile <log file name>". This can be done by specifying the following options in the bw configuration:
```

    -- -keeplog -logfile mylogfile -set BAAN_SQL_TRACE=02000
```
This enables BAAN_SQL_TRACE with value 02000. The output is written to the file "mylogfile" in the current working directory.

## Server tracing
When BAAN_SQL_TRACE is set, the output is written to a file named "dbs.log". This file is located in the current working directory when the Database Server runs locally (on same host as Display Server). When the database is remote, it is written in the login directory of the corresponding user on that remote system. To enable logging of BAAN_SQL_TRACE in the file "dbs.log", you must also set the environment variable DBSLOG, as follows:
DBSLOG=02000
The "02000" is an octal value, and can be OR-ed with other variables. The meaning of the other values is described in a separate document (Logging Database Information (DBSLOG)).

## Query identification
A QueryIdentifier (QID) identifies each query. This makes it easy to find out which output in the Client log file is related to the output of the Server log file.

## Trace options
The following values for BAAN_SQL_TRACE are available (C indicates that an option can be used for the client; S indicates that it can be used for the server):
| | | |
|---|---|---|
| BAAN_SQL_TRACE | C/S | Explanation |
| 1 | C | Shows the initial parse tree of the SQL statement and the validated parse tree after resolving column names to column references, resolving enum constants to integers and defining the select targets. |
| 2 | C+S | Shows the initial execution tree and the execution tree after optimization. |
| 4 | C+S | Shows the evaluation of the execution tree. |
| 100 | C | Shows the efficiency of the statement cache. |
| 200 | C+S | Shows the network packets being transferred between the client and the server. |
| 2000 | C | Shows the interface calls on the statement. |
| 4000 | C | Same as BAAN_SQL_TRACE=2000, but with extra detailed interface calls. |
You can combine trace options by adding the values. For example:
```

BAAN_SQL_TRACE=02200
```
This produces the results of both options 02000 and 0200.

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
