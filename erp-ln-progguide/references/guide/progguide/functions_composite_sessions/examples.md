# Composite Sessions Code Examples

## Composite Session Controller
Below an example script is shown of a Composite Session Controller session. This session is linked to a 3GL-Session script
```

#include <bic_cps>

function void main()
{
	long retval
	long pane1
	long pane2

	retval = cps.init()

	pane1 = cps.create.splitpane(CPS.VERTICAL, 50)
	pane2 = cps.create.splitpane(CPS.HORIZONTAL, 30, pane1)

	cps.add.child("tewhr6501m000", CPS.MENUBAR+CPS.TOOLBAR,
   				  "Title 1", pane2)
	cps.add.child("tewhr6502m000", CPS.TOOLBAR, "Title 2", pane2)
	cps.add.child("tewhr6602m000", CPS.TOOLBAR, "Title 3", pane1)

	cps.start()
}
```

## Composite Child 4GL-Session
Below some specific parts in a Composite Child 4GL-Session script are shown. The code constructions which are directly related with Composite Child sessions are shown in italic.
```

after.form.read:
	|For data-synchronization create a keyfields object.
	keyfields = create.keyfields.object("tewhr602")

choice.mark.occur:
after.choice:
	|Use PRCM for data synchronization between composite child
	|sessions
	if hold.record <> tewhr602.uuid and
	    sel.num.selected() = 1 then
		hold.record = tewhr602.uuid

		keyfields.to.object(keyfields)
		prcm.notify("tewhr602:" & str$(parent), "", keyfields)

	endif
```

## Composite Child GBF-Session
Below some specific parts in a Composite Child GBF-Session script are shown. The code constructions which are directly related with Composite Child sessions are shown in italic
```

#include <bic_gbf>				| GBF defines
long keyobject

function void main()
{
	long	retval			|to test return values

	|Register with PRCM for data synchronization with another
	|Composite child session.
	prcm.register("tewhr602:" & str$(parent))

	retval = gbf.init(gbf.current.library(), "",
			GBF.MENU.ALL + GBF.MENU.FILE.OPEN + GBF.MENU.FILE.READ,
			GBF.BUTTON.ALL, GBF.OPT.DEFAULT + GBF.OPT.DEBUG)
	if retval < 0 then
		exit(retval)
	endif
	if gbf.set.sort.strategy( GBF.SORT.DESC
				+ GBF.SORT.ASCENDING
				+ GBF.SORT.INSENSITIVE) then
		message("Cannot change sort strategy")
	endif
	exit(gbf.start(2, 2))		|Show and read the first level
}

function extern long gbf.get.top.level()
{
	long	retval

	if keyobject < 0 then
		object.to.keyfields(keyobject)

		select	tewhr602.*
		from	tewhr602
		where	tewhr602.uuid = :tewhr602.uuid
		selectdo
			retval = gbf.add.interior(strip$(tewhr602.uuid),
				get.part.descr(strip$(tewhr602.item)),
				0)
			if retval < 0 then
				return (GBF.DO.EXIT)
			endif
		endselect
	endif
	return (0)
}

function extern long gbf.bms.received(long sender.id, const string mask(), const string mss(), long length)
{

	if prcm.bms.is.notification() then
		keyobject = prcm.get.data()
		return(GBF.DO.RESTART.TREE)		|Force GBF to call gbf.get.top.level() again
	endif

	return(GBF.DO.CONTINUE)
}
```

## Drag from 4GL-Session
Below some parts of a 4GL-UI scripts are shown which are specific for the implementation of dragging records from a 4GL-multi-occurrence session.
```

before.program:
	enable.drag()
	prcm.register("tewhr601") |For updating the UI when table changed in other session

choice.bms:
on.choice:
	if prcm.bms.is.notification() then
		|* Refresh all data on the screen (for instance after a drop on another session)
		refresh.all.occs()
	endif
```

