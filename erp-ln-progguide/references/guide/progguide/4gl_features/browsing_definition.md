# Definition
The GUI Style Guide defines a Browse list session as follows:
- *A browse list is a modal, secondary window* that is started when the user browses on an input field in the Details window or Overview window to retrieve a value for that input field.
- The browse list displays a list of objects or properties of objects. Only those objects or properties of objects are displayed that are valid within the context of the related input field(s) (browse filter).   Analyzing this definition gives the following:
- A browse list is a modal window. This means that the *parent session is blocked* for user input until the browse list ends.
- A browse list is used to help the user retrieve a value for an input field. This means that the whole *purpose of the browse list is to help the user* as much as possible. E.g. the browse list should show data based on the value of the input field(s) of the parent session.
- A browse list only shows data that is valid within the context of the related input field. This means that *a browse filter may be implemented*.

## Related topics
- [Overview of browsing](browsing_overview.md)
- [Importing variables](browsing_importing.md)
- [Exporting variables](browsing_exporting.md)
- [Starting a browse list session](browsing_starting.md)
