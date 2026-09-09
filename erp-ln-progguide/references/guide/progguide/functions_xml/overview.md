# XML object overview
The purpose of this document is to define the functional requirements for the XML object. The XML object is an extension of the Baan VM allowing a 3GL/4GL application to exchange structured data using the XML format.

## Environment
The XML object functionality is integrated into the Baan VM. It is accessible by 3GL/4GL programs using a set of Baan 3GL functions. The XML object is applied by CMF for communication between a messaging service and a 4GL application. The XML object is also applied by B3 for constructing and exploring communication objects. The XML object functionality is not restricted to CMF and B3 but may be used by other applications that want to exchange structured data using the XML format.

## Architecture
The architecture of the XML object functionality is shown the following picture:

## References
| | |
|---|---|
| [XMLSTD] | Extensible Markup Language 1.0, W3C Recommendation, February 10, 1998: [http://www.w3.org/TR/1998/REC-xml-19980210](http://www.w3.org/TR/1998/REC-xml-19980210) and October 6, 2000: [http://www.w3.org/TR/2000/REC-xml-20001006](http://www.w3.org/TR/2000/REC-xml-20001006). |
| [EXPAT] | Expat is an XML1.0 parser written in C written by James Clark. Source code and information can be found at: "http://www.jclark.com/xml/expat.html" |
| [CMFDS] | Common Message Facility, Definition study, Doc.Nr: D0525 US |
In this figure, the following components are shown:

- XML Object API. A set of 3GL functions available to a 3GL/4GL application to access an XML Object.

- XML Object. Baan VM in-memory structure closely representing the structure of an XML document.

- XML Parser. The XML object component which function is to convert an XML document into an XML object.

- XML generator. The XML object component which function is to convert an XML object into an XML document.

## User characteristics
The direct users of the XML object are application programmers using the XML Object API. Users of CMF and B3 use the XML object implicitly.

## Future extensions
A possible future extension is the option of using a validating parser.

## Performance requirements
The XML parser implementation used as a basis for the XML object has been optimized for performance.

## Software system attributes
The approximate size of this component is about 7K lines of C code.
The XML parser is based on James's Clark free minimal XML parser written in C: "expat". See [EXPAT] for source and description.
Naming convention: all XML object functions start with the prefix: "xml".
The following implementation decisions are made:

- The XML functions is built as a library in /logic/lib/xml.

- Conversion from TSS to UTF-8 and vice-versa are built-in.

- Source code conforms to ANSI-C.

## Related topics
- [XML object constraints](constraints.md)

- [XML object glossary](glossary.md)

- [XML object synopsis](synopsis.md)

- [XML object API](api.md)
