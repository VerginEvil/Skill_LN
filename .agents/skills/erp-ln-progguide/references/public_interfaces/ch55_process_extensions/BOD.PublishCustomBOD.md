# BOD.PublishCustomBOD

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1978-1979

```baan
Publish Custom BOD.
This process extension is available from 2020.12 (KB2164036).
Technical information for this process extension:
Usage:       With this Process Extension, it is possible to publish already existing
data through an initial load for custom BODs.
The session Publish Custom BODs (tcbod0299m000) is available as a
framework to publish the custom BODs. By implementing the functions of
this process extension, the session knows which BODs must be published,
how their data must be selected from the database, which function must be
called to publish the BOD for the selected data and how metadata has
to be filled in the BODs.
The following methods are present and must be implemented:
-      tcext.bod0001.get.custom.bodnames()
This method is called when session Publish Custom BODs is started.
With this method you specify which custom BODs need to be
published. You can specify upto 50 BODs. For each BOD the session
will display a separate tab, just like the standard BOD publishing
sessions (for example Publish Order Management Transactional Data
- tdbod0200m000).
You can define custom fields in the process extension to add
selection criteria to the tabs (see below).
-      tcext.bod0001.get.initial.load.query()
This method is called once for each selected custom BOD when the
processing is started in session Publish Custom BODs.
Use this method to return the SQL query to read the root table
of the custom BOD. In this query you can use the custom fields
you defined in the process extension. For each selected record
during the execution of this query, the BOD is created and
published according the common options in the first tab of the
Publish Custom BODs session.
The following methods are present and are mutually exclusive -
one of these two methods must be implemented for a custom BOD:
-      tcext.bod0001.get.custom.bod.publish.function()
This method must be used if the SQL query in the
tcext.bod0001.get.initial.load.query() method contains a GROUP BY
clause or the SQL query returns more records than required for
publishing the BODs and a custom function is needed to further
decide if a selected record should publish a BOD or not. The
custom function should contain functionality to decide if a BOD
must be published, should provide metadata for the BOD, and should
call the BOD.Publish() function to actually publish the BOD.
This method is called for each record that is selected by the SQL
query. Use this method to return the name of the function.
-      tcext.bod0001.get.custom.bod.properties()
This method must be used if a BOD must be published for each
record that is returned by the SQL query in the
tcext.bod0001.get.initial.load.query() method and the SQL query
does not contain a GROUP BY clause. A standard publish BOD
function is called for each record that is selected by the SQL
query. This method is called by this standard publish function
during the BOD creation. Use this method to provide metadata for
the BOD, like the DocumentID and the entity type and entity code
that are used to set the accounting entity and location attributes
in the BOD.
For most custom BODs the standard BOD publish function can be used and
the tcext.bod0001.get.custom.bod.properties() method should be
implemented. Implementation of the
tcext.bod0001.get.custom.bod.publish.function() method is an exception.
Custom fields
You can define custom fields in the process extension for selection
criteria in the query to read the root table of the custom BODs. To
include the custom fields in the session Publish Custom BODs, you need
to create a session extension for this session and add the custom fields
in the extension. Use the Add>Custom Field>Field from Process Extension
option to add the custom fields. The fields will be added to the
Configurable Fields tab of session Publish Custom BODs. With Form
Personalization you can move the custom fields to the tab for the custom
BOD to which the custom fields apply.
Summary of steps:
- Create process extension BOD.PublishCustomBOD
- Implement function tcext.bod0001.get.custom.bodnames()
- Create custom fields for the selection ranges
- Implement function tcext.bod0001.get.initial.load.query()
- Implement either function tcext.bod0001.get.custom.bod.properties() or
implement function tcext.bod0001.get.custom.bod.publish.function()
- If function tcext.bod0001.get.custom.bod.publish.function() is
implemented, program publishing logic in the custom BOD publish function
- Create session extension Publish Custom BODs (tcbod0299m000)
- Add the custom fields from process extension BOD.PublishCustomBOD
- Run session Publish Custom BODs (tcbod0299m000)
- Personalize form to move the custom fields from the Configurable Fields
tab to the BOD specific tab
- Test the publishing of the custom BOD
To implement this process extension, you need to implement the following method(s):
```
