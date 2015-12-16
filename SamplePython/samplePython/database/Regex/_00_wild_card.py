"""
The question mark will match a single character with any value on a filename.
For example, a pattern such as file?.xml will match file1.xml , file2.xml ,
and file3.xml , but it won't match file99

In this expression, we can find two kind of components: literals ( file and .xml )
and metacharacters ( ? ). The regular expressions are
much more powerful than the simple patterns we can typically find on the operating
system command line. A regular expression is a pattern of text that consists of ordinary characters
(for example, letters a through z or numbers 0 through 9) and special characters
known as metacharacters.


In regular expressions, there are twelve metacharacters that should be escaped if
they are to be used with their literal meaning:
•     Backslash \
•     Caret ^
•     Dollar sign $
•     Dot .
•     Pipe symbol |
•     Question mark ?
•     Asterisk *
•     Plus sign +
•     Opening parenthesis (
•     Closing parenthesis )
•     Opening square bracket [
•     The opening curly brace {

Escape the metacharacters by preceding them with a backslash.

In some cases, the regular expression engines will do their best to understand if they
should have a literal meaning even if they are not escaped; for example, the opening
curly brace { will only be treated as a metacharacter if it's followed by a number to
indicate a repetition
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|                (garis vertikal)                   untuk pemilihan;
( dan )          (kurung buka dan kurung tutup)     untuk pengelompokan;
[ dan ]          (kurung siku buka dan tutup)       untuk membuat set karakter/ character classes;
?                (tanda tanya)                      untuk mengartikan opsional.
*                (Asterik)                          mendapatkan nol atau lebih
+                (plus sign)                        mendapatkan satu atau lebih
{n,m}            (Curly braces)                     Between n and m times


Syntax           Description
{n}              The previous character is repeated exactly n times.
{n,}             The previous character is repeated at least n times.
{,n}             The previous character is repeated at most n times.
{n,m}            The previous character is repeated between n and m times (both inclusive).
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
SET KARAKTER (CHARACTER CLASSES)
Element          Description                            
[                Matches the following set of characters
0-9              Matches anything between 0 and 9 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9).
a-z              Matches anything between a and z (a, b, c, d, ..., z)
A-Z              Matches anything between A and Z (A, B, C, D, ..., Z)
^                Negation if in the first char of clurlybracket, if not in curlybracket it Matches the beginning of the line
\/               Matches a / character
\                Matches a \ character
]                End of character set

If we have a character class such as [0-9] meaning anydigit, the negated character class [^0-9] will match anything that is not a digit.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
SHORTCUT
Element   Description (for regex with default flags)
.         This element matches any character except newline \n
\d        This matches any decimal digit; this is equivalent to the class [0-9]
\D        This matches any non-digit character; this is equivalent to the class [^0-9]
\s        This matches any whitespace character; this is equivalent to the class [⇢\t\n\r\f\v]
\S        This matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v]
\w        This matches any alphanumeric character; this is equivalent to the class[a-zA-Z0-9_]
\W        This matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_]
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""