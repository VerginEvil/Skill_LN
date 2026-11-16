# Tools Interface Version (TIV)
The Tools Interface Version (TIV) is a concept supported by the Infor Enterprise Server to guarantee backward compatibility. By setting a TIV number to each object the behavior can be different for incompatible features executed with different versions of the Porting set or Infor Enterprise Engine. The TIV number is a property of the program and library scripts, and can be defined in session "Program Scripts / Libraries (ttadv2530m000)". The bshell also has its own TIV number.

## Determining TIV number
Developers can determine which TIV number is used in an object or Porting set and may use this information to use a different program flow. Next macros are known to determine a TIV number.
| | |
|---|---|
| Macro | Description |
| `GET.BSHELL.TIV()` | Returns TIV number of running bshell |
| `GET.TOOLS.TIV()` | Returns TIV number of tools |
| `GET.OBJECT.TIV()` | Returns the TIV number of the current object, as specified with the -T option of the [compiler](../3gl_features/compiler.md) when it was compiled. |
| `GET.OBJECT.TIV(string object)` | Returns the TIV number of the specified object, as specified with the -T option of the [compiler](../3gl_features/compiler.md) when it was compiled. |

## Caution
When updating a component to a higher TIV level, it can be necessary to do rework. This is for example the case when adopting TIV level 1075 (or higher). Whatever the reason is to do the TIV level upgrading, the rework for Record selection *must* be done. The session will not function with the old record selection mechanism anymore. Mandatory rework is indicated in the table below.

