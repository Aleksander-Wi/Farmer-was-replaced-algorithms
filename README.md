# Farmer-was-replaced-algorithms

Autonomous farming algorithms and spatial navigation logic (DFS Backtracking, Priority Queues, Torus Topology) implemented in Python for "The Farmer Was Replaced".

#  The Farmer Was Replaced - Autonomous Algorithms & Automation

Automation scripts and algorithmic logic implemented in Python for the game *"The Farmer Was Replaced"*. 

This repository demonstrates practical software engineering and robotics concepts, including **graph traversal (DFS)**, **explicit stack backtracking**, **priority queues**, and **toroidal grid navigation**.

---

##  Key Technical Highlights

###  1. Autonomous Maze Solver (`maze.py`)
- **Algorithm:** Depth-First Search (DFS) with a custom **Backtracking Stack**.
- **Mechanics:** Explores unseen path coordinates, tracks visited positions, and unwinds the navigation stack (`visited_2.pop()`) upon hitting dead ends until the treasure coordinates are reached.

###  2. Sunflower Priority Sorter (`sunflowerloop.py`)
- **Algorithm:** Priority Queue simulation using tuple evaluation.
- **Mechanics:** Measures sunflower yields across the field, dynamically selects targets via `max()` evaluation on `(quality, x, y)` tuples, and harvests the highest-value crops first.
- **Navigation:** Custom **Torus Topology Navigation** that calculates the shortest wrapping distance across world boundaries (`world_size / 2`).

###  3. Dynamic Crop Repair System (`pumpkin.py`)
- **Pattern:** Fault Inspection & Task Queue Recovery.
- **Mechanics:** Scans crops for growth failures, queues dead plant coordinates (`dead_pumpkin_x/y`), and switches to a dedicated repair mode to replant and hydrate unharvestable tiles.

---

## 📁 Repository Structure

```text
├── main.py            # Central loop controller and execution manager
├── maze.py            # Standalone DFS maze-solving algorithm
├── sunflowerloop.py   # Priority sorting and toroidal navigation
├── pumpkin.py         # Dynamic fault inspection and crop repair
├── WOOD.py            # Alternating crop pattern optimization
├── HAY.py             # Basic resource harvesting script
├── carrot.py          # Soil-tilling and planting loop
└── reset.py           # Origin position reset sequence
