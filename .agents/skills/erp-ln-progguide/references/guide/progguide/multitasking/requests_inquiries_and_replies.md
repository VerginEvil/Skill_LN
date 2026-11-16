# Requests, inquiries, and replies
A *request* is a message sent by the bshell to the display server requesting some action – for example, the creation of a window or some other UI object. It consists of a package of information that tells the display server what action to perform and the parameters to use for that action. Requests are asynchronous, so the bshell does not wait for a reply from the display server. Consequently, if an error occurs, the bshell does not detect it. The display server, however, may generate an error message on screen and/or in a log file.
An *inquiry* is a request for which a result is returned in the form of a *reply*. Normally, inquiries are used to retrieve information about existing UI objects. When a process sends an inquiry to the display server, it waits for the server to process the inquiry and send a reply. Consequently, inquiries are more time-consuming than asynchronous requests. When response time is important, avoid using the inquiry/reply mechanism. For example, when retrieving information that does not change, you can store the data in variables and retrieve it from those variables instead of sending queries to the display server.
The following example illustrates the use of requests, inquiries, and replies:
```

#include <bic_gpart>

gpart_id = first.gpart( window_id )             | Inquiry-reply
while gpart_id
    get.gpart( window_id, part_id, type, x, y )| Inquiry-reply
    if type = GPLINE then
        destroy.gpart( window_id, gpart_id )    | Request
    endif
    gpart_id = next.gpart( window_id, gpart_id )| Inquiry-reply
endwhile
```

## Related topics
- [Multitasking and the GUI](multitasking_and_the_gui.md)
