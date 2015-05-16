from Agent import Agent
from ProblemSet import ProblemSet
import solver_utils

agent = Agent()
n_correct = 0
n_total = len(ProblemSet("Basic Problems B").problems)

for p in ProblemSet("Basic Problems B").problems:
    print 'Solving problem', p.name
    if solver_utils.is_problem2x2(p):
        source = p.figures['A']
        destination = p.figures['B']
        solver_utils.score_pair(source, destination)
        guess = agent.Solve(p)
        answer = p.checkAnswer(guess)
        if guess == answer:
            print 'correct'
            n_correct += 1
        else:
            print 'incorrect'
    else:
        print 'Not 2x2 problem'

print 'Total correct answers out of ', n_correct, n_total
