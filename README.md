# Ticket Management System

## Overview

The Ticket Management System is a desktop application designed to handle ticketing processes efficiently. Built using Python's Tkinter for the frontend and MySQL for the backend, this system provides an intuitive user interface for managing and tracking tickets. The application utilizes Python for database connectivity, ensuring smooth interactions between the frontend and backend.

## Key Features

- **User-Friendly Interface:** Designed with Tkinter to provide a clear and easy-to-navigate graphical user interface for managing tickets.
- **Ticket Creation and Tracking:** Users can create new tickets, track their status, and manage existing tickets through a straightforward interface.
- **Database Integration:** Uses MySQL as the backend database, enabling secure and efficient storage of ticket information.
- **Python-MySQL Connectivity:** Integrated Python with MySQL for seamless communication between the application and the database.

## Technology Stack

- **Frontend:** Python Tkinter
- **Backend:** MySQL
- **Database Connectivity:** Python with MySQL Connector

## Installation

To set up the Ticket Management System locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ROSHTU/Ticket-Management-System.git
   cd Ticket-Management-System
   ```
2. **Install required Python packages:**
   - Make sure you have mysql-connector-python installed. You can install it using pip:

     ```bash
     pip install mysql-connector-python
     ```
3. **Set up the MySQL database:**
  - Create a MySQL database and import the necessary schema. The schema file should be available in the repository.
  - Update the database connection details in the Python code to match your MySQL setup.
    
5.**Run the application:**
   - Execute the Python script to launch the Tkinter-based GUI:

      ```bash
      python main.py
      ```
## Usage
- **Create Tickets:** Use the provided forms to create new tickets and enter relevant details.
- **Manage Tickets:** View, update, and track the status of existing tickets from the main interface.
- **Database Configuration:** Ensure that the database connection details are correctly configured in the Python script to interact with your MySQL server.

## Contributing
If you'd like to contribute to the project, please fork the repository and submit a pull request with your changes. Contributions and suggestions are always welcome!
