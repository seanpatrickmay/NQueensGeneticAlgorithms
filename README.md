# N-Queens Genetic Algorithm

> A **lean**, **tournament-driven** evolutionary solver that hunts for conflict-free N-Queens layouts with explainable heuristics and no external dependencies.

## Overview
This project explores the N-Queens puzzle through a compact genetic algorithm. Each chromosome encodes a chessboard column-to-row mapping, while a collision-based fitness function guides the population toward valid, non-conflicting boards. The implementation favors transparency over black-box complexity, making it a useful reference for evolutionary search patterns on combinatorial problems.

## Features
- Tournament selection and single-point crossover drive the evolutionary search toward viable boards.
- Mutation probability scales automatically with board size, balancing exploration and convergence.
- Minimal, well-documented code structure with environment-driven configuration for quick experimentation.

## Quickstart
```bash
# Setup
python3 -m venv .venv
source .venv/bin/activate

# Run
python GeneticAlgorithm.py 200 8     # population size 200, board size 8x8
python GeneticAlgorithm.py 12        # defaults population to 200, board size 12x12
```

## Configuration
This project uses environment variables for flexibility and portability.  
Create a `.env` file in the project root with entries like:

```bash
DEFAULT_POPULATION_SIZE=200
MAX_ITERATIONS=200000
```

You can also export these values directly in your shell before running the solver.

## Architecture
- `GeneticAlgorithm.py` encapsulates the evolutionary loop: generation, crossover, mutation, and fitness evaluation.
- `getNextGeneration` performs tournament selection (size three) to assemble parents, then mutates offspring in-place for efficiency.
- `NQueensCollisionFitness` scores solutions via row, column, and diagonal collision counts, ensuring a zero score implies a valid board.
- `printNQueens` renders textual boards for quick visual inspection of results.

## Next Steps
- Introduce adaptive mutation and crossover rates that react to population diversity to accelerate convergence on larger boards.
- Layer in heuristic seeding or local search (e.g., hill climbing) to hybridize global and fine-grained optimization.
- Build an interactive visualization dashboard to compare evolutionary progress across board sizes and parameter settings.

## Tech Highlights
- **Type safety / clarity:** Python standard library only; pure functions keep data flow explicit.
- **Maintainability:** Constants extracted, `.env` loader added for configuration.
- **Scalability:** Stateless execution with configurable iteration caps for long-running experiments.

## Example
```bash
python GeneticAlgorithm.py 16
```

Example output (truncated):
```
Found a solution during iteration 482:
_ |Q|_ |_ | ...
```

## License
TODO: Specify license (e.g., MIT, Apache-2.0).
