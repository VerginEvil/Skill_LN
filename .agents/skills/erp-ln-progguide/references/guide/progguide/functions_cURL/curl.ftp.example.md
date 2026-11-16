# cURL FTP example
This example shows how a file can be uploaded by using cURL. Error handling is not fully handled in this example. The return value of all functions needs to be checked when similar code is used in production environments.

## Main routine
The basic cURL functions as used in the example below are available starting at bshell TIV level 1700.
```

function main()
{
    | Init
    curl.reset()

    string destination(512)
    destination = getenv$("DESTINATION")
    if (destination(1;3) = "ftp")
    then
        | ftp based protocol
        | force binary transfer (which is also default)
        curl.setopt.transfertext(0)
    else
        if (destination(1;4) = "http")
        then
            | http based protocol
            curl.setopt.httpauth(CURLAUTH_ANY)
            | no HTTP body included in post
            curl.setopt.nobody(1)
        endif
    endif

    | This code expects that user and password are not part of the destination URL,
    | but passed in the environment.
    string authuser(512)
    authuser = getenv$("AUTH_USER")

    | Do not allow empty user names
    curl.setopt.username(authuser)

    string authpasswd(512)
    authpasswd = getenv$("AUTH_PASSWD")
    | do not allow empty passwords
    if (authpasswd(1;1) = "$")
    then
        | Encrypted form
        curl.setopt.encrypted.password(authpasswd)
    else
        | Assumption: unencrypted form
        curl.setopt.password(authpasswd)
    endif

    string ftpfile(512)
    ftpfile = getenv$("UPLOADFILE")
    long fp
    fp = seq.open(ftpfile, "r")
    if (fp > 0)
    then
        | Note that destination directory needs to exist if the destination
        | ftp server does not allow creation of directories.
        | Set option to silently create directories, if server supports it.
        curl.setopt.ftp_create_missing_dirs(1)

        | Set destination URL (no rename is done)
        curl.setopt.url(destination & "/" & ftpfile)

        | connect input stream to curl
        curl.setopt.readdata(fp)

        | prepare for upload
        curl.setopt.upload(1)

        | default: no progress (there is no interface to CURLOPT_PROGRESSFUNCTION either)
        | setting progress will affect the output
        curl.setopt.noprogress(1)

        | send verbose output to stderr if you want it. Otherwise, it will affect stderr.
        curl.setopt.verbose(0)

        | perform the cURL request
        long curlRet
        curlRet = curl.perform()

        | close input file
        seq.close(fp)
    endif
}
```
