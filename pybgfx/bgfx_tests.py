import ctypes
import bgfx
import unittest

class TestImport(unittest.TestCase):

    def test_module(self):
        self.assertEqual(bgfx.__author__, 'Jason Nadro')
        self.assertEqual(bgfx.__license__, 'BSD 2-clause')
        self.assertEqual(bgfx.__status__, 'Development')

class TestEnums(unittest.TestCase):

    def test_bgfx_renderer_type(self):
        self.assertEqual(type(bgfx.BGFX_RENDERER_TYPE_NOOP), ctypes.c_int)
        
        self.assertEqual(bgfx.BGFX_RENDERER_TYPE_NOOP.value, 0)
        self.assertEqual(bgfx.BGFX_RENDERER_TYPE_DIRECT3D9.value, 1)
        self.assertEqual(bgfx.BGFX_RENDERER_TYPE_DIRECT3D11.value, 2)
        self.assertEqual(bgfx.BGFX_RENDERER_TYPE_DIRECT3D12.value, 3)
        self.assertEqual(bgfx.BGFX_RENDERER_TYPE_GNM.value, 4)
        self.assertEqual(bgfx.BGFX_RENDERER_TYPE_METAL.value, 5)
        self.assertEqual(bgfx.BGFX_RENDERER_TYPE_OPENGLES.value, 6)
        self.assertEqual(bgfx.BGFX_RENDERER_TYPE_OPENGL.value, 7)
        self.assertEqual(bgfx.BGFX_RENDERER_TYPE_VULKAN.value, 8)
        self.assertEqual(bgfx.BGFX_RENDERER_TYPE_COUNT.value, 9)


if __name__ == '__main__':
    unittest.main()
