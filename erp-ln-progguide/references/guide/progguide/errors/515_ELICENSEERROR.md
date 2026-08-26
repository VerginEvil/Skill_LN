# 515 ELICENSEERROR - License error or corrupt shared memory
| |
|---|
| *Description:* |
| This error can indicate: That you are trying to use a binary, for example, a database that is not validated. That the shared memory is corrupt.  |
| *Solution:* |
| This problem can be solved in different ways, depending on the following situations: If the error occurred in an existing company, of which you did not change the database, you must extend your license. If you are trying to change a company's database, you are not allowed to use this particular database. Go back to the old situation or contact Infor to validate the new database. If you are trying to set up a new company, and you assigned the company to this database, you must change the database for the new company, or contact Infor to validate the new database. If the shared memory is corrupt, notify all LN users to quit LN and then run LN's *rc.stop* program and *rc.start* program.  |
-
-
-
-
-
