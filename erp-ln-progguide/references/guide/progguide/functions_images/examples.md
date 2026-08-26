# Images on Forms Examples

## Image bound to maintable
Below a part of a 4GL-UI script is shown to illustrate the usage of the image functions. In this example the image is bound to the maintable of the session through the table field *bpmdm001.guid*. The image is shown in the view area of a multi-occ session. The function [enable.save.on.occ.change()](../functions_form_and_form_field_operations/enable.save.on.occ.change.md) must be called to make sure that a possible dropped image is saved before selecting another occurrence in the grid.
```

table   tbpmdm001                           |* Employee
extern  domain ttdyf.picture  image.field   |* image form field

after.form.read:
	bind.image("image.field", "bpmdm001.guid")
	enable.save.on.occ.change()

after.update.db.commit:
	if is.image.changed("image.field") then
		if check.image.present(bpmdm001.guid) then
			|Optionally ask user if we should override the current image.
		endif
		save.image.field("image.field")
	endif

choice.recover.set:
after.choice:
	discard.changed.image("image.field")
```
The image field must be assigned in the DAL of the table:
```

function extern long before.save.object(long i.mode)
{
	bpmdm001.guid = uuid.generate$()
	return(0)
}
```

## Image not bound to maintable
There might also be situations in which an image should be shown which is not bound to the maintable of the session. This occurs for instance when in a header MMT session the image should be shown of the currently selected line in an MMT satellite session.
Note  In these situations no drag and drop of images is possible.
Below a part of the 4GL-UI script of the MMT header session is shown
```

table   ttdsls205                           |* Sales Order Templates
extern  domain  ttdyf.picture   image.field |* image form field
extern  domain  tcguid          image.guid  |* GUID of image

before.program:
	|Subscribe to PRCM messages from satellite to pass a new image GUID.
	prcm.register("tdsls206:" & str$(pid) )

after.form.read:
	|Image is linked to the lines table: tdsls206.
	bind.image("image.field", "image.guid", "tdsls206")

choice.bms:
on.choice:
    long node
    if prcm.bms.is.notification() then
        if prcm.get.subject() = "tssls206:" & str$(pid) then
		|A new GUID is sent by the satellite
		node = prcm.get.data()
		image.guid=xmlData$(node)
		display("image.field")
	  endif
```
In the satellite session the following code must be added to pass on the image GUID field to the header session.
```

table   ttdsls206               |* Sales Order Template Lines
domain  tcguid      hold.guid   |* GUID of image
long    node

before.program:
    node = xmlNewNode("guid")   |XML node to communicate new GUID to header session

choice.mark.occur:
after.choice:
   if is.mmt.satellite() and
      hold.guid <> tdsls206.guid and
      sel.num.selected() = 1 then
            |Send a new GUID to the header session so the header session
            |can update the picture field.
            hold.guid = tdsls206.guid
            node = xmlRewriteDataElement(node, "guid", tdsls206.guid)
            prcm.notify("tdsls206:" & str$(parent), "", node)
   endif
```

## Related topics
- [Images on Forms Overview](overview.md)
- [Images on Forms synopsis](synopsis.md)
