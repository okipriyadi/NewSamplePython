"""
settings (fabric.context_managers.settings)

When you need to temporarily (i.e. for a certain command chain), 
you can use the settings statement (i.e. override env values).

Usage examples:
"""
from fabric.api import settings, sudo
# Perform actions using a different *user*
with settings(user="avionics"):
    sudo("cmd")
    
