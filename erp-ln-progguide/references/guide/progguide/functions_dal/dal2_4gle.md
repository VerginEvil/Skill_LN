# DAL2 and the 4GL Engine
The following table gives an overview of what hooks the 4GL engine calls to update the User Interface. For a number of UI event sections you can see which hooks are called. Note that the actions performed by the 4GL engine are executed just before the mentioned UI section is called. In this way it is possible to e.g. disable a field based on other than DAL constraints.
| | |
|---|---|
| UI section | DAL2 Hooks called |
|  after.form.read:  |  |
|  - remove unused fields - remove unused form commands - remove unused enum keyword  |  field.is.never.applicable() business.method.is.never.allowed() field.enum.is.never.applicable()  |
|  |  |
|  before.new.object:  |  |
|  - set default object values  |  set.object.defaults()  |
|  |  |
|  before.display.object:  |  |
|  - enable/disable maintable fields  |  field.is.applicable() field.is.readonly() field.is.derived()  |
|  - determine enum values  |  field.enum.constant.is.applicable()  |
|  - enable/disable standard commands  |  method.is.allowed()  |
|  - enable/disable form commands  |  business.method.is.allowed()  |
|  |  |
|  choice.mark.occur:after.choice:  |  |
|  - enable/disable standard commands  |  method.is.allowed()  |
|  - enable/disable form commands  |  business.method.is.allowed()  |
|  |  |
|  *field.<fieldname>:check.input:*  |  field.is.never.applicable() field.is.applicable() field.is.readonly() field.is.derived() field.is.mandatory() field.is.valid() / field.enum.constant.is.applicable()  |
|  |  |
|  field.<fieldname>:when.field.changes: - trigger dependent fields - enable/disable maintable fields - determine enum values  |  field.is.applicable() field.is.readonly() field.update() field.is.applicable() field.is.readonly() field.is.derived() field.enum.constant.is.applicable()  |
|  - enable/disable standard commands  |  method.is.allowed()  |
|  - enable/disable form commands  |  business.method.is.allowed()  |
|  |  |
|  main.table.io:read.view:  |  |
|  - enable/disable standard commands  |  method.is.allowed()  |
|  - enable/disable form commands  |  business.method.is.allowed()  |

## Related topics
- [Extended DAL (DAL2)](dal2_overview.md)
