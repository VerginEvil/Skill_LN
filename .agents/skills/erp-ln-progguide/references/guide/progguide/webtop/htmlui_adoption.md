# Implementing LN UI support

## Introduction
As LN UI does not support functionality that requires a higher privilege level on the client, some client access functions are not allowed anymore. Calls to these functions have to be replaced with other client access functions which are allowed to be used when running in HTMLUI mode. Also, when a session has fields on its form for specifying a client file or client folder, these fields have to be hidden when running in HTMLUI mode.

## unsupported client functions in HTMLUI mode
The following functions are not supported when the client runs in HTMLUI mode:

- [client2server()](../functions_client_file_access/client2server.md)

- [server2client()](../functions_client_file_access/server2client.md)

- [create.local.file()](../functions_client_file_access/create.local.file.md)

- [create.local.directory()](../functions_client_file_access/create.local.directory.md)

- [dir.select.dialog.local()](../functions_client_file_access/dir.select.dialog.local.md)

- [get.client.directory()](../functions_client_file_access/get.client.directory.md)

- [get.client.hostname()](../functions_client_file_access/get.client.hostname.md)

- [get.local.filename()](../functions_client_file_access/get.local.filename.md)

- [remove.local.directory()](../functions_client_file_access/remove.local.directory.md)

- [remove.local.file()](../functions_client_file_access/remove.local.file.md)

- [seq.fstat.local()](../functions_client_file_access/seq.fstat.local.md)

- [seq.open.dialog.local()](../functions_client_file_access/seq.open.dialog.local.md)

- [seq.open.dialog.next()](../functions_client_file_access/seq.open.dialog.next.md)

- [seq.saveas.dialog.local()](../functions_client_file_access/seq.saveas.dialog.local.md)

- [start.application.local()](../functions_client_file_access/start.application.local.md)

When one of these functions is used while running in HTMLUI mode, the following message appear:
This function is not supported in the LN UI: <function>

## LN UI client functions
The following functions have to be used when the client runs in HTMLUI mode:
Single file functions:

- [client.upload.file](../functions_client_file_access/client.upload.file.md)

- [client.download.file](../functions_client_file_access/client.download.file.md)

- [client.show.file](../functions_client_file_access/client.show.file.md)

Multiple file functions:

- [client.prepare.download](../functions_client_file_access/client.prepare.download.md)

- [client.add.download.file](../functions_client_file_access/client.add.download.file.md)

- [client.start.download](../functions_client_file_access/client.start.download.md)

- [client.upload.files](../functions_client_file_access/client.upload.files.md)

- [client.get.upload.filecount](../functions_client_file_access/client.get.upload.filecount.md)

- [client.get.upload.file](../functions_client_file_access/client.get.upload.file.md)

- [client.delete.upload.file.object](../functions_client_file_access/client.delete.upload.file.object.md)

Assisting functions:

- [get.ui.mode()](../functions_system_and_user_information/get.ui.mode.md)

- [tc.is.html.ui()](../functions_webtop/tc.is.html.ui.md)

- [tc.is.thin.client()](../functions_webtop/tc.is.thin.client.md)

- [client.get.media.type](../functions_client_file_access/client.get.media.type.md)

When one of the LN UI client functions is used while NOT running in HTMLUI mode, the following message appear:
This function is not supported in the WebUI: <function>

## LN UI detection
Two functions are available to detect whether a session should run in HTMLUI mode

- [get.ui.mode()](../functions_system_and_user_information/get.ui.mode.md)

- [tc.is.html.ui()](../functions_webtop/tc.is.html.ui.md)

## Implement LN UI support
To Support LN UI, the developer has to:

- Cleanup the UI of the session by hiding form fields used for entering a client file or a client folder. Note: also remove checks of these fields (check.input or DAL is.valid hook)

- Implement an alternative path for accessing client files based on legitmate LN UI functions.

Restrictions to LN UI support:

- Starting a client application without a file is no longer supported.

- It strongly depends on the user (as the user is in control when LN UI) whether a client application is opened.

## Hiding form fields
Characteristics: session allows user to specify a file on the client. The entered client path is used to access (create, open, etc) a file on the client machine

## before.program
The location to hide the fields is the before.program section of the UI-script. Add the following code in this section with the appropriate field names:
```

if tc.is.html.ui() then
	inputfield.invisible("<name of field 1>")
	inputfield.invisible("<name of field 2>")  ... etc
endif
```

