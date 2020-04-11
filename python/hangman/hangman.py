STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = "_" * len(self.word)
        self.word2 = word

    def guess(self, char):
        if self.remaining_guesses==-1:
            raise ValueError('You are out of guesses')
        if self.get_status()=='win':
            raise ValueError('You already Won')
        result = self.word2.find(char)
        if result == -1:
            self.remaining_guesses -= 1
            self.result_check()
            return
        while(self.word2.find(char) != -1):
            result = self.word2.find(char)
            self.word2 = self.word2[0:result] + " " + self.word2[result + 1:]
            temp = self.masked_word[0:result] + char + self.masked_word[result + 1:]
            self.masked_word = temp
        self.result_check()
    
    def result_check(self):
        print(self.masked_word)
        if self.word == self.masked_word:
            self.status = STATUS_WIN
        if self.remaining_guesses == -1:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status