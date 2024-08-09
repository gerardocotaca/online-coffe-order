# Bottle Coffee Order System

## Overview

The Bottle Coffee Order System is a Python-based graphical application built with Tkinter for creating and managing coffee orders. Users can select items from a menu, enter their name, and receive a total cost for their order. The system also writes order details to a CSV file, making it easy to track and review orders. This project demonstrates basic GUI development with Tkinter, file handling, and user interaction.

## Project Goals

The main goal of this project was to create an intuitive and functional order management system for a coffee shop. This application highlights the ability to build interactive GUI applications in Python, handle user input, and manage data using file operations.

## Key Features

- **Graphical User Interface (GUI)**: Designed with Tkinter to provide a user-friendly interface for placing orders.
- **Dynamic Order Management**: Allows users to select items, calculate total cost, and display order details.
- **CSV File Handling**: Records order details in a CSV file for persistent storage and review.
- **Image Integration**: Incorporates images to enhance the visual appeal of the application.
- **Clear User Interaction**: Provides feedback on the order summary and total cost, and includes an option to exit the application.

## Technologies Used

- **Python 3.x**: The application is implemented in Python, leveraging Tkinter for the GUI and PIL for image handling.
- **Tkinter**: Used for creating the graphical user interface, including frames, labels, checkboxes, and buttons.
- **PIL (Pillow)**: Utilized for image processing and integration within the Tkinter application.
- **CSV**: Employed for writing and storing order details in a CSV file.

## Implementation Details

The project consists of the following components:

1. **Tkinter GUI Setup**: Initializes the main window, sets up frames, labels, checkboxes, and buttons.
2. **Order Management**: Handles user input, calculates total cost, and updates the result label.
3. **CSV File Operations**: Writes order details to a CSV file for record-keeping.
4. **Image Integration**: Loads and displays an image (e.g., logo) within the Tkinter window.

### Key Functions

- **`button_click()`**: Handles the order submission process, calculates the total cost, displays the result, and writes to the CSV file.
- **`clear_checkboxes()`**: Resets all checkboxes after an order is submitted.
- **`close()`**: Closes the Tkinter application window.

## Relevance to Software Engineering Roles

This project aligns with roles requiring skills in GUI development and file handling. The focus on building a user-friendly interface and managing data demonstrates key skills relevant to software engineering positions, such as:

- **GUI Development**: Showcases ability to create interactive applications using Tkinter.
- **File Management**: Demonstrates experience with file I/O operations for data persistence.
- **User Experience**: Highlights the importance of clear and intuitive user interactions in software applications.

## How to Use

1. **Clone the Repository**: Download or clone this repository to your local machine.
2. **Install Dependencies**: Ensure you have the required libraries (`PIL`, `tkinter`) installed. You can install Pillow via `pip install pillow`.
3. **Run the Application**: Execute the Python script to launch the Tkinter GUI.
4. **Place Orders**: Select items from the menu, enter your name, and submit your order to view the total cost.
5. **Exit**: Click the "Exit" button to close the application.

## Future Enhancements

- **Advanced Order Features**: Introduce options for customizing orders and tracking order history.
- **Enhanced Reporting**: Implement reporting features to analyze order trends and generate summaries.
- **GUI Improvements**: Refine the graphical interface for better usability and visual appeal.

## License

This project is licensed under the MIT License.
