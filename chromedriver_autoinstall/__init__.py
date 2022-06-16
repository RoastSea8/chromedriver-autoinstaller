from chromedriver_autoinstall import script
import os

def install():
   script.install()
   path = os.path.abspath(os.getcwd())
   print(f"install path: {path}")

def get_platform():
   return script.get_platform()

def get_version():
   return script.get_version()