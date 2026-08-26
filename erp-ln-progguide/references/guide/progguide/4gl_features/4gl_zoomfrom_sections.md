# 4GL zoom.from sections
You use zoom.from sections to program actions that you want to be executed when the current session is activated as a zoom process. A zoom process can be activated by a form-specific command of type session, by zooming on an input field, by pressing CTRL+B, or by calling [zoom.to$()](../functions_starting_and_stopping_programs/zoom.to.md) in the program script. Zoom.from sections consist of a main section and a subsection. The main section specifies the process for which the actions must be executed. The subsections specify when the actions must be executed.

## Main sections

## zoom.from.<zoom name>:
Each field has a name that can be used as a zoom name. You can specify the zoom name in this main section. The zoom name indicates which field the current session was zoomed from (when the subprocess is started from a form command, the zoom name is "choice"). The subsections associated with this main section are executed when the current process was zoomed to from the specified process.

## zoom.from.all:
The subsections associated with this main section are executed for all processes from which the current session can be zoomed to.

## zoom.from.other:
A subsection associated with this section is executed for all processes for which the particular subsection has not been programmed in a *zoom.from.<zoom name>* section.

## Subsections

## on.entry:
The actions programmed in this subsection are executed each time the current process is started from the specified process(es). You can use this subsection to import variables.

## on.exit:
The actions programmed in this subsection are executed at the end of the current process, if the current process was started from the process(es) specified in the main section. You can use this subsection to export variables.

## Example
```

zoom.from.all:
on.entry:
                   import("globvar", localvar)
on.exit:
                export("globvar", localvar)
```

## Related topics
- [Programming a UI Script overview](overview.md)
- [4GL event sections](4gl_event_sections.md)
- [Flow of 4GL engine](flow_of_standard_program.md)
