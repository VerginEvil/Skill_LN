# Chapter 2 Application Function Server

One of the preferred methods of integration between Infor ERP systems (Baan IVc, Baan5.x, and ERP Enterprise (LN) and third-party products is by means of Business Object Interfaces or BOIs. BOIs provide an Application Programming Interface (API) for the ERP Baan business logic and run in the context of BCBE, OpenWorldX, or Open Architecture Adapter Suite.

The high-level interfaces that the BOIs provide cannot be used directly against the ERP Baan business logic due to the ERP Baan architecture. The business logic is implemented by means of sessions, which are primarily user-interface based. Programmatic access to sessions is provided by means of a low-level message protocol. This message protocol is encapsulated into a set of function primitives called the Application Function Server (AFS); these functions are located in the API- handler. The BOI code accesses the session business logic by means of the AFS. The public, high- level interfaces exposed by the BOIs are internally translated to the low level primitives understood by the AFS, which then communicates with the session logic by means of the message protocol.

Usually, you are not required to create BOIs and AFS-DLLs from scratch. Instead, you can generate BOIs with the BOI generator, for BCBE, or BOI Builder, for Open Architecture Studio. AFS-DLLs can be created with the AFS-DLL generator (ttstpcreatdll).

The use of both of these tools is described inBOI Builder Developer’s Guideand the*Developer's* Guide for ERP Baan IV, ERP Baan5.x and ERP Enterprise Servers (LN) . You can use the generated BOIs and AFS-DLLs directly to solve straightforward integration problems where only one BOI and one AFS-DLL are involved to implement a particular interface function set. Complex integration scenarios in which multiple BOIs and AFS-DLLs are involved, for example, sales orders, require extra development in the generated BOI and AFS-DLL code. This extra development cannot be accomplished without detailed knowledge of the architecture and programming constructs involved in both the BOI and AFS-DLL code.

The use of an AFS-DLL is optional; the BOIs can also use the function primitives of the AFS directly. However, the function names generated in the AFS-DLL have logical names (for example, field names instead of field codes), so typing errors will be caught by the compiler. Otherwise, typing errors will be found at runtime. The AFS-DLL creates as extra layer on top of the Baan Standard Program, or ‘stpapi’, which decreases the performance. With the AFS-DLL, however, typing errors can be caught by the compiler, because the AFS uses logical names, for example, field names instead of field codes. Without the AFS-DLL, typing errors will not be found until runtime. The use of AFS is not restricted to BOIs only. In addition, other Baan 3GL or 4GL programs can use the AFS to call other sessions with their business logic to perform particular tasks.

Because the BOI programming constructs are described in detail in theDeveloper's Guide for ERP Baan IV, ERP Baan and ERP Enterprise Servers (LN) , this document describes only the details of the AFS here.

## Architecture

The role of the AFS in the BOI architecture is shown in this diagram:

The diagram clearly illustrates that the BOI communicates with the underlying Infor ERP session by means of the AFS.

## Explanation diagram:

- BOI/3GL/4GL: The program that wants to access the Infor ERP session business logic.

- AFS-DLL: The DLL that contains wrapper functions to the AFS function primitives. This DLL is optional.

- AFS2: The DLL that contains the implementation of the AFS function primitives. This DLL communicates with the 4GL-Engine through a dedicated BMS protocol to enable the session to run the requested functionality.

- AFS Server: Server process that communicates with the 4GL-Engine through a dedicated BMS protocol to permit the session to run the requested functionality.

- Field buffer: The field buffer contains the fields (names and values) of the form, which are input for the session. If the first API-call to a specific session is carried out, these fields are retrieved from the session. These fields can be table fields, but also other form fields, which are used for input.

The values from the BOI are buffered in the field buffer. If the session needs these values in the field loop of the session, the 4GL-Engine takes the values from the field buffer and makes the values available in the session.

After the session changed the field values, such as during an update or browse set, the field buffer is updated and the BOI can retrieve the new values. For more information, refer to Chapter 4, “Special issues.”

- 4GL-Engine: The engine for each Baan 4GL application session, which performs all form, field, event, and main table handling, etc. This engine is the same 4GL-Engine that is used to run the session in the user interface, for example, Baan Windows. While the session usually waits for user interactions, for example, filling fields, pressing buttons, etc., the session now waits for AFS commands. The variable api.mode is set to True, which causes the 4GL-Engine to handle differently. In addition, the session logic can use this predefined variable to have different behavior when called from the AFS.

- Session logic: The Baan 4GL application sessions that is run with the AFS. More sessions can exist if a session opens more subsessions or in the case of multi-occurrence/single-occurrence synchronization, ERP Baan 5.x and ERP Enterprise (LN) only.

Only one instance can be active for a session. The AFS keeps track of the session instances and sends the BMS messages to the process number, which is attached to that session instance internally.

Bear in mind that the session only works for one record at a time. For multi-occurrence forms, type 2 or 3, only one occurrence is used.

**Example of using AFS**

```baan
function long add.record.to.table(
domain dtseno i.seno,
domain dtkey1 i.key1,
domain dtname i.name,
ref string o.mess())
{
long   retval
string dummy.msg(1)
stpapi.put.field("dtfsa1101s000", "dtfsa100.seno", str$(i.seno)) |* 1
stpapi.put.field("dtfsa1101s000", "dtfsa100.key1", i.key1)  |* 2
stpapi.put.field("dtfsa1101s000" , "dtfsa100.name", i.name)
retval = stpapi.insert("dtf sa1101s000", true, o.mess)  |* 3
if not retval then
retval = stpapi.recover("dtfs a1101s000", dummy.msg)  |* 4
endif
stpapi.end.session("dt fsa1101s000")    |* 5
return(isspace(o.mess))
}
```

## Explanation of the example

The numbers in the following list refer to the comments in the source code of the example:

1  The first API-call for the session, or the first argument, results in the activation of the session and the creation of the field buffer. The sections before.program, main.table.io/before.read and form1/before.form of the session are executed if present. Because it is a put.field function, the value of i.seno is put in the field buffer.

2  Other put functions on a session already activated only result in an update of the field buffer.

3  During the insert in the session, the relevant sections are run, such as choice.add.set/before.choice etc., and the field loop starts, which includes all fields of all forms. For these fields, the field sections are run, such as before.field, before.checks and check.input, or the check.property hook in the DAL for ERP Baan 5.x and ERP Enterprise (LN) only. If an error occurs, this information is returned in retval, but the message is also returned in o.mess. Because the do.save flag is set to True, the sections choice.update.db/before.choice etc. also run.

4  Recover is necessary to stop the update mode of the session if an error occurred.

5  The session must be ended; choice.end.program runs.

This example is provided here merely offer an idea of programming with the AFS. Chapter 3, “Baan 4GL engine primitives,” which describes the AFS function primitives, offers a number of additional examples.

## Structure of the AFS-DLL

The structure of the AFS-DLL can best be described by looking at an example of one. Appendix A shows the AFS-DLL for the Maintain Areas (tcmcs0145m000) session. The AFS-DLL is realized as an Infor ERP library named tcmcsf0145m000. Note the “f” in the AFS library name. The standard naming convention for an AFS-DLL is to use the name of the parent session and insert an “f” after the module code.

The AFS-DLL contains functions for setting and retrieving values for fields in the underlying session. This AFS-DLL also contains functions to add, modify, and delete records from the session. Functions for browsing are also provided. In addition, miscellaneous functions for setting answers to questions, handling subsessions, and retrieving error messages are provided.

A number of important features must be noted. First, all of the functions follow a naming convention that is obvious when the example code is perused. The naming convention must be followed when making changes to the AFS-DLL, as the BOI relies on this (if it is generated). Second, all of the AFS- DLL functions are merely a thin shell on the low-level primitives exposed by the 4GL Engine. These primitives in turn encapsulate the message protocol described previously. For more details, refer to the following chapter, which provides an in-depth description of the function primitives. An explanation of the function primitives must suffice to also describe the AFS-DLL functions.

## Compilation

To compile programs that use the AFS functions, the library ottstpapihand must be linked to the program or code #pragma used dll ottstpapihand in the script.
