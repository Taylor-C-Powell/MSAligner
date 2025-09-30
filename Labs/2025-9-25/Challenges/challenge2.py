class Challenge2:
    """
    A class to encapsulate the solution for Challenge 2.
    """

    def __init__(self, data: str):
        """
        Initialize the challenge with input data.
        :param data: Any input data needed for the challenge.
        """
        self.data = data

    def count(self) -> int:
        """
        Implement the main logic for the challenge.

        :return: The result of the computation.
        """
        # TODO: Implement the solution logic here
        return self.data.count('_') + 1
    
if __name__ == "__main__":
    # Example usage
    challenge = Challenge2(">NODE_1_length_142_cov_30.24_cutoff_0")
    result = challenge.count()
    print(f"Result: {result}")