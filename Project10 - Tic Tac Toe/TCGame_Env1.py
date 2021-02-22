from gym import spaces
import numpy as np
import random
from itertools import groupby
from itertools import product



class TicTacToe():

    def __init__(self):
        """initialise the board"""
        
        # initialise state as an array
        self.state = [np.nan for _ in range(9)]  # initialises the board position, can initialise to an array or matrix
      
        # all possible numbers
        self.all_possible_numbers = [i for i in range(1, len(self.state) + 1)] # , can initialise to an array or matrix

        self.reset()


    def is_winning(self, curr_state):
        """Takes state as an input and returns whether any row, column or diagonal has winning sum
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan]
        Output = False"""
        rowWise = [[0,1,2],[3,4,5],[6,7,8]]
        columnWise = [[0,3,6],[1,4,7],[2,5,8]]
        diagonal = [[0,4,8],[2,4,6]]
        
        rowWiseSum = [np.sum(np.array(curr_state)[i]) for i in rowWise]
        columnWiseSum = [np.sum(np.array(curr_state)[i]) for i in columnWise]
        diagonalSum = [np.sum(np.array(curr_state)[i]) for i in diagonal]
        
        rowWin =  list(filter(lambda x : x == 15,rowWiseSum))
        columnWin =  list(filter(lambda x : x == 15,columnWiseSum))
        diagonalWin =  list(filter(lambda x : x == 15,diagonalSum))                
        if(len(rowWin) + len(columnWin) + len(diagonalWin) > 0):
            return True
        else:
            return False
        

    def is_terminal(self, curr_state):
        # Terminal state could be winning state or when the board is filled up

        if self.is_winning(curr_state) == True:
            return True, 'Win'

        elif len(self.allowed_positions(curr_state)) == 0:
            return True, 'Tie'

        else:
            return False, 'Resume'


    def allowed_positions(self, curr_state):
        """Takes state as an input and returns all indexes that are blank"""
        return [i for i, val in enumerate(curr_state) if np.isnan(val)]


    def allowed_values(self, curr_state):
        """Takes the current state as input and returns all possible (unused) values that can be placed on the board"""

        used_values = [val for val in curr_state if not np.isnan(val)]
        agent_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 !=0]
        env_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 ==0]

        return (agent_values, env_values)


    def action_space(self, curr_state):
        """Takes the current state as input and returns all possible actions, i.e, all combinations of allowed positions and allowed values"""

        agent_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[0])
        env_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[1])
        return (agent_actions, env_actions)



    def state_transition(self, curr_state, curr_action):
        """Takes current state and action and returns the board position just after agent's move.
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [7, 9] or [position, value]
        Output = [1, 2, 3, 4, nan, nan, nan, 9, nan]
        """
        new_state = [i for i in curr_state]
        new_state[curr_action[0]] = curr_action[1]
        return new_state

    def step(self, curr_state, curr_action):
        """Takes current state and action and returns the next state, reward and whether the state is terminal. Hint: First, check the board position after
        agent's move, whether the game is won/loss/tied. Then incorporate environment's move and again check the board status.
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [7, 9] or [position, value]
        Output = ([1, 2, 3, 4, nan, nan, nan, 9, nan], -1, False)"""
        
        new_state = self.state_transition(curr_state,curr_action)

        reachedTerminal,message = self.is_terminal(new_state)
        if reachedTerminal == True:
            if message == "Win":
                reward = 10
                game_message = "Agent Won !"
            else:
                reward = 0
                game_message = "Its  a tie !"
            
            return new_state,reward,reachedTerminal,game_message
        else:
            _,env_actions = self.action_space(new_state)
            env_action = random.choice([ac for i,ac in enumerate(env_actions)])

            newStateEnvActions = self.state_transition(new_state,env_action)

            reachedTerminal, message = self.is_terminal(newStateEnvActions)
            if reachedTerminal == True:
                if message == "Win":
                    reward = -10
                    game_message = "Environment Won !"
                else:
                    reward = 0
                    game_message = "Its  a tie !"
            else:
                reward = -1
                game_message = "Resume"
            return newStateEnvActions,reward,reachedTerminal,game_message


    def reset(self):
        return self.state
