# Appendix A - AFS-DLL example

This example is the AFS-DLL for the Maintain Areas (tcmcs0145m000) session in Infor ERP.

```baan
|------------------------------------------------------------------------------
| File created by ttstpcreatdll, Date: 28/05/03
| Created for session: tcmcs0145m000
|------------------------------------------------------------------------------
#pragma used dll ottstpapihand
function extern void f0145m000.put.area( const domain tccreg value )
{
DLLUSAGE
Function to set area ( tcmcs045.creg ) in session tcmcs0145m000
arg: - value to put in area
ENDDLLUSAGE
stpapi.put.field( "tcmcs0145m000", "tcmcs045.creg", value )
}
function extern domain tccreg f0145m000.get.area( )
{
DLLUSAGE
Function to get area ( tcmcs045.creg ) from session tcmcs0145m000
return: - value of area
ENDDLLUSAGE
string value(3)
stpapi.get.field( "tcmcs0145m000", "tcmcs045.creg", value )
return( value )
}
function extern void f0145m000.put.description( const domain tcdsca value )
{
DLLUSAGE
Function to set description ( tcmcs045.dsca ) in session tcmcs0145m000
arg: - value to put in description
ENDDLLUSAGE
stpapi.put.field( "tcmcs0145m000", "tcmcs045.dsca", value )
}
function extern domain tcdsca f0145m000.get.description( )
{
DLLUSAGE
Function to get description ( tcmcs045.dsca ) from session tcmcs0145m000
return: - value of description
ENDDLLUSAGE
string value(30) mb
stpapi.get.field( "tcmcs0145m000", "tcmcs045.dsca", value )
return( value )
}
function extern void f0145m000.end([string error(500)])
{
DLLUSAGE
Function to end connection to session tcmcs0145m000
ENDDLLUSAGE
if get.argc() = 0 then
stpapi.end.session( "tcmcs0145m000" )
else
error = get.string.arg(1)
stpapi.end.session( "tcmcs0145m000" , error  )
put.string.arg(1, error)
endif
}
function extern long f0145m000.insert( long do.update, ref string error )
{
DLLUSAGE
Function to insert a record in session tcmcs0145m000
Fields must be put before calling this function
ENDDLLUSAGE
return( stpapi.insert( "tcmcs0145m000", do.update, error ) )
}
function extern long f0145m000.update( long do.update, ref string error )
{
DLLUSAGE
Function to update a record in session tcmcs0145m000
Record must be made current and fields to be changed before calling
this function
ENDDLLUSAGE
return( stpapi.update( "tcmcs0145m000", do.update, error ) )
}
function extern long f0145m000.delete( long do.update, ref string error )
{
DLLUSAGE
Function to delete a record in session tcmcs0145m000
Record must be made current before calling this function
ENDDLLUSAGE
return( stpapi.delete( "tcmcs0145m000", do.update, error ) )
}
function extern long f0145m000.mark([string error (500)])
{
DLLUSAGE
Function to mark the current record in session tcmcs0145m000
ENDDLLUSAGE
long ret
if get.argc() = 0 then
return( stpapi.mark( "tcmcs0145m000" ) )
else
error = get.string.arg(1)
ret =  stpapi.mark( "tcmcs0145m000" , error  )
put.string.arg(1, error)
return( ret )
endif
}
function extern long f0145m000.recover( ref string error )
{
DLLUSAGE
Function to undo an update/insert/delete in session tcmcs0145m000
ENDDLLUSAGE
return( stpapi.recover( "tcmcs0145m000", error ) )
}
function extern long f0145m000.save( ref string error )
{
DLLUSAGE
Function to save an update/insert/delete in session tcmcs0145m000
ENDDLLUSAGE
return( stpapi.save( "tcmcs0145m000", error ) )
}
function extern long f0145m000.find( [string error(500)] )
{
DLLUSAGE
Function to find a record in session tcmcs0145m000
Search fields must be put before calling this function
ENDDLLUSAGE
long ret
if get.argc() = 0 then
return( stpapi.find( "tcmcs0145m000"  ) )
else
error = get.string.arg(1)
ret =  stpapi.find( "tcmcs0145m000" , error  )
put.string.arg(1, error)
return( ret )
endif
}
function extern long f0145m000.synchronize.dialog( string mode(8), ref string err.mesg)
{
DLLUSAGE
Function to set up a synchronized dialog between multi-occurrence
and single-occurrence session
ENDDLLUSAGE
return( stpapi.synchronize.dialog("tcmcs0145m000", mode , err.mesg) )
}
function extern void f0145m000.clear( )
{
DLLUSAGE
Function to clear the current record in session tcmcs0145m000
ENDDLLUSAGE
stpapi.clear( "tcmcs0145m000" )
}
function extern void f0145m000.print( ref string error )
{
DLLUSAGE
Function to start the print option in session tcmcs0145m000
ENDDLLUSAGE
stpapi.print.report( "tcmcs0145m000", error )
}
function extern void f0145m000.set.report( const string reportname, const string device, ref string error )
{
DLLUSAGE
Function to set report name and device for a subsequent print action
in session tcmcs0145m000
ENDDLLUSAGE
stpapi.set.report( "tcmcs0145m000", reportname, device, error )
}
function extern long f0145m000.first([string error(500)] )
{
DLLUSAGE
Function to find the first record in session tcmcs0145m000
ENDDLLUSAGE
long ret
if get.argc() = 0 then
return( stpapi.browse.set( "tcmcs0145m000", "first.set" ) )
else
error = get.string.arg(1)
ret = stpapi.browse.set( "tcmcs0145m000", "first.set" , error )
put.string.arg(1, error)
return( ret )
endif
}
function extern long f0145m000.next([string error(500)] )
{
DLLUSAGE
Function to find the next record in session tcmcs0145m000
ENDDLLUSAGE
long ret
if get.argc() = 0 then
return( stpapi.browse.set( "tcmcs0145m000", "next.set" ) )
else
error = get.string.arg(1)
ret = stpapi.browse.set( "tcmcs0145m000", "next.set" , error )
put.string.arg(1, error)
return( ret )
endif
}
function extern long f0145m000.previous([string error(500)] )
{
DLLUSAGE
Function to find the previous record in session tcmcs0145m000
ENDDLLUSAGE
long ret
if get.argc() = 0 then
return( stpapi.browse.set( "tcmcs0145m000", "prev.set" ) )
else
error = get.string.arg(1)
ret = stpapi.browse.set( "tcmcs0145m000", "prev.set" , error )
put.string.arg(1, error)
return( ret )
endif
}
function extern long f0145m000.last([string error(500)] )
{
DLLUSAGE
Function to find the last record in session tcmcs0145m000
ENDDLLUSAGE
long ret
if get.argc() = 0 then
return( stpapi.browse.set( "tcmcs0145m000", "last.set" ) )
else
error = get.string.arg(1)
ret = stpapi.browse.set( "tcmcs0145m000", "last.set" , error )
put.string.arg(1, error)
return( ret )
endif
}
function extern long f0145m000.set.view( [string error(500)] )
{
DLLUSAGE
Function to define another view in session tcmcs0145m000
ENDDLLUSAGE
long ret
if get.argc() = 0 then
return( stpapi.change.view( "tcmcs0145m000" ) )
else
error = get.string.arg(1)
ret = stpapi.change.view( "tcmcs0145m000",  error )
put.string.arg(1, error)
return( ret )
endif
}
function extern string f0145m000.get.last.message.code([string error(500)])
{
DLLUSAGE
Function to get the code of the message which occurred on
the last insert/update/delete/save/recover action in session tcmcs0145m000
ENDDLLUSAGE
string ret(20)
if get.argc() = 0 then
return( stpapi.get.mess.code( "tcmcs0145m000" ) )
else
error = get.string.arg(1)
ret = stpapi.get.mess.code( "tcmcs0145m000", error )
put.string.arg(1, error)
return( ret )
endif
}
function extern string f0145m000.get.last.error( )
{
DLLUSAGE
Function to get the error message which occurred on
the last action in the Function Server
ENDDLLUSAGE
return( stpapi.get.error( ) )
}
function extern void f0145m000.handle.sub.process( const string sub.process, const string action )
{
DLLUSAGE
Function to define an action when a sub process is started.
Possible actions are: add/send/ignore/kill
add     - add child session to internal structure,
session dll of child can be used
send    - send all api calls to child instead of parent
ignore  - child process is ignored, parent will wait
until child exits (for background processes)
kill    - child process is killed immediately
ENDDLLUSAGE
stpapi.handle.subproc( "tcmcs0145m000", sub.process, action )
}
function extern void f0145m000.define.enum.answer( const string question, bset answer )
{
DLLUSAGE
Function to define an answer on a question, when the default answer should not be taken.
ENDDLLUSAGE
stpapi.enum.answer( "tcmcs0145m000", question, answer )
```

}
