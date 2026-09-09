# Application locks: overview
Use these functions to handle application locks for 4GL processes.
You use application locks to prevent other applications and users from reading and/or modifying an application's data during critical operations. For example, to prevent access to data when it is being updated.
You can set an application lock only for the current 4GL process. You can test for or delete an application lock only within the application to which it applies.

## Application lock features
- Each application lock has an owner, which is automatically assigned. The owner consists of a combination of the login ID of the application user, and the process ID of the application.

- Each application lock has a unique name, which you define when you create the lock.

- An application lock is automatically removed when the application ends. You can also remove it with the *appl.delete()* function.

- An application lock applies only to an application and that application's data. It is not part of the RDBMS and is not linked to a table or a particular database transaction. To set table locks, use [db.lock.table()](../functions_db_operations/db.lock.table.md).

## Application lock types
There are three main types of application locks:

- *Read locks* When you set a read lock, the owner of that lock has only read access to the application's data. Other applications can read and modify the data. Other users of the application can set read and write locks on it. But they cannot set an exclusive application lock.Each application can have several read-type application locks.

- *Write locks* When you set a write lock, the owner of that lock has both read and write access to the application's data. Other applications can read the data but not modify it. Other users of the application can set read locks on it, but not a write lock or an exclusive lock.Each application can have only one write-type application lock. So you cannot set this type of lock when there is a write-type or exclusive-type lock already present.

- *Exclusive locks* When you set an exclusive lock, the owner of that lock has exclusive access to the application's data. Other applications and users can neither read nor modify the data, nor can they set any application locks on it.You can set an exclusive lock only when there are no other locks (of any type) already present.

There is one additional lock type, which you can combine with any of the other types:

- *Application-wide locks* Normally, an application lock is set for the current company only. By using this additional lock mode, you can apply the lock globally to all companies. This means that the application lock is valid in all companies.

## Related topics
- [Application locks: synopsis](application_locks_synopsis.md)
