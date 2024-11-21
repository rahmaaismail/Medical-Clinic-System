# Medical Clinic System  

## Overview  
This repository contains the code and documentation for a Medical Clinic System implemented in Python. The system manages patient data, records, and notes in a clinic, ensuring persistence across sessions. The project was completed in collaboration with a classmate and spans three major phases:  

- **Assignment 3**: Initial implementation of the system's core functionality, including data models and basic operations.  
- **Assignment 4**: Enhancements for persistent data storage and exception handling.  
- **Assignment 5**: Development of a Graphical User Interface (GUI) for improved usability and interaction.  

## Table of Contents  
- [Overview](#overview)  
- [Features](#features)  
- [Installation](#installation)  

## Features  

### Core Functionality  
- CRUD operations for managing patients and notes.  
- Search and filtering capabilities for patient records using PHNs and names.  
- Exception handling for invalid operations, such as duplicate entries or invalid updates.  

### Data Persistence  
- File-based storage using JSON for patients and Pickle for patient notes.  
- DAO (Data Access Object) pattern for modular and scalable persistence handling.  
- Autosave functionality to ensure data integrity across sessions.  

### Graphical User Interface (GUI)  
- Built using PyQt6 with intuitive components for managing clinic data.  
- Displays patient lists in `QTableView` and notes in `QPlainTextEdit`.  
- Fully adheres to the MVC (Model-View-Controller) design pattern for separation of concerns.  

## Installation  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/medical-clinic-system.git  
   cd medical-clinic-system  

