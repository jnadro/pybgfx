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

class TestAPI(unittest.TestCase):

    def test_init(self):
        init = bgfx.bgfx_init_t()
        bgfx.init_ctor(ctypes.pointer(init))

        result = bgfx.init(ctypes.pointer(init))
        self.assertEqual(result, True)

        bgfx.shutdown()

    def test_get_supported_renderers(self):
        renderers = (bgfx.bgfx_renderer_type * bgfx.BGFX_RENDERER_TYPE_COUNT.value)(-1, -1, -1, -1, -1, -1, -1, -1, -1)
        num_renderers = bgfx.get_supported_renderers(bgfx.BGFX_RENDERER_TYPE_COUNT.value, ctypes.cast(renderers, ctypes.POINTER(bgfx.bgfx_renderer_type)))
        self.assertGreater(num_renderers, 0)
        self.assertLessEqual(num_renderers, bgfx.BGFX_RENDERER_TYPE_COUNT.value)

        for i in range(0, bgfx.BGFX_RENDERER_TYPE_COUNT.value):
            renderer_type = renderers[i]
            if i < num_renderers:
                self.assertGreaterEqual(renderer_type, 0)
                self.assertLess(renderer_type, bgfx.BGFX_RENDERER_TYPE_COUNT.value)
            else:
                self.assertEqual(renderer_type, -1)

    def test_get_renderer_name(self):
        self.assertEqual(bgfx.get_renderer_name(0), b'Noop')
        self.assertEqual(bgfx.get_renderer_name(1), b'Direct3D 9')
        self.assertEqual(bgfx.get_renderer_name(2), b'Direct3D 11')
        self.assertEqual(bgfx.get_renderer_name(3), b'Direct3D 12')
        self.assertEqual(bgfx.get_renderer_name(4), b'GNM')
        self.assertEqual(bgfx.get_renderer_name(5), b'Noop')
        self.assertEqual(bgfx.get_renderer_name(6), b'OpenGL 2.1')
        self.assertEqual(bgfx.get_renderer_name(7), b'OpenGL 2.1')
        self.assertEqual(bgfx.get_renderer_name(8), b'Vulkan')

    def test_get_renderer_type(self):
        renderer_type = bgfx.get_renderer_type()
        print(renderer_type)

if __name__ == '__main__':
    unittest.main()
