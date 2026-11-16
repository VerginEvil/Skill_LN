# Example chart
Below an example program script is shown, for showing a chart of initial type bar.
```

#include <bic_dialog>
    table   ttewhr004
    long chart

function main()
{
        long dlg

        dlg = dialog.new("Chart demo", DLG_BUTTONS, 0)
        dialog.add.button(dlg, "mod.chart", "modify chart...")
        chart = dialog.add.chart(dlg, CHART_TYPE_BAR,
            CHART_TYPE_BAR+CHART_TYPE_LINE+CHART_TYPE_LINE_SCATTER)
       chart.set.title(chart, "Stock on hand")
        addData(chart)
        dialog.show(dlg)
}

function extern mod.chart()
{
    chart.clear.data(chart)
      addData(chart)
}

function void addData(long chart)
{
    long    series

    series = chart.add.series(chart, "With packing")

    select tewhr004.descr, tewhr004.packing, tewhr004.stoh
    from tewhr004
    where tewhr004.packing = tepack.yes
    selectdo
        chart.add.data.point(series, tewhr004.descr, tewhr004.stoh)
    endselect

    series = chart.add.series(chart, "Without packing")

    select tewhr004.descr, tewhr004.packing, tewhr004.stoh
    from tewhr004
    where tewhr004.packing = tepack.no
    selectdo
        chart.add.data.point(series, tewhr004.descr, tewhr004.stoh)
    endselect
}
```

## Related topics
- [Programmable dialogs synopsis](synopsis.md)
