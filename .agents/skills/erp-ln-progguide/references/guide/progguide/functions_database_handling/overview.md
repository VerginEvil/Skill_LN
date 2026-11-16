# Database handling overview
Infor Enterprise Server data is stored in a relational database, which is managed by a Relational Database Management System (RDBMS). The RDBMS acts as the database server for Infor Enterprise Server applications. The RDBMS products supported by Infor Enterprise Server can be found in the platform support matrix.
The Infor Enterprise Server architecture includes a database driver. This provides the application server (that is, the bshell) with a common interface to the database server, regardless of which RDBMS product is used. This enables the application server to be database independent. The database driver is responsible for translating database commands received from the application server into RDBMS-specific commands. Although, the database driver's interface with the application server is the same for all RDBMS products, its interface with the RDBMS is RDBMS-specific. Therefore, there is a separate database driver for each of the supported RDBMS products.

## Database tables
A relational database presents information to the user in the form of *tables*. In a table, data is organized in columns and rows. Each column (also referred to as a field) represents a category of data. Each row (also referred to as a record) represents a unique instance of data for the categories defined by the columns.
A field always refers to a domain, which defines a set of values from which one or more fields can draw their actual values. For example, the 'tcweek' domain is the set of all integers greater than zero and less than or equal to 53.

## Primary keys
Every database table has a field, or a combination of fields, which uniquely identify each record in the table. This unique identifier is referred to as the *primary key*. Primary keys are fundamental to database operations, as they provide the only record-level addressing mechanism in the relational model. Primary keys act as references to the records in a table.

## Relationships/references
With a relational database, you can store data across multiple tables and you can define relationships between the tables. This means that individual tables can be kept small and data redundancy can be minimized. A relationship exists between two tables when they have one or more fields in common. So, for example, a Customer Details table can be linked to an Orders table by including a Customer ID field in both tables. In the Customer Details table, the Customer ID field is the primary key. In the Orders table, it is referred to as a foreign key. By linking the two tables in this way, there is no need for the Orders table to include customer details such as name and address. Note that references from one table to another must always use the primary key.

## Combined fields
A *combined field* is a field that consists of two or more child fields. You can use combined fields as primary keys, and you can also use them for references and indexes.

## Indexes
*Indexes* facilitate speedy searching and sorting of database tables. An index is a special kind of file (or part of a file) in which each entry consists of two values, a data value and a pointer. The data value is a value for some field in the indexed table. The pointer identifies the record that contains this value in the particular field. This is analogous to a conventional book index, where the index consists of entries with pointers (the page numbers) that facilitate the retrieval of information from the body of the book.
Note that it is also possible to construct an index based on the values of a combination of two or more fields.
Every table must have at least one index, which is an index on the primary key field(s). This is referred to as the primary index. An index on any other field(s) is referred to as a secondary index.

## Structured Query Language (SQL)
Infor Enterprise Server SQL is the database query language that you use to access data in the database tables. Using Infor Enterprise Server SQL, you can construct queries to retrieve specific data from the database. The syntax and usage of Infor Enterprise Server SQL is discussed fully in the section [Infor Enterprise Server SQL](baan_sql.md).

## Naming conventions
The naming syntax for tables, record buffers, and table fields is as follows:
```

tppmmmxxx           | table
rcd.tppmmmxxx       | record buffer of table
ppmmmxxx.ffffffff   | logical field of table
```
where *t* stands for table, *pp* is the package code, *mmm* is the module code, *xxx* is the tablenumber (range 000 to 999), and *ffffffff* is a field name (maximum 8 alphanumeric characters, starting with an alphabetic character).

## Using tables in program scripts
If a table is used in a script it must be declared with the following statement:
```

table tppmmmxxx
```
Declaration of a table implies declaration of all its fields and its record buffer. It is not necessary to declare these separately.
There are no special functions for opening and closing tables. A table is automatically opened at the first database call on that table and it is automatically closed at the end of the session.
You can use the record buffer of a table to save the contents of a record in a temporary string. And you can subsequently restore the record from the buffer. If a record contains numeric fields, you can only save and restore records. You cannot perform any other actions on the temporary string, as the presence of NULL characters will cause loss of data.

## Data types
The data type is the internal representation of table field and domain data. The following data types are available.
| |
|---|
| DB.BYTE |
| DB.ENUM |
| |
|---|
| DB.INTEGER |
| |
|---|
| DB.LONG |
| DB.BITSET |
| DB.DATE |
| DB.MAIL |
| DB.TEXT |
| |
|---|
| DB.TIME |
| |
|---|
| DB.FLOAT |
| |
|---|
| DB.DOUBLE |
| |
|---|
| DB.STRING |
| |
|---|
| DB.MULTIBYTE |
| |
|---|
| DB.COMBINED |

## Related topics
- [Transaction handling](transaction_handling.md)

- [Locking](locking.md)

- [Retry points](retry_points.md)

- [Error handling](error_handling.md)

- [Hints for using SQL](hints_for_using_sql.md)

- [Hints for using db.retry.point](hints_for_using_db.retry.point.md)

- [Infor Enterprise Server SQL](baan_sql.md)
