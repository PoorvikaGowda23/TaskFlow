# Real-Time To-Do List Application 🚀

A full-stack web application with user authentication, task management, and **real-time synchronization** across multiple clients using Flask and Socket Programming. Perfect for collaborative task tracking!

## 🌟 Features

- **🔐 User Authentication**
  - Register new users
  - Login with existing credentials
- **📝 Task Management (CRUD)**
  - Add new tasks with descriptions
  - Edit existing tasks
  - Delete tasks
  - View all tasks
- **⚡ Real-Time Sync**
  - Instant updates across all connected devices
  - Socket-based notifications for task changes
- **💾 Persistent Storage**
  - JSON-based data persistence
  - Automatic backups in `users.json`

## 🛠 Tech Stack

| Component               | Technology                         |
|-------------------------|------------------------------------|
| Frontend                | HTML, Bootstrap , JavaScript       |
| Backend                 | Python 3.9+, Flask                 |
| Real-Time Communication | Python Socket Programming          |
| Data Storage            | JSON (File-based storage)          |
| Package Manager         | pip                                |

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/todo-list-app.git
   cd todo-list-app

2.  **Install dependencies**
        pip install flask

3.  **Run the servers (in separate terminals)**
    # Terminal 1 - Start Flask Web Server (Port 5000)
        python app.py
    # Terminal 2 - Start Socket Server (Port 12346)
        python server.py

4.  **Access the application**
        Open http://localhost:5000 in your browser.

   
