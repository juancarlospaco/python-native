git_repo = "https://github.com/juancarlospaco/python-native.git"




import sys, subprocess, setuptools, platform
from setuptools.command.install import install
assert platform.architecture()[0] == "64bit", "ERROR: Python must be 64 Bit!. OS must be 64 Bit!."
assert sys.version_info > (3, 5, 0), "ERROR: Python version must be > 3.5!."
subprocess.call("nimble --accept --noSSLCheck install " + git_repo)
setuptools.setup()
