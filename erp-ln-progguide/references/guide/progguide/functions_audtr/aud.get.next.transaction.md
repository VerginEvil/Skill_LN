# aud.get.next.transaction()

## Syntax:
`function long aud.get.next.transaction( long selection.id, long number.of.retries, long retry.interval, ref string transaction.id, ref long commit.time, ref string session, ref string user )`

## Description
After the transactions to be selected have been specified using [aud.select.transactions()](aud.select.transactions.md) the next step is to retrieve the audit data from the audit trail. The retrieved audit data can be processed in combination with the acquired meta data. The aud.get.next.transaction function fetches the next transaction data based on the selection defined with the [aud.select.transactions()](aud.select.transactions.md) function. When a transaction is read successfully, the function returns the transaction header, consisting of *transaction.id*, *commit.time*, *session* and *user*.

## Arguments
| | | |
|---|---|---|
| `long` | `selection.id` |  Id of the selected transactions returned by [aud.select.transactions()](aud.select.transactions.md).  |
| `long` | `number.of.retries` |  |
| `long` | `retry.interval` |  Number of milliseconds to wait before doing a retry to retrieve the data.  |
| `ref string` | `transaction.id` |  Id of the transaction, as read from the audit trail.  |
| `ref long` | `commit.time` |  The commit date and time of the next transaction (UTC format).  |
| `ref string` | `session` |  The code of the session that is responsible for the transaction.  |
| `ref string` | `user` |  The Infor Enterprise Server user code of the user who is responsible for the transaction.  |

## Return values
| | |
|---|---|
| AUD_OK | Next transaction could be determined and transaction header data is retrieved successfully  |
| AUD_FAIL | An error occurred when trying to retrieve the transaction data  |
| AUD_NO_MORE_TRANSACTIONS | If there are no more transactions that meet the selection criteria defined, using function aud.select.transactions, the function returns NO_MORE_TRANSACTIONS.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Restrictions
Aud.select.transactions has to be called successfully prior to this function. The *selection.id* must be equal to the *selection.id* returned by [aud.select.transactions()](aud.select.transactions.md).

## Related topics
- [Audit management overview](audit_management_overview.md)
- [Audit management synopsis](audit_management_synopsis.md)
- [Audit management examples](audit_management_examples.md)
