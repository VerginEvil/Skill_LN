# Database errors
The database errors are the bdb_errno errors generated. The numbers below 1000 are specific to the portingset database layer. The others are native to the RDBMS. To get the actual error code of the RDBMS involved, subtract 1000 from the error number.
The portingset database layer error messages are:
| |
|---|
| [100 EDUPL - Duplicate Record](100_EDUPL.md) |
| [101 ENOTOPEN - Table is not open](101_ENOTOPEN.md) |
| [102 EBADARG - Illegal argument](102_EBADARG.md) |
| [103 EBADKEY - Illegal key description](103_EBADKEY.md) |
| [106 ENOTEXCL - Non-exclusive access](106_ENOTEXCL.md) |
| [107 ELOCKED - Record locked](107_ELOCKED.md) |
| [108 EKEXISTS - Key already exists](108_EKEXISTS.md) |
| [109 EPRIMKEY - Key does not exist](109_EPRIMKEY.md) |
| [110 EENDFILE - End/begin of file](110_EENDFILE.md) |
| [111 ENOREC - No record found](111_ENOREC.md) |
| [112 ENOCURR - No current record](112_ENOCURR.md) |
| [113 EFLOCKED - Table locked](113_EFLOCKED.md) |
| [114 EFNAME - Index could not be created](114_EFNAME.md) |
| [126 EDEADLOCKVICTIM - Transaction is aborted due to deadlock](126_EDEADLOCKVICTIM.md) |
| [201 EROWCHANGED - Row changed by other user](201_EROWCHANGED.md) |
| [203 ETRANSACTIONON - Transaction is on](203_ETRANSACTIONON.md) |
| [204 EISREADONLY - Transaction is read-only](204_EISREADONLY.md) |
| [205 ENOTINRANGE - Value is out of range](205_ENOTINRANGE.md) |
| [206 ENOTLOCKED - Record not locked](206_ENOTLOCKED.md) |
| [207 EAUDIT - Error of audit trailer](207_EAUDIT.md) |
| [208 EPERMISSION - Permission denied](208_EPERMISSION.md) |
| [209 EMIRROR - Mirroring error](209_EMIRROR.md) |
| [210 EMLOCKED - Record in mirroring is locked](210_EMLOCKED.md) |
| [213 ETRANSACTIONOPEN - Transaction is started, but not updated](213_ETRANSACTIONOPEN.md) |
| [214 EUNALLOWEDCOMPNR - Operation not allowed for a logical company](214_EUNALLOWEDCOMPNR.md) |
| [215 EDBDILLEGAL - Illegal internal condition](215_EDBDILLEGAL.md) |
| [217 ECORRUPTROLE - Role file is corrupt](217_ECORRUPTROLE.md) |
| [251 EAUDSETUP - Incorrect audit server setup](251_EAUDSETUP.md) |
| [252 EAUDCORRUPT - An audit file is corrupt](252_EAUDCORRUPT.md) |
| [253 EAUDLOCKED - An audit file is locked](253_EAUDLOCKED.md) |
| [254 EAUDABORT - Commit transaction on the audit server has failed.](254_EAUDABORT.md) |
| [299 EEXTENSIONHOOKERROR - Error raised by hook in extension](299_EEXTENSIONHOOKERROR.md) |
| [301 ESQLQUERY - SQL query failed](301_ESQLQUERY.md) |
| [302 ESQLSYNTAX - Syntax error in SQL statement](302_ESQLSYNTAX.md) |
| [303 ESQLREFER - SQL reference not found](303_ESQLREFER.md) |
| [304 ESQLUNDEFINED - Undefined SQL error.](304_ESQLUNDEFINED.md) |
| [306 ESQLDIVBYZERO - Division by zero](306_ESQLDIVBYZERO.md) |
| [307 ESQLSTRINGTRUNCATION - SQL String truncation](307_ESQLSTRINGTRUNCATION.md) |
| [308 ESQLINDEXOUTOFDIMS - Array column index out of range](308_ESQLINDEXOUTOFDIMS.md) |
| [309 ESQLSUBSTRINGERROR - SQL invalid substring length](309_ESQLSUBSTRINGERROR.md) |
| [310 ESQLCARDINALITYVIOLATION - SQL subquery (with comparison) returns more than 1 row](310_ESQLWRONGROW.md) |
| [311 ESQLFILEIO - SQL file i/o error](311_ESQLFILEIO.md) |
| [312 ESQLINVALIDPARAMETERTYPE - SQL Invalid parameter type](312_ESQLINVALIDPARAMETERTYPE.md) |
| [319 ESQLINVALIDESCCHAR - Invalid escape character](319_ESQLINVALIDESCCHAR.md) |
| [325 ESQLINVALIDESCSEQ - Invalid escape sequence](325_ESQLINVALIDESCSEQ.md) |
| [401 EBADFILEFMT - Bad file format](401_EBADFILEFMT.md) |
| [402 ECONFIG - Configuration error](402_ECONFIG.md) |
| [501 EMEMORY - Internal memory error](501_EMEMORY.md) |
| [502 EBDBON - User already logged in to database](502_EBDBON.md) |
| [503 EBADADRS - Illegal address](503_EBADADRS.md) |
| [504 EBADFLD - Bad column](504_EBADFLD.md) |
| [505 ENOSERVER - Server not available](505_ENOSERVER.md) |
| [506 ENOTABLE - Table does not exist](506_ENOTABLE.md) |
| [507 ETABLEEXIST - Table already exists](507_ETABLEEXIST.md) |
| [508 EBDBNOTON - Not logged on to a database](508_EBDBNOTON.md) |
| [509 EBADCURSOR - Bad cursor](509_EBADCURSOR.md) |
| [510 EDBNOTON - Database not on](510_EDBNOTON.md) |
| [511 EWRONGVERSION - Wrong databasedriver version.](511_EWRONGVERSION.md) |
| [512 EDDCORRUPT - Incorrect table definition](512_EDDCORRUPT.md) |
| [513 ENODD - Table definition not found](513_ENODD.md) |
| [514 ESECURITY - No permission](514_ESECURITY.md) |
| [515 ELICENSEERROR - License error or corrupt shared memory](515_ELICENSEERROR.md) |
| [517 EDELAYED - General error for delayed locking](517_EDELAYED.md) |
| [518 ENOSESSION - No valid session code](518_ENOSESSION.md) |
| [519 ENOCOMPNR - No valid company number](519_ENOCOMPNR.md) |
| [520 EBUFUPD - Buffered update failed](520_EBUFUPD.md) |
| [521 ENOSHM - No shared memory](521_ENOSHM.md) |
| [522 EBDBDBCONNECTIONLOST - Connection to the database has been lost](522_EBDBDBCONNECTIONLOST.md) |
| [523 EFULL - Database is full](523_EFULL.md) |
| [540 EDBLOGONDENIED - Database logon denied](540_EDBLOGONDENIED.md) |
| [600 EREFERENCE - Reference error](600_EREFERENCE.md) |
| [601 EREFLOCKED - Reference table locked](601_EREFLOCKED.md) |
| [602 EUNDEFREF - Undefined reference](602_EUNDEFREF.md) |
| [604 EREFUPDATE - Reference not updated](604_EREFUPDATE.md) |
| [605 EREFEXISTS - Delete failed due to reference](605_EREFEXISTS.md) |
| [606 EREFNOTEXISTS - Reference does not exist](606_EREFNOTEXISTS.md) |
| [607 ENOREFTBL - Reference table not found](607_ENOREFTBL.md) |
| [700 ESETLOCALE - Failed to set locale](700_ESETLOCALE.md) |
| [850 EABORT - Transaction aborted](850_EABORTON.md) |
