class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return f'Слово - {self.word}, подслова - {self.subwords}'

    def get_length_subwords(self):
        """
        :return: длину сптска с подсловами
        """
        return len(self.subwords)

    def answer_check(self, user_atept):
        """
        проверяет слово по параметру длины и наличию в списке под слов
        :param user_atept: пользовательский ответ
        :return: bool
        """

        if len(user_atept) <= 2:
            print("Слишком короткое слово!")
            return False

        elif user_atept not in self.subwords:
            print("Такого слова нет!")
            return False

        else:
            return True



    def make_question(self):
        """
        :return: составленный вопрос
        """
        length = self.get_length_subwords()
        return f"Составьте {length} слов из слова {self.word} "
