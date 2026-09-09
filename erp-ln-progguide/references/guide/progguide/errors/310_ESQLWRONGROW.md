# 310 ESQLCARDINALITYVIOLATION - SQL subquery (with comparison) returns more than 1 row
310 ESQLCARDINALITYVIOLATION - SQL subquery (with comparison) returns more than 1 row
| |
|---|
| *Description:* |
| This error occurs if a scalar subquery returns more than 1 row. A subquery that is specified with a comparison operator (=,>, etc.) may return at most 1 row. Note This error applies only to Infor Enterprise Server releases. |
| *Solution:* |
| Ensure all subqueries with a comparison return at most one row. |
