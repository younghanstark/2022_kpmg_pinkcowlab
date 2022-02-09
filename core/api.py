import sys
import string_processing as sp
import base64

inputString = sys.argv[1]
result = sp.get_core(inputString)
print(base64.b64encode(result.encode('utf-8')))
