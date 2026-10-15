# Chapter 5: InContext Modeling

> Summary treatment for this release: orientation-level coverage. The full cleaned source text is preserved below; consult the source guide for exhaustive detail.

Infor OS Portal contains various context widgets or Infor Ming.le contains various context applications that
show data that is related to LN objects. See these examples:
- An LN Business Partner has an address; if a user opens a Business Partner record, the corresponding
location is displayed in the Map context widget/application.
- A Sales order can have multiple documents attached to it. The Business Partner, to which the Sales Order
applies, can also have multiple documents attached to it. Both, the documents attached to the Sales
Order and to the Business Partner, are displayed in the Related Information context widget/application.
### Context messages

The integration between Infor LN and the Infor OS Portal or Infor Ming.le context widgets/applications is
based on context messages. In these context messages, the characteristics of the LN objects, which have
focus in the UI, are sent to the context widgets/applications. Context messages are generated from InContext
Models.
## InContext model

An InContext model describes which fields are required for the context messages and how these fields can
be retrieved.
Two types of InContext models exist:
- InContext Reference Model
- InContext Implementation Model
InContext Reference Model (IRM)
The IRM is a model of tables and references that is generated from the existing table definitions and other
data. This model contains a basic link between table(field)s and context messages. An IRM belongs to an
application, a set of packages that belong to each other and have the same version.
InContext Implementation Model (IIM)
The IIM contains the link between the tables and sessions and the context messages that must be generated.
This model can be generated initially from the IRM. In the IIM, hooks are available to influence the default
behavior.
In LN Studio, you can modify the IIM on table level and session level:
- Table level
A table level model contains the applicable context message types for a particular table, and the fields
that must be used to construct the message. This model applies to all sessions where that particular
table is the main table, unless the table level model is overruled by the session level model.
You can modify the table level model in the Table InContext Model Editor.
- Session level
A session level model contains the applicable context message types for a particular session.
Session level models are used for these purposes:
- To specify the context message types for sessions without main table.
- To define session-specific extensions to the table level model for sessions that have a main table.
You can modify the session level model in the Session Model Editor.
## Related topics

- Infor Enterprise Server InContext Modeling Development Guide
- The online help of the Table InContext Model Editor
- The online help of the Session Model Editor
- The online help of the Dependent InContext Models view
