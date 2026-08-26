# cURL email example
This example shows how an email can be sent to multiple recipients and arbitrary "from" address using cURL. Error handling is not fully handled in this example. The return value of all functions need to be checked when similar code is used in production environments.

## Main routine
The basic cURL functions as used in the example below are available starting at bshell TIV level 2001.
```

function main()
{
        long status
        string url(100)
        long ListId, fp

        | This must be the name of your SMTP server.
        url = "smtp://mail.infor.com."
        status = curl.setopt.url(url)

        curl.setopt.mail_from("<sender.name@example.org>")

        | This string will be used to specify the authentication address (identity)
        | of a submitted message that is being relayed to another server.
        curl.setopt.mail_auth("sender.name@example.org")

        | Add all mail recipients here.
        ListId = 0
        ListId = curl.slist.append(ListId,"<recipient1@some.place.org>"))
        ListId = curl.slist.append(ListId,"<recipient2@some.other.org>"))
        curl.setopt.mail_rcpt(ListId))

        | There are various ways to provide the body of the mail. This uses a file.
        | The contents of the file should at least have a "Subject: " followed
        | by an empty line, followed by the body of the mail.
        fp = seq.open("body_of_mail.txt", "r")
        curl.setopt.readdata(fp)
        curl.setopt.upload(1)

        | actually send the mail
        status = curl.perform()

        seq.close(fp)
}
```
