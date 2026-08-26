# open.url.local()

## Syntax:
`#include <bic_desktop>`
`function boolean open.url.local( string url, long mode, [ string dialog.title, string dialog.message, string browser.title, string redir.param, ref long params.node ] )`

## Description
This function opens a *URL* in an (embedded) browser. This function is only supported in WebUI and LN UI.

## Arguments
| | | |
|---|---|---|
| `string` | `url` |  This specifies the URL that needs to be started.  |
| `long` | `mode` |  Specifies the start mode of the browser. Possible values are: OPEN_URL_EXTERNAL: Open the URL in an new tab of the browser. OPEN_URL_INTERNAL: Open the URL embeded in the WebUI or LN UI. OPEN_URL_WAIT: Open the URL embeded in the WebUI or LN UI and block the current session till the browser window is closed.  |
| `[ string` | `dialog.title ]` |  When the browser is started in the mode *OPEN_URL_WAIT* a modal dialog is created for the session. If this dialog should have a title then the parameter dialog.title must be filled. This argument is optional and is only applicable for the *OPEN_URL_WAIT* mode.  |
| `[ string` | `dialog.message ]` |  When the browser is started in the mode *OPEN_URL_WAIT* a modal dialog is created for the session. If this dialog should have a message the parameter dialog.message must be filled. This argument is optional and is only applicable for the *OPEN_URL_WAIT* mode.  |
| `[ string` | `browser.title ]` |  When the browser is started in the mode *OPEN_URL_WAIT* or *OPEN_URL_INTERNAL*, this is the title of the new WebUI or LN UI Tab.  |
| `[ string` | `redir.param ]` |  The name of the URL parameter which must be added to the URL. The value of this URL parameter is set to a redirect URL which will close the embeded browser window. This parameter is only used when mode is OPEN_URL_WAIT.  |
| `[ ref long` | `params.node ]` |  This parameter is only used when mode is OPEN_URL_WAIT and redir.param is filled. When the open.url.local() function returns, this parameter might be filled with an XML node. The attributes in this XML node are the values returned by the web paged.  |

## Return values
| | |
|---|---|
| true | Browser application started successfully. |
| false | iBrowser application failed to start. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Notes  The optional parameters *redir.param* and *params.node* are available from tools [TIV](../tiv/tiv_overview.md) [level 2110](../tiv/tiv_2110.md).
Due to browser security restrictions it is not possible to open a local (client side) file. So a url which starts with *file://{filepath}* will not open the local file.

## LN Session Example
```

long paramsNode
string retparam1(20)
paramsNode = 0
if open.url.local("https://www.thirdparty.com/webapplication?input=val",
               OPEN_URL_WAIT, "Web Application" ,
               "Waiting for thirdparty webapplication" ,
               "Web Application Title", "RedirectUrl", paramsNode) then
	| Web Application closed successfully
	if paramsNode <> 0 then
		| Web Application returned some parameters.
		retparam1 = xmlAttribute$("retparam1")
            xmlDelete(paramsNode)
	endif
endif
```

## Example explanation
The above example demonstrates showing a web page embedded in LN UI. The LN session will wait until this Web Page is closed. The application running in this web page can initiate the close of this page by redirecting its browser window to the URL passed in parameter "RedirectUrl". The example code belows shows the corresponding JavaScript code to be included in the Web Page.

## Web Page JavaScript example
```

<script type="text/javascript">
var qs = (function(a) {
    if (a == "") return {};
    var b = {};
    for (var i = 0; i < a.length; ++i)
    {
        var p=a[i].split('=', 2);
        if (p.length == 1)
            b[p[0]] = "";
        else
            b[p[0]] = decodeURIComponent(p[1].replace(/\+/g, " "));
    }
    return b;
})(window.location.search.substr(1).split('&'));

function closeApp() {
	var redirectUrl = qs['RedirectUrl']
	if (redirectUrl) {
		window.location.replace(redirectUrl +
				"?retparam1=" + document.querySelector("#param1").value);
	}
}
</script>
```

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
