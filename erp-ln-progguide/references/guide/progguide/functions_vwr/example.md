# Document Viewer example
Some specific parts in a Composite session with a Navigation panel and a Document Viewer panel are shown.
Below some specific parts in the Composite child Navigation session script are shown.
```

  Use PRCM for data synchronization between composite child sessions
	     long node = xmlNewDataElement(“PATH”, serverfilePath)
		prcm.notify("showfile:" & str$(parent), "", node)
```
Composite child Document Viewer session .
```

#include <bic_vwr>

main()
{
	|Register with PRCM for data synchronization with another Composite child session.
	prcm.register("showfile:" & str$(parent))
	vwr.init()

	| Optionally show initial file
	client.show.file(source, false,“”)

	vwr.start()
}

function extern void vwr.bms.received(long sender.id, const string mask, const string mss, long length)
{
	long node
	if prcm.bms.is.notification() then
		node = prcm.get.data()
		client.show.file(xmlData$(node), false, “”)
	endif
}
```

## Related topics
- [Document Viewer overview](overview.md)
- [Document Viewer synopsis](synopsis.md)
