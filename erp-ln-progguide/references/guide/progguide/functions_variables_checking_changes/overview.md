# Variables (checking changes) overview
These functions provide a mechanism for checking changes to variables. The variables can be of type string, long, double, domain, or array.
You start the mechanism for a particular variable by calling [on.change.check()](on.change.check.md). The current value of the variable becomes the checkpoint value for the checking mechanism. The variable is considered to have changed if its value differs from the checkpoint value. Using the checking mechanism slows down program execution.
Note that the report writer also uses these functions. And use of the functions in a report script can have unpredictable results.

## Related topics
- [Variables (checking changes) synopsis](synopsis.md)
- [Variables (checking changes): sample program](example.md)
