# FactoryTrackQuery.QueryExtend

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for FactoryTrackQuery
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2011-2011

Extend Factory Track Queries. This process extension is available from 2020.09 ( KB2143379 ). Technical information for this process extension:

```baan
Usage:        With this Process Extension, standard Factory Track queries can be
extended and custom queries can be created.
Extensions on standard queries can be implemented in method
brext.qry0001.standard.query.extension.
Custom queries can be implemented in method brext.qry0001.custom.query.
The following query BDEs can be extended:
-               IFTStdHUPackingQuery
-               IFTStdTimeTrack
-               IWMStdConsignmentWrhQuery
-               IWMStdExtQuery
-               IWMStdHoursQuery
-               IWMStdKanQuery
-               IWMStdPackingQuery
-               IWMStdQuery
```

To implement this process extension, you need to implement the following method(s):
