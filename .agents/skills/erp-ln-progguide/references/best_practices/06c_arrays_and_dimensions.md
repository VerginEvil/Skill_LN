# Pillar 5: Domain Arrays & Dimension Mechanics

> **Hub**: [4GL Coding Standards & Caveats Hub](06_4gl_coding_standards_and_caveats.md)

---

## 6. Pillar 5: Domain Arrays and Dimension Mechanics

Arrays in Baan 4GL operate within fixed bshell runtime memory blocks. Violating array boundary rules causes silent memory corruption or unrecoverable bshell process terminations.

### 6.1 1-Based Indexing and Zero-Index Prohibition

Unlike C or Java, Baan 4GL arrays are strictly **1-based**. The first valid element of an array is at index `1`, and the last element is at index `N` (where `N` is the declared dimension size).

```baan
|* Declared dimension: 5 elements (indices 1, 2, 3, 4, 5)
domain tcitem item_list(5)
```

#### The Zero-Index Catastrophe:
- Accessing `item_list(0)` is an out-of-bounds memory access.
- In some bshell versions, index 0 does not immediately throw a bounds error, but reads or writes into adjacent variable memory on the execution stack, corrupting neighboring variables.
- In modern Infor LN Cloud, accessing index 0 or index > N triggers fatal process termination: `bshell error: Array index out of bounds`.

#### Rules:
1. Always iterate starting at `1`: `for i = 1 to max_elements`.
2. Never iterate from `0`: `for i = 0 to max_elements - 1` is strictly forbidden.
3. Guard all dynamic index calculations with boundary checks: `if idx >= 1 and idx <= MAX_DIM then ... endif`.

---

### 6.2 Declaring Dimensioned Domain Arrays: Numeric vs. String Domains (Rule ARR002)

When declaring arrays in Baan 4GL, developers must understand the critical architectural distinction between **Numeric / Enum / Date domains** and **String domains**.

#### 1. Numeric, Long, Date, and Enum Domains (Single Dimension `arr(count)`)
For numeric, date, long, double, and enum domains, declaring `domain <domain_name> arr(count)` allocates an array of `count` scalar elements (1-based indices `1..count`), accessed via `arr(i)`:

```baan
#define MAX_ELEMENTS 500

|* Single-dimensional domain arrays for numeric/date/enum types
domain tcamnt     period_totals(MAX_ELEMENTS) |* 500 currency amounts (1..500), accessed as period_totals(i)
domain tcpono     line_numbers(MAX_ELEMENTS)  |* 500 line positions (1..500), accessed as line_numbers(i)
domain tcdate     batch_dates(MAX_ELEMENTS)   |* 500 dates (1..500), accessed as batch_dates(i)
domain tfacr.trec mark_trec(MAX_ELEMENTS)     |* 500 transaction types (1..500), accessed as mark_trec(i)
domain tfgld.docn mark_ninv(MAX_ELEMENTS)     |* 500 document numbers (1..500), accessed as mark_ninv(i)

|* Multi-dimensional domain array for numeric matrices
domain tcamnt     period_matrix(12, 5)        |* 12 months x 5 cost centers, accessed as period_matrix(m, c)
```

#### 2. String Domains (Mandatory 2D Syntax: `string arr(len, count)`)
> [!CAUTION]
> **The 1D String Domain Catastrophe (Rule ARR002)**:
> In Baan 4GL (`bic` compiler), **strings are character arrays**.
> If you write:
> ```baan
> |* WRONG: This declares a single string of length 500, NOT 500 strings!
> domain tccom.bpid mark_itbp(500)
> ```
> The bshell compiler treats `(500)` as the character length of a single string variable (overriding the domain's default length), **NOT** an array of 500 strings.
> Subsequently accessing `mark_itbp(i)` or `mark_itbp(1, i)` fails at compilation with:
> `Illegal number of array subscripts for 'mark_itbp'`.

To declare an array of strings in Baan 4GL, you must use **2-dimensional string syntax**:
- **Dimension 1**: String buffer length / character width (e.g., 9 for Business Partner IDs, 3 for Transaction Types).
- **Dimension 2**: Number of elements in the array.

```baan
#define MAX_MARKED_LINES 500

|* Correct 2D String Array Declarations: string arr(string_length, array_size)
string mark_itbp(9, MAX_MARKED_LINES)   |* 500 Business Partner IDs (9 chars each)
string mark_ttyp(3, MAX_MARKED_LINES)   |* 500 Transaction Types (3 chars each)
string cust_list(9, MAX_MARKED_LINES)   |* 500 Customer IDs (9 chars each)
```

#### Accessing 2D String Arrays:
String arrays require **2 subscripts**: `arr(start_char_pos, element_index)`. Subscript 1 is the 1-based character position within the string (usually `1`), and subscript 2 is the 1-based element index:

```baan
|* Storing into string array element 'marked_count' starting at character 1
mark_itbp(1, marked_count) = txcmg010.itbp
mark_ttyp(1, marked_count) = txcmg010.ttyp
cust_list(1, c)            = txcmg010.itbp

|* Reading / comparing from string array element 'i'
if cust_list(1, i) = txcmg010.itbp then
    ...
endif
```

For Data Dictionary domains that themselves have predefined array dimensions (configured in `ttadv4500m000`), declaring `domain <array_domain> var_name` automatically allocates all elements defined by the domain.

---

### 6.3 Passing Arrays Across Function Signatures (`fixed` and `()`)

Passing arrays across function boundaries requires explicit signature conventions in 4GL:

1. **Unbounded Dimension Notation (`()`)**:
   Use empty parentheses in the function parameter signature to accept single-dimensional arrays of any declared length:
   ```baan
   function long summarize_amounts(
       const domain tcamnt i.amounts(),
       const long          i.num_elements,
       ref   domain tcamnt o.total_sum)
   ```

2. **Multi-Dimensional Notation with `fixed`**:
   For multi-dimensional arrays, use the `fixed` keyword for each dimension dimensioned by the caller:
   ```baan
   function long process_matrix(
       domain tcamnt io.grid(fixed, fixed),
       const long    i.rows,
       const long    i.cols)
   ```

3. **Invocation Syntax**:
   When invoking a function that takes an array parameter, pass the array identifier **without subscript brackets**:
   ```baan
   summarize_amounts(l.order_amounts, 5, l.total)
   ```

#### Anti-Pattern vs. Compliant Pattern:
```baan
|* ========================================================================
|* ANTI-PATTERN: 0-based iteration and subscript passing syntax errors
|* ========================================================================
function void process_buffer()
{
    domain tcitem items(5)
    long i

    for i = 0 to 4                      |* FATAL: items(0) corrupts stack memory!
        items(i) = "ITEM" & str$(i)
    endfor

    send_items(items(1))                |* ERROR: Passes only element 1 instead of whole array!
}

|* ========================================================================
|* COMPLIANT PATTERN: 1-based bounds and valid array signature passing
|* ========================================================================
function void process_buffer()
{
    domain tcitem items(5)
    long i

    for i = 1 to 5                      |* CORRECT: Clean 1-based loop
        items(i) = "ITEM" & str$(i)
    endfor

    send_items(items, 5)                |* CORRECT: Passes entire array symbol
}

function long send_items(
    const domain tcitem i.items(),
    const long          i.count)
{
    long i
    for i = 1 to i.count
        log_item(i.items(i))
    endfor
    return(0)
}
```
