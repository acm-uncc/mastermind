from game import run_agent, Game


@run_agent()
def one_pass(game: Game):
    colors = iter(game.colors)

    for color in colors:
        guess = [color] * game.length
        rr, rw = game.check(guess)
        if rr > 0:
            break

    need = set(colors)
    done = set()

    for i in range(game.length):
        temp = guess.copy()

        for color in need:
            temp[i] = color
            rr_, rw_ = game.check(temp)

            if rr_ + rw_ == rr:
                done.add(color)
                continue

            if rr_ > rr:
                guess[i] = color
                rr = rr_
                if rr == game.length:
                    return guess
                break

            if rw_ == 2:
                break

        need -= done
        done.clear()

    return guess