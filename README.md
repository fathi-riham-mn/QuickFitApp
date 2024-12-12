# Quick Fit Memory Allocation Simulator

## Overview
This project simulates the Quick Fit memory allocation algorithm, a technique optimized for frequent fixed-size memory allocations. The simulator provides both a command-line and graphical interface for demonstrating the algorithm's functionality.

## Features
- **Dynamic Memory Allocation**: Allocates and deallocates memory blocks efficiently.
- **Graphical User Interface (GUI)**: A user-friendly interface built using Tkinter.
- **Testing**: Comprehensive unit tests to validate functionality.
- **Visualization**: Charts and logs for tracking memory usage.

## Project Structure
- `quickfit_ui/`: Contains the core logic and user interface.
  - `allocator.py`: The memory allocation logic for Quick Fit.
  - `ui.py`: The Tkinter-based UI.
- `main.py`: Entry point to start the application.
- `tests/`: Unit tests for the allocator.
  - `test_allocator.py`: Tests for memory allocation functionality.
- `requirements.txt`: The list of Python libraries used in the project.
- `docs/`: Documentation folder.
  - `README.md`: Project documentation.
```plaintext
QuickFitApp/
├── quickfit_ui/              # Main package containing core logic and UI
│   ├── __init__.py           # Makes it a package (can be empty)
│   ├── allocator.py          # Core logic for Quick Fit memory allocation algorithm
│   ├── ui.py                 # UI implementation using Tkinter
├── main.py                   # Entry point to run the application
├── requirements.txt          # Lists all required Python libraries
├── tests/                    # Unit tests for the Quick Fit memory allocator
│   ├── test_allocator.py     # Tests for the memory allocation functionality
├── docs/                     # Documentation folder
│   └── README.md             # Project documentation (README)
```

## Requirements
- Python 3.8+
- Tkinter (built-in with Python standard library)
- pytest (for testing)


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/fathi-riham-mn/QuickFitApp
   ```

2. Navigate into the project directory:
   ```bash
   cd QuickFitApp
   ```

3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
   
## Usage
1. Run the application:
   ```bash
   python main.py
   ```

2. Use the graphical interface to:
- Allocate memory for processes.
- Deallocate memory.
- View memory state.

## Running Tests
1. To execute the unit tests, run::
   ```bash
   pytest tests/test_allocator.py
   ```

2. Future Enhancements:
- Add support for more advanced visualizations (e.g., heatmaps for memory usage).
- Implement additional memory allocation algorithms for comparison.
- Enhance the user interface for better interactivity.



## Memory Allocation Algorithm: Quick Fit
Quick Fit is designed for systems requiring frequent fixed-size memory allocations. It uses size-specific free lists to minimize allocation time, making it suitable for systems with repetitive memory demands.

### Example
1. Allocate memory for sizes 50 KB, 100 KB, and 200 KB.
2. Deallocate memory to demonstrate reuse of free blocks.
3. Visualize the memory state in the GUI.

## Contribution
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m 'Add feature-name'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License
This project is licensed under the MIT License.

## Author
Developed by MN Fathima Riham[321425551].


This structure ensures clear organization, making navigating and scaling the project easy. You can extend or modify the components as needed!



