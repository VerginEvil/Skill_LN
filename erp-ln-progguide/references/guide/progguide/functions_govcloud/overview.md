# GovCloud functions overview

## Introduction
This section describes functions related to the GovCloud, security and FIPS-140-2 related features and limitations. In a secure environment, SSL (Secure Socket Layer) connections are forced between LN-UI and the bshell, and between bshells that use sockets to communicate with other bshells.
FIPS mode excludes the use of certain older cryptographic functions to guarantee a decent level of security. True FIPS requirements also force a FIPS-certified implementation of the cryptographic functions.
The portingset has two resources to configure security: fips_140_mode and ssl. See the technical reference guide for details.

## Functions to detect GovCloud mode
A function called [in.fips.mode()](in.fips.mode.md) is available for the 3GL/4GL programmer to determine the FIPS mode of the PortingSet.
A function called [ssl.mode()](ssl.mode.md) is available for the 3GL/4GL programmer to determine the SSL mode of the Portingset.

## Functions for secure communications
The sock.listen.ssl() and sock.connect.ssl() can be used to establish secure connections between bshells.

## Related topics
- [GovCloud functions synopsis](synopsis.md)

- [GovCloud and FIPS-140-2 Coding Standards and Examples](examples.md)
