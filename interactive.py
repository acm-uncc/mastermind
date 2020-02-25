from game import run_agent, Game


@run_agent()
def interactive(game: Game):
    length = game.length
    colors = ''.join(sorted(game.colors))

    print('length = {!r}\ncolors = {!r}'.format(length, colors))

    while True:
        guess = input('> ')

        right, wrong = game.check(guess)
        print('{} red, {} white'.format(right, wrong))

        if right == length:
            return guess