# Maps Workbench synopsis
```
long
```
```
void
```
```
long
```
```
long
```
```
long
```
```
void
```
```
void
```
```
void
```
```
void
```
```
long
```
```
void
```
```
void
```
```
void
```
```
double
```
```
boolean
```
| | | |
|---|---|---|
|  | [map.create()](map.create.md) | `()` |
|  | [map.delete()](map.delete.md) | `(long mid)` |
|  | [map.add.point()](map.add.point.md) | `(long mid, double lat, double lon, string icontype)` |
|  | [map.add.arrow()](map.add.arrow.md) | `(long mid, const string start.pointid, const string end.pointd, long arrow.direction, long arrow.weight, const string arrow.color, boolean is.clickable, const string arrowid)` |
|  | [map.disable.route()](map.disable.route.md) | `(long mid)` |
|  | [map.add.circle()](map.add.circle.md) | `(long rpid, double radius, string color, double opacity)` |
|  | [map.set.shapecolor()](map.set.shapecolor.md) | `(long rpid, string color)` |
|  | [map.set.shapeicon()](map.set.shapeicon.md) | `(long rpid, string image)` |
|  | [map.set.shapetext()](map.set.shapetext.md) | `(long rpid, string text)` |
|  | [map.add.info()](map.add.info.md) | `(long rpid, string title)` |
|  | [map.add.infoline()](map.add.infoline.md) | `(long infoid, string label, string value)` |
|  | [map.add.legendline()](map.add.legendline.md) | `(long mid, string label, string icontype[, string color])` |
|  | [map.show()](map.show.md) | `(long mid, string title)` |
|  | [map.getroutedistance()](map.getroutedistance.md) | `(long mid)` |
|  | [map.is.active()](map.is.active.md) | `(long mid)` |

## Related topics
- [Maps Workbench overview](overview.md)

- [Maps Workbench examples](examples.md)
