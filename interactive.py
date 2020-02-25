from game import run_agent, Game


@run_agent()
def interactive(game: Game):
    length = game.length
    colors = ''.join(sorted(game.colors))

    print('length = {!r}\ncolors = {!r}'.format(length, colors))

    while True:
        guess = input('> ')

        right, wrong = game.check(guess)  # inform your next guess with these
        # right: red pegs. Right color, right position.
        # wrong: white pegs. Right color, wrong position

        print('{} red, {} white'.format(right, wrong))

        if right == length:
            return guess