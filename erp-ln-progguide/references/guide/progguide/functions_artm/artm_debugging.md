# Application Response Time Measurement (ARTM) Debugging
The [bshell resource](../misc/bshell_resources.md) *art_trace* can be set for debugging the ARTM code in the application scripts. One can trace access and results of calling the loaded ARM shared library, supplied by third party or one can emulate results. The latter is useful for developing ARTM when no ARM shared libraries are avaiable. Trace information is written to $BSE/tmp/bshell.pid, unless overruled by -tracefile file option (see IBaanVM interface).
| | |
|---|---|
| 0 | Tracing disabled. |
| 1 | Tracing enabled for access to loaded ARM shared library. |
| 3 | Detailed tracing enabled for access to loaded ARM shared library. |
| 5 | Tracing enabled with emulation of ARM shared library via stubs. |
| 5 | The trace information is send to the file *$BSE/tmp/bshell.pid*.  |

## Related topics
- [Application Response Time Measurement (ARTM) Overview](artm_overview.md)
- [Application Response Time Measurement (ARTM) Synopsis](artm_synopsis.md)
- [Application Response Time Measurement (ARTM) Error Codes](artm_error_codes.md)
- [Application Response Time Measurement (ARTM) Examples](artm_examples.md)
- [Bshell resource "art_trace"](../misc/bshell_resources.md)
