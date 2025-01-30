# Conway's Game of Life

This project is a Python implementation of Conway's Game of Life, a zero-player game where cells on a grid evolve based on simple rules.

## Features
- Randomly generated initial grid configuration.
- Clear terminal-based visualization using Unicode characters.
- Dynamic simulation with adjustable grid size.
- Handles infinite generations until interrupted by the user.

## Rules of the Game
1. Any live cell with two or three live neighbors survives.
2. Any dead cell with exactly three live neighbors becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

## Installation
### Prerequisites
- Python 3.6 or higher
- `numpy` library

To install `numpy`, run:
```bash
pip install numpy
```

### Clone the Repository
```bash
git clone https://github.com/yourusername/conways-game-of-life.git
cd conways-game-of-life
```

## Usage
Run the program by executing the following command:
```bash
python game_of_life.py
```

### Controls
- The simulation runs continuously.
- Press `Ctrl+C` to stop the simulation.

## Customization
You can customize the grid size by modifying the `rows` and `cols` variables in the `if __name__ == "__main__":` section of the code:
```python
rows, cols = 20, 40
```

## Example Output
Below is an example of the grid visualization:
```
□ □ □ ■ □ □ □
□ □ ■ ■ ■ □ □
□ □ □ ■ □ □ □
□ □ □ □ □ □ □
```
`■` represents live cells, and `□` represents dead cells.

## Project Structure
```
conways-game-of-life/
├── main.py  # Main Python script
├── README.md        # Project documentation
```

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.
