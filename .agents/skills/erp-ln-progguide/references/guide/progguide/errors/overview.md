# Infor ES errors and messages
This section describes the Infor ES error and informational messages that can occur. There are several categories of errors:

- Errors that are raised by the Operating System. These values are shown as the 'errno' and/or 'lasterror' values in the generated log message. The value and the meaning of these errors are Operating System specific. Consult the OS vendor documentation for more information regarding a specific error number value. Examples of such errors are: OS resource errors, permission errors, network errors e.t.c.

- Errors that are related to the database. These values are shown as the 'bdberrno' value in the generated log messages. Error numbers below 1000 are related to the portingset database layer, or native database errors that are mapped to generic porting set database errors, e.g. EDBNOTON (=510). An error code of 1000 and above indicates a native error of the database. The value and the meaning of these errors are database specific. To get the actual error code of the database involved, subtract 1000 from the error number. Example: bdberrno=1604 is database error 604. Please consult the RDBMS vendor's documentation for more information.

Errors can be fatal, a warning or informative messages. Messages are typically logged in $BSE/log (on UNIX) or Event Viewer (Windows). When messages are logged to a file, then each application has its own log file (e.g. log.bdbpost). In general, an error value of 0 means no error/success.
