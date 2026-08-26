# bc.decode()

## Syntax:
`function long bc.decode( const string encoded.barcode, ref long bytes.read, [ ref long xmlid ] )`

## Description
Use this function to decode the output of [bc$()](bc.md) function.

## Arguments
| | | |
|---|---|---|
| `const string` | `encoded.barcode` |  The input string, which typically contains the output of the bc$() function.  |
| `ref long` | `bytes.read` |  The number of bytes read from the input buffer.  |
| `[ ref long` | `xmlid ]` |  The decoded output in XML form. If no xmlid is provided, the encoded barcode string is not validated.  |

## Return values
Returns zero upon success, non-zero otherwise. If an xmlid argument is supplied, then xmlid contains an XML document upon success. When finished, use [xmlDelete](../functions_xml/delete_nodes.md) to free the returned XML document from memory. In case of error return, the xmlid argument value is always zero. The function will return with an error if an xmlid was provided and the encoded input contains an invalid barcode string. In case of error return, the bytes.read argument is set if the input was a barcode, even if the encoded input encapsulated an invalid barcode string.

## Context
This function is implemented in the porting set and can be used in all script types.

## Remarks
The bc.decode() function translates its input string, which typically contains the encoded output from the bc$() function, to an XML document. The input parameters of bc$() are translated to attributes in the XML document with a similar name (type, height/rows, barcode caption, options). An example of such an XML document is shown below.
The data in the barcode XML node is the [base64](../functions_base64/base64_overview.md) encoded output of the provided barcode caption for bc$(). This data may contain single-byte/ [ASCII](../misc/ascii_table.md), multibyte/ [TSS](../misc/tss.md) or even binary data. In case the input is valid TSS (which comprises single-byte/ASCII) and valid XML, a caption attribute is added to the XML document.
All options provided to bc$() are translated to speaking literal names and put as attributes to the XML document, including the options that are set implicitly (if any) by the porting set.

## Example XML document
```

<barcode
	type="1"
	height="3"
	options="18"
	caption="12345678"
	BC_TRANSPARENTBACKGRND="1"
	BC_EXTENDBEARERS="1">MTIzNDU2Nzg=
</barcode>
```

## Possible error conditions
A list of possible/common error conditions is provided below.
- Invalid input data.
- The provided input exceeds allowed ranges, e.g. a barcode type that is outside the 1 - 2000 range.    Availability  This function is available from bshell TIV 2050.

## Related topics
- [bc$()](bc.md)
- [Delete Nodes](../functions_xml/delete_nodes.md)
- [Base64 overview](../functions_base64/base64_overview.md)
- [ASCII table (C0 Controls and Basic Latin)](../misc/ascii_table.md)
- [TSS Encoding](../misc/tss.md)
