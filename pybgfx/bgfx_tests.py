import bgfx
import unittest

class TestImport(unittest.TestCase):

    def test_module(self):
        self.assertEqual(bgfx.__author__, 'Jason Nadro')
        self.assertEqual(bgfx.__license__, 'BSD 2-clause')
        self.assertEqual(bgfx.__status__, 'Development')

if __name__ == '__main__':
    unittest.main()
    