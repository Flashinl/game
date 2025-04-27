
# Naval Battle Royale

A 2D naval combat game set in the Age of Sail featuring three ship classes, Battle Royale mode, and multiple difficulty settings.

## Game Controls

- **Movement:**
  - W / Up Arrow: Move forward
  - S / Down Arrow: Move backward
  - A / Left Arrow: Turn left
  - D / Right Arrow: Turn right
  
- **Combat:**
  - Space: Fire cannons

- **Game Over Screen:**
  - R: Restart game
  - Q: Quit game

## Features

- **Ship Classes:**
  - **Caravel**: Fast and agile, but lower health and damage
  - **Fluyt**: Slow but tanky, high health and medium damage
  - **Carrack**: Balanced stats, good damage and medium speed

- **Battle Royale Mode:**
  - Player + 3 Ally ships vs 4 Enemy ships
  - Last team standing wins

- **Difficulty Levels:**
  - Easy: Enemy ships are less accurate and aggressive
  - Medium: Balanced enemy AI
  - Hard: Enemy ships are highly accurate and aggressive

## Requirements

- Python 3.6 or higher
- Pygame

## Installation

1. Install Python from [python.org](https://www.python.org/downloads/)
2. Install Pygame:
   ```
   pip install pygame
   ```
3. Run the game:
   ```
   python main.py
   ```

## How to Deploy Your Game (Create an executable)

### Step 1: Install PyInstaller
```
pip install pyinstaller
```

### Step 2: Create the executable

#### For Windows:
```
pyinstaller --onefile --windowed --add-data="assets;assets" main.py
```

#### For macOS:
```
pyinstaller --onefile --windowed --add-data="assets:assets" main.py
```

#### For Linux:
```
pyinstaller --onefile --windowed --add-data="assets:assets" main.py
```

### Step 3: Find your executable
The executable will be created in the `dist` folder. You can distribute this executable file to others.

## Note

Before deploying, make sure you have all the required assets in the `assets` folder. See assets/README.md for details.
