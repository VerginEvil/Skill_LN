# Functions with variable number of arguments: sample program
```

function long change.attributes( long id, ...)
{
    long    argc
    long    i
    long    long_value
    double  double_value
    string  string_value

    argc    = get.argc()

    for i = 3 to argc step 2
        on case get.long.arg(i-1)
        case DS_TITLE:
            string_value = get.string.arg(i)
            ......
            break
        case DS_BACKGROUND:
            long_value = get.long.arg(i)
            ......
            break
        default:
            ......
            break
        endcase
    endfor

    return(0)
}

function call:

    change.attributes(
        window_id,
        DS_TITLE,   "Title",
        DS_BACKGROUND,  CW.GREEN,
        DS_FOREGROUND,  CW.WHITE,
        DS_WIDTH,   80,
        DS_HEIGHT,  40
    )
```

## Related topics
- [Functions with variable number of arguments: overview](overview.md)

- [Functions with variable number of arguments: synopsis](synopsis.md)
