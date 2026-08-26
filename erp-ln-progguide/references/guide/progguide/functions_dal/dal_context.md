# DAL Context

## Overview
The Data Access Layer can be used in different contexts. E.g. it can be used by the 4GL engine in a more or less interactive mode. But it can also be used in a process session or the Business Object Layer (BOL). Depending on whether the Data Access Layer is used by the 4GL engine or a BOL, the Data Access Layer has to behave slightly different. This is why the concept of a DAL context has been introduced.
A DAL runs in one of the following contexts:
- Data Input
- Data Check
- Process
- Integration
| | |
|---|---|
| Context | Explanation |
| Data Input |  This context is set by the 4GL engine when an end-user is entering data on a form. The Data Access Layer will: - Provide error messages that are focussed to the end-user. - Check derived fields whether they may be changed by the end-user.  |
| Data Check |  This context is set by the 4GL engine when an end-user does an action, like pressing save or executing a form command. The Data Access Layer will: - Provide error messages that are focussed to the end-user. - Not check any derived fields so that the application can assign values to these fields.  |
| Process |  This context is the default context. It is used for process and print sessions, but also for 3GL programs. The Data Access Layer will: - Provide error messages that are better suited to be printed on a report. - Not check any derived fields so that the application can assign values to these fields.  |
| Integration |  This context is set when the DAL is used via the BOL. The Data Access Layer will: - Provide error messages that are better suited to be printed on a report. - Check derived fields whether they may be changed by the end-user.  |
The current context can be retrieved by function [dal.get.context()](../functions_db_operations/dal.get.context.md).
