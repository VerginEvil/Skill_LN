# Functions that should be used with caution
The following functions should be used with caution. Wrong use of them might cause the 4GL Engine not to respond when running in WebUI or LN UI.

## run.prog()
Only use this function when the program requires no user-interaction.

## sleep()
If the sleep function is used in order to create a modal overview session (which does not look as a zoom session) then use the function start.session(MODAL_OVERVIEW, ). This works for all client types (LN UI, WebUI and BW). You can also create a form command starting a session, and specify the start mode of this session as:"Modal Overview".

## start.application.local()
Don't use this function to start applications that might not be present on each desktop (like BW.exe).

## wait() and reactivate()
Only use these functions if you have in-depth knowledge of the 4GL Engine.
