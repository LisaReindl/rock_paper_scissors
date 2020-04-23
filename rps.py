import random


moves = ['rock', 'paper', 'scissors']


class Player():

    def __init__(self):
        self.score = 0

    def move(self):
        return moves[0]

    def learn(self, learn_move):
        pass


class RandomPlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.learn_move = None

    def move(self):
        if self.learn_move is None:
            throw = moves[0]
        else:
            throw = self.learn_move
            return (throw)

    def learn(self, learn_move):
        self.learn_move = learn_move


class HumanPlayer(Player):

    def move(self):
        throw = input('CHOOSE A MOVE: rock, paper, scissors!\n')
        while throw != 'rock'and throw != 'paper'and throw != 'scissors':
            print('Sorry wrong input, try again!')
            throw = input('CHOOSE A MOVE: rock, paper, scissors!')
        return (throw)


class ReflectPlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.learn_move = None

    def move(self):
        if self.learn_move is None:
            thrown = moves[0]
        else:
            throw = self.learn_move
            return (throw)

    def learn(self, learn_move):
        self.learn_move = learn_move


class Cycles(Player):

    def __init__(self):
        Player.__init__(self)
        self.step = 0

    def move(self):
        throw = None
        if self.step == 0:
            throw = moves[0]
            self.step = self.step + 1
        elif self.step == 1:
            trhow = moves[1]
            self.step = self.step + 1
        else:
            throw = moves[2]
            self.step = self.step + 1
        return throw


class Game:

    def __init__(self, p2):
        self.p1 = HumanPlayer()
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        result = Game.play(move1, move2)
        self.p1.learn(move2)
        self.p2.learn(move1)

    def play_game(self):
        print('\nGAME STARTS!\n')
        for round in range(3):
            print(f'Round {round}:')
            self.play_round()
        if self.p1.score > self.p2.score:
            print('*** YOU WON! ***\n')
        elif self.p1.score < self.p2.score1:
            print('*** YOU LOST! ***\n')
        else:
            print('*** IT IS A TIE! ***\n')
        print('The final score ' + str(self.p1.score) + ' TO '
              + str(self.p2.score))

    def play_single(self):
        print('\nGAME STARTS!\n')
        print(f'Round 1 out of 1:\n')
        self.play_round()
        if self.p1.score > self.p2.score:
            print('*** YOU WON! ***\n')
        elif self.p1.score < self.p2.score:
            print('*** YOU LOST! ***\n')
        else:
            print('*** IT IS A TIE! ***\n')
        print('The final score: Player 1 ' +
              str(self.p1.score) + ' Player 2 ' +
              str(self.p2.score))

    def play(self, move1, move2):
        print(f'You played {move1}!\n')
        print(f'Opponent played {move2}!\n')
        if beats(move1, move2):
            print('*** YOU WON! ***\n')
            print(f'SCORE: Player 1 {move1} | Player 2 {move2}\n\n')
            self.p1.score += 1
            return 1
        elif beats(move2, move1):
            print('*** YOU LOST! ***\n')
            print(f'SCORE: Player 1 {move1} | Player 2 {move2}\n\n')
            self.p2.score += 1
            return 2
        else:
            print('*** IT IS A TIE! ***\n')
            print(f'SCORE: Player 1 {move1} | Player 2 {move2}\n\n')
            return 0


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


if __name__ == '__main__':
    answer = [Player(), RandomPlayer(), Cycles(), ReflectPlayer()]
    p2 = input('Select the type of game you would like to play?\n'
               'Hit [1] for choosing always rock, [2] for choosing random,'
               '[3] for the reflective mode or [4] for cycles mode!\n')
    while p2 != 1 or p2 != 2 or p2 != 3 or p2 != 4:
        p2 = random.choice(answer)
        break
    if p2 == '1':
        p2 = Player()
    elif p2 == '2':
        p2 = RandomPlayer()
    elif p2 == '3':
        p2 = Cycles()
    elif p2 == '4':
        p2 = ReflectPlayer()
    rounds = input('Enter [s] for a single game or [f] for a full game!\n')
    Game = Game(p2)
    while True:
        if rounds == 's':
            Game.play_single()
            break
        elif rounds == 'f':
            Game.play_game()
            break
        else:
            print('Sorry wrong input, try again!')
            rounds = input('Enter [s] for a single game or'
                           '[f] for a full game!\n')
