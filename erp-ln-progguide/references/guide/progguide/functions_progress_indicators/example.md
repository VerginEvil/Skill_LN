# Progress indicators sample program
```

#include <bic_dam>

function process.elements()
{
        long    i
        long    n
        long    ret
        long	progr
        boolean	exists

        | If the calling process has already a progress indicator
        | created then reuse that indicator. If not then create a new one.

        | Check whether the progress indicator is already created
        exists = progress.indicator.exists()
        progr = -1
        if not exists then
            | Create a progress indicator
            progr = create.progress.indicator( form.text$("tdsls1100.01" ),
                    PROGRESS.BAR + PROGRESS.STOP + PROGRESS.NOAUTODESTROY )
        endif
        if exists or progr = 0 then
            | We do not want any delay in this case
            change.progress.delay(0)
            | Display an initializing message
            ret = change.progress.indicator( 0, form.text$("tdsls1100.02") )
            |* Initializing...
        endif
        | Now determine the number of elements to process
        n = count.elements()

        | Process the elements
        for i = 1 to n
            if exists or progr = 0 then
                if change.progress.indicator( (i * 100) / n ) <> 0 then
                        abort.transaction()
                        break
                endif
            endif
            | Process element i
        endfor

        if progr = 0 then
            destroy.progress.indicator()
        endif
}
```

## Related topics
- [Progress indicators overview and synopsis](overview_and_synopsis.md)
