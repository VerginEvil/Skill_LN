# Record selection Overview
In Infor Enterprise Server there are two ways for the tools to handle record selections in overview sessions.
- The first way of handing record selections is limited and not like other Windows applications.
- The second way is improved and more like other Windows applications.   How the tools handle the selection for a session depends on the [Tools Interface Version (TIV)](../tiv/tiv_overview.md) version of session's script. If the TIV version is equal to or higher than [TIV 1075](../tiv/tiv_1075.md) the improved way is used, otherwise the non-Windows way is used. For sessions that have code for handling record selections in the program script, work should be done when moving to a TIV of 1075 or higher. The type of changes are described in the [Improved Record selection Cookbook](cookbook.md).
The most important features the improved selection mechanism introduces are:
- using the Shift and Control keys to extend the selection
- scroll through the selection
- tools functions that make it easy to make a session that uses the selection of its parent
- a Select All ( [4GL choice sections](../4gl_features/4gl_choice_sections.md)) standard command
- constistent execution of the mark.occur sections   Note  Improved record selection functionality is available from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 1075](../tiv/tiv_1075.md).

## Related topics
- [Record selection Synopsis](synopsis.md)
- [Improved Record selection Cookbook](cookbook.md)
