# GovCloud and FIPS-140-2 Coding Standards and Examples

## Fips mode Example
Below a part of 3GL usage of [in.fips.mode()](in.fips.mode.md) call
```

      if in.fips.mode() then
      |  FIPS-140-2 specific code
      else
      | do non FIPS compliant code
      endif
```

## Related topics
- [GovCloud functions overview](overview.md)
- [GovCloud functions synopsis](synopsis.md)
