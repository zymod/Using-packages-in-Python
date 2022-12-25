#!usr/bin/env python
import os
import sys
import package_loader
# Bellow we can import host variable because of imported package_loader
from communication.comm import host

print(host)

# Without package_loader we need:
from custom_packages.communication.comm import port

print(port)
