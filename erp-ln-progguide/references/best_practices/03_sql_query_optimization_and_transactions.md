# SQL Query Optimization & Transaction Management Guide

> **Reference Documents**: [Baan SQL Reference](../sql/progguide/functions_database_handling/select_statement.md) | [Dev Tools Chapter 2: Software Components](../dev_tools/ch02_overview_of_software_components.md) | [Hints for using db.retry.point](../guide/progguide/functions_database_handling/hints_for_using_db.retry.point.md)  
> **Target Audience**: Infor LN Database Engineers, Backend Developers, and AI Coding Agents

---

## 1. Embedded Baan SQL: Syntax & Core Mechanics

Infor ERP LN uses **Embedded Baan SQL** executed within the bshell process. Queries interact with the database engine through cursor buffers bound directly to 4GL table variables.

### 1.1 The Canonical Query Structure

```baan
select  tdsls400.orno, tdsls400.sotp, tdsls400.odat
from    tdsls400
where   tdsls400.ofbp = :customer.code
    and tdsls400.hdst in (tdsls.hdst.created, tdsls.hdst.approved)
order by tdsls400._index2
selectdo
    |* Executed for every matching record fetched
    process_order(tdsls400.orno)
selectempty
    |* Executed if zero records matched the query
    handle_no_orders_found()
selecterror
    |* Executed if a database runtime error occurred
    log_sql_error()
selecteos
    |* Executed after the last record is fetched (End Of Selection)
    finalize_order_batch()
endselect
```

### 1.2 Binding & Variable Scope
- **Host Variables**: 4GL local/global variables must be prefixed with a colon (`:variable`) inside SQL statements.
- **Table Record Buffer**: Table columns (e.g. `tdsls400.orno`) are automatically bound to the session's active table buffer upon each `selectdo` cycle.
- **Column Projections**: Avoid `SELECT *` in performance-critical loops. Select only the columns required to reduce network bandwidth and memory overhead.

---

## 2. Index Alignment & Query Optimization Rules

The Infor LN query optimizer maps Embedded SQL queries onto native RDBMS queries (Oracle, MS SQL Server, DB2). To prevent costly full table scans (FTS), queries must align with table indices defined in the Data Dictionary.

### 2.1 The Index Leading Field Rule
An index is only utilized efficiently if the `WHERE` clause specifies **equality predicates (`=`)** on the **leading fields** of that index.

*Example*: Table `tdsls401` (Sales Order Lines) has `_index1` composed of `(orno, pono, sqnb)`.

| Query WHERE Clause | Index Used? | Performance Impact |
|---|---|---|
| `where tdsls401.orno = :orno and tdsls401.pono = :pono` | **YES** (`_index1`) | Instant index seek |
| `where tdsls401.orno = :orno` | **YES** (`_index1`) | High-speed range scan |
| `where tdsls401.pono = :pono` | **NO** (leading field missing) | Full table scan (Fatal for large tables!) |
| `where tdsls401.orno = :orno and tdsls401.item = :item` | **PARTIAL** | Index seek on `orno`, filter on `item` |

### 2.2 Explicit Index Hints (`order by <table>._index<N>`)
Specify the index explicitly in the `order by` clause when table size is large or when predictable execution plans are required:

```baan
select  tdsls400.*
from    tdsls400
where   tdsls400.cprj = :project.code
order by tdsls400._index4  |* Index 4 leading field is cprj
selectdo
    ...
endselect
```

### 2.3 Optimization Rules of Thumb:
1. **Never Wrap Indexed Columns in Expressions**: Writing `where toupper(tdsls400.orno) = :orno` disables index seeking. Keep columns naked.
2. **Beware Mismatched Domain Lengths**: Ensure host variables have identical domains/lengths as the database columns they compare against.
3. **Avoid Disjunctions (`OR`) Across Different Columns**: An `OR` condition spanning non-indexed columns forces the query optimizer to abandon indices and perform a table scan.

---

## 3. Cursor & Memory Management

### 3.1 Set-Oriented Array Fetching (`as set with <N> rows`)
By default, Baan SQL fetches records one at a time. Using set specifications reduces round-trip bshell-to-database latency and memory footprint.

#### Single-Record Lookups:
Always use `as set with 1 rows` when checking for existence or fetching a single unique record:

```baan
select  tccom100.nama
from    tccom100
where   tccom100.bpid = :bpid
as set with 1 rows
selectdo
    found.name = tccom100.nama
endselect
```

