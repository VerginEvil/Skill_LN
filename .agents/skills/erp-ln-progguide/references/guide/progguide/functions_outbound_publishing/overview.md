# Outbound Publishing functions overview

## Overview
Use the event manager publishing functions to publish XML messages. The functions are used by first invoking the publish.open(), then invoking publish.message() one or more times, and finally invoking publish.close(). If a message could not be built successfully, publish.error.message() can be used instead of publish.message(). It is mandatory to use publish.close() after a successful publish.open().
Each of the functions has a reference parameter result.xml. If the function returns an error value, result.xml contains the details for the error. Otherwise result.xml will be empty (0). Important: if result.xml is filled, it must be cleaned up afterwards using
xmlDelete().
The xml tree is formatted in accordance with the standard result message.
Publishing is done by invoking the OpenWorld Adapter. If the OpenWorld Adapter is unavailable, the functions will return an error. In most cases, the implementation of the publishing functions will invoke an error handler instead of returning the error. In that case the return value will not indicate an error, and no result XML is provided.

## Related topic
- [Outbound Publishing functions synopsis](synopsis.md)
