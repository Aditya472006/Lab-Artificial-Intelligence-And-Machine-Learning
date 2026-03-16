# Simple 8 Puzzle representation

def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Initial and Goal states
initial_state = [1,2,3,
                 4,0,6,
                 7,5,8]

goal_state = [1,2,3,
              4,5,6,
              7,8,0]

print("Initial State:")
display(initial_state)

print("Goal State:")
display(goal_state)
