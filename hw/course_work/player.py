
class Player:
    def __init__(self, name, player_words = []):
        self.name = name
        self.player_words = player_words

    def __repr__(self):
        return f"Пользователь - {self.name}, угадано слов: {self.player_words}"

    def save_used_words(self, word):
        """
        сохраняет введеное слово
        :param word: пользовательский ответ
        :return:
        """
        self.player_words.append(word)

    def get_lenth_used_words(self):
        """
        :return: длину списка с пользовательскими правильными ответами
        """
        return len(self.player_words)

    def if_word_used(self, new_word):
        """
        проверяет было ли слово уже в списке
        :param new_word: введеное слово
        :return:
        """
        if new_word in self.player_words:
            print("Это слово уже использовалось")
            return False
        else:
            return True
