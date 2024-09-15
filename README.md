# Internship Approval, Tracking, and Management System

This is a web-based **Internship Approval, Tracking, and Management System** built with ReactPy. It allows students to apply for internships, check their application status, and provide feedback, while faculty members can log in, view applications, approve or disapprove them, and view feedback.

## Features

- **Home Page**: Introduction and description of the system.
- **Apply Page**: Students can fill out an internship application form.
- **Check Status Page**: Students can check the current status of their internship applications.
- **Feedback Page**: Students can provide feedback about completed internships.
- **View Feedback Page**: Faculty members can view all feedback submitted by students.
- **Faculty Login**: Faculty members can log in to review and manage internship applications.
- **Internship Control Dashboard**: Faculty members can approve or disapprove applications.
- **Logout Feature**: Faculty members can log out of the system.

## Installation

Follow these steps to set up the project locally.

### Prerequisites

- Python 3.x
- Node.js and npm (for ReactPy)

### Setup Instructions

1. Clone this repository:

    ```bash
    git clone https://github.com/gokulmohankumar/reactPY-InternManagement.git
    ```

2. Navigate into the project directory:

    ```bash
    cd internship-management-system
    ```

3. Create a virtual environment for Python:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the project:

    ```bash
    python main.py
    ```

6. Open your browser and navigate to `http://localhost:8000` to see the app running.

### note
for faculty login <br>
facultyID : faculty123 <br>
password : password456 <br>

### Project Structure

```plaintext
.
├── frontend/             # ReactPy components and static assets
├── pages/                # Individual pages for Home, Apply, Status, etc.
├── main.py               # Entry point for the app
├── watcher.py            # Automatically restarts the project on file changes
├── venv/                 # Virtual environment for Python dependencies
├── requirements.txt      # List of Python dependencies
└── README.md             # This file
![image](https://github.com/user-attachments/assets/011c0b8b-d326-4436-a41b-909df07a401a)
![image](https://github.com/user-attachments/assets/12d60f01-90c1-455d-8d31-5df7ca608525)
![image](https://github.com/user-attachments/assets/f565453c-e37a-4cb1-baf1-f109763ceb71)
![Uploading image.png…]()

