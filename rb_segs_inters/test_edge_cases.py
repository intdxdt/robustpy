import unittest

from inter import rbSegIntersection


class TestTestVertLines(unittest.TestCase):
    def test_det(self):
      red  = [[ [ 224, 328 ], [ 224, 331 ] ] ]
      blue = [[ [ 224, 146 ], [ 224, 330] ] ]
      def visit (r, b):
          self.assertTrue(True)
      rbSegIntersection(red, blue, visit=visit)


suite = unittest.TestLoader().loadTestsFromTestCase(TestTestVertLines)
unittest.TextTestRunner(verbosity=4).run(suite)