# The Call Graph Profiler
The Call Graph Profiler is a performance profiler for Baan 3GL and 4GL programs. It is designed to give information about the bottlenecks in the profiled application.
The Call Graph Profiler collects statistics about the execution of the profiled program. The data is presented in a HTML browser. The Call Graph Profile provides hierarchical information for each function in the program. It reports the time that is spent in the function itself and the time spent in the functions called by the function (children). This makes it easy to relate execution time to the high-level activities of the application (e.g. sections in the UI, sections in the DAL, functions in DLLs) and understand where the time is spent.
The Call Graph Profile also provides information about SQL statements (parse, exec and fetch times) and other functions that are related to the database (e.g. db.update, commit.transaction, abort.transaction). This makes it easy to find which database operations are executed too often or are running too long.
The Call Graph Profiler does not require profiled objects in the Baan environment (these are objects compiled in profile mode, used in the 'old' profiling mechanism). The Call Graph Profiler does not require source code in the Baan environment.

## Related topics
- [Using the Call Graph Profiler](using.md)

- [The Call Graph Profile](output.md)

- [Analyzing the Call Graph Profile](analyzing.md)

- [Call Graph Profiler Example](example.md)

- [Call Graph Profiler Glossary](glossary.md)
