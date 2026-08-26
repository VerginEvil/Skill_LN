# Reliability of double.cmp()
Suppose the following variables:
| |
|---|
| double1 = 1.0000 |
| double2 = 1.0001 |
| tolerance= 0.0001 |
Question: are these doubles equal to each other? Expected answer is 'No' because the difference between the doubles is not less than the tolerance. However, this is not completely reliable. You need knowledge about the internal format of a double. Especially variable 'double2' will have some "disturbance". Herewith the difference can become somewhat less than 0.0001 or somewhat greater than 0.0001. Also the tolerance itself will be "disturbed". Since the double.cmp function has also used double comparison the result is unpredictable.

## Example
| | | |
|---|---|---|
| Variable | Value | Approximate 'real' value |
| double1 | 1.1 | 1.10000000000000010000 |
| double2 | 1.2 | 1.20000000000000000000 |
| difference | 0.1 | 0.09999999999999986700 |
| tolerance | 0.1 | 0.10000000000000000600 |
Now according double.cmp() these two variables are equal ! Do we this again with the original values (so: double.cmp(1.1, 1.2, 0.1) then the conclusion is that 1.1 is less than 1.2 ! Another example: double.cmp(1.2, 1.3, 0.1) = -1 (because 1.2 is less than 1.3).

## Conclusion
When the difference between two doubles is (almost) equal to the tolerance then double.cmp() gives unreliable results.

## Related topics
- [Considerations on doubles](considerations.on.doubles.md)
- [Reliability of double.cmp()](reliability.of.double.cmp.md)
- [Comparison of doubles in queries](comparison.of.doubles.in.queries.md)
