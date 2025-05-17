@ -1,182 +1,136 @@

# University Self-Enrolment System

**Self-Enrolment CLI & GUI Application for University Coursework Management**

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [User Stories](#user-stories)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
  - [CLI Interface](#cli-interface)
  - [GUI Interface](#gui-interface)
- [UML Diagrams](#uml-diagrams)
- [Demo & Showcase](#demo--showcase)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview

The University Self-Enrolment System is a Python-based application that allows students to register, log in, and enrol in subjects through both a command-line interface (CLI) and a graphical user interface (GUI). Administrative users can manage student records, group, partition, and clear enrolments. Data persistence is handled via a simple file-based database (students.data).

This project was developed as part of Assessment 1 for the Software Development module and includes Requirements Analysis, Implementation (Part 2), and will be presented in a showcase presentation (Part 3).

## Features

- **Student Registration & Authentication**: Securely register and log in with email, name, and password.
- **Subject Enrolment**: Enrol, view, change, or remove subjects (up to 4 per student).
- **Administrative Tools**: View all students, group by criteria, partition subjects, remove student records, and clear databases.
- **Dual Interfaces**: Fully featured CLI menus and intuitive Tkinter-based GUI.
- **Persistent Storage**: Student and enrolment data stored in `data/students.data`.

## User Stories

Key user stories derived from the backlog -Assessment part 1

_For the full backlog, see **Assessment 1 - Part 1 - Submission - Group2-Cmp1-Lab 07 (Final)** in the `docs/` directory._

## Architecture

This system follows an MVC-like structure:

- **Models** (`university_system/models`): Defines `Student`, `Subject`, and `Admin` entities.
- **Database Layer** (`university_system/database.py`): Handles reading/writing to `data/students.data`.
- **Controllers** (`SubjectController`, etc.): Encapsulate business logic for enrolment and administration.
- **CLI Entry Point** (`main.py`): Launches the text-based menus for University, Student, and Admin.
- **GUI Modules** (`gui_login.py`, `gui_home.py`, `gui_enrol.py`, `gui_subject.py`): Build the Tkinter windows for user interaction.

## Installation

1. **Clone the repository**
```
bash
git clone https://github.com/LukiSky/FundamentalOfSoftwareDevelopment.git
cd FundamentalOfSoftwareDevelopment
```

2. **Create a virtual environment**
```
bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. **Install dependencies**
> No external packages required; uses Python standard library (Tkinter for GUI).

## Usage

### CLI Interface

1. **Start the CLI**
```
bash
python main.py
```

2. **Navigate Menus**
- **University Menu**: Choose Student or Admin.
- **Student Menu**: Register, Log In, Enrol, View/Change/Remove Enrolments.
- **Admin Menu**: Show students, Group, Partition, Remove, Clear database.

### GUI Interface

1. **Launch GUI**
```
bash
python gui_login.py
```

2. **GUI Workflow**
- **Login Window**: Enter credentials to access.
- **Home Window**: Navigate between enrolment and subject management.
- **Enrolment Window**: Add or remove subjects.
- **Subject Window**: View subject details and summaries.

## UML Use-Case and Class Diagrams

Visual specifications:
- Use-Case Diagram: Actors, goals, and relationships.
- Class Diagram: Classes, attributes, methods, and associations.

_See `docs/Assessment 1 - Part 1 - Submission - Group2-Cmp1-Lab 07 (Final).pdf` for detailed diagrams._

Note: Some changes were made in the build phase to better reflect an MVC model.

## Contributing

Contributions are welcome! Please:
1. Fork the repo and create your branch (`git checkout -b feature/YourFeature`).
2. Commit your changes (`git commit -m 'Add feature'`).
3. Push to the branch (`git push origin feature/YourFeature`).
4. Open a Pull Request.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgments

- Developed by **Team Group2-Cmp1-Lab 07 - Lucky Luki, Lia, Yeojin, Rob**
- Inspired by and a special thanks to Tausif.
