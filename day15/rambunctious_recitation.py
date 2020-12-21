from os.path import dirname, realpath
from typing import List
from collections import defaultdict, deque
from progress.bar import IncrementalBar


def play(game_input : List[int], turn_limit=0) -> int:
    turn = 1
    memory = defaultdict(lambda: deque(maxlen=2))
    prev = None
    while turn <= turn_limit:
        if turn < len(game_input) + 1:
            number = game_input[turn - 1]
        elif len(memory[prev]) == 1:
            number = 0
        else:
            number = memory[prev][0] - memory[prev][1]

        yield number

        memory[number].appendleft(turn)
        prev = number
        turn += 1


if __name__ == "__main__":
    game_input = [12,20,0,6,1,17,7]
    for number in play(game_input, turn_limit=2020):
        pass
    print(number)

    turns = 30_000_000
    bar = IncrementalBar('playing', max=turns)
    for number in play(game_input, turn_limit=turns):
        bar.next()
    bar.finish()
    print(number)

