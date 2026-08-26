# Example XML generation
Below a piece of Baan-C code is shown for generating an XML document. For ease of reading, no checking on the return codes of the functions is done.
```

long    cmfId, identId, recipientsId, fromId, dtdId
long    fd, retVal

|Create the doctype element and populate its contents
dtdId = xmlNewNode("CMF", XML_DTD)
retVal = xmlsetAttribute(dtdId,  "NAMEURL", "cmf1.dtd")

|Create the root element and make it a right sibling of the XML_DTD node.
cmfId = xmlNewNode("CMF" )
retVal = xmlAdd(dtdId, cmfId )

|Create IDENTIFICATION element and add its attributes
identId = xmlNewNode("IDENTIFICATION", XML_ELEMENT, cmfId)

retVal = xmlSetAttribute (identId,  "MESSAGE-ID", "34a98u0erirori" )
retVal = xmlSetAttribute(identId,   "CLASS", "order" )
retVal = xmlSetAttribute(identId,   "SUBJECT", "Subject string" )

|Create RECIPIENTS element
recipientsId = xmlNewNode("RECIPIENTS", XML_ELEMENT, cmfId)

|Create FROM element and add its attributes
fromId = xmlNewNode("FROM", XML_ELEMENT, recipientsId)

retVal = xmlSetAttribute(fromId,  "NAME", "Jan Jansen" )
retVal = xmlSetAttribute(fromId,  "TYPE", "SMTP" )
retVal = xmlSetAttribute(fromId,  "ADDRESS", "jjansen@example.com" )

|Open a file for write and store the XML document
fd = seq.open("/home/ssauser/file.xml", "w" )
xmlWritePretty(fd, dtdId, 0 )
seq.close(fd)

|Free the complete XML object from memory
xmlDelete(dtdId, 0)
```
The resulting XML-document is shown below:
```

<?xml version="1.0"?>
<!DOCTYPE CMF SYSTEM "cmf1.dtd">
<CMF>
        <IDENTIFICATION
                MESSAGE-ID="34a98u0erirori"
                CLASS="order"
                SUBJECT="Subject string"
        />
        <RECIPIENTS>
                <FROM
                        NAME="Jan Jansen"
                        TYPE="SMTP"
                        ADDRESS="jjansen@example.com"
                />
        </RECIPIENTS>
</CMF>
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [Example XML parsing](example_xml_parsing.md)
