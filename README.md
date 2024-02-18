# HTN Visualizer with PyHOP and customtkinter

## Overview

This HTN (Hierarchical Task Network) Visualizer is a practical tool developed during a lab in the Artificial Intelligence course at the University of Örebro.
It utilizes PyHOP, created by Dana S. Nau, to demonstrate how a robot navigates within a room to perform tasks such as fetching and transporting boxes.
The visualizer allows for interactive planning through custom start, end, and box positions, or through random generated test scenarios for navigation, fetching, and transporting.

## Features

- **Interactive Planning**: Customize the robot's start and end positions, as well as the box position, and see the plan solved in real time.
- **Preset Test Scenarios**: Quickly test the robot's navigation, fetching, and transporting capabilities with random scenarios.
- **Dynamic Environment Interaction**: Open and close doors within the environment by clicking on them to affect the robot's planning path.
- **Step-by-Step Plan Visualization**: Each step the robot takes is clearly outlined, providing insight into the planning process.

## Getting Started

### Prerequisites

- Python installation is required.
- `customtkinter` library is needed for the GUI components.
- `pillow` library is needed for loading images

### Installation

1. Clone this repository to your local machine:
   git clone https://github.com/vikander86/HTN_Visualizer/

2. Install libraries:
   pip install -r requirements.txt

3. Clone PyHOP from Dana S. Nau's Bitbucket repository into the same folder:
   git clone https://bitbucket.org/dananau/pyhop/src/master/

4. Rename the cloned PyHOP directory from `master` to `pyhop` to ensure proper module referencing:
   mv master pyhop

### Running the Visualizer

Navigate to the project directory and run the main.py file:
python3 main.py

## Usage

- **Custom Planning**: Specify the Start position, End position, and Box position, then press "Solve".
- **Test Scenarios**: Run predefined scenarios using "Test Navigate", "Test Fetch", and "Test Transport".
- **Environment Interaction**: Click doors to open/close them, influencing the planning process.

## Contributing

I welcome contributions, including bug reports, feature requests, and code improvements. Please use GitHub issues and pull requests.

## Images

- Images for robot and box have been acquired from www.vecteezy.com

## Acknowledgments

- Dana S. Nau for PyHOP, enabling detailed HTN planning.
- The Artificial Intelligence course team
- The `customtkinter` library for enhancing the UI experience.
