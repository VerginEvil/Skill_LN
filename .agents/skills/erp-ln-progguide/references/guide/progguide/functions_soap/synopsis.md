# SOAP client synopsis
```
long
```
```
long
```
```
void
```
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
```
void
```
```
void
```
```
void
```
```
long
```
| | | |
|---|---|---|
|  | [soap.init](soap.init.md) | `( )` |
|  | [soap.newMessage](soap.newMessage.md) | `( const string soapNsURI )` |
|  | [soap.deleteMessage](soap.deleteMessage.md) | `( ref long soapMessage)` |
|  | [soap.getEnvelope](soap.getEnvelope.md) | `( long soapMessage )` |
|  | [soap.getBody](soap.getBody.md) | `( long soapMessage )` |
|  | [soap.getHeader](soap.getHeader.md) | `( long soapMessage )` |
|  | [soap.getMethod](soap.getMethod.md) | `( long soapMessage )` |
|  | [soap.getFault](soap.getFault.md) | `( long soapMessage )` |
|  | [soap.setAction](soap.setAction.md) | `( long soapMessage, const string soapAction )` |
|  | [soap.addHeader](soap.addHeader.md) | `( long soapMessage, long method )` |
|  | [soap.addMethod](soap.addMethod.md) | `( long soapMessage, long method )` |
|  | [soap.invoke](soap.invoke.md) | `( long soapMessage, const string url, ref long responseMessage)` |

## Related topics
- [SOAP client overview](overview.md)
