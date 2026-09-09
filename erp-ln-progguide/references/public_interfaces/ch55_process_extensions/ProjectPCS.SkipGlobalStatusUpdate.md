# ProjectPCS.SkipGlobalStatusUpdate

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProjectPCS
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2185-2185

```baan
Skips status update when executing Global Status Update of PCS projects.
This process extension is available from 2024.10 (KB3518588).
To implement this process extension, you can use the information below:
Usage:        Process Extension ProjectPCS.SkipGlobalStatusUpdate can be used
to skip certain PCS Project when changing the status for a range of
Projects.
Sessions where this Process Extension can be implemented:
- Global Update of Project Status (tipcs2280m000)
Fields that are available to be used in this Process Extension:
- All fields of table: Project Details (tipcs030)
- From table Description and Project Type, fields:
tipcs020.kopr
```
