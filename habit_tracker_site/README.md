# Habit Tracker

A simple web application built with Python and Flask to track your daily habits.

## Features

*   Add and delete habits.
*   Mark habits as complete/incomplete for each day on a calendar.
*   View your progress for the current month.

## Technologies Used

*   Python
*   Flask
*   SQLAlchemy
*   Flask-Migrate
*   SQLite

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd habit_tracker_site
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
    *(On Windows, use `venv\Scripts\activate`)*

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialize the database:**
    ```bash
    flask db upgrade
    ```

5.  **Run the application:**
    ```bash
    flask run
    ```

The application will be available at `http://127.0.0.1:5000`.

## How to Use

*   **Add a habit:** Type the name of the habit in the input field and click "Add Habit".
*   **Track a habit:** Click on a date in the calendar next to a habit to mark it as complete for that day. Click again to unmark it.
*   **Delete a habit:** Click the "Delete" button next to the habit you want to remove.
