# Database Change Management (DBCM) error codes
Several DBCM functions return specific error codes in an error situation, or they set the predefined variable *e* to a certain value. In the table below these error codes are mentioned.
| | |
|---|---|
| Code | Value |
| `cDbcm_NoError` | 0 |
| `cDbcm_IncorrectLength` | 1 |
| `cDbcm_IncorrectType` | 2 |
| `cDbcm_IncorrectDepth` | 3 |
| `cDbcm_IncorrectChecksum` | 4 |
| `cDbcm_NoDeployment` | 5 |
| `cDbcm_NoModel` | 6 |
| `cDbcm_UnknownTable` | 7 |
| `cDbcm_BufferTooSmall` | 8 |
| `cDbcm_DllNotFound` | 9 |
| `cDbcm_FunctionNotFound` | 10 |
| `cDbcm_IncorrectReturnType` | 11 |
| `cDbcm_IncorrectArgumentCount` | 12 |
| `cDbcm_IncorrectArgumentType` | 13 |
| `cDbcm_IncorrectObjectId` | 14 |
| `cDbcm_UndeployedType` | 15 |
| `cDbcm_EnumerationAborted` | 16 |
| `cDbcm_DatabaseErrorBeforeCallbacks` | 17 |
| `cDbcm_DatabaseErrorBeforeCallback` | 18 |
| `cDbcm_DatabaseErrorDuringCallback` | 19 |
| `cDbcm_DatabaseErrorAfterCallbacks` | 20 |
| `cDbcm_DatabaseErrorRemoveToid` | 21 F8) |
| `cDbcm_DatabaseUpdateCOBO` | 21 | FP9 and later |
| `cDbcm_InvalidType` | 22 |
| `cDbcm_ObjectNotCheckedOut` | 23 |
| `cDbcm_ObjectCheckedOutInOtherCompany` | 24 |

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
