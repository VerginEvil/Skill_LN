# Application Response Time Measurement (ARTM) Overview
The ARTM functions can be used by the application developer to monitor the performance of transactions. The actual monitoring is done by an external application.
ARTM is designed for system administrators to monitor the overall user response time of the whole Infor Enterprise Server system, as well as to monitor specific functionality within a specific application. The data can be analyzed later on.
ARTM helps the IT manager to meet their service level agreement and helps the system administrator to detect slow responses to users and find the bottlenecks in an installed Baan system.
ARTM is not a tracing system that generates huge amounts of data. The information provided by ARTM must be kept to a minimum to give the system administrator a quick overview about the responsiveness of the system.
This implies that transactions should be implemented on a high level, starting when a user action begins, and ending when the user action is finished.
Transactions can be implemented in 4GL UI-script, the DAL script as well as 3GL applications. They may be nested.
For more details, see the Application Response Measurement API guide, located at http://www.cmg.org/regions/cmgarmw/marcarm.html

## Related topics
- [Application Response Time Measurement (ARTM) Synopsis](artm_synopsis.md)
- [Application Response Time Measurement (ARTM) Error Codes](artm_error_codes.md)
- [Application Response Time Measurement (ARTM) Debugging](artm_debugging.md)
- [Application Response Time Measurement (ARTM) Examples](artm_examples.md)
