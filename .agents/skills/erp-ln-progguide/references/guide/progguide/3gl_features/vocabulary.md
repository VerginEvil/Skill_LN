# Vocabulary

## Character set
You can include the following characters in a 3GL language statement:

- the full alphabet - a-z and A-Z §

- the digits 0-9 §

- the characters # $ ^ & * ( ) - _ + = { } [ ] | \;: ",. / < >

This document uses uppercase characters to indicate keywords. However, this is not necessary in your programs.

## Continuation symbol
If a statement does not fit on one line, you can split it across two or more lines. There is no limit to the number of lines that you can use for one statement. Wherever you can include a space, you can also make a new line.
There are two exceptions: a string constant and a macro definition. If these do not fit on one line, you must place a caret symbol [^] at the beginning of the second and subsequent lines. You can use the caret symbol in other statements also, but this is not necessary.

## Comment
The pipe symbol [|] indicates that the text from the symbol to the end of the line must be handled as a comment. The compiler ignores this text. Good comments help the reader of a program source to understand the program better.

## Separators
You can use tabs, newlines, and spaces as separators in your program.

## Reserved words
The Baan 3GL programming language includes a number of words with defined meanings. These are reserved words that you cannot use other than in the context for which they were designed. Not all these words are described in this document; some are for internal use or for compatibility with older releases.
The following is a list of these reserved words:
| | | | |
|---|---|---|---|
| AND AT BASE BASED BOOLEAN BREAK BSET CALL CASE COMMON CONST CONTINUE DEFAULT DELETE DELETEEMPTY DELETEERROR DIM DLLUSAGE DOMAIN DOUBLE ELSE | EMPTY END ENDCASE ENDFOR ENDFUNCTIONUSAGE ENDDELETE ENDIF ENDUPDATE ENDWHILE ENDSELECT ENDDLLUSAGE EQ EXTERN FALSE FIXED FOR FUNCTION FUNCTIONUSAGE GE GLOBAL GOTO | GT IF IN INPUT LE LONG LT MB MULTIBYTE NE NOT ON OR PRINT PROMPT REF REFERENCE REPEAT RETURN SELECT SELECTBIND | SELECTDO SELECTEMPTY SELECTEOS SELECTERROR STATIC STEP STOP STRING TABLE THEN TO TRUE UNTIL UPDATE UPDATEEMPTY UPDATEERROR VOID WHEREBIND WHEREUSED WHILE |

## Related topics
- [3GL programming language features: overview](overview.md)
