pybgfx
========

pybgfx provides python bindings for [bgfx](https://github.com/bkaradzic/bgfx).  It uses no dependencies other than [ctypes](https://docs.python.org/2/library/ctypes.html) for Python.

[PyPI](https://pypi.python.org/pypi/pybgfx)

Hello World:

<img align="left" src="https://github.com/jnadro/pybgfx/blob/master/helloworld.png">

Examples
--------

See my other repo with bgfx examples ported to python! [Link](https://github.com/jnadro/pybgfx_examples)


Functions Implemented
---------------------

Here are a list of the bgfx functions that have bindings that have been tested.

35 / 130 ~26%

* vertex_decl_begin
* vertex_decl_add
* vertex_decl_skip
* vertex_decl_end
* init
* shutdown
* reset
* frame
* alloc
* copy
* get_renderer_type
* set_debug
* dbg_text_clear
* dbg_text_printf
* dbg_text_image
* create_index_buffer
* destroy_index_buffer
* alloc_transient_buffers
* set_transient_index_buffer
* set_transient_vertex_buffer
* create_shader
* create_program
* destroy_program
* create_uniform
* destroy_uniform
* set_state
* set_transform
* set_index_buffer
* set_vertex_buffer
* set_view_rect
* set_view_clear
* set_view_transform
* touch
* submit
* set_platform_data

Todo
----

* Cleanup respository (too many things in root directory)
* Write a tutorial
* Installation instructions
* Implement the rest of the bgfx Examples
* Test on Mac
* Remove bgfx and glfw binaries
* Write documentation

Features
--------

TODO

Installation
------------

Currently only works for Windows 64-bit.

```
pip install pybgfx
```

Contribute
----------

- Source Code: [github.com/jnadro/pybgfx](github.com/jnadro/pybgfx)

For development purposes you can locally install this package to test.  This can be done with the following pip command:

```
python -m pip install -e C:\path\to\this\directory\on\your\harddrive
```

If the src/bgfx, src/bx, src/bximg or src/glfw are empty after cloning this repo you will need to manually pull down these submodules like so.  See **Cloning a Project with Submodules** [here](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

```
git submodule init
git submodule update
```

Building bgfx is straight forward on windows.  Detailed instructions are [here](https://bkaradzic.github.io/bgfx/build.html), but as a quick reminder:

1. ```cd bgfx```
2. ```..\bx\tools\bin\windows\genie --with-examples --with-dynamic-runtime vs2017```
3. ```start .build\projects\vs2017\bgfx.sln```
4. Pick **Release** and **x64** and build the whole solution.

Debugging
---------

Sometimes it is necessary to have to debug the bindings to see how the data is being passed between Python and C.  [This](https://docs.microsoft.com/en-us/visualstudio/python/debugging-mixed-mode-c-cpp-python-in-visual-studio?view=vs-2017) article shows how to do mixed mode debugging in Visual Studio.

1. Build debug versions of the bgfx dll.  Place **bgfx-shared-libDebug.dll** and **bgfx-shared-libDebug.pdb** in the pybgfx/pybgfx directory.
2. Setup a python project in visual studio.

todo: fillout more details and set up an example project.

Deployment
----------

Requirements: pip install twine

1. Clean **pybgfx.egg-info**, **dist**, and **build** directories.
2. Bump version in setup.py
3. python setup.py sdist
4. twine upload dist/*

Support
-------

If you are having issues, please let us know.

License (BSD 2-clause)
----------------------

<a href="http://opensource.org/licenses/BSD-2-Clause" target="_blank">
<img align="right" src="http://opensource.org/trademarks/opensource/OSI-Approved-License-100x137.png">
</a>

	Copyright (c) 2016, Jason Nadro
	All rights reserved.

	Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

	1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

	2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


[bgfx License (BSD 2-clause)](https://bkaradzic.github.io/bgfx/license.html)
-----------------------------------------------------------------------

<a href="http://opensource.org/licenses/BSD-2-Clause" target="_blank">
<img align="right" src="http://opensource.org/trademarks/opensource/OSI-Approved-License-100x137.png">
</a>

	Copyright 2010-2016 Branimir Karadzic. All rights reserved.
	
	https://github.com/bkaradzic/bgfx
	
	Redistribution and use in source and binary forms, with or without
	modification, are permitted provided that the following conditions are met:
	
	   1. Redistributions of source code must retain the above copyright notice,
	      this list of conditions and the following disclaimer.
	
	   2. Redistributions in binary form must reproduce the above copyright
	      notice, this list of conditions and the following disclaimer in the
	      documentation and/or other materials provided with the distribution.
	
	THIS SOFTWARE IS PROVIDED BY COPYRIGHT HOLDER ``AS IS'' AND ANY EXPRESS OR
	IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
	MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
	EVENT SHALL COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
	INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
	(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
	LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
	ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
	(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
	THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

[glfw License (zlib)](http://www.glfw.org/license.html)
-------------------------------------------------------

	Copyright (c) 2002-2006 Marcus Geelnard
	Copyright (c) 2006-2010 Camilla Berglund <elmindreda@elmindreda.org>

	This software is provided 'as-is', without any express or implied
	warranty. In no event will the authors be held liable for any damages
	arising from the use of this software.

	Permission is granted to anyone to use this software for any purpose,
	including commercial applications, and to alter it and redistribute it
	freely, subject to the following restrictions:

	1. The origin of this software must not be misrepresented; you must not
	   claim that you wrote the original software. If you use this software
	   in a product, an acknowledgment in the product documentation would
	   be appreciated but is not required.

	2. Altered source versions must be plainly marked as such, and must not
	   be misrepresented as being the original software.

	3. This notice may not be removed or altered from any source
	   distribution.
