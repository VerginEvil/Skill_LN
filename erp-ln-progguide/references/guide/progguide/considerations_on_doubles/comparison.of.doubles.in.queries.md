# Comparison of doubles in queries

## Problem description
The comparison of two doubles or floats inside queries is unreliable. For example, if a query contains the expression "double.col > 1.23" then a value may be returned which is equal to, or even slightly less than, 1.23. If an expression "double.col = 1.23" is in a query, and the database contains the value 1.23 it may, or may not be returned. This can lead to programs taking wrong decisions.

## Rewriting comparisons
If a query contains a construction like
where double.col = 0.0
and the tolerance of the comparison is known, it can be rewritten into
where double.col > 0.0 -:tolerance and double.col < 0.0 +:tolerance
Similarly, the expression
double.col > 0.0
can be rewritten into
double.col > 0.0 -:tolerance
If the absolute difference between two doubles is (approximately) equal to the tolerance, the result is still unpredictable.

## Related topics
- [Reliability of double.cmp()](reliability.of.double.cmp.md)

- [Comparison of doubles in queries](comparison.of.doubles.in.queries.md)
