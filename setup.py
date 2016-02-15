"""Setup module for pybgfx

based on:
https://python-packaging-user-guide.readthedocs.org/en/latest/distributing/#requirements-for-packaging-and-distributing
https://github.com/pypa/sampleproject/blob/master/setup.py
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pybgfx",

    # Version scheme: 
    # https://python-packaging-user-guide.readthedocs.org/en/latest/distributing/#choosing-a-versioning-scheme
    version="1.0.0.dev1",

    description="Python bindings for bgfx.",
    long_description=long_description,

    url="https://github.com/jnadro/pybgfx",

    author="Jason Nadro",

    license="BSD 2-clause",

    classifiers=[
        # How mature is this project?
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD 2-clause",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython"
        "Operating System :: Microsoft :: Windows",
        "Topic :: Multimedia :: Graphics :: 3D Rendering"
    ],

    keywords="graphics, bgfx, opengl, directx",

    package_data={
        # I'm not sure if this will work or is proper, but I am packing
        # Windows specific dlls so pybgfx can find them without the user
        # building them.
        "pybgfx": ["bgfx-shared-lib.dll", "glfw3.dll", "renderdoc.dll"]
    },
)
