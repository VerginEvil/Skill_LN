# oauth1_signature()

## Syntax:
`function long oauth1_signature( const string method, const string uri, const string consumer_secret, const string token_secret, ref string signature, long protocol_parameters, [long form_parameters] )`

## Description
This function takes an URL and two sets of parameters that are going to be passed to a webserver, and calculates the OAUTH1 signature of that request, given a secret password (which must be shared with the web service) and a token obtained in a previous step (see OAUTH1 protocol specification on the web for more details).
The function returns the resulting hash as a base-64 encoded string in a reference argument.
When the function succeeds, the return code is 0. Otherwise, an error code is returned and the output argument is unaltered. Additional details about an error will be logged by the bshell.

## Arguments
| | | |
|---|---|---|
| `const string` | `method` |  The method that is going to be used to contact the webserver. Usually "GET" or "POST".  |
| `const string` | `uri` |  The base URI that is going to be sent.  |
| `const string` | `consumer_secret` |  The secret password that is used to prove to the webserver that you have access to this password (without sending it in any form over the network). This password can be passed in plain text, or using one of the standard encryption formats supported by the bshell. Using encrypted passwords is obviously more secure.  |
| `const string` | `token_secret` |  The secret token that has been obtained in a previous step. This token can be passed in plain text, or using one of the standard encryption formats supported by the bshell. Using encrypted tokens is obviously more secure.  |
| `ref string` | `signature` |  The output string. This is a base-64 encoded signature. The signature is a secure hash of the URI, the parameters (see below), the consumer secret and the token secret. The length of the given result string is resized automatically by the function to make sure it can hold the result. The length depends on the chosen HMAC (Message Authentication) algorithm, which is one of the protocol_parameters (see below). Any change to one of the inputs will result in a totally different result. The webserver will compute the same signature given the URI and other data it receives. When the signature it computes differs from the signature you pass, the web service call will be rejected.  |
| `long` | `protocol_parameters` |  This is a Json handle that must reference an array of strings (pairs of keys and values). These are the extra protocol parameters that are part of the request. See example below. One of the protocol parameters can be "oauth_signature_method". When this value is not supplied, the function will automatically provide the default value "HMAC-SHA1". Valid values are: HMAC-SHA1, HMAC-SHA256, HMAC-SHA384 and HMAC-SHA512, PLAINTEXT. More complex algorithms result in a longer signature. Note: PLAINTEXT is special, it results in a signature that is not a cryptographic hash of the data, but just a concatenation of the two (decrypted) secrets (consumer_secret + token_secret). This can then be transmitted to the remote host, but that should be done over a secure channel, obviously. Use with care. Also note that when tracing is turned on for bshell functions, the "secrets" will show up in plain text in the trace as well.  |
| `[long` | `form_parameters]` |  This is an (optional) Json handle of the same form as the previous parameter. These are the optional parameters passed to the webserver. See example below.  |

## Return values
| | |
|---|---|
| 0 | Success |
| -1 | Curl Escape Encoding error. One of the strings that need to be encoded are invalid TSS strings.  |
| -2 | Invalid Json handle. Either the protocol_parameters or the form_parameters did not refer to a valid, properly formatted Json structure. The log will have more details.  |
| -4 | One of the values given in the Json parameter blocks is not of type 'string'. The log will have more details.  |
| -5 | HMAC algorithm failure for method X. The given HMAC method is supported, but the internal function failed. The log will have more details.  |
| -6 | Invalid digest X. The values passed for the oauth_signature_method is not one of the supported values. See log.  |
| -7 | BaanGenericDecrypt decrypt failure. One of the encrypted passwords could not be decrypted using the standard functions.  |
| -100 | Other failure. Something unexpected happened, the log may show more details.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2370.

## Example
This example is also used in the RFC that describes the OAUTH1 protocol.
```

function main ()
{
        string                  url_str(512)
        string                  signature_method(20)
        string                  consumer_key(128)
        string                  consumer_secret(128)
        string                  token(128)
        string                  token_secret(128)
        string                  timestamp(22)
        string                  nonce(UUID.SIZE.STRING)
        string                  version(3)
        string                  result(1)       | resized automatically
        long                    oauth1_params
        long                    form_params

        | Values here are taken from the RFC example.
        url_str          = "http://photos.example.net/photos"
        consumer_key     = "dpf43f3p2l4k3l03"
        consumer_secret  = "$1S$6C33C0DB7EAA2E514A57CFCE88C46723" | "kd94hf93k423kf44", encrypted
        token_secret     = "$1S$BF402DE075C55122B5B4B0A3282F0F8A" | "pfkkdhi9sl3r4s00", encrypted

        token     = "nnch734d00sl2jdk"
        nonce     = "kllo9940pd9333jh"
        version   = "1.0"
        timestamp = "1191242096"

        oauth1_params = json_new_object()
        json_set_string(oauth1_params, "oauth_signature_method", "HMAC-SHA1")   | Is also default
        json_set_string(oauth1_params, "oauth_consumer_key", consumer_key)
        json_set_string(oauth1_params, "oauth_nonce", nonce),
        json_set_string(oauth1_params, "oauth_timestamp", timestamp)
        json_set_string(oauth1_params, "oauth_token", token)
        json_set_string(oauth1_params, "oauth_version", version)

        form_params = json_new_object()
        json_set_string( form_params, "file", "vacation.jpg")
        json_set_string( form_params, "size", "original")

        long rc
        rc = oauth1_signature("GET", url_str, consumer_secret, token_secret, result, oauth1_params, form_params)
        if (rc = 0)
        then
                | result is now "tR3+Ty81lMeYAr/Fid0kMTYa/WM="
        else
                | Error handling, rc indicates the type of error.
        endif
}
```

## Related topics
- [Security Functions overview](security_overview.md)
- [Secure Functions synopsis](security_synopsis.md)
