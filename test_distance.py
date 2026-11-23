import json
from pathlib import Path
import unittest
from distance import edit_distance


class DistanceTests(unittest.TestCase):
    def test_invalid_types(self):
        class Subclass(str):
            pass
        for bad in [None, 1, True, [], {}, b"abc", Subclass("abc")]:
            for pair in [(bad,""),("",bad)]:
                with self.subTest(pair=pair), self.assertRaises(ValueError):
                    edit_distance(*pair)

    def test_length_validation(self):
        for pair in [("a"*257,""),("","a"*257),("a"*257,"a"*257)]:
            with self.subTest(pair=pair), self.assertRaises(ValueError):
                edit_distance(*pair)

    def test_limit_256(self):
        self.assertEqual(edit_distance("a"*256,"b"*256),256)
        self.assertEqual(edit_distance("a"*256,""),256)

    def test_long_shift(self):
        self.assertEqual(edit_distance("ab"*128,"ba"*128),2)

    def test_independent_calls(self):
        self.assertEqual(edit_distance("ab","ba"),2)
        self.assertEqual(edit_distance("",""),0)
        self.assertEqual(edit_distance("deply","deploy"),1)

    def test_symmetry_identity_and_bounds(self):
        values=["","a","ab","ba","abc","aac","猫😀","e\u0301"]
        for a in values:
            self.assertEqual(edit_distance(a,a),0)
            for b in values:
                value=edit_distance(a,b)
                self.assertIs(type(value),int)
                self.assertEqual(value,edit_distance(b,a))
                self.assertLessEqual(abs(len(a)-len(b)),value)
                self.assertLessEqual(value,max(len(a),len(b)))

    def test_triangle_inequality(self):
        values=["","ab","ba","cab","abc"]
        for a in values:
            for b in values:
                for c in values:
                    self.assertLessEqual(edit_distance(a,c),edit_distance(a,b)+edit_distance(b,c))


def make_test(left,right,expected):
    def test(self):
        result=edit_distance(left,right)
        self.assertIs(type(result),int)
        self.assertEqual(result,expected)
    return test

for name,left,right,expected in json.loads(Path(__file__).with_name("cases.json").read_text()):
    setattr(DistanceTests,"test_"+name,make_test(left,right,expected))

if __name__=="__main__": unittest.main()
