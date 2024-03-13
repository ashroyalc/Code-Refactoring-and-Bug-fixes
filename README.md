# Code-Refactoring-and-Bug-fixes

## Simple Note Taking App

Welcome to the Simple Note Taking App, a lightweight web application developed using Flask and Jinja2 templating. This app allows users to create and view the notes with ease.

### Description

The Simple Note Taking App is designed to provide a seamless note-taking experience. It was initially developed with basic functionality, but after rigorous testing, we identified and fixed several bugs to improve its performance and user experience.

### Features

- Create new notes with a title and body
- View all your notes in one place

### Refactoring and Bug Fixes

We have recently refactored the codebase to make it more efficient, maintainable, and scalable. The refactoring process included:

1. Improving the code structure

During this process, we also addressed and fixed several bugs, including:

1. [Bug 1]: Changed form method to "post" & Changed button type to submit
2. [Bug 2]: Changed request.arge.get() to request.form.get() to read form attributes
3. [Bug 3]: Handled None while loading for the first time

Please refer to the commit history for more detailed information about each bug fix and code refactoring change.

### Installation

To get started with the Simple Note Taking App, follow these steps:

1. Clone the repository: `git clone https://github.com/ashroyalc/Code-Refactoring-and-Bug-fixes`
2. Navigate to the project directory: `cd Code-Refactoring-and-Bug-fixes`
3. Create a virtual environment: `python -m venv env`
4. Activate the virtual environment: `source env/bin/activate` (Unix) or `env\Scripts\activate` (Windows)
5. Install the required packages: `pip install flask`
6. Run the application: `python3 app.py`

### Usage

After running the application, open your web browser and navigate to `http://127.0.0.1:5000/` to start using the Simple Note Taking App.

### Contributing

We welcome contributions from the community. If you wish to contribute, please submit a pull request with your proposed changes.

### License

This project is licensed under the [MIT License](LICENSE).

### Contact

For any questions or suggestions, please feel free to reach out to us at [avinash.chintham@gmail.com](mailto:avinash.chintham@gmail.com).

Happy note-taking!
