import sys
# import python_cad_bundle
from pprint import pprint

lib = "C:\Users\Alf\Programmering\snap-generator\cadquery_bundled\lib"
if lib not in sys.path:
    sys.path.append(lib)

import cadquery
with open("test_file.txt", "w") as f:
    f.write("yes it worked")