## Supported Porting set TIV numbers
The supported TIV numbers related to Porting set versions are listed below.
| | | | |
|---|---|---|---|
| TIV | Type | Description | Remarks |
| 200 | bshell | original TIV level when TIV was introduced in 4c |  |
| 500 | bshell | original TIV level when TIV was introduced in Corelli |  |
| [1000](tiv_1000.md) | bshell tools | Initial TIV level for Porting set 7.5a |  |
| 1010 | bshell | Initial TIV level for Porting set 7.6a |  |
| [1012](tiv_1012.md) | bshell tools | Porting set 7.6a.01 | Functions for Outbound Publishing String size limit removed for xmlSetAttribute and other xml functions db.get.child.transaction function added in bshell |
| [1014](tiv_1014.md) | Tools | Added tt.is.domain.separated() function. |  |
| [1020](tiv_1020.md) | tools | Enterprise Server 8.2 |  |
| 1050 | bshell | Porting set 7.6b | Added Unicode support. |
| [1075](tiv_1075.md) | bshell tools | Porting set 7.6c Enterprise Server 8.3 | Note: Mandatory rework in [record selection](../functions_selection/cookbook.md). |
| 1076 | bshell | Porting set 8.2b |  |
| 1078 | bshell | Porting set 8.2b.01 |  |
| 1100 | bshell | Porting set 8.3a |  |
| 1101 | bshell | Porting set 8.2b.01 | changed interface handle.report.pool() to handle more than 252 arguments added syslibpath.env.var$() bshell function. Useful for ERP installer to determine system dependent env. var. |
| [1200](tiv_1200.md) | bshell tools | Porting set 8.3b Enterprise Server 8.4 |  |
| [1300](tiv_1300.md) | bshell tools | Porting set 8.4b Enterprise Server 8.4 | New functions for handling field dependencies. |
| [1306](tiv_1306.md) | tools | New behavior in Enterprise Server 8.4 for ncrs selection groups |  |
| 1501 | tools | Function tt.label.desc.by.lang added. |  |
| 1601 | bshell | Porting set 8.6a |  |
| 1620 | bshell | Porting set 8.6a.01 |  |
| 1641 | bshell | Porting set 8.6a.02 (rebuild) Added function [mb.coerce.to.sb()](../functions_multibyte_strings/mb.coerce.to.sb.md) |  |
| 1660 | bshell | Porting set 8.6a.03 |  |
| [1700](tiv_1700.md) | bshell tools | Porting set 8.7a Enterprise Server 8.7 | Possible rework needed when moving to object TIV 1700 for use of the [alloc.mem()](../functions_memory_operations/alloc.mem.md) function. |
| [1753](tiv_1753.md) | tools | Enterprise Server 8.7a |  |
| [1800](tiv_1800.md) | bshell tools | Porting set 8.8a Enterprise Server 8.8 |  |
| [1801](tiv_1801.md) | tools | Enterprise Server 8.8 |  |
| [1802](tiv_1802.md) | tools | Enterprise Server 8.8 |  |
| [1804](tiv_1804.md) | tools | Enterprise Server 8.8 |  |
| [1900](tiv_1900.md) | bshell tools | Porting set 8.9a Enterprise Server 10.3 |  |
| [2000](tiv_2000.md) | tools | Enterprise Server 10.4 |  |
| [2010](tiv_2010.md) | bshell | Porting set 9.0a.01. | New cURL functions to support secure email. New functions to support error bypass |
| [2020](tiv_2020.md) | bshell | Porting set 9.0b |  |
| [2030](tiv_2030.md) | bshell tools | Porting set 9.0b.01 Enterprise Server 10.4.2 |  |
| [2040](tiv_2040.md) | bshell tools | Porting set 9.0c Enterprise Server 10.4.2 |  |
| [2050](tiv_2050.md) | bshell | Porting set 9.0c.01 |  |
| [2100](tiv_2100.md) | bshell tools | Porting set 9.1a. Enterprise Server 10.5 |  |
| [2110](tiv_2110.md) | tools | Enterprise Server 10.5.0.1 |  |
| [2120](tiv_2120.md) | bshell tools | Porting set 9.1b. Enterprise Server 10.5.1. |  |
| [2130](tiv_2130.md) | bshell | Porting set 9.1b.01. |  |
| [2140](tiv_2140.md) | bshell tools | Porting set 9.1c. Enterprise Server 10.5.2. |  |
| [2150](tiv_2150.md) | bshell tools | Porting set 9.1c.01 Enterprise Server 10.5.2.1 | Added TLINK macro |
| [2153](tiv_2153.md) | tools | Enterprise Server 10.5.2.1 |  |
| [2200](tiv_2200.md) | bshell tools | Porting set 9.2a. Enterprise Server 10.6. |  |
| [2201](tiv_2201.md) | tools | Enterprise Server 10.6 |  |
| [2202](tiv_2202.md) | tools | Enterprise Server 10.6 |  |
| [2210](tiv_2210.md) | bshell tools | Porting set 9.2a.01 Enterprise Server 10.6.0.1 |  |
| [2220](tiv_2220.md) | bshell tools | Porting set 9.2b Enterprise Server 10.6.1 |  |
| [2230](tiv_2230.md) | bshell tools | Porting set 9.2b.01 Enterprise Server 10.6.1.1 |  |
| [2231](tiv_2231.md) | tools | Enterprise Server 10.6.1.1 |  |
| [2300](tiv_2300.md) | bshell tools | Porting set 9.3a Enterprise Server 10.7 |  |
| [2310](tiv_2310.md) | bshell tools | Porting set 9.3b Enterprise Server 10.7.0.1 |  |
| [2320](tiv_2320.md) | bshell tools | Porting set 9.3c Enterprise Server 10.7.1 |  |
| [2330](tiv_2330.md) | bshell tools | Porting set 9.3d Enterprise Server 10.7.1.1 |  |
| [2340](tiv_2340.md) | bshell tools | Porting set 9.3e Enterprise Server 10.7.2 |  |
| [2350](tiv_2350.md) | bshell tools | Porting set 9.3f Enterprise Server 10.7.2.1 |  |
| [2360](tiv_2360.md) | bshell tools | Porting set 9.3g Enterprise Server 10.7.3 |  |
| [2361](tiv_2361.md) | bshell | Porting set 9.3g.01 |  |
| [2370](tiv_2370.md) | bshell tools | Porting set 9.3h Enterprise Server 10.7.3.1 |  |
| [2381](tiv_2381.md) | tools | Enterprise Server 10.7.4 |  |
| [2390](tiv_2390.md) | tools | Enterprise Server 10.7.4.1 |  |
| [2391](tiv_2391.md) | tools | Enterprise Server 10.7.4.1 |  |
| [2392](tiv_2392.md) | tools | Enterprise Server 10.7.4.1 |  |
| [2393](tiv_2393.md) | tools | Enterprise Server 10.7.4.1 |  |
| [2395](tiv_2395.md) | tools | Enterprise Server 10.7.4.1 |  |
| [2400](tiv_2400.md) | tools | Enterprise Server 10.8 |  |
| [2401](tiv_2401.md) | tools | Enterprise Server 10.8 |  |
| [2410](tiv_2410.md) | tools | Enterprise Server 10.8.1 |  |
| [2420](tiv_2420.md) | bshell tools | Porting set 9.4c Enterprise Server 10.8.2 |  |
| [2430](tiv_2430.md) | bshell | Porting set 9.4d |  |
| [2431](tiv_2431.md) | bshell tools | Porting set 9.4d Enterprise Server 10.8.3 |  |
| [2432](tiv_2432.md) | bshell | Porting set 9.4d (Linux Cloud-only rebuild) |  |
| [2440](tiv_2440.md) | bshell | Porting set 9.4e |  |
| [2450](tiv_2450.md) | bshell tools | Porting set 9.4f Enterprise Server 10.8.5 |  |
| [2451](tiv_2451.md) | tools | Enterprise Server 10.8.5 |  |
| [2460](tiv_2460.md) | bshell tools | Porting set 9.4g Enterprise Server 10.8.6 |  |
| [2461](tiv_2461.md) | tools | Enterprise Server 10.8.6 |  |
| [2470](tiv_2470.md) | bshell tools | Porting set 9.4h Enterprise Server 10.8.7 |  |
| [2481](tiv_2481.md) | tools | Enterprise Server 10.8.8 |  |
| [2490](tiv_2490.md) | bshell tools | Porting set 9.4j Enterprise Server 10.8.9 |  |
| [2491](tiv_2491.md) | bshell tools | Porting set 9.4j Enterprise Server 10.8.9 |  |
| [2492](tiv_2492.md) | tools | Enterprise Server 10.8.9 |  |
| [2495](tiv_2495.md) | tools | Enterprise Server 10.8.10 |  |
| [2496](tiv_2496.md) | tools | Enterprise Server 10.8.10 |  |
| [2500](tiv_2500.md) | bshell | Porting set 9.5a |  |
| [2510](tiv_2510.md) | bshell | Porting set 9.5b |  |
| [2520](tiv_2520.md) | bshell | Porting set 9.5c |  |
| [2521](tiv_2521.md) | tools | Enterprise Server 10.8.11 |  |
| [2530](tiv_2530.md) | bshell tools | Porting set 9.5d Enterprise Server 10.8.12 |  |
| [2531](tiv_2531.md) | tools | Enterprise Server 10.8.12 |  |
| [2540](tiv_2540.md) | bshell | Porting set 9.5e |  |
| [2550](tiv_2550.md) | bshell | Porting set 9.5f |  |
| [2560](tiv_2560.md) | bshell | Porting set 9.5g |  |
| [2570](tiv_2570.md) | bshell | Porting set 9.5h | *bshell:* Able to handle large 3GL and bshell calls to handle more than 255 (max 2047) function arguments. TIV level 2570 or higher is needed for this functionality. *bic:* Added -largecalls to handle more than 255 function arguments (max 2047). |
| [2590](tiv_2590.md) | tools | Enterprise Server 10.8.13 |  |
| [2610](tiv_2610.md) | tools | Enterprise Server 10.8.14 |  |

