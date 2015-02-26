from distutils.core import setup, Extension
import os
os.environ["CC"] = 'g++'
setup(name='textify', version='1.0',  \
      ext_modules=[
      Extension('textify', 
        ['textifymodule.c'],
        include_dirs=['/usr/local/include'],
        library_dirs=['/usr/local/lib'],
        libraries=['textify'])
      ])