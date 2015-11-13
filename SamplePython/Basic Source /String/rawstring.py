"""
You should also have noticed a small " r " in front of the folder name. If you've read
Chapter 1, then you know this means to designate the object as a "raw string," or one that
takes all characters of a string verbatim, meaning do not translate special character combi-
nations. For example, \n usually means a newline character, but in a raw string, it means
(literally) two characters: a backslash followed by an n . So the purpose of a raw string is
specifically for DOS file paths, telling Python to not translate special characters (if there
are any).
"""

a = r'==>\n\tsaya<=='
b = '==>\n\tsaya<=='

print "a = ", a
print "b = ", b