import os

from setuptools import setup

def read(*paths):
  """Build a file path from *paths* and return the contents."""
  with open(os.path.join(*paths), 'r') as f:
    return f.read()

setup(
  name='Pi7SegPy',
  version='0.1.0',
  description='Easily use Multiple 7 segment displays connected to 74HC595 and Other Shift registers with your Raspberry Pi',
  long_description=(read('README.rst')),
  url='https://github.com/shrikantpatnaik/Pi7SegPy',
  license='MIT',
  author='Shrikant Patnaik',
  author_email='me@shrikantpatnaik.com',
  py_modules=['Pi7SegPy'],
  install_requires=['PiShiftPy'],
  include_package_data=True,
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ],
  )
