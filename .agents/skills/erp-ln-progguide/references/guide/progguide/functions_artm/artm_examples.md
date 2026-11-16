# Application Response Time Measurement (ARTM) Examples

## Example 1
```

function extern start.mrprun()
{
long    tra.class.id
long    tra.id

        | Define the MRP transaction class
        tra.class.id = artm.define.transaction.class(
                "MRP run",
                "This is a logistic MRP run within Infor Enterprise Server.",
                ART.CODE, "State",
                ART.GAUGE, "Memory" )

        | Start the MRP run
        session.tra.id = artm.begin.transaction(
                tra.class.id,
                ART.CODE, "Starting",
                ART.GAUGE, get.mem() )

        while not end,of.run()
                process.next.mrp.item()

                | Give feedback about the status
                artm.update.transaction(
                        session.tra.id,
                        ART.CODE, "In progress",
                        ART.GAUGE, get.mem() )
        endwhile

        | Run was successful.
        artm.end.transaction(
                tra.id,
                ART.TRANSACTION.SUCCESS,
                ART.CODE, "Finished",
                ART.GAUGE, get.mem() )
}
```

## Example 2:
Update of the metrics of a predefined session transaction class at the beginning of a session.
```

before.program:
        | Redefine the transaction belonging to form command
"Process orders"
        redefined.tra.class.id = artm.redefine.transaction.class(
                "process.orders",
                ART.COUNTER, "Order count",
                ART.CODE, "Customer code" )

functions:
function extern process.orders()                | Attached to form
command
{
        long    tra.id

        | User has started order processing. Start the transaction
        tra.id = artm.begin.transaction(
                redefined.tra.class.id,
                ART.COUNTER, 0,
                ART.CODE, "" )

        for i = 1 to order.count
                process.order()

                | Give feedback about the order processed
                artm.update.transaction(
                        tra.id,
                        ART.COUNTER, i,
                        ART.CODE, cust.code )
        endfor

        | All orders are processed. End transaction.
        artm.end.transaction(
                tra.id,
                ART.TRANSACTION.SUCCESS,
                ART.COUNTER, order.count,
                ART.CODE, "" )
}
```
