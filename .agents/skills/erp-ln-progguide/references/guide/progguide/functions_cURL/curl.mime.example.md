# cURL MIME example
This example shows how a mail message can be sent with multiple attachments, the source of the attachment coming from various places.
Error handling is not fully handled in this example. The return value of all functions needs to be checked when similar code is used in production environments.
The full documentation of the MIME functions can be found on de cURL website. Keep in mind that the bshell does not support pointers, so these are translated to type `long` handles. Other than that, the bshell does not interfere with the functionality of the cURL functions.

## Main routine
The basic cURL functions as used in the example below are available starting at bshell TIV level 2220.
The example demonstrates that the source of the attachment data can come from a string, an open stream and a (local) file name. The result is mail with 3 attachments and one in-line HTML text part.
```

function void   main()
{
        long    MimeH, bodyPart, MimeP1, MimeP2, MimeP3
        long    ListMailHeaders, ListBodyHeaders, ListMailRcpt
        long    size, mode, inode, dev, uid, gid, n.link, c.time, a.time, m.time

        | Create a multi-part MIME message. It all starts with a MIME handle.
        MimeH = curl.mime.init()

        |---------------------------------------------------------------------------------
        | Construct global headers for the mail message
        ListMailHeaders = 0
        ListMailHeaders = curl.slist.append(ListMailHeaders,"Subject: Example subject")
        ListMailHeaders = curl.slist.append(ListMailHeaders,"Custom-Header1: Woof")
        curl.setopt.httpheader(ListMailHeaders)

        |---------------------------------------------------------------------------------
        | Construct the text of the body. Can be HTML or plain data. Use HTML here.
        long bodyfp
        string bodyfile(1000)
        bodyPart = curl.mime.addpart(MimeH)

        ListBodyHeaders = 0
        ListBodyHeaders = curl.slist.append(ListBodyHeaders,"Content-Disposition: inline")
        ListBodyHeaders = curl.slist.append(ListBodyHeaders,"Custom-Header2: Mooo")
        curl.mime.headers(bodyPart,ListBodyHeaders)
        curl.mime.type(bodyPart,"text/html")

        | Generate a file with some HTML lines.
        bodyfile = "WorkData.body"
        bodyfp = seq.open( bodyfile, "w" )
        seq.write("<html><body>" & lf$(), -1,bodyfp)
        seq.write("<H1>Big text</H1>" & lf$(), -1,bodyfp)
        seq.write("<p>This is body text<br>" & lf$(), -1,bodyfp)
        seq.write("This mail produced by Curl and Bshell<br>" & lf$(), -1,bodyfp)
        seq.write("</p></body></html>" & lf$(), -1,bodyfp)
        seq.close(bodyfp)

        | Find the size of the file
        stat.info(bodyfile, size, mode, inode, dev, uid, gid, n.link, c.time, m.time, a.time )

        | Open the file and pass the file handle and requested bytes to curl. Note that this
        | can be any type of stream handle that you can pass here!
        bodyfp = seq.open(bodyfile, "r")
        curl.mime.data_cb(bodyPart,bodyfp,size)

        |-------------------------------------
        | Add 3 attachements: One from a string, one from an open file, one
        | from a local existing file.
        MimeP1 = curl.mime.addpart(MimeH)   | Each part requires a handle
        MimeP2 = curl.mime.addpart(MimeH)
        MimeP3 = curl.mime.addpart(MimeH)

        | Set local names for the parts.
        curl.mime.name(MimeP1,"Part1")
        curl.mime.name(MimeP2,"Part2")
        curl.mime.name(MimeP3,"Part3")

        | Attach remote filenames to the parts. These will show up as the
        | name of the attachment in the mail itself.
        curl.mime.filename(MimeP1,"RemotePart1")
        curl.mime.filename(MimeP2,"RemotePart2")

        | This one will be lost, because the default remote name of an attached
        | file is the base name of the file itself.
        curl.mime.filename(MimeP3,"RemotePart3")
        |********************************************************************
        | Add data to part 1: Easy way: String. Note: Only the LAST string you
        | pass is actually used.
        curl.mime.data(MimeP1,"This data will be lost" & lf$())
        curl.mime.data(MimeP1,"This is some data to appear in part1" & lf$())
        curl.mime.type(MimeP1,"text/plain")

        |********************************************************************
        | Add data to part 2: With a callback to an open file
        | Create a local file with some junk, open it and attach that FP to part 2.
        | Note: The bshell handles the I/O callback.
        string fname1(1000)
        long fp1, i

        fname1 = WorkData.1"
        fp1 = seq.open( fname1, "w" )

        | Write a bunch of lines to the file. Any file size is acceptable.
        for i = 1 to 200
                seq.write(sprintf$("This is data from an opened file, line %d" & lf$(),i),-1,fp1)
        endfor
        seq.close(fp1)
        | Ask how many bytes it is.
        stat.info(fname1, size, mode, inode, dev, uid, gid, n.link, c.time, m.time, a.time )
        fp1 = seq.open(fname1, "r")

        | Now tell curl to use this open file as data source, and encode it in base64
        | Other types of encoding are possible. The entire file will be attached.
        curl.mime.data_cb(MimeP2,fp1,size)
        curl.mime.encoder(MimeP2,"base64")

        |********************************************************************
        | Add data to part 3: A local file
        string fname2(1000)
        long fp2
        fname2 = "WorkData.2"
        fp2 = seq.open( fname2, "w" )
        | Write some data to the file. Any size is acceptable.
        for i = 1 to 200
                seq.write(sprintf$("This is data from local file, line %d" & lf$(),i),-1,fp2)
        endfor
        seq.close(fp2)

        | Now tell curl to use this local file as a data source
        | Side-effect of filedata call is to set the remote name, so RemotePart3 is lost here
        curl.mime.filedata(MimeP3,fname2)
        curl.mime.encoder(MimeP3,"binary")

        |********************************************************************
        | Now set the destination and sender. The URL must be a valid SMTP server.
        curl.setopt.url("smtp://mail.acme.com")
        curl.setopt.mail_from("w.e.coyote@acme.com")

        | Then one or more recipients
        ListMailRcpt = 0
        ListMailRcpt = curl.slist.append(ListMailRcpt,"road.runner@acme.com")
        curl.setopt.mail_rcpt(ListMailRcpt)

        | Now actually do it.
        curl.setopt.mimepost(MimeH)
        curl.perform()

        | Now these lists can be freed. If you do this too early (before perform),
        | cURL will refer to freed memory and results will be unpredictable,
        | a bshell crash is likely!

        curl.slist.free.all(ListMailHeaders)
        curl.slist.free.all(ListBodyHeaders)
        curl.slist.free.all(ListMailRcpt)

        | And we're done!
        curl.mime.free(MimeH)
        curl.reset()
}
```
