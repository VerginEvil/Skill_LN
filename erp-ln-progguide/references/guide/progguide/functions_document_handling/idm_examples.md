# Document Management (IDM) examples

## Upload document
This example shows a function that uses [dms.idm.upload.document](dms.idm.upload.document.md) to upload a file to IDM.
```

function upload.document(
	const	string	i.filename,
	const	string	i.mimetype)
{
	domain	ttxmlnode	doct.attr.list
	domain	ttxmlnode	doc.response
		string		error.mess(132)
		long		ret

	doct.attr.list = dms.idm.create.doctype.attribute.list()
	ret = dms.idm.list.add.doctype.attribute(doct.attr.list,
		"MDS_id1", tdsls400.orno, true)
	ret = dms.idm.list.add.doctype.attribute(doct.attr.list,
		"MDS_AccountingEntity", "infor.ln.0052", false)
	ret = dms.idm.list.add.doctype.attribute(doct.attr.list,
		"MDS_EntityType", "InforSalesOrder", false)

	ret = dms.idm.upload.document("MDS_GenericDocument",
		doct.attr.list,
		i.filename, path.filename(i.filename), i.mimetype,
		true, doc.response, error.mess)
}
```

## Search document
This example shows a function that uses [dms.idm.query.documents](dms.idm.query.documents.md) to search for a specific file in the PDF files linked to the current sales order.
```

function find.document(
	const	string	i.filename)
{
	domain	ttxmlnode	doct.attr.list
	domain	ttxmlnode	docs.response
	domain	ttxmlnode	doc.response
		string		document.filename(256) mb
		long		filter
		string		error.mess(132)
		long		ret

	doct.attr.list = dms.idm.create.doctype.attribute.list()
	ret = dms.idm.list.add.doctype.attribute(doct.attr.list,
		"MDS_id1", tdsls400.orno, true)
	ret = dms.idm.list.add.doctype.attribute(doct.attr.list,
		"MDS_AccountingEntity", "infor.ln.0052", false)
	ret = dms.idm.list.add.doctype.attribute(doct.attr.list,
		"MDS_EntityType", "InforSalesOrder", false)

	filter = dms.idm.create.filter()
	dms.idm.filter.set.mimetype(filter, "application/pdf")

	| Query the documents based on the attribute values and the filter.
	| Of course a filter based on the given filename could have been used.
	ret = dms.idm.query.documents("MDS_GenericDocument", doct.attr.list,
		filter, docs.response, error.mess)

	| Get the first document from the response, if any.
	doc.response = dms.idm.query.response.get.first.document(docs.response)

	while doc.response <> 0
		| Loop through the document to find the correct one.
		document.filename = dms.idm.document.get.filename(doc.response)
		if str.equals(document.filename, strip$(i.filename)) then
			| File is found, do something with it.
			break
		endif
		doc.response = dms.idm.query.response.get.next.document(doc.response)
	endwhile

}
```