## Skip validation of hidden fields
Although you've hidden the field, validation checks might still go off. Use the tc.is.html.ui() function to check the UI-mode and only validate these fields if the UI-mode is not HTMLUI. E.g.:
```

field.curr.impf:
check.input:
	string	impf.dir(255) mb
	string	impf.file(255) mb
	long	size

	if not tc.is.html.ui() then
		if isspace(curr.impf) then
			set.input.error("ttadv227006")
			|* Enter (correct) path.
		endif
	endif
```

## Displaying File alternative
Characteristics: session displays a file with server2client followed by start.application.local.
The construction usally looks something like:
```

if server2client(aServerFile, aClientFile, textMode) = 0 then
	aClientApplication = "anApplication.exe"
	start.application.local(aClientApplication & " " &
			quoted.string(aClientFile), aWaitFlag, someExitCode)
endif
```
Displaying a file in HTMLUI mode can be done using one of the following two functions:

- [client.show.file](../functions_client_file_access/client.show.file.md)

- [client.download.file](../functions_client_file_access/client.download.file.md)- followed by the user opening the downloaded file

The main differences between these functions are:

- [client.download.file](../functions_client_file_access/client.download.file.md) shows a dialog in whitch the user can choose to download the file. [client.show.file](../functions_client_file_access/client.show.file.md) does not show a dialog but directly shows or downloads the file.

- [client.download.file](../functions_client_file_access/client.download.file.md) waits until the user closes the download dialog. [client.show.file](../functions_client_file_access/client.show.file.md) returns immediately. The actual file transfer to the client is done later so the file cannot be removed immediately after [client.show.file](../functions_client_file_access/client.show.file.md) returns. The optional parameter "remove.after.download" of [client.show.file](../functions_client_file_access/client.show.file.md) can be used to control automatic removal of the server file after the file has been downloaded by the client.

- [client.show.file](../functions_client_file_access/client.show.file.md) will show some browser recognized file types immediately inside the browser. [client.download.file](../functions_client_file_access/client.download.file.md) will always download the file to the client file system.

Browsers typically recognizes files with the following file extensions:

- .txt - mime type: text/plain

- .pdf - mime type: application/pdf

- .htm(l) - mime type: text/html,

