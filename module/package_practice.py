# import myfirstpackage.module1
# import myfirstpackage.module2
# myfirstpackage.module1.myfunc()
# myfirstpackage.module2.myfunc()

# from myfirstpackage import module1, module2
# module1.myfunc()
# module2.myfunc()

# from myfirstpackage.module1 import myfunc
# myfunc()

# import myfirstpackage
# myfirstpackage.myfunc()

# from myfirstpackage.subdir import *
# myfunc()
# myfunc2()

import myfirstpackage.subdir.module2
myfirstpackage.subdir.module2.myfunc2()