#### Prepared Sets for Concurrent Mutation:
If your loop modifies or deletes the table being queried, use `as prepared set` to prevent cursor corruption:

```baan
select  tdsls401.*
from    tdsls401 for update
where   tdsls401.orno = :order.no
as prepared set
selectdo
    db.delete(ttdsls401, db.retry)
endselect
```

### 3.2 Eliminating Nested N+1 Queries
**Anti-Pattern**: Fetching parent records in a `selectdo` loop and querying children inside the loop creates hundreds of round-trips.

```baan
|* POOR: N+1 nested cursor overhead
select tdsls400.orno from tdsls400 where tdsls400.sotp = "NOR" selectdo
    select tdsls401.item from tdsls401 where tdsls401.orno = :tdsls400.orno selectdo
        ...
    endselect
endselect

|* OPTIMAL: Single joined query
select  tdsls400.orno, tdsls401.pono, tdsls401.item
from    tdsls400, tdsls401
where   tdsls400.sotp = "NOR"
    and tdsls401.orno = tdsls400.orno
selectdo
    ...
endselect
```

---

## 4. Query Extensions in 4GL Sessions

In 4GL session scripts, dynamic filtering is achieved via `query.extend.*` functions without rewriting the base session queries.

```baan
before.program:
    |* Dynamically restrict session to current year's records
    query.extend.where("tdsls400.odat >= " & str$(date.to.utc(current_year, 1, 1, 0, 0, 0)))
    
    |* Join secondary table for display field
    query.extend.from("tccom100")
    query.extend.where("tccom100.bpid = tdsls400.ofbp")
    query.extend.select("tccom100.nama:customer_name")
```

---

## 5. Transaction Concurrency & Locking Architecture

Data consistency in Infor LN relies on strict transaction boundaries:
- `db.retry.point()`: Establishes a savepoint. If a lock conflict or transient failure occurs, execution rewinds to this point.
- `commit.transaction()`: Flushes all modified record buffers and releases locks.
- `abort.transaction()`: Reverts all uncommitted changes back to the last retry point.

### 5.1 The 4 Canonical Concurrency Patterns

#### Pattern 1: Commit Per Fetch (High Concurrency, Minimal Locks)
Used when processing large batches where each record is an independent atomic transaction:

```baan
db.retry.point()
select  tisfc001.*
from    tisfc001 for update
where   tisfc001.pdno inrange :pdno.f and :pdno.t
order by tisfc001._index1 with retry
selectdo
    tisfc001.proc = tcyesno.yes
    db.update(ttisfc001, db.retry)
    commit.transaction()
endselect
```

#### Pattern 2: Batch Commit Over Groups with `selecteos`
Used when committing per logical unit (e.g. per Sales Order) spanning multiple fetched rows:

```baan
save.orno = ""
db.retry.point()
select  tdsls401.*
from    tdsls401 for update
where   tdsls401.orno inrange :orno.f and :orno.t
order by tdsls401._index1 with retry repeat last row
selectdo
    if tdsls401.orno <> save.orno then
        if not isspace(save.orno) then
            commit.transaction()
        endif
        save.orno = tdsls401.orno
    endif
    
    tdsls401.stat = tdsls.stat.processed
    db.update(ttdsls401, db.retry)
selecteos
    |* Commit final order group
    commit.transaction()
endselect
```

#### Pattern 3: Strict Locking Window (`for update`)
Hold locks for the shortest time possible. Fetch read-only first, perform computations, and lock only immediately before updating:

```baan
|* 1. Read without lock
select  tdsls400.oamt, tdsls400.hdst
from    tdsls400
where   tdsls400.orno = :order.no
as set with 1 rows
selectdo
    new_amount = calculate_complex_rebate(tdsls400.oamt)
endselect

|* 2. Lock and update with minimal lock window
db.retry.point()
select  tdsls400.*
from    tdsls400 for update
where   tdsls400.orno = :order.no
as set with 1 rows
selectdo
    tdsls400.oamt = new_amount
    db.update(ttdsls400, db.retry)
    commit.transaction()
endselect
```

### 5.2 Deadlock Prevention Rules:
1. **Acquire Locks in Hierarchical Order**: Always lock parent before child (e.g., `tdsls400` header before `tdsls401` lines).
2. **Never Open a UI Session or User Dialog While Holding a Lock**: Holding records `for update` while waiting for user keyboard response will block other users and cause deadlocks.
3. **Always Match `db.retry.point()` with `commit.transaction()` / `abort.transaction()`**: An open transaction without a commit/abort will hold table locks until the bshell terminates.
