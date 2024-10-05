
class Word:
    """
    Represents a word with its meanings and associated weight.

    Attributes:
        name (str): The name of the word.
        meanings (list[str]): A list of meanings for the word.
        weight (int): The weight associated with the word, indicating its importance or frequency.
    """

    def __init__(self, name: str, meanings: list[str], weight: int):
        """
        Initializes the Word instance.

        :param name: The name of the word.
        :param meanings: A list of meanings for the word.
        :param weight: The weight associated with the word.
        """
        self.name = name
        self.meanings = meanings
        self.weight = weight