## Drag to GBF-Session
Below some parts of a GBF session script are shown which are specific for the implementation of dropping objects from another session onto a GBF node
```

function void main()
{
	long	retval			|to test return values

	retval = gbf.init(…)
	if retval < 0 then
		exit(retval)
	endif

	retval = gbf.enable.drop("tewhr6501m000", gbf.current.library(), "gbf.on.drop")
	if retval < 0 then
		exit(retval)
	endif
	exit(gbf.start()
}

function extern long gbf.on.drop(long from.pid, long collection, long drop.obj, const string drop.key,
		 long drop.value, long drop.type, boolean copy)
{
	long keyfields.object
	boolean updates.done
	long retval

	db.retry.point()

	keyfields.object = get.first.keyfields.object(collection)

	updates.done = false

	while keyfields.object <> 0
		object.to.keyfields(keyfields.object)

		|Check and decrement stock in tewhr601
		select tewhr601.item
		from tewhr601 FOR UPDATE
		where tewhr601.item = :tewhr601.item
		selectdo
			if tewhr601.stock > 0 then
				DEC(tewhr601.stock)
				db.update(ttewhr601, DB.RETRY)

				| Insert new record in tewhr602
				tewhr602.uuid = uuid.generate$()
				tewhr602.item = tewhr601.item
				tewhr602.pare = drop.key
				db.insert(ttewhr602, DB.RETRY)
				updates.done = true
			else
				message("No stock available for item: " & tewhr601.item)
			endif
		endselect

		keyfields.object = get.next.keyfields.object(keyfields.object)
	endwhile

	commit.transaction()

	retval = GBF.DO.CONTINUE

	if updates.done then
		|Make sure current object is refreshed.
		retval = GBF.DO.RESTART.CURRENT

		|Update the session from which the record(s) were dragged.
		prcm.notify("tewhr601")
	endif

	return(retval)
}
```

## Drag from a GBF session
Below some parts of a GBF session script are shown which are specific for the implementation of dragging objects from a GBF session onto another session.
```

function void main()
{
	long	retval			|to test return values

	|Register with PRCM for drop synchronization.
	prcm.register("tewhr602")

	retval = gbf.init(gbf.current.library(), "",
			GBF.MENU.ALL + GBF.MENU.FILE.OPEN + GBF.MENU.FILE.READ,
			GBF.BUTTON.ALL, GBF.OPT.DEFAULT + GBF.OPT.SESSION.DRAG)
	if retval < 0 then
		exit(retval)
	endif
	exit(gbf.start()
}

function extern long gbf.on.drag(long to.pid, const string to.session, long drag.obj,
	const string drag.key, long drag.value, long drag.type, reference long collection)
{
	collection = create.keyfields.collection()
	long numSelected
	long i
	long retval
	domain teuuid keyvalue

	if drag.obj > 0 then
		|Only one object selected.
		add.key.object(drag.key, collection)
	else
		|More than one object selected.
		numSelected = -drag.obj
		for i = 1 to numSelected
			if gbf.get.selected(i, drag.obj, keyvalue, drag.value, drag.type) = 0 then
				add.key.object(keyvalue, collection)
			endif
		endfor
	endif

	if get.num.keyfields.object(collection) > 0 then
		retval = GBF.DO.CONTINUE
	else
		|No objects added to collection. Abort drag operation.
		delete.keyfields.collection(collection)
		collection = 0
		retval = GBF.DO.ABORT
	endif
	return(retval)
}

function void add.key.object(const domain teuuid keyvalue, long collection)
{
	long keyfields.object

	select	tewhr602.*
	from	tewhr602
	where	tewhr602.uuid = :keyvalue
	selectdo
		keyfields.object = create.keyfields.object("tewhr602", collection)
		keyfields.to.object(keyfields.object)
	endselect
}

function extern long gbf.bms.received(long sender.id, const string mask(), const string mss(), long length)
{
	if prcm.bms.is.notification() then
		return(GBF.DO.RESTART.TREE)
	endif
	return(GBF.DO.CONTINUE)
}
```

## Drop on a 4GL session
Below some parts of a 4GL-UI scripts are shown which are specific for the implementation of dropping records from another session.
```

before.program:
	enable.drop("tewhr6602m000", "on.drop")

function extern void on.drop(long from.pid, long collection, boolean copy)
{
	long keyfields.object
	boolean updates.done

	db.retry.point()

	keyfields.object = get.first.keyfields.object(collection)

	updates.done = false

	while keyfields.object <> 0
		object.to.keyfields(keyfields.object)

		|Remove record from tewhr602
		select tewhr602.*
		from tewhr602 for UPDATE
		where tewhr602.uuid = :tewhr602.uuid
		selectdo
			|Increment related stock in tewhr601
			select tewhr601.*
			from tewhr601 FOR UPDATE
			where tewhr601.item = :tewhr602.item
			selectdo
				INC(tewhr601.stock)
				db.update(ttewhr601, DB.RETRY)
			endselect

			db.delete(ttewhr602, DB.RETRY)
			updates.done = true
		endselect

		keyfields.object = get.next.keyfields.object(keyfields.object)
	endwhile

	commit.transaction()

	if updates.done then
		|Make sure last record which was modified becomes visible.
		execute(find.data)

		|Update the session from which the record(s) were dragged.
		prcm.notify("tewhr602")
	endif
}
```

## Related topics
- [Composite Sessions overview](overview.md)

- [Composite Sessions synopsis](synopsis.md)
