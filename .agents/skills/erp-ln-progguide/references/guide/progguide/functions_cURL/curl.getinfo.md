# curl.getinfo

## Syntax:
`function void curl.getinfo( )`

## Description
This isn't the actual function. This help topic lists all curl.getinfo functions.
See [curl website](https://curl.se/) for more information on these functions
```

	double	curl.getinfo.connect_time()
	double	curl.getinfo.content_length_download()
	double	curl.getinfo.content_length_upload()
	double	curl.getinfo.namelookup_time()
	double	curl.getinfo.pretransfer_time()
	double	curl.getinfo.redirect_time()
	double	curl.getinfo.size_download()
	double	curl.getinfo.size_upload()
	double	curl.getinfo.speed_download()
	double	curl.getinfo.speed_upload()
	double	curl.getinfo.starttransfer_time()
	double	curl.getinfo.total_time()

	long	curl.getinfo.filetime()
	long	curl.getinfo.header_size()
	long	curl.getinfo.http_connectcode()
	long	curl.getinfo.httpauth_avail()
	long	curl.getinfo.lastsocket()
	long	curl.getinfo.num_connects()
	long	curl.getinfo.os_errno()
	long	curl.getinfo.proxyauth_avail()
	long	curl.getinfo.redirect_count()
	long	curl.getinfo.request_size()
	long	curl.getinfo.response_code()
	long	curl.getinfo.ssl_verifyresult()
	long	curl.getinfo.cookielist()

	string	curl.getinfo.content_type$()
	string	curl.getinfo.effective_url$()
	string	curl.getinfo.ftp_entry_path$()
```

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [cURL handling overview](overview.md)

- [cURL website](https://curl.se/)
