# Medical-Clinic-System
# Medical Clinic System - Assignment 3 & 4

## Overview

This repository contains the code and documentation for a **Medical Clinic System** implemented in Python. The system manages patients' data, records, and notes in a clinic, ensuring persistence across sessions. The project is divided into two major assignments:

- **Assignment 3**: Focuses on the initial implementation of the system's core functionality, including models and basic operations.
- **Assignment 4**: Builds upon Assignment 3 by introducing persistence handling for the clinic’s data, ensuring that patient information is saved and loaded correctly.

## Table of Contents

1. [Assignment 3 - Initial Implementation](#assignment-3-initial-implementation)
2. [Assignment 4 - Model Persistence](#assignment-4-model-persistence)
   1. [Step 1: Handle New Assertions for Exceptions](#step-1-handle-new-assertions-for-exceptions)
   2. [Step 2: Refactor Code and Move Collections into Data Access Objects (DAOs)](#step-2-refactor-code-and-move-collections-into-data-access-objects-daos)
   3. [Step 3: Enable Autosave and Add Code for File Handling](#step-3-enable-autosave-and-add-code-for-file-handling)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Tests](#tests)
6. [Contributing](#contributing)
7. [License](#license)

---

## Assignment 3 - Initial Implementation

### Project Overview

In **Assignment 3**, the goal was to implement the basic functionality of a **Medical Clinic System**. This system consists of multiple components:

- **Patient**: A class that holds personal information about patients, including their name, age, health number, and associated records.
- **Patient Record**: A class that stores medical notes associated with a patient.
- **Note**: A class that represents a single medical note in a patient's record.
- **Controller**: The class responsible for managing the interaction between different models, ensuring that operations such as adding patients and notes are performed correctly.

### Key Features

- Basic CRUD operations (Create, Read, Update, Delete) for managing patients, patient records, and notes.
- Each patient can have multiple associated notes in their record.
- Exception handling for common errors like attempting to add a patient with a duplicate health number.

### Files

- **controller.py**: Manages the flow of the system and calls methods from the model classes.
- **patient.py**: Defines the Patient class.
- **patient_record.py**: Defines the PatientRecord class.
- **note.py**: Defines the Note class.
- **patient_test.py**: Unit tests for the Patient class.
- **patient_record_test.py**: Unit tests for the PatientRecord class.
- **note_test.py**: Unit tests for the Note class.

---

## Assignment 4 - Model Persistence

### Project Overview

In **Assignment 4**, the goal was to implement **persistent storage** for the system, ensuring that patient information and notes are saved between application runs. The persistence layer is designed to handle saving and loading of data using files (JSON for patients and Pickle for patient records).

### Phase Breakdown

#### Step 1: Handle New Assertions for Exceptions

- **Objective**: Modify the `Controller` class to handle new exceptions that were introduced in the integration tests.
- **Details**: The system needs to raise specific exceptions in case of incorrect usage (e.g., adding a patient with an invalid health number or duplicate records).
- **Changes**: 
  - Exception classes are imported from the `exceptions` directory.
  - The `Controller` class is refactored to raise these exceptions in relevant parts of the code.

#### Step 2: Refactor Code and Move Collections into Data Access Objects (DAOs)

- **Objective**: Refactor the code to move the collections (patients and notes) into their respective **Data Access Objects (DAOs)**.
- **Details**: 
  - A `PatientDAOJSON` class is introduced to handle CRUD operations for patients.
  - The `NoteDAOPickle` class is introduced to handle CRUD operations for notes associated with patient records.
  - The `Controller` and `PatientRecord` classes delegate the collection operations to these DAO objects.
  
#### Step 3: Enable Autosave and Add Code for File Handling

- **Objective**: Implement the ability to save and load data using files. 
- **Details**:
  - **User Handling**: The system reads user credentials (usernames and password hashes) from the `users.txt` file. 
  - **Patient Handling**: The `PatientDAOJSON` class is updated to load patients from the `patients.json` file and save them after any state changes.
  - **Note Handling**: The `NoteDAOPickle` class is updated to handle saving and loading patient records, with separate files for each patient's notes (using Pickle for binary serialization).

### New Components

- **Data Access Objects (DAOs)**:
  - **PatientDAOJSON**: Handles CRUD operations for patients using JSON for persistence.
  - **NoteDAOPickle**: Handles CRUD operations for notes using Pickle for binary persistence.
- **Users File**: `users.txt` holds usernames and password hashes, read into memory when the system starts.

### Files

- **controller.py**: Now includes the `autosave` functionality and exception handling. Data access is delegated to DAOs for patient and note handling.
- **patient.py**: Refactored to work with `PatientDAOJSON`.
- **patient_record.py**: Refactored to work with `NoteDAOPickle`.
- **note.py**: Updated for integration with `NoteDAOPickle`.
- **patient_test.py**: Integration and unit tests now include persistence-related tests.
- **patient_record_test.py**: Tests for the persistence of patient records.
- **integration_test.py**: Includes tests for the new persistence functionality.
- **users.txt**: A text file containing usernames and password hashes for user authentication.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/medical-clinic-system.git
   cd medical-clinic-system
