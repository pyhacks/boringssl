import ctypes
import os

import rootwin


dir_name = os.path.split(__file__)[0]
root_interface = rootwin.root_interface


def load_boringssl():
    root_interface.ProcessLine(b".include boringssl")
    root_interface.ProcessLine(b".include boringssl/include")
    root_interface.ProcessLine(b".include boringssl/ssl")    
    root_interface.ProcessLine(b"""#include \"openssl/ssl.h\"""")    
    root_interface.ProcessLine(b"""#include \"internal.h\"""")
    root_interface.ProcessLine(b""".L ssl.dll""")
    root_interface.ProcessLine(b""".L crypto.dll""")
    root_interface.ProcessLine(b""".L pki.dll""")
    root_interface.ProcessLine(b""".L decrepit.dll""")
    root_interface.ProcessLine(b""".L boringssl_gtest.dll""") 


def init():
    cd = os.getcwd()
    os.chdir(dir_name)  
    load_boringssl()
    os.chdir(cd)


init()
