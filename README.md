//////////////////////////////////////////////////////////////////////////////////////////////
# Please note: This isn't finished, has bugs and ineffiencies!
/////////////////////////////////////////////////////////////////////////////////////////////
### Planned:
- Script Clean up!
- Local/Network Multiplayer functionality
- 
-
////////////////////////////////////////////////////////////////////////////////////////////

# PyGBag_PyGame_Template
For anyone who wants a head start with their PyGame Projects and want to port to HTML5 for upload on Itch.io

## Overview

This is a Template you may use for your Pygame games, it is PyGBag ready. This allows you to port to HTML5 and upload your game to HTML-Game hosting platforms like Itch.io or Gamejolt.com.


## PyGBag:
Pygbag is a tool that enables the packaging of Python-based games developed with libraries like Pygame into a browser-playable format using WebAssembly. This allows games to run in a web browser without requiring users to install Python or additional dependencies. Pygbag provides an easy way to distribute Python games to a wide audience via the web.

### Key Features of Pygbag:
- Converts Python and Pygame applications into WebAssembly (WASM).
- Generates HTML files that can be hosted on platforms like GitHub Pages or other web hosting services.
- Allows for interactive debugging in the browser.
- Ideal for showcasing games or applications to a broad audience without requiring installation.

---

## Features
- **Interactive Objects**: Dynamic objects with behaviors and animations.
- **Animations**: Integrated animated sprites for enhanced visuals.
- **Game Loop**: Core loop to manage updates, rendering, and user interaction.
- **Modular Design**: Easily extendable and modular codebase.

---

## Requirements

### Python Version
- Python 3.8 or higher

### Dependencies
- `pygame`

Install dependencies via pip:

pip install pygame pygbag


## Usage

### Running:

- PyGBag games can be run like any other PyGame.

### Compiling to HTML5:

- Main application MUST be called "Main.py"
- with PyGBag already installed, navigate to project directory "cd PATH_TO_PROJECT"
- type "python -m pygbag --archive" to covert "main.py" to a html package (zip) which can be uploaded and played on Itch.io


- https://github.com/pygame-web/pygbag   (More documanetation found here!)

### Customization
- Modify game assets and settings in the respective sections of the code.
- Add or enhance object behaviors by editing the object classes.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments
Special thanks to the `pygame` community for providing extensive documentation and examples to support game development.
