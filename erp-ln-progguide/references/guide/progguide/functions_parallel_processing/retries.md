# Parallel Application Processing Database Retries
The functions par.server.retry.point() and par.server.retry.hit() are meant to report excessive database retries in the server back to the client. If MAX_RETRY is set to 10 (this is default), only a maximum of 9 retries will be done per server. When this is reached by one of the servers, that specific server sends an abort message to the client, which stops all servers and the communication. Next example shows a fragment of the source code of a the server process which uses these functions.
```

par.server.retry.point()
db.retry.point()
if db.retry.hit() then
   par.server.retry.hit()
endif
```

## Related topics
- [Parallel Application Processing Overview](overview.md)

- [Parallel Application Processing synopsis](synopsis.md)
