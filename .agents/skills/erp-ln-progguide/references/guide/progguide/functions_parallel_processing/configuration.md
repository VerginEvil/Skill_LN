# Parallel Application Processing Configuration
Whether or not an application (which is designed for Parallel Processing), will actually use this feature must be configured at deployment time. For the existing Parallel Processing mechanism, configuration must be done using session "Performance Boosters (tcmcs0597m000)". This configuration information is stored in table "tcmcs097" and can be retrieved using DLL the function "tcmcs.dll0011.read.number.of.servers()". For the new API a new configuration mechanism is implemented. This mechanism is comparable with the existing mechanism in package "tc" but now implemented in "tt". This configuration information will be stored in table "ttaad720" and the related session is "Parallel Processing Configuration (ttaad7520m000)".

## Environment Variables
The following environment variables can be set in the client Bshell which influence the Parallel Bshell functionality

- DS_AS – see section [Parallel Application Processing Debugging](debugging.md)

- TRACEPARBSHELL – see section [Parallel Application Processing Tracing](tracing.md)

- PAR_STARTUP_TIMEOUT – Specifies the time the client waits for the first response from the server after startup (in seconds). The default value is 120 (2 minutes). In the old API this was variable COMDLL0200_STARTUP_TIMEOUT

## Server Start Options
Each server can be started with special options. E.g. one wants to trace some activities of only one server. This mechanism is identical to the mechanism used with the existing parallel Bshell functions.
These options can be written into the file $BSE/lib/defaults/opt.server.{logname}. When this file is not present the system will search for the file $BSE/lib/defaults/opt.server. When one of these files is present the content will be read. The creation of this file should be done by a system administrator or by software that has permissions to write this file. This file should be written before the function par.client.start.servers() is called.
An example of an option: -set ENVVAR_X=VALUE
Here, the environ variable ENVVAR_X will be set while starting a server. Normally each option is valid for all servers to be started. But an option can also be set for each individual server. In this case each line should start with %XXX where XXX is the server number in format '999'. So, %005-set ENVVAR_X=VALUE is only for server number 5. Another feature is the characters $$$. When these 3 chars are present in an option line, they will be replaced by the server number. So, -set ENVVAR_X=VALUE$$$ will become in server 4: -set ENVVAR_X=VALUE004.

## Related topics
- [Parallel Application Processing Overview](overview.md)

- [Parallel Application Processing synopsis](synopsis.md)
