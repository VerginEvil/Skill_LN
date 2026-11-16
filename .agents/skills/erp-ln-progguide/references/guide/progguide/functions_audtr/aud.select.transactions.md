# aud.select.transactions()

## Syntax:
`function long aud.select.transactions( long nr.tables, const string table.codes(,), const long companies(), const string selection.criteria, ref long selection.id )`

## Description
Before transactional data can be read from the audit trail the developer has to select the transactions. This function selects transactions from the audit trail using a list of tables and, if required, some additional selection criteria. The *selection.criteria* is given in a SQL 'where' like fashion and is used to filter the desired transactions.

## Arguments
| | | |
|---|---|---|
| `long` | `nr.tables` |  The number of tables for which transaction data must be selected. This must be greater than 0.  |
| `const string` | `table.codes(,)` |  An array containing the tables for which transaction data must be selected. This array must have at least *nr.tables* elements.  |
| `const long` | `companies()` |  An array containing the company for each table in the table.codes array. This array must have at least *nr.tables* elements. The physical company number must be used, because the audit trail is created per physical company. For a logical table, the physical company can be retrieved using function db.get.physical.compnr().  |
| `const string` | `selection.criteria` |  A string that holds the where clause for the selection. This string may be empty, in which case you will select all transaction data for the specified tables.  |
| `ref long` | `selection.id` |  Id of the prepared selection of transactions. This value can be used in subsequent function calls to functions like aud.get.next.transaction().  |

## Return values
| | |
|---|---|
| AUD_OK | Success. |
| AUD_NO_TABLES | No tables are specified. |
| AUD_NO_AUDIT | The specified tables/companies are not valid, or audit is not on for one of the tables. |
| AUD_INCORRECT_SELECTION | The selection.criteria is not valid. |
| AUD_TOO_BIG | Too many tables, too many different companies, or a very long selection.criteria string are specified. |
| AUD_MULTI_COMPANY | The *companies* array contains multiple different companies, but the system setup doesn't allow simultaneous selection of transaction data for those companies. |
| AUD_FAIL | The *selection.criteria* is not valid. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Restrictions
None.

## How to specify the selection criteria
The *selection.criteria* string is an expression that is used to create the 'where' clause of an SQL statement. Instead of using table fields in the expression the user must use predefined identifiers.
The following identifiers are available for the user:
| | |
|---|---|
| #TRANSID# | The transaction id. Transaction id values are in string format. |
| #COMMITTIME# | The commit time of the transaction. Note that the date/time is represented in UTC format. |
| #SESSION# | The session in which the transaction has been done. |
| #USER# | The Baan user that has performed the update. |
Using these identifiers the developer can construct any expression that complies with the constraints of a 'where' condition of Infor Enterprise Server SQL.

## Constraints
| | |
|---|---|
| Number of tables | The number of tables for which transaction data can be selected simultaneously is limited.As a rule of thumb, you can presume the function will have no problems if the sum of the number of tables and the number of different companies is less than or equal to 30.If too many tables, or too many different companies, or a very long selection.criteria string are specified, aud.select.transactions() will return AUD_TOO_BIG. Furthermore, take into account that the number of tables influences the performance of the function. |
| Number of companies | By default, transaction notifications are logged in company 000. But the user has the option to log transaction notifications in the application company. If this is done (by setting resource variable "audit_per_compnr" for the Infor Enterprise Server Virtual Machine), the functionality of aud.select.transactions() is limited, because it can only read from one company at a time. So if the resource variable is set, the function will only succeed if each table has the same company specified, or if the transaction notifications for the specified companies are stored in the same company. In other words, if the transaction notifications for the specified tables are stored in multiple physical companies, the function will return AUD_MULTI_COMPANY. |
| Joins | In the selection.criteria, a join with other tables is not possible because aud.select.transactions() creates an SQL statement with only the transaction notification table in the from list. The function returns an error if other tables are used in the selection criteria. |
| Case-sensitive identifiers | When the selection criteria string is parsed, the identifiers (such as #USER#) are searched and the table field equivalent will be substituted for the identifier. The search and replace process is case-sensitive so only the identifiers as described above will be replaced. Other versions of the identifiers such as #User# or #user# are left unchanged and will present errors during the selection process. |
| Time ranges | Note that with a time range the end time is included in the selection. To specify a time range of one hour use 08:00:00 - 08:59:59 and not 08:00:00 - 09:00:00. The time range must be specified in UTC time, which is independent of the current time zone. |
| Parameter checking | Parameter checking is limited. For the table and company parameters, only the data type is checked. So if you specify non-existing tables or companies, the aud.select.transactions() function may succeed, but no data will be selected. Also if you use tables for which auditing is not on, you will not notice this, except for the lack of transactions being retrieved. For the selection.criteria, if the string can be parsed, the function will succeed, without checking the semantics. So you can for example specify selection.criteria like "#USER# < 'John' and #USER# = 'Mary'". |

## Example of a selection.criteria string
```

long    my.nr.tables
string  my.tables(8, 3)
long    my.companies(3)
long    my.selection.id
long    retval
my.nr.tables = 3
my.tables(1,1) = "tdsls400" | sales order headers
my.companies(1) = 200
my.tables(1,2) = "tdsls401" | sales order lines
my.companies(2) = 200
my.tables(1,3) = "tcibd001" | general item data
my.companies(3) = 100
retval = aud.select.transactions(my.nr.tables, my.tables, my.companies,
    "#TRANSID# > '12345678901234567890' and #USER# in {'John', 'Mary'}",
    my.selection.id)
```

## Related topics
- [Audit management overview](audit_management_overview.md)

- [Audit management synopsis](audit_management_synopsis.md)

- [Audit management examples](audit_management_examples.md)
