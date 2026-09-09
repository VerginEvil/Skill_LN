# Substitute session sample program
```

    #pragma used dll "ottstpsubstproc"

  function extern switch.to.other.session()       | called by Form Command
  {
    static long other.pid

    if other.pid = 0 then
    other.pid = parent  | we don't know whether this process is activated first or
                | that the other process has activated this one. In the
                | first case, the session codes (of parent session and session
                | to be started) do not match and so the session is started.
                | In the latter case, the session codes do match and so the
                | other session is reactivated.
    endif

    other.pid = substitute.session(pid, "ppmmmssssm000", other.pid)
  }
```

## Related topics
- [Substitute session overview](overview.md)

- [Synchronized sessions synopsis](synopsis.md)