- images - mime type: image/*

Note  It is highly recommended to use client.show.file(). This function will stream the file directly to the browser without the download question being asked.

## HTML support - for other file types than .txt, .pdf and .htm(l) and images
For commonly used extensions (e.g..xlsx,.docx) the client will most likely have an application associated with the file extension. For unknown file extensions, the user will be asked which application to associate with the file extension of the downloaded file. When the user decides to open the file, the associated application will automatically be launched to open the file. The HTMLUI support code will look something like:
```

if tc.is.html.ui() then
	client.show.file(aServerFile, false, "", "", aMimeType)
else
	… original code as depicted in the box above
endif
```
Note  Either the file extension of the file name should be set correctly (e.g. “.txt”) or the mime type should be set accordingly (e.g. “text/plain”). This enables the client running in LN UI to use the correct application for opening the file.

## HTML support - for .txt, .pdf and htm(l) and images
For files with a.txt,.pdf, htm(l) and images extension, the file can be streamed to the browser without actually downloading the file. This means that the user will not be asked explicitly for the download. This function automatically shows the content of the file in a new tab or a new browser.
```

if tc.is.html.ui() then
	client.show.file(aServerFile, aNewWindow, aTitle, aMimeType)
else
	… original code …
endif
```
Note  this variant may open a separate window when aNewWindow is set to true.

## Editing File alternative
Characteristics: copy a server file to the client with server2client followed by start.application.local to edit the file and copy the changed file back to the server with client2server
The construction is usually something like:
```

if server2client(aServerFile, aClientFile, textMode) = 0 then
	aClientApplication = “anApplication.exe”
	start.application.local(aClientApplication & " " &
			quoted.string(aClientFile), aWaitFlag, someExitCode)
	client2server(aClientFile, aServerFile, textMode, true)
endif
```
The Single action for editing has to be replace with two actions:

- An action to download the file from the server to the client. Afterwards the user can edit the file with the appropriate application.

- An action to upload the changed file from the client to the server.

## LN UI support - download/edit part
```

if tc.is.html.ui() then
	client.download.file(aServerFile, aMimeType)
else
	… original code as depicted in the box above
endif
```

## LN UI support - download zipped archive
```

long	handle

if tc.is.html.ui() then
	| Zip files and directories in file with .zip extension
	handle = zipinfo.new(aServerZipFile)
	zipinfo.add(handle, aServerFile1)
	zipinfo.add(handle, aServerFile2)
	zipinfo.add(handle, aServerDirectory1)
	zipinfo.add(handle, aServerDirectory2)
	zipfile.build(handle)
	zipinfo.delete(handle)

	| Delete intermediate zipfile
	client.show.file(aServerZipFile, false, ””, ””, ””, ””, true)
else
	… original code as depicted in the box above
endif
```

## HTML support - upload part
The upload part requires the following two changes:

- a form command implementation that will upload the file from the client back to the server.

- a command on the session/form to call this implementation. This command is only available if the client is running in HTMLUI mode.

The form command implementation will look something like:
```

Function extern upload.file()
{
	client.upload.file(aServerFile, theSelectedClientFile, aMimeType)
}
```
or with uploading a zip archive
```

Function extern upload.and.unzip.archive()
{
	client.upload.file(aServerArchive, aServerZipFile)
	zipfile.extract(aServerZipFile, theRootSelectedArchive)
	| Delete intermediate extracted zipfile
	file.rm(aServerZipFile)
}
```
Note  there is a risk that the server file was changed in the mean time. Uploading an old version of the file will overwrite these changes. When implementing this two phased (i.e. download/upload) approach for editing a file, a mechanism should be added to determine whether the server file has been changed in the meantime. If a changed server file is detected, the user should be warned and ask to continue before performing the actual upload.
The form command can be removed from the session by:
```

after.form.read:
	if not tc.is.html.ui() then
		remove.form.commands("upload.file")
	endif
```

## GBF
GBF is fully supported in LN UI but there is one usage pattern which is difficult to support in LN UI. Node descriptions in a tabular manner in BW only works when using fixed-sized fonts. (all characters have the same width)
Using a fixed-sized font is archieved in Worktop/BW due to the fact that the application passes the value: GBF.OPT.FONT.FIXED in the gbf.init() call.
In case of Webui, the WebUI is not able to determine the column bounderies.

## LN UI support - use fixed fonts (not recommended)
By using fixed width fonts in LN UI for GBF descriptions, the alignment of the characters in the description remains correct. As described above, this can be achieved by performing a gbf.init() call with the GBF.OPT.FONT.FIXED passed. However, fixed width fonts are not that pretty to and might even harm the overall look and feel of the UI.

## LN UI support - use variable width fonts (recommended)
To display descriptions in a tabular manner with variable width fonts, the function gbf.desc.to.column() can be used.
So, whenever the gbf.add.object is called with a ‘formatted’ description (see example below:
```

func.ret = gbf.add.object(where.used.key,
		sprintf$("%4d %3d %47s %15s %13.4g %3d %6s "&
		"%u002 %U001 %6s %u002 %U001 ",
		tibom010.pono,tibom010.seqn,
		tibom010.mitm, tcibd001.dsca(1;15),
		tibom010.qana, tibom010.opno, tibom010.efco,
		tibom010.indt, tibom010.indt,
		tibom010.exco, tibom010.exdt, tibom010.exdt),
		WHERE.VAL, GBF.LEAF, par.leaf.val, 0, 0, 0,
		MASK.TOOLS, line.col, line.style)
```
the call must be changed into:
```

func.ret = gbf.add.object(where.used.key,
		gbf.desc.to.column(
		tibom010.pono,tibom010.seqn,
		tibom010.mitm, tcibd001.dsca(1;15),
		tibom010.qana, tibom010.opno, tibom010.efco,
		tibom010.indt, tibom010.indt,
		tibom010.exco, tibom010.exdt, tibom010.exdt),
		WHERE.VAL, GBF.LEAF, par.leaf.val, 0, 0, 0,
		MASK.TOOLS, line.col, line.style)
```
Note  as gbf.desc.to.column also works for other UIs (e.g. BW and WebUI), there is no need use tc.is.html.ui() to check client mode.
