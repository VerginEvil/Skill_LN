# Programmable Dialogs Example
This dialog can be created by the following script
```

#include <bic_dialog>

extern  domain  ttaad.pacc      pacc
extern  domain  ttadv.cpac      cpac.f, cpac.t
extern  domain  ttadv.cmod      cmod.f, cmod.t
extern  domain  ttadv.cprs      cprs.f, cprs.t
extern  domain  ttyeno          def.query.yn
extern  long    log.by
extern  string  txt.field(1003)
extern  string  query.lib.file(80)
extern  domain  ttutc       my.utc

function main()
{
        long dlg
        long    logno(3)
        string  logdesc(10,3)

    txt.field = "This is supposed to be a very long string" &
       " and it should be much longer than this." &
       " Therefore I repeat this line" &
       " Therefore I repeat this line" &
       " Therefore I repeat this line" &
       " Therefore I repeat this line" &
       " Therefore I repeat this line" &
       " Therefore I repeat this line" &
       " Therefore I repeat this line" &
       " Therefore I repeat this line" &
       " Therefore I repeat this line" &
       " Therefore I repeat this line" &
       " Therefore I repeat this line" &
       " Therefore I repeat this line" &
       " Therefore I repeat this line" &
       " Therefore I repeat this line" &
       " Therefore I repeat this line" &
       " Therefore I repeat this line" &
       " Therefore I repeat this line" &
       " Therefore I repeat this line" &
       " Therefore I repeat this line"

        dlg = dialog.new("Example",
           DLG_STATUSBAR,       true,
       DLG_SAVE_GET_DFLTS,  "",
           DLG_OK_TEXT,         "All Right")

        dialog.add.field(dlg, "pacc", "Package Combination",
                DLG_ZOOM_PROG,  "ttaad1520m000",
                DLG_ZOOM_RETURN,"ttaad120.pacc",
                DLG_FIELD_CHECK,"pacc.check.input",
                DLG_DOMAIN,     "ttaad.pacc")

    dialog.add.text(dlg, "Programmable dialogs offer a very flexible way" &
       " of developing dialogs. The dialogs can be configured at run time." &
       " All you have to do is writing some function calls. Basically," &
       " there are 3 commands: dialog.new() for creating a dialog structure,"&
       " dialog.add.field() for adding fields to the dialog structure and" &
       " finally dialog.show() for displaying the created dialog on the" &
       " screen. dialog.add.text and dialog.add.listbox are just" &
       " variants of dialog.add.field().",
       DLG_FIELD_WIDTH, 100)

        dialog.add.field(dlg, "cpac.f", "Packages",
           DLG_ZOOM_PROG,       "ttadv1100m000",
           DLG_ZOOM_RETURN,     "ttadv100.cpac",
           DLG_RANGE_FIELD,     "cpac.t",
           DLG_DOMAIN,          "ttadv.cpac")

        dialog.add.field(dlg, "cmod.f", "Modules",
           DLG_ZOOM_PROG,       "ttadv1101m000",
           DLG_ZOOM_RETURN,     "ttadv101.cmod",
           DLG_RANGE_FIELD,     "cmod.t",
           DLG_DOMAIN,          "ttadv.cmod")

        dialog.add.field(dlg, "cprs.f", "Scripts",
           DLG_ZOOM_PROG,       "ttadv2530m000",
           DLG_ZOOM_RETURN,     "ttadv230.cprs",
           DLG_RANGE_FIELD,     "cprs.t",
           DLG_DOMAIN,          "ttadv.cprs")

        dialog.add.field(dlg, "query.lib.file", "Query Library File",
           DLG_FIELD_WIDTH,     40,
           DLG_ZOOM_PROG,       "@start.editor")

        dialog.add.field(dlg, "def.query.yn", "Default Query",
           DLG_FIELD_TYPE,      DLG_TYPE_CHECKBOX)

        logno(1) = 1    logdesc(1,1) = "Package"
        logno(2) = 2    logdesc(1,2) = "Module"
        logno(3) = 3    logdesc(1,3) = "Query"

        dialog.add.listbox(dlg, "log.by", "Log by", 3, logno, logdesc,
                DLG_MANDATORY,  true)
        if log.by = 0 then
                log.by = 1
        endif

        dialog.add.field(dlg, "my.utc", "This is a date/time control",
           DLG_FIELD_TYPE,      DLG_TYPE_UTC)

        dialog.add.field(dlg, "txt.field", "Enter your text here",
           DLG_FIELD_LENGTH,    40,
           DLG_FIELD_TYPE,      DLG_TYPE_MULTI_LINE)

        dialog.add.button(dlg, "do.sth", "Do it")
        dialog.add.button(dlg, "undo.sth", "Undo it")

        if not dialog.show(dlg) then
                message("You pressed cancel")
        endif
}

function extern long    pacc.check.input()
{
        if pacc(1;1) = "a" then
                message("Package Combination cannot start with an a")
                return(false)
        endif
        return(true)
}

function extern do.sth()
{
        footnote("Done it")
        fill.status.field(2,"")
}

function extern undo.sth()
{
    footnote("")
        fill.status.field(2,"Undone it")
}

function extern start.editor()
{
        fill.status.field(2,"editing")
        message("Editor should be started here")
        fill.status.field(2,"")
}
```

## Related topics
- [Programmable dialogs synopsis](synopsis.md)
