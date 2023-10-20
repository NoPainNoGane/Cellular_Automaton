# Simulation of complex systems using cellular automata

## Task 1. Cellular automaton "Life"
Perform a software implementation of a cellular automaton functioning in accordance with the following rules:
1) the cell can be in two states - passive and active;
2) eight neighboring cells are considered as a neighborhood;
3) if there are two active cells in the vicinity of a passive cell, then this cell also becomes active ("born");
4) if there are three or more active cells in the vicinity of an active cell, then
it becomes passive ("dies").
Implement the algorithm on a cellular space of 32x32 cells. The initial distribution of active and passive cells is random, obeying a uniform distribution law. Also, select the initial distributions corresponding to stationary and cyclic structures (three examples of each structure).

The results of the program are shown below. Passive cells are marked in white, and active cells are marked in black.

Initial distribution:  

![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/1feb30d6-eb8f-49ec-b5a3-9a0b24c2573a)

Last iteration  

![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/c2252cbb-8ee9-42ed-a50d-f1fd9f78e145)

Consider the initial distributions corresponding to stationary and cyclic structures.  

Stationary structures  

![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/7e081f57-c637-4fab-aa84-d27a4cb815eb)

Example of cyclic structure No. 1  

![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/05a84379-2c30-49de-97ac-8ec7e4977e0d)

Example of cyclic structure No. 2  

![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/00d9e117-2cbf-4ca8-afcd-47d0ab70e85a)

Example of cyclic structure No. 3  

![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/acbd1563-a492-4bd6-973a-4106a2fc0af2)


## Task 2. Cellular automaton "Neural network"
This automaton simulates phenomena in a homogeneous two-dimensional neural network consisting of excitable elements, and functions according to the following rules:
1) the cell can be in three states: dormant, active and recovery state;
2) eight neighboring cells are considered as a neighborhood;
3) the transition to the state of activity depends on some parameter called the activator level. In the excited state of the cell, the activator level is 1. In other states, it decays by A % per clock cycle;
4) if the cell was at rest and the total amount of activator in eight neighboring cells and in this cell exceeded the activation threshold P, then the cell is excited for T cycles;
5) after T cycles, the excited cell goes into a recovery state for B cycles, and then goes into a rest state.
Implement the algorithm with the following parameters: cell space of 256x256 cells, A = 30%, N = 3, T = 5, B = 8. The initial distribution of the state of cells is given by a flat front. There is also a periodic source of excitation (3x3 cells) with a period of 15 cycles. To reveal the nature of the interaction between different excitation fronts.

The cell can be in three states: dormant – white, active – yellow and recovery state – black. The initial distribution of the state of cells is given by a flat front in the form of a straight line. Below are the results of the program.

Initial distribution:  

![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/3bc19802-3474-4b51-a70f-95f71d091145)

The moment before the collision  

![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/ade2a2dd-ecab-4a08-8fa9-7b22f7c83b27)

The moment of merging  

![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/68069b03-0a9d-46ad-a3fe-052cd5372f16)

Continuation of the movement  

![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/35ca689d-ecf0-4c4c-af63-157485772e86)
![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/d587209a-5728-4431-a0d2-771ba711eb43)
![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/65b6fb11-6ea0-486d-8f34-8cd849fc2f2a)

During the operation of the cellular automaton, circular waves are observed, which are created by a periodic source of excitation. A flat front collides with itself during a collision and is extinguished due to active particles.


## Task 3. Cellular automaton "Organisms - nutrient medium"
The cellular automaton simulates the interaction of unicellular organisms with the nutrient medium and functions according to the following rules:
1) the cell space forms a field of N x N cells
2) the neighborhood of a cell consists of eight neighboring cells;
3) each cell corresponds to the P value of the nutrient content of the solution (energy intensity), which can vary from 0 to Pmax
4) the delta P increase in the nutritional value (energy intensity) of the cell solution over a time cycle is performed as follows: delta P = 0 at P = Pmax and delta P = r at P < Pmax, where r is the rate of nutritional gain
5) the total energy reserve of the nutrient solution is determined by the total nutritional value (energy) of all cells and cannot be more than ```math N^2 Pmax```;
6) a cell may be free or contain no more than one unicellular or other living organism;
7) a single-celled individual draws energy from the nutrient solution of the cell in which it is located, reducing its nutritional value and increasing its energy reserve by delta p per tact
8) the maximum possible amount of energy stored by a unicellular does not exceed p1
9) an individual spends delta e of energy per clock cycle for his needs
10) the individual always tries to move to the next free cell, choosing the direction of transition randomly;
11) the lifetime of an individual is L cycles
12) if the lifetime of an individual has exceeded the life span for these organisms or the energy reserve has decreased to zero, then the individual dies;
13) starting from the age of T cycles, an individual is considered mature and can produce its own kind, spending delta r energy with each division additionally. In this case, the old individual moves to a free neighboring cell, and the new one remains in the old one. If there are no free cells in the neighborhood, then division does not occur;
14) the initial distribution of individuals in the cellular space is subject to a uniform distribution law. The initial number of individuals is A% of the maximum possible, equal to ```math N^2 ```.

Initial distribution  

![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/e8c61082-84e0-49c2-bced-2e5d617b0959)

Iteration No. 10  

![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/619228bb-5743-47a9-95d2-664b0f699ecb)

Iteration No. 20  

![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/ba223990-4b3b-429e-9078-7b511badb1f6)

Iteration No. 35  

![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/b0ca475d-e863-484e-aa5b-e9597d1ab735)

Iteration No. 50  

![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/99165194-2b81-4afb-999e-668836ee29d0)

In connection with the achievement of adulthood, an increase in living cells occurs (No. 10), then, due to the achievement of life expectancy, the number decreases and the process of enriching the nutrient medium begins. At No. 50, the medium comes to an equilibrium position. This process has the property of periodicity.



## Task 5. Modified cellular automaton "Organisms - nutrient medium"
Perform a modification of the algorithm from task 3, replacing rule 10 with the following: an individual always tries to move to the neighboring free cell with the highest level of energy intensity. If the cells in the neighborhood have a smaller energy reserve, then the individual remains in the same cell.

Initial distribution of the modified cellular automaton "Organisms – nutrient medium"  

![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/08ae260e-06c5-4a52-a222-c8d5ce0c2f4e)

The established movement of the modified cellular automaton "Organisms – nutrient medium"  

![image](https://github.com/NoPainNoGane/Cellular_Automaton/assets/64308897/53915287-31c2-474d-b218-f3e893daaf4a)

According to the figures above, it can be concluded that the distribution of individuals in the modified algorithm is more uniform than in the first case. This is due to the fact that in the modified algorithm, an individual always tries to move to the neighboring free cell with the highest level of energy intensity, creating a uniform filling of the cell space. In this case, there is also an increase in the number of living cells due to reaching adulthood and a decrease due to reaching the maximum life expectancy. As a result of optimal use of nutrient medium resources, organisms are more viable in the modified algorithm.



