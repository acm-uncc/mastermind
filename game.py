import operator as op
import random
from collections import Counter


class Game:
    def __init__(self, colors=None, length=None):
        self.length = length or 4
        self.colors = set(colors or 'abcdef')

        self.__key = random.choices(list(self.colors), k=self.length)

        self.__key_count = Counter(self.__key)

        self.attempts = 0

    def check(self, guess):
        assert (c in self.colors for c in guess), \
            'Invalid color. Must be in {!r}'.format(''.join(self.colors))

        assert len(guess) == len(self.__key), \
            'Invalid length. Must be {!r}'.format(self.length)

        count = Counter(guess)

        right = sum(map(op.eq, guess, self.__key))
        both = sum(min(count[c], self.__key_count[c]) for c in self.__key_count.keys())
        wrong = both - right

        self.attempts += 1
        return right, wrong

    def summarize(self, agent, answer):
        agent = agent.__name__

        answer = ''.join(answer)
        key = ''.join(self.__key)

        status = 'correct' if key == answer else 'incorrect'

        length = self.length
        choices = len(self.colors)

        attempts = self.attempts

        fmt = 'Results for {}:\n' \
              '  answer: {!r}\n' \
              '     key: {!r}\n' \
              '  {}.\n' \
              '  {!r} chars, {!r} choices\n' \
              '  {} attempts.\n'

        return fmt.format(agent, answer, key, status, length, choices, attempts)


def run_agent(agent=None, colors=None, length=None):
    def decorate(_agent):
        game = Game(colors=colors, length=length)

        answer = _agent(game)
        print(game.summarize(_agent, answer))

        return _agent

    return decorate(agent) if agent else decorate


