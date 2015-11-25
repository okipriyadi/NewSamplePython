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

| (garis vertikal) untuk pemilihan;
( dan ) (kurung buka dan kurung tutup) untuk pengelompokan;
[ dan ] (kurung siku buka dan tutup) untuk membuat set karakter;
? (tanda tanya) untuk mengartikan opsional.

"""