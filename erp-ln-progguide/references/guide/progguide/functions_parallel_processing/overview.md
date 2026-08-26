# Parallel Application Processing Overview
Parallel processing is used to spread workload of a certain functionality over multiple application servers (bshells). The aim of parallel processing is to reduce the throughput time (total duration) of batch sessions. It will utilize the full system power. The performance of a parallel application is not in linear proportion to the number of CPUs in a system. Because the scalability depends on many factors, one cannot give a formula to determine the optimal number of servers. The optimal number of servers must be determined by practical experience.

## Technique
Parallel processing can be used by an application by including <bic_parallel>. This include will make sure that the library "ottstppardll" is used. Communication between client and server bshells is based upon TCP/IP sockets.

## History
This functionality supersedes the "Parallel Application Processing" functionality which is implemented in "tccomdll0200". This implementation has some drawbacks with respect to stability. The main factors which make the parallel processing implementation in tccomdll0200 instable are:
- Based on message queues (on Unix) and Mail slots (Windows). Both technologies are not self cleaning. So when a process which creates/owns these objects exits abnormally, these objects are not automatically removed
- Messages placed in message queues are limited in size.
- Using timers to check whether all participants are still alive. When the system is very busy, timeouts might occur, which are unjustified. Also when the system clock is not stable (e.g. moved back or forth because of a time synchronization), incorrect timeouts can occur.   This new implementation of parallel processing is not replacing the existing functionality but can live side by side with the existing parallel processing functionality.
In the section [Parallel Application Processing Cross Reference](crossreference.md) a table is shown which can be used to migrate an application from the existing parallel processing implementation to the new implementation.

## Topology
In the next figure a general topology for parallel processing is shown.
One client can define one or more server groups. Within each server group, one or more bshells can be running. All bshells in a server group must run the same server session. A client session can send messages to a server group or to a specific server. A message usually represents a request to a server to perform a portion of work. When a message is sent to a server group, it will be dispatched to a session within this group which is currently free. When there is currently no free server, the send function will wait until a server becomes ready. A message can also be sent to a specific server session within a group. When this server is currently busy, the send function will wait until this specific server becomes ready.
A server session can optionally send some data back to the client session. In the client session a specific get.message call must be programmed to handle this response data.
Optionally a server session can send requests to a dedicated support session in the client. This can be useful for a central handling of first free numbers to prevent contention on a single table from several servers.

## Related topics
- [Parallel Application Processing Configuration](configuration.md)
- [Parallel Application Processing Debugging](debugging.md)
- [Parallel Application Processing Tracing](tracing.md)
- [Parallel Application Processing Cross Reference](crossreference.md)
- [Sequence Diagrams](sequence.md)
- [Parallel Application Processing Database Retries](retries.md)
- [Parallel Application Processing synopsis](synopsis.md)
- [Parallel Application Processing Examples](examples.md)
