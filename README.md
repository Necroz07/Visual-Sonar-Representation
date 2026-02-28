# Visual Sonar Representation

Visual Sonar Representation is a real-time sonar simulation in pygame demonstrating wave propagation, echo detection, and distance calculation.

The project visualizes how sonar systems estimate distance by measuring the time taken for sound waves to travel to an object and return as echoes.


---
## Demo

### https://www.youtube.com/watch?v=UHLWVBOWFMs

<img width="588" height="627" alt="image" src="https://github.com/user-attachments/assets/98ca4987-2e8c-4427-828f-085fd3c66ea1" />


## How It Works

### Sonar Simulation Logic

- A wave pulse originates from the center point and expands outward
- When the wave reaches a placed target point, an echo wave is triggered
- The system measures:
    - Time from emission to contact
    - Time for echo return
    - Distance is calculated using time-of-flight principles and a simulated speed of sound
- Results are displayed in both meters and pixels





### User Interaction

- Click anywhere on screen to place a sonar ping target
- The system automatically detects when the wave intersects the target
- Echo response is visualized in real time
- Distance and time are displayed on the HUD
- Previous measurements are stored in a history log




### Controls

- Mouse Click → Place sonar target
- ESC → Pause menu
- TAB → History / overview panel

  

### Purpose and Learning Goals

This project was built to explore:

- Real-time simulation logic
- Time-based physics modeling
- Pygame rendering and surface management
- Event-driven input handling
- UI overlays and state control
- Audio integration in simulations
- The goal was to create an intuitive visualization of sonar concepts rather than a game.


---

## Features

- Real-time wave propagation simulation
- Echo detection system
- Distance calculation using time-of-flight
- Pause menu with SFX and music toggles
- History tracking of measurements
- Layered UI overlays
- Integrated sound effects and background audio

---

## Tech Stack
- Python
- Pygame
- Basic physics/time-of-flight modeling
- GitHub for version control

---

## How to Run

1. Clone the repository
   ```
   git clone https://github.com/Necroz07/Visual-Sonar-Representation
   ```

2. Navigate to the project directory
   ```
   cd Visual-Sonar-Representation
   ```

3. Install pygame
   ``` pip install pygame ```

4. Run the application
   ```
   python "sonar app.py"
   ```

---

## Project Structure

```
Visual-Sonar-Representation/
├── assets/
│   ├── Minecraftia-Regular.ttf
|   ├── background.png
|   ├── clock.png
|   ├── icon.png
|   ├── music.png
|   ├── object1.png
|   ├── sfx.png
|   └── spawn.png
├── sounds/
│   ├── bg.mp3
│   ├── cat.wav
│   ├── click.mp3
│   ├── pause.wav
│   ├── wave_end.wav
│   └── wave_start.wav
├── .gitattributes
└── sonar app.py
```

---

## What I Learned
- Managing real-time stimulations in python
- Structuring event-driven loops
- Handling layered rendering with transparency
- Implementation timing-based physics calculations
- Using Git and GitHub for version control and collaboration
