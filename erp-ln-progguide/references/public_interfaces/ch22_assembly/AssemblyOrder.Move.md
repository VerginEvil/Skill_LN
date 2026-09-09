# AssemblyOrder.Move

> Chapter: Chapter 22 Public Interfaces for Assembly
>
> Group: Public Interfaces for AssemblyOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 862-864

```baan
DLL:   tiextascapi
This function is available from 2026.06 (KB3651069).
Syntax: long AssemblyOrder.Move(
domain  tiasln           iAssemblyLine,
domain  tiasl.segm       iLineSegment,
domain  tcorno           iAssemblyOrderToMove,
domain  tiasl.posi       iPositionsToMove,
domain  tiasl.domo       iDirectionOfMovement,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Use this Public Interface to move an assembly order from
existing position in line sequence to a newer position in
line sequence based on movement direction and number of
positions to move.
Moving means changing the position of an assembly order in the
sequence of a certain segment, also the position of assembly
orders in between the old sequence number of the order and the
new sequence number of the order have to be changed.
A reschedule will for instance not be possible if the move
results in too late arrival of assembly orders in current or
next segments.
NOTE:   This Public Interface reschedules firm and delayed assembly
orders as well and Public Interface will be executed always in
non-simulation mode
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process. Transaction handling
will be done inside Public Interface.
Input:
iAssemblyLine
- Assembly Line (Mandatory)
iLineSegment
- Assembly Line Segment (Mandatory)
iAssemblyOrderToMove
- Assembly Order to Move (Mandatory)
iPositionsToMove
- Number of Positions to Move (Mandatory)
iDirectionOfMovement
- Direction of Movement of Order (Mandatory)
iProcessingOptionSet
- Processing Option Set (Optional). If 0, then user
default/session default values are applied.
A Processing Option Set can be created via a call to
ProcessingOptionSet.Create() in DLL tcextextapi. After
the call the option set can be deleted by calling
ProcessingOptionSet.Delete().
NAME                        TYPE                DEFAULT
IncludeLinkedSegments       Domain tcyesno      tcyesno.no
PrintReport                 Domain tcyesno      tcyesno.no
PrintingDevice              domain tcmcs.str14  ""
PrintingFileoutPathAndName  domain tcmcs.str100 ""
Default Values:
IncludeLinkedSegments
- If input variable field "IncludeLinkedSegments" is
given, it will be used as default value. Otherwise,
it will be defaulted with "tcyesno.no". With improved
rescheduling logic, the "IncludeLinkedSegments"
option can be used to also reschedule the order on
segments that are linked to "iLineSegment" via a
'FIFO'-buffer. That means: a buffer either of type
FIFO, or of type Random Access, and number of R/A
places is 1.
PrintReport
- If input variable field "Print Report" is given, it
will be used as default value. Otherwise, it will be
defaulted with "tcyesno.no". This is to print what is
rescheduled. If PrintReport is activated, Input variable
Fields "PrintingDevice" and "PrintingFileOutPathName"
will be used as default values otherwise these values
will be defaulted with empty string.
Note: If Print Report is (YES or NO), error messages will be
logged to message log and as well as exception structure.
For Reschedule Assembly orders Report option is only for
the process report. So, error messages will be stored to
exception structure
Output:
oExceptionMessage
- The last error message found during the execution of
public interface. If multiple error messages are found,
by using "oExceptionID", messages can be retrieved.
oExceptionID
- An ID that refers to the exception information. Use
"Exception" related functions to retrieve related
information.
Return:
0               - Success. Assembly Order is Moved.
DALHOOKERROR
- Error occurred during Move process.
```
