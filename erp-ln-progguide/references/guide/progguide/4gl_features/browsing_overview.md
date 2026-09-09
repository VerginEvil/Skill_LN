# Overview of browsing
Before describing how to implement browsing, it is useful to see what happens when a browse list is started. This also gives more insight in how the [4GL engine](../glossary/glossary.md#fourgl_engine) is involved.
In short when a browse list starts the following steps are executed:

- The browse list session imports one or more variables from the parent session.This is required because a browse list should show data based on the value of the input field(s) of the parent session. E.g. when the user enters 'KO' in a Business Partner field and then starts the Business Partners browse list, the list should show Business Partners whose BP id field has a value equal to or greater than 'KO'.

- The browse list session imports any browse filters set in the parent session. The parent session may have set a browse filter, using the *query.extend.*.in.zoom()* functions. The browse list session adds this filter to the query it uses to read data from the maintable.

- The browse list session retrieves the data from its maintable using the values of the imported variables.E.g. it should start reading at the Business Partner 'KO'.

- The browse list session displays the data on its form and waits for user actions.

- After the user selects a record and ends the session by pressing OK, the browse list session exports the data of the selected record to the parent session.The browse list session therefore needs to know which fields to export to the parent session. E.g. a Business Partner id.

Steps 1, 2 and 5 are specific to browse list sessions. In the next sections we concentrate on steps 1 and 5.

## Related topics
- [Definition](browsing_definition.md)

- [Importing variables](browsing_importing.md)

- [Exporting variables](browsing_exporting.md)

- [Starting a browse list session](browsing_starting.md)
