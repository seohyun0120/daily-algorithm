problem = input()

problem = problem.replace('XXXX', 'AAAA')
problem = problem.replace('XX', 'BB')

if 'X' in problem:
    print(-1)
else:
    print(problem)