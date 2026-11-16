# brext.qry0001.standard.query.extension

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for FactoryTrackQuery
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2033-2041

```baan
Syntax: long brext.qry0001.standard.query.extension(
domain  tcmcs.str40      i.query.bde,
long             i.query.number,
domain  tcmcs.s999       i.query.input,
domain  tcmcs.s999       i.query.ext.input,
ref             boolean          o.skip.row,
ref     domain  tcmcs.str999m    o.error.message mb )
Usage:        Expl:   Use this method to extend standard Factory Track queries. This
method will be called from the standard process for each query
output row, just after it is created.
The following scenarios are supported:
- Add custom elements to the query output.
- Remove output rows from the query output.
- Return an error message.
Public interface FactoryTrackQuery.CreateElement can be used to
create custom elements in the current query output row.
Public interface FactoryTrackQuery.GetElement can be used to
read custom elements from the current query output row.
Note: To prevent conflicts with possible future additions in the
standard query, it is strongly advised to use prefix "Ext",
"ext" or "ext_" in custom element names.
Note: If this process extension removes all output rows for some
query, then the query will return an error message.
The following list contains the queries which are extensible.
Queries that are not mentioned are not extensible. The tables
that are current in the process extension, are listed next to
query numbers. Fields of those tables can be used without
re-reading the table in this process extension. This holds also
for customer defined fields in those tables.
IFTStdHUPackingQuery 1: whwmd530
IFTStdHUPackingQuery 2:
IFTStdHUPackingQuery 3: brpac911, whwmd530
IFTStdHUPackingQuery 4: whwmd530
IFTStdHUPackingQuery 5:
IFTStdHUPackingQuery 6: brpac911, whwmd530
IFTStdHUPackingQuery 7: brpac911, whwmd530
IFTStdHUPackingQuery 8: (**)
IFTStdHUPackingQuery 9: (**)
IFTStdHUPackingQuery 10: whwmd530
IFTStdHUPackingQuery 11: brpac911, whwmd530
IFTStdHUPackingQuery 12:
IFTStdHUPackingQuery 13: whwmd530
IFTStdHUPackingQuery 14:
IFTStdHUPackingQuery 15: whinh225
IFTStdHUPackingQuery 16: brpac911, whwmd530
IFTStdHUPackingQuery 17: brpac910 (**)
IFTStdHUPackingQuery 18: (**)
IFTStdHUPackingQuery 19: (**)
IFTStdHUPackingQuery 20: brpac911, whwmd530
IFTStdHUPackingQuery 21:
IFTStdHUPackingQuery 22:
IFTStdHUPackingQuery 23:
IFTStdTimeTrack 9:
IFTStdTimeTrack 10:
IFTStdTimeTrack 19: tisfc010
IFTStdTimeTrack 31: bpmdm050
IFTStdTimeTrack 129:
IFTStdTimeTrack 211: tisfc001
IFTStdTimeTrack 220: tiasc210, tipcs400, tisfc010 (**) (***)
IFTStdTimeTrack 247: tiasc210, tipcs400, tisfc010 (**) (***)
IFTStdTimeTrack 274: tiasc210, tipcs400, tisfc010 (**) (***)
IFTStdTimeTrack 275:
IFTStdTimeTrack 276:
IFTStdTimeTrack 277:
IFTStdTimeTrack 278: (**) (***)
IFTStdTimeTrack 279: tisfc014, tipcs405, tstdm211 (**) (***)
IFTStdTimeTrack 280: tpptc231 (**) (***)
IFTStdTimeTrack 281: tisfc014, tipcs405, tstdm211 (**) (***)
IFTStdTimeTrack 282:
IFTStdTimeTrack 283: (**) (***)
IFTStdTimeTrack 284: (**) (***)
IWMStdConsignmentWrhQuery 12: brcnd100
IWMStdExtQuery 12: brcnd100
IWMStdExtQuery 55: (**)
IWMStdExtQuery 56:
IWMStdExtQuery 57:
IWMStdExtQuery 58:
IWMStdExtQuery 59:
IWMStdExtQuery 60:
IWMStdExtQuery 61:
IWMStdExtQuery 62:
IWMStdExtQuery 100: brmcs999 (**)
IWMStdHoursQuery 1: brtmm100
IWMStdHoursQuery 2:
IWMStdHoursQuery 3:
IWMStdHoursQuery 4: brtmm102
IWMStdHoursQuery 5: bpmdm050
IWMStdHoursQuery 6: tcmcs048
IWMStdHoursQuery 7: tcmcs065
IWMStdHoursQuery 8: tcppl030
IWMStdHoursQuery 9: bpmdm050
IWMStdHoursQuery 10: tcmcs048
IWMStdHoursQuery 11: tcmcs048
IWMStdHoursQuery 12:
IWMStdHoursQuery 21:
IWMStdHoursQuery 22: brtmm101
IWMStdHoursQuery 23: (**)
IWMStdHoursQuery 24: (**)
IWMStdHoursQuery 25: (**)
IWMStdHoursQuery 26: brtmm900
IWMStdHoursQuery 27: brtmm105
IWMStdHoursQuery 28: brtmm106
IWMStdHoursQuery 29: brtmm111
IWMStdHoursQuery 30: brtmm110
IWMStdHoursQuery 31: bpmdm050
IWMStdKanQuery 800: brkan000 (**)
IWMStdKanQuery 801: brkan010, brkan030, whwmd211 (*)
IWMStdKanQuery 802:
IWMStdKanQuery 803: brkan010, brkan030, whwmd211 (*)
IWMStdKanQuery 804:
IWMStdKanQuery 805:
IWMStdKanQuery 806: brkan010, brkan030, whwmd211 (*)
IWMStdKanQuery 807: tisfc001
IWMStdPackingQuery 1: whinh225
IWMStdPackingQuery 2:
IWMStdPackingQuery 3:
IWMStdPackingQuery 4: brpac903
IWMStdPackingQuery 5:
IWMStdPackingQuery 6:
IWMStdPackingQuery 7:
IWMStdPackingQuery 8:
IWMStdPackingQuery 9: (**)
IWMStdPackingQuery 10:
IWMStdPackingQuery 11: brpac902
IWMStdPackingQuery 12: brpac901
IWMStdPackingQuery 13: brpac903
IWMStdPackingQuery 14: brpac902
IWMStdPackingQuery 15: brpac901
IWMStdPackingQuery 16: brpac905
IWMStdPackingQuery 17: whinh225
IWMStdPackingQuery 18: brpac901
IWMStdPackingQuery 21: whinh225
IWMStdPackingQuery 900:
IWMStdQuery 1:
IWMStdQuery 2:
IWMStdQuery 3: whltc100
IWMStdQuery 4: whwmd300
IWMStdQuery 5: whinr140
IWMStdQuery 6:
IWMStdQuery 7:
IWMStdQuery 8:
IWMStdQuery 9:
IWMStdQuery 10:
IWMStdQuery 11:
IWMStdQuery 12:
IWMStdQuery 13:
IWMStdQuery 16:
IWMStdQuery 17:
IWMStdQuery 18: tisfc010
IWMStdQuery 19: tisfc010
IWMStdQuery 20: tisfc001
IWMStdQuery 21:
IWMStdQuery 22: whinr140
IWMStdQuery 24:
IWMStdQuery 26: whinr140
IWMStdQuery 27: whwmd530
IWMStdQuery 28:
IWMStdQuery 29:
IWMStdQuery 30:
IWMStdQuery 31: tcibd401, timfc010
IWMStdQuery 32: tcibd401, timfc010
IWMStdQuery 34: whwmd300
IWMStdQuery 35:
IWMStdQuery 39: whinh225
IWMStdQuery 40:
IWMStdQuery 42:
IWMStdQuery 44: whltc500
IWMStdQuery 45:
IWMStdQuery 49: tcppl030
IWMStdQuery 50:
IWMStdQuery 51:
IWMStdQuery 54: timfc011
IWMStdQuery 57:
IWMStdQuery 59:
IWMStdQuery 60: timfc011
IWMStdQuery 63:
IWMStdQuery 67: whinr140
IWMStdQuery 68:
IWMStdQuery 76: tcibd401, timfc010
IWMStdQuery 93:
IWMStdQuery 94:
IWMStdQuery 95:
IWMStdQuery 102:
IWMStdQuery 112: tcppl101
IWMStdQuery 140: tcmcs001
IWMStdQuery 141:
IWMStdQuery 142:
IWMStdQuery 146:
IWMStdQuery 148:
IWMStdQuery 152: tcibd401
IWMStdQuery 166:
IWMStdQuery 169:
IWMStdQuery 172:
IWMStdQuery 173: (**)
IWMStdQuery 174:
IWMStdQuery 199: whinr100
IWMStdQuery 200:
IWMStdQuery 235: whltc500
IWMStdQuery 236:
IWMStdQuery 237: whinh225
IWMStdQuery 238:
IWMStdQuery 239: whinh225
IWMStdQuery 240:
IWMStdQuery 241:
IWMStdQuery 242:
IWMStdQuery 243:
IWMStdQuery 244:
IWMStdQuery 245:
IWMStdQuery 246:
IWMStdQuery 248:
IWMStdQuery 249:
IWMStdQuery 250:
IWMStdQuery 251:
IWMStdQuery 252:
IWMStdQuery 253:
IWMStdQuery 254:
IWMStdQuery 255: whinr140
IWMStdQuery 256: whwmd530
IWMStdQuery 257:
IWMStdQuery 258:
IWMStdQuery 259: whwmd410
IWMStdQuery 260: (**)
IWMStdQuery 261: (**)
IWMStdQuery 262: whwmd530
IWMStdQuery 263: whwmd530
IWMStdQuery 265: whwmd530
IWMStdQuery 266: whwmd530
IWMStdQuery 267: whwmd530
IWMStdQuery 268: whwmd530
IWMStdQuery 269:
IWMStdQuery 270: whwmd530
IWMStdQuery 271: whwmd530
IWMStdQuery 272:
IWMStdQuery 273: whwmd405
IWMStdQuery 276:
IWMStdQuery 277:
IWMStdQuery 278:
IWMStdQuery 279:
IWMStdQuery 280: whwmd300
IWMStdQuery 281: whltc100
IWMStdQuery 282:
IWMStdQuery 283:
IWMStdQuery 284:
IWMStdQuery 285: whwmd410
IWMStdQuery 286: whwmd405
IWMStdQuery 287:
IWMStdQuery 288:
IWMStdQuery 289: whwmd530
IWMStdQuery 290: tisfc010
IWMStdQuery 291: tcibd401, timfc010
IWMStdQuery 292:
IWMStdQuery 293:
IWMStdQuery 294:
IWMStdQuery 295: tisfc001
IWMStdQuery 296: whwmd530
IWMStdQuery 297:
IWMStdQuery 298: tcppl101
IWMStdQuery 299: whwmd300
IWMStdQuery 300:
IWMStdQuery 301: (**)
IWMStdQuery 302:
IWMStdQuery 303: whwmd530
IWMStdQuery 304:
IWMStdQuery 305: whinh225
IWMStdQuery 306:
IWMStdQuery 307:
IWMStdQuery 308: whwmd260
IWMStdQuery 309:
IWMStdQuery 310:
IWMStdQuery 311:
IWMStdQuery 312: whwmd260
IWMStdQuery 313:
IWMStdQuery 314: whwmd530
IWMStdQuery 315:
IWMStdQuery 316:
IWMStdQuery 317:
IWMStdQuery 318: tirpt040, tirpt041
IWMStdQuery 319: tirpt436
IWMStdQuery 320:
IWMStdQuery 321:
IWMStdQuery 323:
IWMStdQuery 324:
IWMStdQuery 325: timfc010
IWMStdQuery 326: tcibd401, timfc010
IWMStdQuery 327: tcmcs050
IWMStdQuery 328:
IWMStdQuery 329:
IWMStdQuery 330:
IWMStdQuery 331:
IWMStdQuery 332: (**)
IWMStdQuery 333:
IWMStdQuery 334: whltc100
IWMStdQuery 335: whwmd530
IWMStdQuery 336:
IWMStdQuery 337:
IWMStdQuery 338: tiasl145
IWMStdQuery 339: tiasc210
IWMStdQuery 340: whwmd530
IWMStdQuery 341:
IWMStdQuery 342:
IWMStdQuery 350:
IWMStdQuery 351:
IWMStdQuery 400:
IWMStdQuery 401: whinh225
IWMStdQuery 402:
IWMStdQuery 451: whwmd300 (**) (***)
IWMStdQuery 452: (**) (***)
IWMStdQuery 453: (**) (***)
IWMStdQuery 454: bpmdm050 (**) (***)
IWMStdQuery 455: whwmd530 (**) (***)
IWMStdQuery 456: whinr140 (**) (***)
IWMStdQuery 457: (**) (***)
IWMStdQuery 458: (**)
IWMStdQuery 459: tisfc001, tisfc006
IWMStdQuery 460: tcmcs001
IWMStdQuery 461: tcppl010 (**) (***)
IWMStdQuery 462: tisfc021 (**) (***)
IWMStdQuery 463: tisfc041 (**) (***)
IWMStdQuery 464: tisfc042 (**) (***)
IWMStdQuery 465: tisfc031 (**) (***)
IWMStdQuery 466: tisfc032 (**) (***)
IWMStdQuery 467: titrp011 (**) (***)
IWMStdQuery 468: tirou462 (**) (***)
IWMStdQuery 469: tirou001 (**) (***)
IWMStdQuery 470: qmncm001
IWMStdQuery 471: qmncm002
IWMStdQuery 472:
IWMStdQuery 473: tisfc200
IWMStdQuery 474:
IWMStdQuery 475: tiasc222 (**) (***)
IWMStdQuery 476: tiasc213 (**) (***)
IWMStdQuery 500: (**) (***)
(*) If kanban is integrated with warehousing, then whwmd211 is
current. Otherwise brkan010 and brkan030 are current.
(**) It is not possible to remove output row(s).
(***) It is not possible to read output element "lastrecord"
from the query output. When trying to read this output element
by means of public interface FactoryTrackQuery.GetElement,
the system will return an error.
Example implementation:
- Add custom element "ExtAddress" to the output of IWMStdQuery
1, which holds the address code of the warehouse.
- Return an error message in IWMStdQuery 2 if item signal is
filled.
- Skip units in IWMStdQuery 140 which have no description.
#pragma used dll obrextqryapi
#include <bic_dam>
table   ttcmcs001       |* Units
function extern long brext.qry0001.standard.query.extension(
domain  tcmcs.str40     i.query.bde,
long            i.query.number,
domain  tcmcs.s999      i.query.input,
domain  tcmcs.s999      i.query.ext.input,
ref             boolean         o.skip.row,
ref     domain  tcmcs.str999m   o.error.message)
{
long            ret.val
long            exception.id
domain  tccwar          warehouse
domain  tccom.cadr      address
domain  tcitem          item
domain  tcdsca          item.signal.description
o.skip.row = false
o.error.message = ""
on case i.query.bde
case "IFTStdHUPackingQuery":
break
case "IFTStdTimeTrack":
break
case "IWMStdConsignmentWrhQuery":
break
case "IWMStdExtQuery":
break
case "IWMStdHoursQuery":
break
case "IWMStdKanQuery":
break
case "IWMStdPackingQuery":
break
case "IWMStdQuery":
on case i.query.number
case 1:
|* Read the warehouse from the query output.
ret.val = FactoryTrackQuery.GetElement(
"whwmd200cwar",
o.error.message,
exception.id,
warehouse)
if ret.val <> 0 then
return(ret.val)
endif
|* Read the address code.
select  tcmcs003.cadr :address
from    tcmcs003
where   tcmcs003._index1 = { :warehouse }
as set with 1 rows
selectdo
selectempty
address = ""
endselect
|* Create the custom element.
ret.val = FactoryTrackQuery.CreateElement(
"ExtAddress",
domainof(address),
o.error.message,
exception.id,
address)
if ret.val <> 0 then
return(ret.val)
endif
break
case 2:
|* Read the item from the query output.
ret.val = FactoryTrackQuery.GetElement(
"itemcode",
o.error.message,
exception.id,
item)
if ret.val <> 0 then
return(ret.val)
endif
|* Read the item signal
select  tcmcs018.dsca :item.signal.description
from    tcmcs018, tcibd001
where   tcibd001._index1 = { :item }
and     tcibd001.csig <> ""
and     tcibd001.csig refers to tcmcs018
unref skip
as set with 1 rows
selectdo
o.error.message = "Item Signal: " &
item.signal.description
return(DALHOOKERROR)
endselect
break
case 140:
|* Table tcmcs001 is current.
if isspace(tcmcs001.dsca) then
o.skip.row = true
endif
break
default:
break
endcase
endcase
return(0)
}
Pre:    NA
Post:   NA
Input:
i.query.bde             - The called query bde
i.query.number          - The called query number
i.query.input           - The standard query input
i.query.ext.input       - The extended query input
Output:
o.skip.row              - Remove the current query output row
o.error.message         - The error message in case of an error
Return:
0                       - Success
<> 0                    - Error
```
