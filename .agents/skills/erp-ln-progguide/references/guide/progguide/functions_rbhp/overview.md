# Role Based Home Pages overview
These functions are used to support drillback from Role Based Home Pages. When the user performs a drillback from a Role Based Home Page, which refers to a Infor Enterprise Server session, a specific DLL function is called called depending on the ICMDrillback parameter in the drillback URL.
If the ICMDrillback parameter is set and its value is "true", the tools DLL function icm.drillback() in the tticmdll0002 library is called. If the ICMDrillback parameter is not set or not present in the URL, the application DLL function: tcint.dll0001.drill.back() is called. From this function, a number of specific tools functions can be used to:

- determine the parameters passed in the drillback URL

- indicate which session must be started

- indicate the company in which this session must be started

- indicate the session mode

- indicate the index of the session

- indicate the query extends for this session

From every 4GL Session the function is.rbhp.mode() can be called to determine if the session was started from a Role Based Home Page drillback. In case a session is started from such a drillback, the function rbhp.get.parameter() can be used to retrieve the parameters passed in the drillback URL.
Note  Drillback from Role Based Home Pages is only supported through the WebUI/LN UI client.

## Related topics
- [Role Based Home Pages synopsis](synopsis.md)
