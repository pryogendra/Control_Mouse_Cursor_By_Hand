#Automation: Control the Mouse Cursor Using Color

This project automates mouse control using color recognition. The program detects specific colors in a video feed and translates them into mouse actions:

    Red: Scroll the screen.
    Green: Trigger click events.
    Yellow: Control cursor movement.

This tool is designed for automation tasks, accessibility purposes, or as a demonstration of computer vision in action.
Features

    Red Color Detection: Scrolls the screen vertically on red object.
    Green Color Detection: Executes mouse clicks (left-click) when a green object is detected.
    Yellow Color Detection: Moves the mouse cursor to follow a yellow object in real time.

Installation
Prerequisites

Ensure you have the following installed:

    Python 3.x
    OpenCV (cv2) library
    NumPy library
    Pyautogui library
    Time Library

Steps

    Clone the repository:

    bash

git clone https://github.com/pryogendra/Control_Mouse_Cursor_By_Hand.git
cd Control_Mouse_Cussor_By_Hand

Install the required packages:

bash

pip install -r requirements.txt

Run the program:

bash

    python3 main.py

Usage

    Setup: Ensure your webcam or video feed is active and visible.
    Interaction: Hold objects or surfaces of the respective colors (Red, Green, Yellow) within the camera's view.
        Red: Move the red object up or down to scroll.
        Green: Hover or flash the green object to click.
        Yellow: Move the yellow object to guide the cursor.

Example

    Hold a yellow sticky note to move the mouse pointer.
    Use a red marker to scroll a webpage up and down.
    Use a green object like a leaf to click on icons or links.

Contributing

Contributions are welcome! If you have ideas for improvement or find bugs, feel free to open an issue or submit a pull request.

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes and commit them (git commit -m 'Add feature').
    Push to the branch (git push origin feature-branch).
    Open a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgements

    Thanks to the OpenCV and NumPy communities for their fantastic libraries.
    Special thanks to all contributors for their support and contributions.
