# Parallel Application Processing Examples

## Parallel Processing Client
Below an example script is shown of a client which can run both in normal mode and in parallel processing mode.
```

table     tttmmm000
long      group.id

#include <bic_parallel>		| Needed for parallel processing functions
#include "ippmmm0000"

#define SERVER.SESS     "ttmmm0000s000"
#pragma used    session "ttmmm0000s000"

function main()
{
    long    nr.of.server

    |* Read Configuration
    nr.of.server = par.get.no.of.server()
    if nr.of.server > 0 then
        |* Start communication
        group.id = par.init.client.to.server(nr.of.server, SERVER.SESS)
        |* Start the servers
        if group.id < 1 or
           not par.client.start.servers(group.id) then
            return
        endif
    endif

    select  ttmmm000.*
    from    ttmmm000
    where   ...
    selectdo
        if nr.of.server > 0 then
            |* Send job to free server
            if not start.process.external() then
                break
            endif
        else
            |* Process job internally
            start.process.internal()
        endif
    endselect
    if nr.of.server > 0 then
    	|* Wait until all servers are ready
    	par.client.wait.read(group.id)

        |* Close the communication and stop the servers
        par.client.close.servers(group.id)
    endif
}

function boolean start.process.external()
{
    return(par.client.send.message(group.id, edit$(ttmmm000.yrun, "9999")))
}

function start.process.internal()
{
    db.retry.point()
    ippmmm000.process.termination.per.docn() |* include function
    commit.transaction()
}
```

## Parallel Processing Server
Below an example script is shown of the server script which corresponds with the client shown in the previous example.
```

#include <bic_parallel>		| Needed for parallel processing functions
#include "ippmmm0000"

function main()
{
   long    group.number
   long    server.number
   string  messg(20)

   if not par.init.server.to.client(group.number, server.number) then
   	message("not started in server mode")
   	return
   endif

   while par.server.get.message(messg) > 0
        terminate.document(messg)
   endwhile
}

function terminate.document(const string i.messg)
{
    ttmmm000.yrun = lval(i.messg(1;4))

    par.server.retry.point()
    db.retry.point()
    if db.retry.hit() then
        par.server.retry.hit()
    endif
    ippmmm0000.process.termination.per.docn()
    commit.transaction()
}
```

## Related topics
- [Parallel Application Processing Overview](overview.md)

- [Parallel Application Processing synopsis](synopsis.md)