## Base TIV levels per Enterprise Server Feature Pack
The Base TIV levels per Feature Pack are as specified below. Those levels are the *base* levels. During the lifetime of a Feature Pack, additional numbers may be inserted.
If software is developed on a 'latest Feature Pack' development system, for release to customers who might be on a lower Feature Pack, the TIV level of the software should be maximized to the base level of the target Enterprise Server Feature Pack. If specific functionality within the target Feature Pack is necessary, installation of additional tools solutions or another Porting set might be necessary before the newly developed software works correctly.
Example: when developing software for an ES 7 (Infor LN FP1) system, the TIV level of the new components should be maximized on TIV level 1010. Only when the function tt.is.domain.separated() is used the level should be set to 1014 (And the target system needs to have solution 202854).
| | |
|---|---|
| Version | *BASE* TIV level |
| Infor LN without feature packs | 1000 |
| Enterprise Server 7 (Infor LN FP1) | 1010 |
| Enterprise Server 8.2 (Infor LN FP2) | 1020 |
| Enterprise Server 8.3 (Infor LN FP3) | 1075 |
| Enterprise Server 8.4 (Infor LN FP4) | 1200 |
| Enterprise Server 8.5 (Infor LN FP5) | 1500 |
| Enterprise Server 8.6 (Infor LN FP6) | 1600 |
| Enterprise Server 8.7 (Infor LN FP7) | 1700 |
| Enterprise Server 8.8 (Infor LN FP8) | 1800 |
| Enterprise Server 10.3 (Infor LN FP9) | 1900 |
| Enterprise Server 10.4 | 2000 |
| Enterprise Server 10.4.1 | 2020 |
| Enterprise Server 10.4.2 | 2040 |
| Enterprise Server 10.5 | 2100 |
| Enterprise Server 10.5.0.1 | 2110 |
| Enterprise Server 10.5.1 | 2120 |
| Enterprise Server 10.5.1.1 | 2130 |
| Enterprise Server 10.5.2 | 2140 |
| Enterprise Server 10.5.2.1 | 2150 |
| Enterprise Server 10.6 | 2200 |
| Enterprise Server 10.6.0.1 | 2210 |
| Enterprise Server 10.6.1 | 2220 |
| Enterprise Server 10.6.1.1 | 2230 |
| Enterprise Server 10.7 | 2300 |
| Enterprise Server 10.7.0.1 | 2310 |
| Enterprise Server 10.7.1 | 2320 |
| Enterprise Server 10.7.1.1 | 2330 |
| Enterprise Server 10.7.2 | 2340 |
| Enterprise Server 10.7.2.1 | 2350 |
| Enterprise Server 10.7.3 | 2360 |
| Enterprise Server 10.7.3.1 | 2370 |
| Enterprise Server 10.7.4 | 2380 |
| Enterprise Server 10.7.4.1 | 2390 |
| Enterprise Server 10.8 | 2400 |
| Enterprise Server 10.8.1 | 2410 |
| Enterprise Server 10.8.2 | 2420 |
| Enterprise Server 10.8.3 | 2430 |
| Enterprise Server 10.8.4 | 2440 |
| Enterprise Server 10.8.5 | 2450 |
| Enterprise Server 10.8.6 | 2460 |
| Enterprise Server 10.8.7 | 2470 |
| Enterprise Server 10.8.8 | 2481 |
| Enterprise Server 10.8.9 | 2492 |
| Enterprise Server 10.8.10 | 2510 |
| Enterprise Server 10.8.11 | 2521 |
| Enterprise Server 10.8.12 | 2530 |
| Enterprise Server 10.8.12 | 2531 |
| Enterprise Server 10.8.13 | 2590 |
| Enterprise Server 10.8.14 | 2610 |
*Note:* The TIV level can *not* be set higher than the current level of the tools or Porting set.
