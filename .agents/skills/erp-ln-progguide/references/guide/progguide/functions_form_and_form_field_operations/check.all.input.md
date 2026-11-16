# check.all.input()

## Syntax:
`function void check.all.input( )`

## Description
This executes all [check.input](../4gl_features/4gl_field_sections.md) subsections (if any) included in the program script. When an input error is detected, the [choice.again()](choice.again.md) function is automatically executed. The check.all.input function doesn't work for array fields.
When a DAL is used, the property checks in the DAL are executed after the *check.input* subsections of the UI script are executed.

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Example
```

choice.cont.process:
before.choice:
check.all.input()
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
