class Difference:
    def __init__(self) -> None:
        pass

    def get_difference(self, original: str, new: str) -> list[str]:
        pass

    def get_lcs_matrix(self, original: str, new: str) -> list[list[int]]:
        """Returns the Longest Common Subsequence (LCS) matrix of
        dimension M x N for two strings of length N and M respectively.

        Read more: https://en.wikipedia.org/wiki/Longest_common_subsequence
        Explanation: https://www.youtube.com/watch?v=NnD96abizww

        :param M: Length of first string
        :param N: Length of second string

        :return: LCS Matrix of dimension M x N
        """
        M = len(original) + 1
        N = len(new) + 1
        lcs_matrix = [[1 for _ in range(N)] for _ in range(M)]
        for row in range(M):
            for column in range(N):
                lcs_matrix[row][0] = 0
                lcs_matrix[0][column] = 0
                if original[row - 1] == new[column - 1]:
                    lcs_matrix[row][column] = lcs_matrix[row - 1][column - 1] + 1
                else:
                    lcs_matrix[row][column] = max(
                        lcs_matrix[row][column - 1], lcs_matrix[row - 1][column]
                    )
        return lcs_matrix


if __name__ == "__main__":
    difference_object = Difference()
    matrix = difference_object.get_lcs_matrix("GAC", "AGCAT")
    for row in matrix:
        print(row)
