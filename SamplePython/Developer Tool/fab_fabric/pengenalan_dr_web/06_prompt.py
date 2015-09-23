"""
prompt (fabric.operations.prompt)

When you find yourself in need of some extra flexibility working with Fabric, 
prompt will come to your rescue. This command does exactly what its name suggests and asks 
the user (i.e. one that is running the script) to input a certain data to use during 
the successive execution.

If you are using a single file to manage with multiple applications, for example, 
you can use prompt to set one to perform the actions.

Before starting with anything, prompt can also be used to query the port number to use.

Usage examples:
"""

from fabric.api import prompt
# Prompt the user
port_number = prompt("Which port would you like to use?")

# Prompt the user with defaults and validation
port_number = prompt("Which port?", default=42, validate=int)