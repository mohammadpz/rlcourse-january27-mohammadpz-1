# McGill University Reinforcement Learning Course (Winter 2017)

This repo contains codes and slides for materials presented in RL course by Doina Precup and Pierre-Luc Bacon.

## Running code

mdp.py contains a simple code for *iterative policy evaluation* and *policy iteration* for the example of grid world example.

```
python mdp.py

  Value Function, iter:1
|-------|-------|-------|-------|
|   0.0 |  0.0  |  0.0  |  0.0  |
|-------|-------|-------|-------|
|   0.0 |  0.0  |  0.0  |  0.0  |
|-------|-------|-------|-------|
|   0.0 |  0.0  |  0.0  |  0.0  |
|-------|-------|-------|-------|
|   0.0 |  0.0  |  0.0  |  0.0  |
|-------|-------|-------|-------|

  Value Function, iter:2
|-------|-------|-------|-------|
|   0.0 |  -5.8 |  -4.8 |  -4.0 |
|-------|-------|-------|-------|
|  -6.7 |  -6.5 |  -4.3 |  -2.6 |
|-------|-------|-------|-------|
|  -6.8 |  -6.8 |  -2.9 |  -1.4 |
|-------|-------|-------|-------|
|  -7.7 |  -8.2 |  -6.1 |  0.0  |
|-------|-------|-------|-------|

  Value Function, iter:3
|-------|-------|-------|-------|
|   0.0 |  -1.5 |  -4.2 |  -3.5 |
|-------|-------|-------|-------|
|  -4.5 |  -3.9 |  -3.4 |  -2.5 |
|-------|-------|-------|-------|
|  -7.7 |  -3.3 |  -2.4 |  -1.3 |
|-------|-------|-------|-------|
|  -8.7 |  -2.5 |  -1.3 |  0.0  |
|-------|-------|-------|-------|

  Value Function, iter:4
|-------|-------|-------|-------|
|   0.0 |  -1.5 |  -2.6 |  -3.3 |
|-------|-------|-------|-------|
|  -4.1 |  -3.8 |  -3.3 |  -2.5 |
|-------|-------|-------|-------|
|  -4.0 |  -3.3 |  -2.4 |  -1.3 |
|-------|-------|-------|-------|
|  -3.5 |  -2.5 |  -1.3 |  0.0  |
|-------|-------|-------|-------|

  Value Function, iter:5
|-------|-------|-------|-------|
|   0.0 |  -1.5 |  -2.6 |  -3.3 |
|-------|-------|-------|-------|
|  -4.1 |  -3.7 |  -3.2 |  -2.5 |
|-------|-------|-------|-------|
|  -4.0 |  -3.3 |  -2.4 |  -1.3 |
|-------|-------|-------|-------|
|  -3.5 |  -2.5 |  -1.3 |  0.0  |
|-------|-------|-------|-------|

The Optimal Policy:
State 11 -- right --> State 12
State 10 -- right --> State 11
State 13 -- right --> State 14
State 12 -- down  --> State 16
State 15 -- right --> State 16
State 14 -- right --> State 15
State 04 -- down  --> State 08
State 16 -- NONE  --> State 16
State 03 -- left  --> State 02
State 08 -- down  --> State 12
State 09 -- right --> State 10
State 02 -- left  --> State 01
State 01 -- NONE  --> State 01
State 06 -- right --> State 07
State 05 -- right --> State 06
State 07 -- right --> State 08
```

### Convergence Rate

As the convergence rate is a function of the discount factor (Gamma), by changing the value of `gamma` in code, the speed of convergence varies. 

## Read the example of grid world from the following link

* [Link](https://webdocs.cs.ualberta.ca/~sutton/book/ebook/node41.html) - The Grid World example
