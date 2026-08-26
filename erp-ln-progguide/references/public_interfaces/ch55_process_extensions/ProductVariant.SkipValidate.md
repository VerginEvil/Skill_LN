# ProductVariant.SkipValidate

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2152-2153

Skips validation of Product Variants. This process extension is available from 2024.10 ( KB3526537 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension ProductVariant.SkipValidate can be used to skip
validating certain Product Variants.
Sessions where this Process Extension can be implemented:
-               Validate Product Variants (tipcf5200m000)
Fields that are available to be used in this Process Extension:
-               All fields of table: Product Variant IDs (tipcf500)
-               All fields of table: Business Partners (tccom100) only if Business
Partner is present in the tipcf500.
-               All fields of table: Items (tcibd001)
```

## Process Extensions for ProjectBudget

The following process extension(s) is/are available: ProjectBudget.SkipGenerateServiceOrders
