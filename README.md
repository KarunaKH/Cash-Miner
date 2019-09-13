# CASH-MINER
Cash Miner is a Flash Game in which you control a virtual figure to move in a grid map and finally reach cells containing cash rewards! 

# Goal:
CRACK THE GAME and Find the optimal control sequence to get the maximum expected rewards.

# Game Description:
- The virtual figure moves in a grid size of N* N.
- There are cells which contain cash rewards.
- In addition, there maybe some cells containing walls with negative rewards.
- All the other grids are empty. A typical grid is shown below:
![Capture](https://user-images.githubusercontent.com/54697582/64828231-62195880-d57c-11e9-92c8-2954384519ed.JPG)

# Valid Move:
- At each non-reward state, the virtual figure has 4 valid moves!\
U: Move UP\
D: Move DOWN\
L: Move LEFT\
R: Move RIGHT
- At reward/terminal state, the virtual figure has only 1 valid move.\
E: EXIT with reward
- At the wall state, the virtual figure has no actions.\
N: NO ACTION in the wall state.

# Rules:
- The environment in this game is stochastic because sometimes wind may blow the virtual figure away from its intended direction, so there a chance "P" for the virtual figure to reach its intended direction.
- The virtual figure may end up off course either 45 degrees clockwise or counter-clockwise with a probability of (1-P)/2:

![1](https://user-images.githubusercontent.com/54697582/64828260-73626500-d57c-11e9-8d5e-1f521ce53cfe.JPG)



- If the result of an action would move the virtual figure out of the grid, the virtual figure stays in its original cell:

![2](https://user-images.githubusercontent.com/54697582/64828273-807f5400-d57c-11e9-81f5-e88c82e93f40.JPG)



- If the result of an action would move the virtual figure into a wall cell, the virtual figure also stays in its original cell. Because there is a probability (1-P)/2 that the wind blows the figure into that wall, there is a (1-P)/2 probability that the figure ends up back in the current position:

![3](https://user-images.githubusercontent.com/54697582/64828276-8a08bc00-d57c-11e9-8f10-7e5f2212dbb6.JPG)



- On every turn, the virtual figure receives a reward R.
- You want to receive your money as soon as possible, so money received on your next turn is not always worth as much as money received right now, by a discount factor of 𝛾.


# Input:
- N: Grid Size.
- M: Wall States Number.
- Wall States positions: M lines with the coordinates of wall cells.
- T: Terminal State Number.
- Terminal States position: T lines indicating the coordinates of Terminal cells .
- P: Transition Model, which is the probability of moving as intended.
- Rp: Rewards!
- 𝛾: Discount Factor in the interval [0,1].

# Output: OPTIMAL ACTION GRID
An N* N grid indicating optimal action in each square.

# Logic:
1. Create two N* N grids; one to calculate probabilities(initialized to very small value(-9999)) and the other to record the best move as we go along.
2. Update the Walls and Terminal States with their rewards and actions!
3. While(there still some changes made as compared to previous iterations *AND* these changes are not small); keep going.
4. For each square in the grid, Calculate the ultility for each move.
5. Calculate the move with highest utility!
6. Update the move!

# Conclusion:
THATS IT! This is all required from this problem! All you have to do is calculate which move will bring you closer to getting a higher reward.\
The main challenge is how you calculate that utility for each move and for each square and when to stop computing?\
You can create HashSet to keep record of the possible cells to reach when you are on a particular position *OR* you can pre-calculate the utilities for each move in each cell so when you have to find the best move, you update your utility with reward and just find the max!

The more pre-processing you do, the lesser time you waste inside the nested loop, the faster your code is.\
You have Endless ways to really optimise the code here!\
LET YOUR IMAGINATION RUN WILD!

The paricular solution posted in this repository achieves an optimal solution for 100* 100 under **3 seconds!*

