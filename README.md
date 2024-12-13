Run with arguments: Population-Size Number-Of-Queens, or only Number-Of-Queens.

If you run with only Number-Of-Queens specified, population size will default to 200.

Very simple and unpolished implementation of genetic algorithm for solving the N-Queens problem for fun.
Represents each population member as N-length array of int 1-N.

Uses simple "number of conflicts" heuristic to assess fitness.

Very interesting to see how easily this can solve for N up to 10.
At 11, it starts to struggle. Experimenting with population sizes could probably help.
