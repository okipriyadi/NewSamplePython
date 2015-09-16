"""
A simple but integral aspect of Fabric is what is known as the “environment”: 
a Python dictionary subclass, which is used as a combination settings registry and 
shared inter-task data namespace.

The environment dict is currently implemented as a global singleton, 
fabric.state.env, and is included in fabric.api for convenience. 
Keys in env are sometimes referred to as “env variables”.
"""

