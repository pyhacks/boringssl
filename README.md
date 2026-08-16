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

# Version Info
Boringssl commit [673e61fc215b178a90c0e67858bbf162c8158993](https://github.com/google/boringssl/tree/673e61fc215b178a90c0e67858bbf162c8158993) is taken as a basis and then it is further patched using the [boringssl.patch](https://github.com/lexiforest/curl-impersonate/blob/9607b22ccf6c440e560c5f8ad5292b8044bb6dd7/patches/boringssl.patch) file from [curl-impersonate](https://github.com/lexiforest/curl-impersonate/tree/9607b22ccf6c440e560c5f8ad5292b8044bb6dd7) v1.5.2 in order for it to be compatible with [curl-cffi](https://github.com/lexiforest/curl_cffi) v0.15.0. 
