class Challenge3:
    """
    A class to encapsulate the solution for Challenge 3.
    """

    def __init__(self, coord: str):
        """
        Initialize the challenge with input data.
        :param data: Any input data needed for the challenge.
        """
        self.coord = coord

    def get_row_col(self) -> tuple[int, int]:
        """
        Implement the main logic for the challenge.

        :return: The result of the computation.
        """
        # TODO: Implement the solution logic here
        row = int(self.coord[1]) - 1
        col = ord(self.coord[0].upper()) - ord('A')
        return (row, col)
    
if __name__ == "__main__":
    challenge = Challenge3("B7")
    result = challenge.get_row_col()
    print(f"Row: {result[0]}, Column: {result[1]}")