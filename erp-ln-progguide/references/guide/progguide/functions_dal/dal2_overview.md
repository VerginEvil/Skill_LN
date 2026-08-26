# Extended DAL (DAL2)

## Overview
In Infor Enterprise Server the DAL concept is introduced to centralize integrity checks. One of the goals is to be able to re-use these integrity checks rather than implementing them again and again. In practice however, it appears that these integrity checks are hard to re-use in the UI layer. As a result, a lot of business logic is programmed in the UI scripts. Another problem is that since developers often only test the application via the User Interface, the DAL on its own is not well tested.
It also appeared that it is very hard to use the current DALs for Integrations via Baan OpenWorld, because too often business logic is spread across the DAL and the UI scripts.
The DAL2 concept is introduced to tackle these issues. With DAL2 a number of new hooks is introduced that make it possible to define the integrity checks in such a way that they are easier to re-use. One of the major benefits is that the 4GL engine now re-uses these hooks to perform automatic disabling/enabling of fields and commands.
Another important improvement is that DAL2 makes it possible to define field dependencies in such a way that they can be used to determine correct values for fields that are not known by other components. Until now (in the Corelli Release), this was already possible for external products that Integrated with Infor Enterprise Server using Baan OpenWorld. The DAL2 concept now makes it possible to re-use the field dependencies in the Infor Enterprise Server application as well. Also, the 4GL engine makes use of the defined field relations in order to determine default values in the User Interface.

## Include files
You have to include *bic_dal2* in your DAL to make it an Extended (DAL2) DAL.

## Testing DALs
The 4GL engine can be run in 3 different modes that can be used to test an Extended (DAL2) DAL. See [DAL2 Test Mode](dal2_test_mode.md) for more information.

## Related topics
- [DAL2 Field hooks](dal2_field_hooks.md)
- [DAL2 Business method hooks](dal2_bm_hooks.md)
- [DAL2 Field dependencies](dal2_field_dependencies.md)
- [DAL2 and the 4GL Engine](dal2_4gle.md)
- [DAL2 Test Mode](dal2_test_mode.md)
- [DAL2 Flow of field hooks](dal2_flow.md)
