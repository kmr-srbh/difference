class Difference:
    def __init__(self, original: str, new: str) -> None:
        self.original = original
        self.new = new
        self.ORIGINAL_STRING_LENGTH = len(self.original)
        self.NEW_STRING_LENGTH = len(self.new)

    def get_lcs(self) -> str:
        """Returns the Longest Common Subsequence (LCS) between `original` and `new`.

        :return: Longest Common Subsequence (LCS) between `original` and `new`.
        """
        lcs_table = self.get_lcs_table()
        row = self.ORIGINAL_STRING_LENGTH
        column = self.NEW_STRING_LENGTH

        lcs = str()

        while row > 0 and column > 0:
            if self.original[row - 1] == self.new[column - 1]:
                lcs = self.original[row - 1] + lcs
                row -= 1
                column -= 1
            elif lcs_table[row][column - 1] > lcs_table[row - 1][column]:
                column -= 1
            else:
                row -= 1

        return lcs

    def get_length_of_lcs(self) -> int:
        """Returns the length of the Longest Common Subsequence (LCS) between
        `original` and `new`.

        :return: Length of Longest Common Subsequence (LCS) between `original` and `new`.
        """
        return self.get_lcs_table()[-1][-1]

    def get_lcs_table(self) -> list[list[int]]:
        """Returns the Longest Common Subsequence (LCS) table of
        dimension ORIGINAL_STRING_LENGTH x NEW_STRING_LENGTH where
        `ORIGINAL_STRING_LENGTH` is the length of `original` and
        `NEW_STRING_LENGTH` of `new`.

        Read more: https://en.wikipedia.org/wiki/Longest_common_subsequence
        Algorithm explanation: https://www.youtube.com/watch?v=NnD96abizww

        :param original: The version of string before the current version.
        :param new: The current version of the string.

        :return: LCS table of dimension ORIGINAL_STRING_LENGTH x NEW_STRING_LENGTH.
        """
        lcs_table = [
            [0 for _ in range(self.NEW_STRING_LENGTH + 1)]
            for _ in range(self.ORIGINAL_STRING_LENGTH + 1)
        ]
        for row in range(1, self.ORIGINAL_STRING_LENGTH + 1):
            for column in range(1, self.NEW_STRING_LENGTH + 1):
                if self.original[row - 1] == self.new[column - 1]:
                    lcs_table[row][column] = lcs_table[row - 1][column - 1] + 1
                else:
                    lcs_table[row][column] = max(
                        lcs_table[row][column - 1], lcs_table[row - 1][column]
                    )
        return lcs_table


if __name__ == "__main__":
    difference_object = Difference("AGCAT", "GAC")
    print("LCS:", difference_object.get_lcs())
    print("Length:", difference_object.get_length_of_lcs())
    lcs_table = difference_object.get_lcs_table()
    for r in lcs_table:
        print(r)
