# manim_name

# Manim Project: Cinematic Text Animation

This project contains a Python script (`manim_name.py`) to generate a cinematic text animation using the Manim library. The animation displays the text "abrar_tanim" with a series of visual effects.

## Animation Sequence
1.  **Write:** The text is drawn on the screen from left to right with a slate color and a bold "Poppins" font.
2.  **Transform:** The text simultaneously grows larger and changes color to purple, creating a cinematic feel.
3.  **Unwrite:** The text is erased from the screen, also from left to right.

---

## Getting Started

Follow these instructions to set up the project and run the animation on your local machine.

### Prerequisites
* Python 3.7 or newer.
* The "Poppins" font must be installed on your system.

### Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone <repository>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # On macOS and Linux
    python3 -m venv manim_env
    source manim_env/bin/activate

    # On Windows
    python -m venv manim_env
    manim_env\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install manim
    ```

---

## Running the Animation

To generate the video, execute the following command from the root of the project directory:

```bash
manim -pql manim_name.py AbrarTanimAnimation
