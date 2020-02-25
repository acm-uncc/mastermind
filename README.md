# Mastermind AI

An agent-based Mastermind implementation. See [`interactive.py`](interactive.py) for an
 example of how to implement and run a user agent.

`@run_agent` accepts two optional keyword arguments: `colors` is a list or string of
 characters which are valid peg colors. The game will select `length` of these, with
 replacement, to be the code.

These default to `'abcdef'` and `4` respectively, to mimic the original game of 4 pegs
 and 6 possible colors.

You may use multiple `@run_agent` decorators to test the same agent on multiple
 scenarios. For example

    @run_agent()
    @run_agent(colors='xy', length=10)
    @run_agent(colors='0123456789', length=5)
    def my_agent(game):
        ...

Might produce:

    Results for one_pass:
      answer: '69505'
         key: '69505'
      correct.
      5 chars, 10 choices
      13 attempts.
    
    Results for one_pass:
      answer: 'xyxyxyyyyy'
         key: 'xyxyxyyyyy'
      correct.
      10 chars, 2 choices
      6 attempts.
    
    Results for one_pass:
      answer: 'fccf'
         key: 'fccf'
      correct.
      4 chars, 6 choices
      7 attempts.
