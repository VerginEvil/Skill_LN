# DAL2 Test Mode

## Overview
By means of the *DAL2_TEST_MODE* environment variable it is possible to test different aspects of a DAL2 DAL from the User Interface. The *DAL2_TEST_MODE* environment variable must be set in the BW Configuration file and can have the following values:
| | | |
|---|---|---|
| Value | Aspect | Explanation |
| 0 | None | Test mode is off |
| 1 | Derived fields | All display maintable fields are shown as input fields. This makes it possible to see whether derived fields are made readonly.  |
| 2 | (Never) applicable, readonly and derived fields and (never) applicable standard and form commands (business methods)  | Same as Mode 1 + All fields and commands stay enabled. In this way is is possible to see if the DAL blocks certain field changes and business methods.  |
| 3 | Same as Mode 2 + updating dependent fields | Same as Mode 2 + Dependent fields are not updated (no defaulting).  |

## Related topics
- [DAL2 Field hooks](dal2_field_hooks.md)
- [DAL2 Business method hooks](dal2_bm_hooks.md)
- [DAL2 Field dependencies](dal2_field_dependencies.md)
- [DAL2 and the 4GL Engine](dal2_4gle.md)
- [DAL2 Test Mode](dal2_test_mode.md)
