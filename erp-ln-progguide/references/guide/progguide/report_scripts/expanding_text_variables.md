# Expanding text variables
Variables or expressions that are included in text lines can be expanded or substituted for report purposes. You must set the variable *lattr.textexpand=TRUE* if you want this to happen. Expressions are internally evaluated by the function [expr.compile()](../functions_expressions_runtime/expr.compile.md).
Customers can use variables in texts. For example, "address", "city", "salary" and so on. Customers must be informed about these variables so that they can use them.

## Syntax
The following is the syntax for variables and expressions included in text lines:
`$ variable or # variable`
`${ expression} or #{ expression}`
When the $ symbol if used, the text moves over to accommodate the expanded variable or expression. When the # symbol is used, the expanded variable or expression overwrites existing text.

## Example
The following is an example of text created by using the text manager. The text includes both variables and expressions that can be expanded/substituted for report purposes.
```

To:     $surname $christian name        #date   , Ede
        $address
        $ZIP code  $city

Dear $christian name:
We have the pleasure of informing you that, as of $date, your salary has been
raised by 5%. For you this implies a gross amount of
${edit( salary + ( salary * 0.05 ), "ZZZZ9,ZZ" )} per month.

                                Kind regards,  $Mgr.
```

## Related topics
- [Report scripts overview](overview.md)

- [Report script sections](sections.md)

- [Predefined variables](predefined_variables.md)

- [Report script functions](functions_in_report_scripts.md)
