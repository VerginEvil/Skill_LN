# curl.setopt

## Syntax:
`function long curl.setopt( )`

## Description
This is not an actual function. This help topic lists all curl.setopt functions. See curl website for more information on these functions.
The general principle is: For most 'easy' cURL options that accept some value (like ` curl_easy_setopt(h,OptionName,OptionValue)` there is a corresponding bshell function that is called `curl.OptionName(OptionValue)`.
The `OptionValue` can be a long or a string, depending on the option being set. For example, the cURL call to set a buffer size is:
` curl_easy_setopt(h,CURLOPT_BUFFERSIZE,size)`
And so the bshell equivalent is:
`long curl.setopt.buffersize(size)`
Note: Not all cURL functions are supported (they can conflict with internal bshell functions, be operating system specific, or various other reasons). The supported options also vary over time (as new versions of the underlying cURL are supported) and/or new support is added to the bshell.
Other functions require more elaborate translations between the structures, pointers and lists used by native cURL and the bshell. For example, see the multipart MIME support functions.
Available from TIV >= 1402
```

	long curl.setopt.altsvc_ctrl(aParameter)
	long curl.setopt.append(aParameter)
	long curl.setopt.autoreferer(aParameter)
	long curl.setopt.buffersize(aParameter)
	long curl.setopt.connect_only(aParameter)
	long curl.setopt.connecttimeout(aParameter)
	long curl.setopt.connecttimeout_ms(aParameter)
	long curl.setopt.cookiesession(aParameter)
	long curl.setopt.crlf(aParameter)
	long curl.setopt.dirlistonly(aParameter)
	long curl.setopt.disallow_username_in_url(aParameter)
	long curl.setopt.dns_cache_timeout(aParameter)
	long curl.setopt.dns_shuffle_addresses(aParameter)
	long curl.setopt.dns_use_global_cache(aParameter)
	long curl.setopt.doh_ssl_verifyhost(aParameter)
	long curl.setopt.doh_ssl_verifypeer(aParameter)
	long curl.setopt.doh_ssl_verifystatus(aParameter)
	long curl.setopt.failonerror(aParameter)
	long curl.setopt.filetime(aParameter)
	long curl.setopt.followlocation(aParameter)
	long curl.setopt.forbid_reuse(aParameter)
	long curl.setopt.fresh_connect(aParameter)
	long curl.setopt.ftp_create_missing_dirs(aParameter)
	long curl.setopt.ftp_filemethod(aParameter)
	long curl.setopt.ftp_skip_pasv_ip(aParameter)
	long curl.setopt.ftpsslauth(aParameter)
	long curl.setopt.ftp_ssl_ccc(aParameter)
	long curl.setopt.ftp_use_eprt(aParameter)
	long curl.setopt.ftp_use_epsv(aParameter)
	long curl.setopt.happy_eyeballs_timeout_ms(aParameter)
	long curl.setopt.haproxyprotocol(aParameter)
	long curl.setopt.header(aParameter)
	long curl.setopt.hsts_ctrl(aParameter)
	long curl.setopt.http09_allowed(aParameter)
	long curl.setopt.httpauth(aParameter)
	long curl.setopt.http_content_decoding(aParameter)
	long curl.setopt.httpget(aParameter)
	long curl.setopt.httpproxytunnel(aParameter)
	long curl.setopt.http_transfer_decoding(aParameter)
	long curl.setopt.http_version(aParameter)
	long curl.setopt.ignore_content_length(aParameter)
	long curl.setopt.infilesize(aParameter)
	long curl.setopt.ipresolve(aParameter)
	long curl.setopt.localport(aParameter)
	long curl.setopt.localportrange(aParameter)
	long curl.setopt.low_speed_limit(aParameter)
	long curl.setopt.low_speed_time(aParameter)
	long curl.setopt.maxage_conn(aParameter)
	long curl.setopt.maxconnects(aParameter)
	long curl.setopt.maxfilesize(aParameter)
	long curl.setopt.maxredirs(aParameter)
	long curl.setopt.netrc(aParameter)
	long curl.setopt.new_directory_perms(aParameter)
	long curl.setopt.new_file_perms(aParameter)
	long curl.setopt.nobody(aParameter)
	long curl.setopt.noprogress(aParameter)
	long curl.setopt.nosignal(aParameter)
	long curl.setopt.port(aParameter)
	long curl.setopt.post(aParameter)
	long curl.setopt.postfieldsize(aParameter)
	long curl.setopt.protocols(aParameter)
	long curl.setopt.proxyauth(aParameter)
	long curl.setopt.proxyport(aParameter)
	long curl.setopt.proxy_transfer_mode(aParameter)
	long curl.setopt.proxytype(aParameter)
	long curl.setopt.put(aParameter)
	long curl.setopt.resume_from(aParameter)
	long curl.setopt.ssh_auth_types(aParameter)
	long curl.setopt.sslengine_default(aParameter)
	long curl.setopt.ssl_sessionid_cache(aParameter)
	long curl.setopt.ssl_verifyhost(aParameter)
	long curl.setopt.ssl_verifypeer(aParameter)
	long curl.setopt.sslversion(aParameter)
	long curl.setopt.tcp_nodelay(aParameter)
	long curl.setopt.timecondition(aParameter)
	long curl.setopt.timeout(aParameter)
	long curl.setopt.timeout_ms(aParameter)
	long curl.setopt.timevalue(aParameter)
	long curl.setopt.transfertext(aParameter)
	long curl.setopt.unrestricted_auth(aParameter)
	long curl.setopt.upkeep_interval_ms(aParameter)
	long curl.setopt.upload(aParameter)
	long curl.setopt.upload_buffersize(aParameter)
	long curl.setopt.use_ssl(aParameter)
	long curl.setopt.verbose(aParameter)

	string curl.setopt.aws_sigv4(aParameter)
	string curl.setopt.cainfo(aParameter)
	string curl.setopt.capath(aParameter)
	string curl.setopt.cookie(aParameter)
	string curl.setopt.cookiefile(aParameter)
	string curl.setopt.cookiejar(aParameter)
	string curl.setopt.cookielist(aParameter)
	string curl.setopt.copypostfields(aParameter)
	string curl.setopt.curlu(aParameter)
	string curl.setopt.customrequest(aParameter)
	string curl.setopt.doh_url(aParameter)
	string curl.setopt.egdsocket(aParameter)
	string curl.setopt.ftp_account(aParameter)
	string curl.setopt.ftp_alternative_to_user(aParameter)
	string curl.setopt.ftpport(aParameter)
	string curl.setopt.interface(aParameter)
	string curl.setopt.keypasswd(aParameter)
	string curl.setopt.krblevel(aParameter)
	string curl.setopt.netrc_file(aParameter)
	string curl.setopt.postfields(aParameter)
	string curl.setopt.protocols_str(aParameter)
	string curl.setopt.proxy(aParameter)
	string curl.setopt.proxy_issuercert(aParameter)
	string curl.setopt.proxyuserpwd(aParameter)
	string curl.setopt.random_file(aParameter)
	string curl.setopt.range(aParameter)
	string curl.setopt.redir_protocols_str(aParameter)
	string curl.setopt.referer(aParameter)
	string curl.setopt.sasl_authzid(aParameter)
	string curl.setopt.ssh_host_public_key_md5(aParameter)
	string curl.setopt.ssh_private_keyfile(aParameter)
	string curl.setopt.ssh_public_keyfile(aParameter)
	string curl.setopt.sslcert(aParameter)
	string curl.setopt.sslcerttype(aParameter)
	string curl.setopt.ssl_cipher_list(aParameter)
	string curl.setopt.ssl_ec_curves(aParameter)
	string curl.setopt.sslengine(aParameter)
	string curl.setopt.sslkey(aParameter)
	string curl.setopt.sslkeytype(aParameter)
	string curl.setopt.tls13_ciphers(aParameter)
	string curl.setopt.url(aParameter)
	string curl.setopt.useragent(aParameter)
	string curl.setopt.userpwd(aParameter)

	long curl.setopt.writedata(long sioId)
	long curl.setopt.writeheader(long sioId)

	long curl.setopt.httpheader(long listId)
```
Available from TIV >= 1700
```

	long curl.setopt.ftp_use_pret(long OptionValue)
	long curl.setopt.postredir(long OptionValue)
	long curl.setopt.redir_protocols(long OptionValue)
	long curl.setopt.wildcardmatch(long OptionValue)

	long curl.setopt.noproxy(const string aString)
	long curl.setopt.password(const string aString)
	long curl.setopt.proxypassword(const string aString)
	long curl.setopt.proxyusername(const string aString)
	long curl.setopt.username(const string aString)

	long curl.setopt.readdata(long sioId)
```
Available from TIV >= 1724
```

	long curl.setopt.issuercert(const string aString)
	long curl.setopt.crlfile(const string aString)
```
Available from TIV >= 1903
```

	long curl.setopt.quote(long listId)
	long curl.setopt.prequote(long listId)
	long curl.setopt.postquote(long listId)
```
Available from TIV >= 2010
```

	long curl.setopt.mail_from(const string mailaddress)
	long curl.setopt.mail_auth(const string mailaddress)
	long curl.setopt.mail_rcpt(long listId)
```
Available from TIV >= 2220
A new function to retrieve the version of the underlying cURL package. [curl.version()](curl.version.md)
These are functions to send mail, or post multi-part MIME messages to a web server. The full documentation can be found on the cURL website, [cURL MIME example](curl.mime.example.md) that demonstrates how to use these functions.
```

	long curl.mime.init      ()
	long curl.mime.addpart   (long mime_handle)
	long curl.mime.name      (long mime_handle, const string name())
	long curl.mime.data      (long PartId, const string data(), [long datasize])
	long curl.mime.data_cb   (long PartId, long sio_id, long datasize)
	long curl.mime.filedata  (long PartId, const string local_filename())
	long curl.mime.filename  (long PartId, const string remote_filename())
	long curl.mime.subparts  (long PartId, long mime_handle)
	long curl.mime.type      (long PartId, const string type())
	long curl.mime.headers   (long PartId, long slist_id)
	long curl.mime.encoder   (long PartId, const string encoding())
	void curl.mime.free      (long mime_handle)
	long curl.setopt.mimepost(long mime_handle)

	| These are 'long' options
	long curl.setopt.accepttimeout_ms(OptionValue)
	long curl.setopt.address_scope(OptionValue)
	long curl.setopt.certinfo(OptionValue)
	long curl.setopt.expect_100_timeout_ms(OptionValue)
	long curl.setopt.gssapi_delegation(OptionValue)
	long curl.setopt.headeropt(OptionValue)
	long curl.setopt.keep_sending_on_error(OptionValue)
	long curl.setopt.path_as_is(OptionValue)
	long curl.setopt.pipewait(OptionValue)
	long curl.setopt.proxy_sslversion(OptionValue)
	long curl.setopt.proxy_ssl_options(OptionValue)
	long curl.setopt.proxy_ssl_verifyhost(OptionValue)
	long curl.setopt.proxy_ssl_verifypeer(OptionValue)
	long curl.setopt.rtsp_client_cseq(OptionValue)
	long curl.setopt.rtsp_request(OptionValue)
	long curl.setopt.rtsp_server_cseq(OptionValue)
	long curl.setopt.sasl_ir(OptionValue)
	long curl.setopt.socks5_auth(OptionValue)
	long curl.setopt.socks5_gssapi_nec(OptionValue)
	long curl.setopt.ssh_compression(OptionValue)
	long curl.setopt.ssl_enable_alpn(OptionValue)
	long curl.setopt.ssl_enable_npn(OptionValue)
	long curl.setopt.ssl_falsestart(OptionValue)
	long curl.setopt.ssl_options(OptionValue)
	long curl.setopt.ssl_verifystatus(OptionValue)
	long curl.setopt.stream_weight(OptionValue)
	long curl.setopt.suppress_connect_headers(OptionValue)
	long curl.setopt.tcp_fastopen(OptionValue)
	long curl.setopt.tcp_keepalive(OptionValue)
	long curl.setopt.tcp_keepidle(OptionValue)
	long curl.setopt.tcp_keepintvl(OptionValue)
	long curl.setopt.tftp_blksize(OptionValue)
	long curl.setopt.tftp_no_options(OptionValue)
	long curl.setopt.transfer_encoding(OptionValue)

	| These are 'string' options supported by curl 7.57.0 and higher.
	long curl.setopt.chunk_data(aString)
	long curl.setopt.closesocketdata(aString)
	long curl.setopt.debugdata(aString)
	long curl.setopt.default_protocol(aString)
	long curl.setopt.dns_interface(aString)
	long curl.setopt.dns_local_ip4(aString)
	long curl.setopt.dns_local_ip6(aString)
	long curl.setopt.dns_servers(aString)
	long curl.setopt.login_options(aString)
	long curl.setopt.pinnedpublickey(aString)
	long curl.setopt.pre_proxy(aString)
	long curl.setopt.proxy_cainfo(aString)
	long curl.setopt.proxy_capath(aString)
	long curl.setopt.proxy_crlfile(aString)
	long curl.setopt.proxy_keypasswd(aString)
	long curl.setopt.proxy_pinnedpublickey(aString)
	long curl.setopt.proxy_service_name(aString)
	long curl.setopt.proxy_sslcert(aString)
	long curl.setopt.proxy_sslcerttype(aString)
	long curl.setopt.proxy_sslkey(aString)
	long curl.setopt.proxy_sslkeytype(aString)
	long curl.setopt.proxy_ssl_cipher_list(aString)
	long curl.setopt.proxy_tlsauth_password(aString)
	long curl.setopt.proxy_tlsauth_type(aString)
	long curl.setopt.proxy_tlsauth_username(aString)
	long curl.setopt.request_target(aString)
	long curl.setopt.rtsp_session_id(aString)
	long curl.setopt.rtsp_stream_uri(aString)
	long curl.setopt.rtsp_transport(aString)
	long curl.setopt.service_name(aString)
	long curl.setopt.ssh_knownhosts(aString)
	long curl.setopt.tlsauth_password(aString)
	long curl.setopt.tlsauth_type(aString)
	long curl.setopt.tlsauth_username(aString)
	long curl.setopt.xoauth2_bearer(aString)
```
Bit options for setopt.httpauth and setopt.proxyauth. Multiple options can be or'ed with bit.or().
```

	CURLAUTH_NONE
	CURLAUTH_BASIC
	CURLAUTH_DIGEST
	CURLAUTH_GSSNEGOTIATE
	CURLAUTH_NTLM
	CURLAUTH_DIGEST_IE
	CURLAUTH_NTLM_WB
	CURLAUTH_ONLY
```
Combined options
```

	CURLAUTH_ANY
	CURLAUTH_ANYSAFE (=all except BASIC and DIGIST_IE)
```
Bit options for setopt.postredir. Multiple options can be or'ed with bit.or().
```

	CURL_REDIR_POST_301
	CURL_REDIR_POST_302
	CURL_REDIR_POST_303
```
Combined options
```

	CURL_REDIR_POST_ALL
```
Options for curl.setopt.http_version.
```

	CURL_HTTP_VERSION_NONE
	CURL_HTTP_VERSION_1_0
	CURL_HTTP_VERSION_1_1
```
Available from TIV >= 2540
```

	long curl.setopt.quick_exit(aParameter)
	long curl.setopt.ca_cache_timeout(aParameter)
	long curl.setopt.mime_options(aParameter)
	long curl.setopt.tcp_keepcnt(aParameter)
	long curl.setopt.maxlifetime_conn(aParameter)
	long curl.setopt.mail_rcpt_allowfails(aParameter)
	long curl.setopt.server_response_timeout(aParameter)
	long curl.setopt.server_response_timeout_ms(aParameter)

	string curl.setopt.accept_encoding(aParameter)
	string curl.setopt.haproxy_client_ip(aParameter)
	string curl.setopt.ssh_host_public_key_sha256(aParameter)

	string curl.getinfo.cainfo()
	string curl.getinfo.capath()
	long   curl.getinfo.used_proxy()
```
These return curl_off_t longs: in 64 bit mode they can be very large values and in 32-bit mode they will return errors on overflow (with a warning log message).
```

	long curl.setopt.maxfilesize_large(aParameter)
	long curl.setopt.max_recv_speed_large(aParameter)
	long curl.setopt.max_send_speed_large(aParameter)
	long curl.setopt.postfieldsize_large(aParameter)
	long curl.setopt.resume_from_large(aParameter)
	long curl.setopt.timevalue_large(aParameter)
	long curl.setopt.xoauth2_encrypted_bearer(aParameter)

	long curl.getinfo.appconnect_time_t()
	long curl.getinfo.conn_id()
	long curl.getinfo.connect_time_t()
	long curl.getinfo.content_length_download_t()
	long curl.getinfo.content_length_upload_t()
	long curl.getinfo.filetime_t()
	long curl.getinfo.namelookup_time_t()
	long curl.getinfo.pretransfer_time_t()
	long curl.getinfo.queue_time_t()
	long curl.getinfo.redirect_time_t()
	long curl.getinfo.retry_after()
	long curl.getinfo.size_download_t()
	long curl.getinfo.size_upload_t()
	long curl.getinfo.speed_download_t()
	long curl.getinfo.speed_upload_t()
	long curl.getinfo.starttransfer_time_t()
	long curl.getinfo.total_time_t()
	long curl.getinfo.xfer_id()
```
Most cURL constants for error codes and options for various functions are also available in bic_bshell since TIV 2540. The complete list is in alphabetical order is:
```

	CURLE_OK (0)

	CURLE_ABORTED_BY_CALLBACK
	CURLE_AGAIN
	CURLE_AUTH_ERROR
	CURLE_BAD_CALLING_ORDER
	CURLE_BAD_CONTENT_ENCODING
	CURLE_BAD_DOWNLOAD_RESUME
	CURLE_BAD_FUNCTION_ARGUMENT
	CURLE_BAD_PASSWORD_ENTERED
	CURLE_CHUNK_FAILED
	CURLE_CONV_FAILED
	CURLE_CONV_REQD
	CURLE_COULDNT_CONNECT
	CURLE_COULDNT_RESOLVE_HOST
	CURLE_COULDNT_RESOLVE_PROXY
	CURLE_ECH_REQUIRED
	CURLE_FAILED_INIT
	CURLE_FILE_COULDNT_READ_FILE
	CURLE_FILESIZE_EXCEEDED
	CURLE_FTP_ACCEPT_FAILED
	CURLE_FTP_ACCEPT_TIMEOUT
	CURLE_FTP_BAD_FILE_LIST
	CURLE_FTP_CANT_GET_HOST
	CURLE_FTP_COULDNT_RETR_FILE
	CURLE_FTP_COULDNT_SET_TYPE
	CURLE_FTP_COULDNT_USE_REST
	CURLE_FTP_PORT_FAILED
	CURLE_FTP_PRET_FAILED
	CURLE_FTP_WEIRD_227_FORMAT
	CURLE_FTP_WEIRD_PASS_REPLY
	CURLE_FTP_WEIRD_PASV_REPLY
	CURLE_FTP_WEIRD_SERVER_REPLY
	CURLE_FUNCTION_NOT_FOUND
	CURLE_GOT_NOTHING
	CURLE_HTTP_POST_ERROR
	CURLE_HTTP_RETURNED_ERROR
	CURLE_HTTP2
	CURLE_HTTP2_STREAM
	CURLE_HTTP3
	CURLE_INTERFACE_FAILED
	CURLE_LDAP_CANNOT_BIND
	CURLE_LDAP_INVALID_URL
	CURLE_LDAP_SEARCH_FAILED
	CURLE_LOGIN_DENIED
	CURLE_NO_CONNECTION_AVAILABLE
	CURLE_NOT_BUILT_IN
	CURLE_OPERATION_TIMEDOUT
	CURLE_OUT_OF_MEMORY
	CURLE_PARTIAL_FILE
	CURLE_PEER_FAILED_VERIFICATION
	CURLE_PROXY
	CURLE_QUIC_CONNECT_ERROR
	CURLE_QUOTE_ERROR
	CURLE_RANGE_ERROR
	CURLE_READ_ERROR
	CURLE_RECURSIVE_API_CALL
	CURLE_RECV_ERROR
	CURLE_REMOTE_ACCESS_DENIED
	CURLE_REMOTE_DISK_FULL
	CURLE_REMOTE_FILE_EXISTS
	CURLE_REMOTE_FILE_NOT_FOUND
	CURLE_RTSP_CSEQ_ERROR
	CURLE_RTSP_SESSION_ERROR
	CURLE_SEND_ERROR
	CURLE_SEND_FAIL_REWIND
	CURLE_SSH
	CURLE_SSL_CACERT
	CURLE_SSL_CACERT_BADFILE
	CURLE_SSL_CERTPROBLEM
	CURLE_SSL_CIPHER
	CURLE_SSL_CLIENTCERT
	CURLE_SSL_CONNECT_ERROR
	CURLE_SSL_CRL_BADFILE
	CURLE_SSL_ENGINE_INITFAILED
	CURLE_SSL_ENGINE_NOTFOUND
	CURLE_SSL_ENGINE_SETFAILED
	CURLE_SSL_INVALIDCERTSTATUS
	CURLE_SSL_ISSUER_ERROR
	CURLE_SSL_PINNEDPUBKEYNOTMATCH
	CURLE_SSL_SHUTDOWN_FAILED
	CURLE_TELNET_OPTION_SYNTAX
	CURLE_TFTP_ILLEGAL
	CURLE_TFTP_NOSUCHUSER
	CURLE_TFTP_NOTFOUND
	CURLE_TFTP_PERM
	CURLE_TFTP_UNKNOWNID
	CURLE_TOO_LARGE
	CURLE_TOO_MANY_REDIRECTS
	CURLE_UNKNOWN_OPTION
	CURLE_UNKNOWN_TELNET_OPTION
	CURLE_UNRECOVERABLE_POLL
	CURLE_UNSUPPORTED_PROTOCOL
	CURLE_UPLOAD_FAILED
	CURLE_URL_MALFORMAT
	CURLE_USE_SSL_FAILED
	CURLE_WRITE_ERROR

	Constants that can be used in various setopt and getinfo calls:

	CURLFTPAUTH_DEFAULT
	CURLFTPAUTH_SSL
	CURLFTPAUTH_TLS

	CURLFTPMETHOD_DEFAULT
	CURLFTPMETHOD_MULTICWD
	CURLFTPMETHOD_NOCWD
	CURLFTPMETHOD_SINGLECWD

	CURLFTPSSL_CCC_NONE
	CURLFTPSSL_CCC_PASSIVE
	CURLFTPSSL_CCC_ACTIVE

	CURLFTP_CREATE_DIR_NONE
	CURLFTP_CREATE_DIR
	CURLFTP_CREATE_DIR_RETRY

	CURLPROXY_HTTP
	CURLPROXY_HTTPS
	CURLPROXY_HTTP_1_0
	CURLPROXY_HTTPS2
	CURLPROXY_SOCKS4
	CURLPROXY_SOCKS5
	CURLPROXY_SOCKS4A

	CURLUSESSL_NONE
	CURLUSESSL_TRY
	CURLUSESSL_CONTROL
	CURLUSESSL_ALL

	CURL_HTTP_VERSION_2

	CURL_HTTP_VERSION_3ONLY

	CURLMIMEOPT_FORMESCAPE
	CURLALTSVC_READONLYFILE
	CURLALTSVC_H1
	CURLALTSVC_H2
	CURLALTSVC_H3

	CURLAUTH_AWS_SIGV4
	CURLAUTH_NEGOTIATE
	CURLAUTH_GSSAPI

	CURLGSSAPI_DELEGATION_NONE
	CURLGSSAPI_DELEGATION_POLICY_FLAG
	CURLGSSAPI_DELEGATION_FLAG

	CURLHEADER_UNIFIED
	CURLHEADER_SEPARATE

	CURLPAUSE_RECV_CONT
	CURLPAUSE_RECV
	CURLPAUSE_SEND_CONT
	CURLPAUSE_SEND

	CURLSSLOPT_ALLOW_BEAST
	CURLSSLOPT_NO_REVOKE
	CURLSSLOPT_NO_PARTIALCHAIN
	CURLSSLOPT_REVOKE_BEST_EFFORT
	CURLSSLOPT_NATIVE_CA
	CURLSSLOPT_AUTO_CLIENT_CERT

	CURL_ERROR_SIZE
	CURL_HET_DEFAULT
	CURL_MAX_READ_SIZE
	CURL_MAX_WRITE_SIZE

	CURL_IPRESOLVE_WHATEVER
	CURL_IPRESOLVE_V4
	CURL_IPRESOLVE_V6

	CURL_UPKEEP_INTERVAL_DEFAULT
```

## Return values
| | |
|---|---|
| 0 | Option set |
| 1 | Illegal option value |
| CURLE_UNKNOWN_OPTION | Option not known by current curl. |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  The use of the function curl.setopt.sslversion() is discouraged. By default the most secure protocol will be used (TLSv1.2 or higher).

## Related topics
- [cURL handling overview](overview.md)
- cURL website
- [TIV Overview](../tiv/tiv_overview.md)
