# 4GL group sections
With dynamic forms, the mapping of groups to forms is not fixed. Consequently, the only form section that is relevant to dynamic forms is the *form.all* section. When dealing with dynamic forms, you use group sections instead of form sections
You use group sections to program actions that you want to be executed when a particular group is activated or ended. Group sections consist of a main section and a subsection. The main section specifies the particular group(s) for which the actions are to be executed. The subsections specify when the actions must be executed – for example, when the group is activated or when the group is ended.
Note that a group becomes active when the form on which it occurs becomes current.

## Main section

## group.<group number>:
This section defines the group for which the actions programmed in the group subsections are executed. The group number is automatically generated when the group is created and can be obtained from the DFE.

## Subsections

## init.group:
The actions programmed in this subsection are executed only the first time the group becomes active, immediately before the *before.group* subsection. You use this subsection to program the first action to be performed by the system when the group becomes active. When the group is split across two or more forms (because not all the group fits on one form or because it is a repeating group), this subsection is executed the first time that the first form on which the group occurs becomes current.
Note: the *init.group* section for group.1 is the former *init.form* section for form.1. Group number 1 is reserved and represents a super group, containing all other groups.

## before.group:
The actions programmed in this subsection are executed each time the specified group becomes active. When the group is split across more than one form, this subsection is executed whenever any form on which it occurs becomes current.

## after.group:
The actions programmed in this subsection are executed each time the form on which the group occurs is ended. When the group is split across more than one form, this section is executed whenever any form on which the group occurs is ended.

## Related topics
- [Programming a UI Script overview](overview.md)
- [4GL event sections](4gl_event_sections.md)
- [Flow of 4GL engine](flow_of_standard_program.md)
