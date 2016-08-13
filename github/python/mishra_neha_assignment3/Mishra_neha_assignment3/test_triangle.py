import unittest
from Mishra_neha_lab_3.Triangle import Triangle

__author__ = 'ebraude'


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.triangle0 = Triangle([1, 2, 3], [20, 30])
        print("In TestTriangulatedFigure.setUp():" + self.triangle0.to_string())
        self.triangle1 = Triangle([2, 1, 77], [130, 20])
        print("In TestTriangulatedFigure.setUp():" + self.triangle1.to_string())

    '''
    def test_get_angles(self):
        self.assertTrue(20 in self.triangle0.get_angles())
        self.assertTrue(30 in self.triangle1.get_angles())

    def test_get_third_angle(self):
        self.assertEqual(130, self.triangle0.third_angle())
        self.assertEqual(30, self.triangle1.third_angle())

'''
def test_has_point(self):
        self.assertTrue(self.triangle0.has_point(1))
        self.assertTrue(self.triangle0.has_point(3))
        self.assertFalse(self.triangle0.has_point(4))
        self.assertTrue(self.triangle1.has_point(77))
'''
    def test_preceding_and_next_point(self):
        self.assertEqual(3, self.triangle0.point_following(2))
        self.assertEqual(1, self.triangle0.point_following(3))
        self.assertEqual(1, self.triangle1.point_preceding(77))
'''