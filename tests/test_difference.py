import unittest

from sys import path

path.append("../difference")
from difference import Difference


class TestDifference(unittest.TestCase):
    def test_get_longest_common_subsequence(self):
        self.assertEqual(Difference("", "").get_lcs(), "")
        self.assertEqual(Difference("ABC", "XYZ").get_lcs(), "")
        self.assertEqual(Difference("ABCD", "AC").get_lcs(), "AC")
        self.assertEqual(Difference("AGCAT", "GAC").get_lcs(), "GA")
        self.assertEqual(Difference("AABCXY", "XYZ").get_lcs(), "XY")
        self.assertEqual(Difference("ABCDEF", "ABCDEF").get_lcs(), "ABCDEF")
        self.assertEqual(Difference("XMJYAUZ", "MZJAWXU").get_lcs(), "MJAU")
        self.assertEqual(Difference("ABCDEFGHIJ", "ECDGI").get_lcs(), "CDGI")


if __name__ == "__main__":
    unittest.main()
