"""hello program
"""

import sys
define_1 = "Grace_kid.py"
define_2 = "w"
define_3 = 0
def grace():
    try:
        file = open(define_1, define_2)
    except:
        sys.exit(define_3)
    s = "{2}{2}{2}hello program{0}{2}{2}{2}{0}{0}import sys{0}define_1 = {2}Grace_kid.py{2}{0}define_2 = {2}w{2}{0}define_3 = 0{0}def grace():{0}{1}try:{0}{4}file = open(define_1, define_2){0}{1}except:{0}{4}sys.exit(define_3){0}{1}s = {2}{3}{2}{0}{1}file.write(s.format(chr(10),chr(32)*4,chr(34),s,chr(32)*8)){0}{1}file.close(){0}{0}grace(){0}"
    file.write(s.format(chr(10),chr(32)*4,chr(34),s,chr(32)*8))
    file.close()

grace()
