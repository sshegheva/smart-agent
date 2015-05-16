from Agent import Agent
from ProblemSet import ProblemSet
import logging
import problem_utils

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


agent = Agent()
n_correct = 0
n_total = len(ProblemSet("Basic Problems B").problems)

for p in ProblemSet("Basic Problems B").problems:
    LOGGER.info('=================================')
    LOGGER.info('Solving problem {}'.format(p.name))
    if problem_utils.is_problem2x2(p):
        source = p.figures['A']
        destination = p.figures['B']
        guess = agent.Solve(p)
        answer = p.checkAnswer(guess)
        if guess == answer:
            LOGGER.info('{}++++++++++++Correct+++++++++++++'.format(p.name))
            n_correct += 1
        else:
            LOGGER.error('Wrong')
    else:
        print 'Not 2x2 problem'

print('Total correct answers {} out of {}'.format(n_correct, n_total))
