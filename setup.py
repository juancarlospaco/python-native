import os, sys, subprocess, setuptools, platform
from setuptools.command.install import install

git_repo = "https://github.com/juancarlospaco/python-native.git"




assert platform.architecture()[0] == "64bit", "ERROR: Python must be 64 Bit!. OS must be 64 Bit!."
assert sys.version_info > (3, 5, 0), "ERROR: Python version must be > 3.5!."
class CustomInstall(install):
  def run(self):
    install.run(self)
    subprocess.call("nimble --accept --noSSLCheck install " + git_repo)

setup(cmdclass={"install": CustomInstall})
