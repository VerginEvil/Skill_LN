# sig.sign.set.level

## Syntax:
`#include <bic_sig>`
`function void sig.sign.set.level( long i.request, string i.level )`

## Description
Set the signature level.

## Arguments
| | |
|---|---|
| `BASELINE_B` | A basic digital signature. |
| `BASELINE_T` | Same as Level B, but with a trusted timestamp. |
| `BASELINE_LT` | Same as Level T, but with Long Term data. This level includes data required to validate the signature (such as all certificates and revocation data). This allows one to validate the signature in the future, when access to the Certificate Authority might not be guaranteed. |
| `BASELINE_LTA` | Same as Level LT, but with an additional archive timestamp signature. This can be used for periodic signing of archived data. The new signature ensures continued authenticity and integrity when hash functions used by previous signatures have become weak. |
When a level other than B is selected, timestamp providers must have been defined in the configuration session.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)

- [Digital Signatures synopsis](synopsis.md)

- [Digital Signatures examples](examples.md)
