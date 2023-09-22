from pathlib import Path
import time

thispath = Path(__file__)

import python_cad_bundle
try:
    import cadquery
    it_worked = True
except:
    it_worked = False

output_path = r"C:\Users\Alf\Programmering\CAD_Generator\testfile.txt"

if it_worked:
    with open(output_path, "w") as f:
        f.write("It worked!!!!")
        print("success")
else:
    with open(output_path, "w") as f:
        f.write("FAIL!!!!!!!")
        print("Fail")

time.sleep(2)