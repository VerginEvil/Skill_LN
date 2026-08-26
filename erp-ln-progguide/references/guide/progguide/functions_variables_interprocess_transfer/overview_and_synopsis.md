# Variables (inter-process transfer) overview and synopsis

## Overview
Use these functions to access the variables of other processes. The variables can be of any type. They must be declared as external (with the keyword EXTERN).

## Synopsis
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
| | | |
|---|---|---|
|  | [get.var()](get.var.md) | `( long processno, "variable", ref variable )` |
|  | [get.indexed.var()](get.indexed.var.md) | `( long processno, "variable", ref variable, long dim1 [, long dim2, long dim3, long dim4 ] )` |
|  | [put.var()](put.var.md) | `( long processno, "variable", expression )` |
|  | [put.indexed.var()](put.indexed.var.md) | `( long processno, "variable", expression, long dim1 [, long dim2, long dim3, long dim4 ] )` |
|  | [import()](import.md) | `( "variable", ref variable )` |
|  | [export()](export.md) | `( "variable", expression )` |
|  | [import.4gl.var()](import.4gl.var.md) | `( "variable", expression )` |
