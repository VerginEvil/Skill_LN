# Document Management via Document Hub examples

## Upload document
This example shows a function that uses [dms.dochub.upload.document](dms.dochub.upload.document.md) to upload a file via the Document Hub. It is assumed that a document type mapping is present for table tdsls400 in application infor.ln.ext.
```

function upload.document.hub(
	const	string	i.filename,
	const	string	i.mimetype)
{
	domain	ttxmlnode	attr.list
	domain	ttxmlnode	doc.response
		string		error.mess(132)
		long		ret

	attr.list = dms.dochub.create.application.attribute.list()
	ret = dms.dochub.list.add.application.attribute(attr.list,
		"id1", tdsls400.orno)

	ret = dms.dochub.upload.document("tdsls400", "", attr.list,
		i.filename, path.filename(i.filename), i.mimetype,
		true, doc.response, error.mess)
}
```

## Search document
This example shows a function that uses [dms.dochub.query.documents](dms.dochub.query.documents.md) to search for a specific file in the PDF files linked to the current sales order. It is assumed that a document type mapping is present for table tdsls400 in application infor.ln.ext.
```

function find.document(
	const	string	i.filename)
{
	domain	ttxmlnode	attr.list
	domain	ttxmlnode	docs.response
	domain	ttxmlnode	doc.response
		string		document.filename(256) mb
		long		filter
		string		error.mess(132)
		long		ret

	attr.list = dms.dochub.create.application.attribute.list()
	ret = dms.dochub.list.add.application.attribute(attr.list,
		"MDS_id1", tdsls400.orno)

	filter = dms.dochub.create.filter()
	dms.dochub.filter.set.mimetype(filter, "application/pdf")

	| Query the documents based on the attribute values and the filter.
	| Of course a filter based on the given filename could have been used.
	ret = dms.dochub.query.documents("tdsls400", "", attr.list,
		filter, docs.response, error.mess)

	| Get the first document from the response, if any.
	doc.response = dms.dochub.query.response.get.first.document(docs.response)

	while doc.response <> 0
		| Loop through the document to find the correct one.
		document.filename = dms.dochub.document.get.filename(doc.response)
		if str.equals(document.filename, strip$(i.filename)) then
			| File is found, do something with it.
			break
		endif
		doc.response = dms.dochub.query.response.get.next.document(doc.response)
	endwhile
}
```
