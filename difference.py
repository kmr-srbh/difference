class Difference:
    """
    Find the difference between two strings.

    Attributes
    ----------
    original : str
        The version of string before change(s).
    new : str
        The version of string after change(s).
    ORIGINAL_STRING_LENGTH (int) : Length of `original`.
    NEW_STRING_LENGTH (int) : Length of `new`.

    Methods
    -------
    get_lcs_table()
        Calculates and returns the longest common subsequence matrix for
        `original` and `new`.
    get_lcs_length()
        Returns the length of the longest common subsequence between
        `original` and `new`.
    get_lcs()
        Calculates and returns the longest common subsequence between
        `original` and `new`.
    """

    def __init__(self, original: str, new: str) -> None:
        """Creates a new `Difference` object.

        Parameters
        ----------
        original : str
            The version of string before change(s).
        new : str
            The version of string after change(s).
        """
        self.original = original
        self.new = new
        self.ORIGINAL_STRING_LENGTH = len(self.original)
        self.NEW_STRING_LENGTH = len(self.new)

    def get_lcs_table(self) -> list[list[int]]:
        """Returns the Longest Common Subsequence (LCS) matrix of
        dimension ORIGINAL_STRING_LENGTH x NEW_STRING_LENGTH where
        `ORIGINAL_STRING_LENGTH` is the length of `original` and
        `NEW_STRING_LENGTH` of `new`.

        Returns
        -------
        lcs_matrix : list[list[int]]
            LCS matrix of dimension ORIGINAL_STRING_LENGTH x NEW_STRING_LENGTH.

        Notes
        -----
        Read more: https://en.wikipedia.org/wiki/Longest_common_subsequence
        """
        lcs_matrix = [
            [0 for _ in range(self.NEW_STRING_LENGTH + 1)]
            for _ in range(self.ORIGINAL_STRING_LENGTH + 1)
        ]
        for row in range(1, self.ORIGINAL_STRING_LENGTH + 1):
            for column in range(1, self.NEW_STRING_LENGTH + 1):
                if self.original[row - 1] == self.new[column - 1]:
                    lcs_matrix[row][column] = lcs_matrix[row - 1][column - 1] + 1
                else:
                    lcs_matrix[row][column] = max(
                        lcs_matrix[row][column - 1], lcs_matrix[row - 1][column]
                    )
        return lcs_matrix

    def get_lcs_length(self) -> int:
        """Returns the length of the longest common subsequence between
        `original` and `new`.

        Returns
        -------
        int
            Length of longest common subsequence between `original` and `new`.
        """
        return self.get_lcs_table()[-1][-1]

    def get_lcs(self) -> str:
        """Returns the longest common subsequence between `original` and `new`.

        Returns
        -------
        str
            The longest common subsequence between `original` and `new`.
        """
        lcs_matrix = self.get_lcs_table()
        row = self.ORIGINAL_STRING_LENGTH
        column = self.NEW_STRING_LENGTH

        lcs = str()

        while row > 0 and column > 0:
            if self.original[row - 1] == self.new[column - 1]:
                lcs = self.original[row - 1] + lcs
                row -= 1
                column -= 1
            elif lcs_matrix[row][column - 1] >= lcs_matrix[row - 1][column]:
                column -= 1
            else:
                row -= 1

        return lcs

    def get_difference(self):
        """Returns the difference between `original` and `new`.

        Returns
        -------
        str
            The difference between `original` and `new`.
        """
        lcs_matrix = self.get_lcs_table()
        row = self.ORIGINAL_STRING_LENGTH
        column = self.NEW_STRING_LENGTH

        difference = str()

        while row > 0 and column > 0:
            if self.original[row - 1] == self.new[column - 1]:
                difference = f"{self.original[row - 1]}" + difference
                row -= 1
                column -= 1
            elif lcs_matrix[row][column - 1] >= lcs_matrix[row - 1][column]:
                column -= 1
                difference = f" +{self.new[column]} " + difference
            else:
                row -= 1
                difference = f" -{self.original[row]} " + difference

        return difference


if __name__ == "__main__":
    difference_object = Difference("", "")
    print("LCS:", difference_object.get_lcs())
    print("Length:", difference_object.get_lcs_length())
    lcs_matrix = difference_object.get_lcs_table()
    print("LCS Matrix:")
    for r in lcs_matrix:
        print(r)
    print("Difference:", difference_object.get_difference())
