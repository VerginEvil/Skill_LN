# Electronic Signature overview
Infor Enterprise Server provides a mechanism, called Electronic Signature, to demand user authentication before performing a specific action (for example the Completion of a Workorder or the Confirmation of a Shipment).
When enabled, a Signature Request Dialog appears before proceeding with the actual action. To continue with the action, the user must specify:

- The Reason for Signing (mandatory) by choosing one of the entries from a pre-defined list of reasons.

- (Optional) User Comments to provide additional clarification on the action to be performed.

- A valid Username and Password (mandatory)

Only after successfully signing the Signature Request Dialog will the action be performed.

## How to implementing Electronic Signature for a specific Document
The implementation of Electronic Signature for a document consist of two parts:

- Adding Signature Request handling to the form command(s) performing the action(s).

- Adding an Electronic Signature Document implementation for that Document

## Adding Signature Request Handling to a form command
Two following two function calls must be added to a form command:

- [signature.start.request()](signature.start.request.md) to start the Signature Request Dialog and ask the user sign for the operation with a valid username and password.

- [signature.finish.request()](signature.finish.request.md) to finalize the Electronic Signature.

## Adding an Electronic Signature Document Implementation
Electronic Signature Documents are implemented in the library tcgendll3000 with the following external functions:

- boolean tcgen.dll3000.signed.document.implemented(domain ttesg.docm i.document.type, ref string o.table.name) this function must return true for the Document Type and also return the root table name.

- [signed.document.add.record()](signed.document.add.record.md) to add the fields and values of a table. This function must be called for all tables related to the Document Type.

- [signed.document.add.extra.field()](signed.document.add.extra.field.md) to add an additional field to the document XML.

- [signed.document.add.field.desc()](signed.document.add.field.desc.md) to add field description to a field in the document XML.

## Related topics
- [Electronic Signature synopsis](synopsis.md)
