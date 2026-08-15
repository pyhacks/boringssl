# boringssl
[rootwin](https://github.com/pyhacks/rootwin) is used to access boringssl from python strings containing C++ code.

# Usage
boringssl.root_interface.**ProcessLine**(code)

You can find documentation about this function [here](https://github.com/pyhacks/rootwin#python-api)

# Example
```python
import boringssl

boringssl.root_interface.ProcessLine(b"const SSL_METHOD *method = TLS_method();")
boringssl.root_interface.ProcessLine(b"std::cout << method << \"\\n\";")
```
