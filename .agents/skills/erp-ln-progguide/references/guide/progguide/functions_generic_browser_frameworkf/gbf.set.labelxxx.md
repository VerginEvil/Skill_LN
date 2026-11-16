# gbf.set.label() *

## Syntax:
`#include <bic_gbf>`
`function long gbf.set.label( const string label1, const string label2, const string label3, const string label4, const string label5 )`

## Description
The gbf.set.label<nr>() functions are actually defines and they are defined as:
| | |
|---|---|
| gbf.set.label1(label) | gbf.set.label(label, “”, “”, “”, “”) |
| gbf.set.label2(label) | gbf.set.label( “”, label, “”, “”, “”) |
| gbf.set.label3(label) | gbf.set.label( “”, “”, label, “”, “”) |
| gbf.set.label4(label) | gbf.set.label( “”, “”, “”, label, “”) |
| gbf.set.label5(label) | gbf.set.label( “”, “”, “”, “”, label) |
The gbf.set.label() function will write the labels to the browser window and will display them in the bottom of this window in a status bar box. Note that the GBF will set and use these five labels for:
| | | |
|---|---|---|
| label id | description | dynamically changed by GBF |
| label1 | current action, like searching…, loading… and so on. | yes |
| label2 | key of the current selected item | yes |
| label3 | company number | no |
| label4 | company description | no |
| label5 | current date | no |
As can be seen from this table label1 and label2 are changed dynamically by the GBF:

- when an action is started this action will be displayed in label1

- when another object becomes selected the key of the selected object will be displayed in label2

The others are only set in [gbf.init()](gbf.init.md) and left unchanged by the GBF, hence an overwrite using this gbf.set.label() will be permanent.
Note that with [gbf.init()](gbf.init.md) it can be customized to have no labels or less than the default 5 labels, which implies that this function will return an error when trying to change a non existing label.
A value of “” for a label means that that label is not changed, where as any other value for which isspace() returns true (like “ ”), that label will be cleared on the screen.

## Argumentsgbf.set.label
| | |
|---|---|
| label1() | The current action, like searching…, loading… and so on. |
| label2() | The key of the current selected item |
| label3() | The company number |
| label4() | The company description |
| label5() | The current date |

## Argumentsgbf.set.labeln (n=1..5)
| | |
|---|---|
| label() | For n: 1. The current action, like searching…and so on. 2. The key of the current selected item 3. The company number 4. The company description 5. The current date |

## Arguments
| | | |
|---|---|---|
| `const string` | `label1` |  current action, like searching…, loading… and so  |
| `const string` | `label2` |  key of the current selected item  |
| `const string` | `label3` |  company number  |
| `const string` | `label4` |  company description  |
| `const string` | `label5` |  current date  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |
| GBF.NO.LABEL | Trying to change a non existing label |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## , gbf.set.label1(), gbf.set.label2(), gbf.set.label3(),gbf.set.label4(), gbf.set.label5()

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Typical usage](typical_usage.md)

- [Getting started](getting_started.md)

- [Example](example.md)

- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)

- [standard menu items and function keys](standard_menu_items_and_function_keys.md)

- [Messages and questions](messages_and_questions.md)
