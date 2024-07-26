import random

class GuessNum:
    def main(self):
        play_again = True
        while play_again:
            play_again = self.runGame()

    def runGame(self):
        winning_number = random.randint(0,100)
        guess = input("Enter your guess for the winning number.")
        users_num = int(guess)
        guess_limit = 4
        while users_num != winning_number and guess_limit > 0:
            if users_num > winning_number:
                guess_limit -= 1
                print("Your guess was too high")
                guess = input("Try again.")
                users_num = int(guess)

            elif users_num < winning_number:
                guess_limit -= 1
                print("Your guess was too low")
                guess = input("Try again.")
                users_num = int(guess)
        if guess_limit <= 0:
            print(f"You are out of guesses! The number was {winning_number}")
            ques = input("Would you like to play again? y/n")
            return ques.lower() == 'y'
        else:
            print(f"You guessed correctly, {winning_number} was right!")
            ques = input("Would you like to play again? y/n")
            return ques.lower() == 'y'
            

if __name__ == '__main__':
    guesser = GuessNum()
    guesser.main()



