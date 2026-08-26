# Example XML parsing
Below a piece of Baan-C code is shown for parsing and exploring the XML document which was shown in the [Example XML generation](example_xml_generation.md).
```

function parse()
{
        long    fd
        long    cmfId, identId,  fromId
        long    retVal
        long    found

        string  error_string(120)
        string  messageId(20)
        string  messageClass(20)
        string  subject(100)

        |Open the XML file for reading.
        fd = seq.open ("/home/ssauser/file.xml", "r" )

        |Parse the XML file
        cmfId = xmlRead(fd, error_string)
        seq.close(fd)

        |Search for the IDENTIFICATION element
        identId = xmlFindFirst( "IDENTIFICATION", cmfId)
        if (identId <> 0 )
        then
                |Get the identificiation attributes
                retVal =  xmlGetAttribute(identId,  "MESSAGE-ID" ,messageId)
                retVal =  xmlGetAttribute(identId,  "CLASS", messageClass)
                retVal =  xmlGetAttribute(identId,  "SUBJECT", subject)
        endif

        |Search for the first FROM element
        fromId = xmlFindFirst( "FROM", cmfId)
        if (fromId <> 0)
        then
                |TODO: Get the from attributes

        endif

        |Alternative 1 to get to the FROM element
        fromId = xmlFindFirstMatch( "<CMF>.<RECIPIENTS>.<FROM>", cmfId)

        |Alternative 2 to get to the FROM element
        fromId = xmlFindFirstMatch( "?<FROM>", cmfId)

        |Alternative 3 to get to the FROM element
        fromId = xmlFindFirstMatch( "-<FROM>", cmfId)

        |Alternative 4 to get to the FROM element
        fromId = xmlFindFirstMatch( "<CMF>.<IDENTIFICATION>.right.fChild", cmfId)

        |Alternative 5 to get to the FROM element
        fromId = xmlFindFirstMatch( "parent.lChild.fChild", identId )

        |Alternative 6 to get to the FROM element
        fromId = xmlFindFirstMatch( "?<FROM NAME TYPE ADDRESS>", cmfId)

        |Alternative 7 to get to the FROM element
        fromId = xmlFindFirstMatch( "?<NAME= TYPE ADDRESS>", cmfId)

        |Alternative 8 to get to the FROM element
        fromId = xmlFindFirstMatch( "?<=""SMTP"">", cmfId)

        |Alternative 9 to get to the FROM element
        fromId = xmlFindFirstMatch( "?<TYPE=""SMTP"">", cmfId)

        |Alternative to get to the CMF element from the FROM element
        cmfId = xmlFindFirstMatch( "^<CMF>", fromId )
}
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [Example XML generation](example_xml_generation.md)
