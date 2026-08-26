# eMessage Connector overview
The Infor LN eMessage Connector provides a developer with a set of functions that can be used in application scripts to enable:
- An Infor LN user to send a message (email) with the help of Microsoft Outlook mail client. This is not supported when using LN UI
- An Infor LN Application to send a message without any user assistance.    The Infor LN eMessage Connector is defined between a Baan messaging-enabled application and one or more providers. A provider is a third party software package. The Infor LN eMessage Connector environment is depicted in the figure shown above.
The Infor LN eMessage Connector relies on the following Infor Enterprise Server products:
- Baan Virtual Machine (Bshell)
- Baan User Interfaces (BW or WebUI).
- Baan 4GL Development tools  The Infor LN eMessage Connector has a relationship with the underlying provider. Examples of providers which could be supported are:
- Microsoft Exchange
- SMTP based provider  The Infor LN eMessage Connector has a relationship with external messaging clients. Examples of external messaging clients are:
- Microsoft Outlook

## Architecture

## Component descriptions

## 4GL Process
The 4GL process represents any Baan 4GL process which needs to communicate with another process which is not located in the same Baan Virtual Machine (BVM). This external process is usually a third party messaging based software (eg. Microsoft Outlook). This 4GL process can be sending messages to an external process, processing incoming messages or both.

## Infor LN eMessage Connector DLL
The Infor LN eMessage Connector DLL is a 4GL DLL which can be used by any Baan process to create, send and receive message objects. Baan processes wishing to use the Infor LN eMessage Connector must utilize this DLL. The DLL contains functions for the creation, examination and transport of message objects. The Infor LN eMessage Connector DLL accesses the Infor LN eMessage Connector Repository to determine the available message types and connectors to handle those message types. When a Baan process wishes to send a message, the Baan eMessage Connector DLL examines the repository to determine the appropriate connector needed to handle the message and starts it.
This dll can be linked to a script by adding the following line:
```

#include <bic_cmf>
```

## Baan eMessage Connector
The Baan eMessage Connector acts as the intermediary between the 4GL process and the provider. When started it examines the Infor LN eMessage Connector Repository to determine how to connect to the external provider and establishes a connection. From then on it handles the transport of the message objects between the 4GL process and the external provider. It also performs message logging. All messages passing through the connector are logged to the Infor LN eMessage Connector Repository log table and the individual message parts are stored in the file system. This ensures traceability. The storage of message objects as files is also important for Baan 4GL applications. The Baan 4GL does not allow the allocation of large memory areas for processing BLOBs (Binary Large Objects) and other large objects. The message log therefore allows the Baan applications to digest these large files in smaller chunks (by reading them from the file system in small pieces).

## Infor LN eMessage Connector Repository
The repository stores several types of information about the Baan eMessage Connector environment.
- Infor LN eMessage Connector services which are supported (email, fax, EDI, SMS, Baan, etc)
- Message types supported per service (SMTP, SMS, fax, telex, etc)
- Infor LN eMessage Connector Service providers ( Outlook, SMTP, etc)
- Message Logs

## Outbound Message Handling
A number of steps must be executed in order for a Baan process to send a message to a provider. First, the Baan process creates the message using the Infor LN eMessage Connector DLL functions. Next the Baan process instructs the Baan eMessage Connector DLL to send the message using a particular service. A Baan eMessage Connector Service is associated with a connector which provides the actual service. The Infor LN eMessage Connector DLL accesses the Infor LN eMessage Connector repository to determine the appropriate connector to be used to process the message object. This connector is then started and the message object passed to it. The connector accesses the Infor LN eMessage Connector repository to determine the appropriate parameters to be used to connect to the provider. Connection is established to the provider and the message sent. The appropriate message logging is also performed.

## Inbound Message Handling
Inbound message handling involves invoking the appropriate connector and having it wait for messages with a particular address. The startup parameters specify the messages the connector should handle. The connector is always started by a 4GL message enabled application. Command line invocation can be achieved by using the 4GL application as a parameter to the bshell on startup. Incoming messages are sent via BMS to the 4GL process which started the connector. The connector can also be started in inbound message handling mode from a currently running BVM. It is not necessary (but seems more practical) to start it from the OS command line.
Note: Inbound message handling is not yet implemented.

## Related topics
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
