# ProductionOrder.SkipGenerateSubcDocuments

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2141-2141

Skips generation of Subcontracting Purchase Documents for Production Order Operations. This process extension is available from 2024.09 ( KB2322308 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension ProductionOrder.SkipGenerateSubcDocuments can be used
to skip certain Production Order Operations when generating subcontracting
purchase documents.
Sessions where this Process Extension can be implemented:
-               Generate Subcontracting Purchase Documents (tisfc2250m000)
Fields that are available to be used in this Process Extension:
-               All fields of table: Production Order Operations (tisfc010)
-               From table Production Orders, fields:
tisfc001.site
tisfc001.clco
```
