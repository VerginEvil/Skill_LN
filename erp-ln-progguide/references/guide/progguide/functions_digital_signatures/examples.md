# Digital Signatures examples

## Retrieve key info
This example shows a function that uses [sig.get.keys.info](sig.get.keys.info.md) to determine the correct key to use.
```

function long get.user.key.info(
	ref		long		o.slot,
	ref		boolean		o.on.hsm,
	ref		string		o.alias)
{
			long		keyinfo.node
			long		alias.node

	if sig.get.keys.info(logname$, keyinfo.node) <> 0 then
		| Message has been set by the function
		return(DALHOOKERROR)
	endif

	if xmlGetNumChilds(keyinfo.node) = 1 then
		alias.node = xmlGetFirstChild(keyinfo.node)
		xmlGetAttribute(alias.node, "slot", o.slot)
		o.on.hsm = xmlAttribute$(alias.node, "onHSM") = "true"
		o.alias = xmlData$(alias.node)
	else
		| Show a dialog to the user to pick the correct key
		| This part is left as an exercise to the reader
	endif

	xmlDelete(keyinfo.node)
	return(0)
}
```

## Basic signature
This example shows a function that signs an XML document with a basic signature. The key used to sign the document comes from a key store.
```

function void sign.xml.document(
	const		string		i.document.path,
	const		string		i.signed.document.path)
{
			long		request

	request = sig.init.sign.request()
	sig.sign.set.document(request, i.document.path)
	sig.sign.set.output(request, i.signed.document.path)
	sig.sign.set.format(request, XAdES)
	sig.sign.set.packaging(request, ENVELOPED)
	sig.sign.set.level(request, BASELINE_B)
	sig.sign.set.key.info(request, false, 0, "password")
	if sig.sign.execute.request(request) <> 0 then
		show.dal.messages()
	endif
	sig.destroy.request(request)
}
```

## Re-use of the request
This example demonstrates that the request can be re-used. The function signs multiple documents with the same configuration and key. The request is executed multiple times and once all documents are signed, the request is destroyed.
```

function void sign.pdf.documents(
			long		i.document.count,
	const		string		i.document.paths(,),
	const		string		i.signed.document.paths(,))
{
			long		request
			long		idocument

	request = sig.init.sign.request()
	sig.sign.set.format(request, PAdES)
	sig.sign.set.packaging(request, ENVELOPED)
	sig.sign.set.level(request, BASELINE_T)
	sig.sign.set.key.info(request, true, 0, "0000", "")

	for idocument = 1 to i.document.count
		sig.sign.set.document(request, i.document.paths(1,idocument))
		sig.sign.set.output(request, i.signed.document.paths(1,idocument))
		if sig.sign.execute.request(request) <> 0 then
			show.dal.messages()
		endif
	endfor

	sig.destroy.request(request)
}
```

## Signing a string
This example shows a function that signs a string with a basic signature. The key used to sign the document comes from a key store.
```

function void sign.string(
	const		string		i.string.to.be.signed,
	const		string		i.signed.document.path)
{
			long		request
			long		ret

	sign.hash = ""
	request = sig.init.sign.request()
	sig.sign.set.key.info(request, false, 0, "password")
	sig.sign.set.level(request, BASELINE_B)
	sig.sign.set.digest.algorithm(request, SHA256)
	sig.sign.set.string(request, i.string.to.be.signed)
	if sig.sign.execute.request(request) <> 0 then
		show.dal.messages()
	else
		sign.hash = sig.sign.get.output.string(request)
	endif
	sig.destroy.request(request)
}
```

## Related topics
- [Digital Signatures overview](overview.md)

- [Digital Signatures synopsis](synopsis.md)
