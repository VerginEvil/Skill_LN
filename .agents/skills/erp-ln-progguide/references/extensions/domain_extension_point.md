# Domain extension point

A domain extension is used to increase the length of a string field in Infor LN.

It is used during Create/Convert to Runtime, to determine the length of the fields. The physical tables are reconfigured based on the new domain length.

This diagram shows the position of the domain extension: Domain Extension Create/Convert to
runtime
LN tables

The domain extension has the Domain extension type.

## Domain

With the properties defined for the extension type Domain, you can change the length of the domain.

The available property is Extended String Length.

## Extended String Length property

You can specify a value that is greater than the standard string length. Domain Extension Create/Convert to runtime LN tables

## Limitations and restrictions

- Strings This feature applies to domains of type (multibyte) string only.

- Forms Forms are automatically adapted to the new length. This can lead to less usable forms, as they are optimized to the standard domain lengths that are defined by Infor. Use form personalization to adjust increase the form’s usability after a domain length change.

- Reports Reports are not automatically adjusted to the new domain lengths. Changing the design in Infor LN Report Designer can be required. If you are using Infor Reporting, you must regenerate the report package by sending the report to the Infor Reporting designer device. Then refresh the package in the report design base.
