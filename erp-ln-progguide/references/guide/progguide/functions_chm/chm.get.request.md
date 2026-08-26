# chm.get.request()

## Syntax:
`function long chm.get.request( long chart_no, ref double category_from_value, ref double category_to_value )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This retrieves a request from the Business Chart Manager. After calling the function, the application waits for a signal from the Chart Manager that a request is ready. It can then check the return value of the function to determine the nature of the request. The application must react to the request appropriately.

## Arguments
| | | |
|---|---|---|
| `long` | `chart_no` |  This returns the ID of the relevant chart, as returned by [chm.open()](chm.open.md).  |
| `ref double` | `category_from_value` |  These indicate the range of data the Chart Manager is asking for. These arguments are relevant only when the return value is CHM_SOURCE_IN.  |
| `ref double` | `category_to_value` |  |

## Return values
| | |
|---|---|
| CHM_ABORT | Quit the Business Chart Manager. |
| CHM_SOURCE_IN | Send data to the Chart Manager. This value is returned when the user chooses the IN command on the Chart Manager's File menu.  |
| CHM_SOURCE_OUT | Retrieve data from the Chart Manager. This value is returned when the user chooses the OUT command on the Chart Manager's File menu.  |
| CHM_TIMER | Execute actions after the interval set by [chm.set.timer()](chm.set.timer.md).  |
| < value > | This is the ID of an application option defined in the Application Options session (ttchm1120s000). When this value is returned, the application must execute the specific actions related to the particular application option.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

long request
double category_from, category_to
repeat
                request = chm.get.request(chartno, category_from,
category_to)
                on case request
                case CHM_SOURCE_IN:
                                ....
                case CHM_SOURCE_OUT:
                                ....
                case CHM_TIMER:
                                chm.draw()
                                break
                case 200:
                                start.session(MODAL,
"ppmodggggmooo", "", "")
                endcase
until (request = CHM_ABORT)
```

## Related topics
- [Chart manager overview](overview.md)
- [Chart manager synopsis](synopsis.md)
- [Creating a chart manager client application](creating_a_chart_manager_client_application.md)
- [Chart manager example](example.md)
