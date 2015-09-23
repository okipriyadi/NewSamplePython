"""
prefix (fabric.context_managers.prefix)

prefix statement does what its name suggests and wraps given run and sudo command 
with the specified one.

Usage examples:
"""
with prefix("cmd arg."):
    run("./start")
# cmd arg. && ./start
