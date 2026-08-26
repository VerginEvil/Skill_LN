# ssl.mode()

## Syntax:
`function string ssl.mode( )`

## Description
This is a function to determine whether the bshell runs in SSL mode, and if so, which. When runing in GovCloud mode, both FIPS and SSL mode are turned on. But a system administrator can also decide to turn SSL mode on outside of a GovCloud environment, using the "ssl" resource in the lib/defaults/bootstrap resource file. This works on all operating systems and environments.
When SSL mode is on, SSL (Secure Socket Layer) communication is enforced between the LN-UI and the bshell, and between bshells that use sockets to communicate to other bshells (using sock.start.process()). This protects data transmitted over the network from eavesdropping and tampering.
This function can be used to find out what minimum level of security is in use. It returns a string.

## Return values
| | |
|---|---|
| off | Bshell does not have SSL security on. Network traffic is unencrypted. This is the default for non GovCloud environments.  |
| on | Bshell has default SSL security turned on. It is up to the cryptographic library in use by the bshell to negotiate a default protocol that is considered sufficient by both ends of the link. As long as some form of SSL is negotiated, the connection will succeed.  |
| tlsv1.1 | The security level is downgraded so (old) TLSv1.1 connections are acceptable. Many modern installations will insist on using at least level TLSv1.2, using this setting may be required to communicate with older installations. During negotiations, a higher level of security may be decided upon.  |
| tlsv1.2 | The security level is set to so TLSv1.2 as minimum, TLSv1.1 on either end will result in a failure to connect. This is the default level for GovCloud environments.  |
| tlsv1.3 | The security level is set to so TLSv1.3 as minimum, TLSv1.1 or v1.2 on either end will result in a failure to connect. At the time of writing (July 2020) many systems do not support v1.3 yet, but WolfSSL based bshells do.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2370.

## Related topics
- [GovCloud functions overview](overview.md)
- [GovCloud functions synopsis](synopsis.md)
