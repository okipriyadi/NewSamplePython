"""
spur = run commands and manipulate files locally or over SSH using the same interface
"""
import spur 

shell = spur.LocalShell()
result = shell.run(["echo", "-n", "hello"])
print result.output 