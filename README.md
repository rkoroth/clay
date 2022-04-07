# CLAY

Clay stands between Orchastration software and a stand-alone script.
It helps to write stand-alone automation script by means ready made modules.

## Internal Structure

Basically clay.py is the main wrapper and often no need to modify.
and clay.py is not meant to be modified by user.

user will modify conf/clay/xyz.yaml 
and the sequence.yaml for the sequence.

When to modify the clay.py .?

- when we create any module for a specific task.

then we need to modify the clay.py (import that moddule)

module should be written in clay standard. so it will work seamlessly.


