import unittest

from sys import path

path.append("../difference")
from difference import Difference

TEST_CASES = [
    {
        "original": "",
        "new": "",
        "lcs": "",
        "difference": "",
    },
    {
        "original": "wierd",
        "new": "weird",
        "lcs": "werd",
        "difference": "w-ie+ird",
    },
    {
        "original": "womans",
        "new": "women",
        "lcs": "womn",
        "difference": "wom-a+en-s",
    },
    {
        "original": "adress",
        "new": "address",
        "lcs": "adress",
        "difference": "a+ddress",
    },
    {
        "original": "beleive",
        "new": "believe",
        "lcs": "belive",
        "difference": "bel-ei+eve",
    },
    {
        "original": "recieve",
        "new": "receive",
        "lcs": "receve",
        "difference": "rec-ie+ive",
    },
    {
        "original": "dokument",
        "new": "document",
        "lcs": "doument",
        "difference": "do-k+cument",
    },
    {
        "original": "accomodate",
        "new": "accommodate",
        "lcs": "accomodate",
        "difference": "acco+mmodate",
    },
    {
        "original": "hello!",
        "new": "hello, world!",
        "lcs": "hello!",
        "difference": "hello+,+ +w+o+r+l+d!",
    },
]


class TestDifference(unittest.TestCase):
    def test_get_lcs(self):
        for test_case in TEST_CASES:
            self.assertEqual(
                Difference(test_case["original"], test_case["new"]).get_lcs(),
                test_case["lcs"],
            )

    def test_get_difference(self):
        for test_case in TEST_CASES:
            self.assertEqual(
                Difference(test_case["original"], test_case["new"]).get_difference(),
                test_case["difference"],
            )


if __name__ == "__main__":
    unittest.main()
