# get.ui.theme()

## Syntax:
`function string get.ui.theme( )`

## Description
This function returns the theme the UI is running in. For the strings that are returned by this function defines have been defined. These defines start with UI.THEME. Best is to use one of the defines to check which theme has been returned.

## Return values
UI.THEME.CLASSIC Classic theme
UI.THEME.MODERN Modern theme

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2492.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function can be called to check which groups or fields should be made hidden in the case a field of type donut or stat has been added to the form.

## Related topics
- [WebUI/LN UI support functions overview and synopsis](overview_and_synopsis.md)
