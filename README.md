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
- **Python 3.9+**
- **pip package manager**

### Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/your-username/todo-list-app.git
    cd todo-list-app
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask server**
    ```bash
    python app.py
    ```

4. **Run the Socket server**
    ```bash
    python server.py
    ```

5. **Access the application**
    Open [http://localhost:5000](http://localhost:5000) in your browser.

## 📂 Project Structure
```
todo-list-app/
│
├── app.py             # Flask application (Web server)
├── server.py          # Socket server for real-time communication
├── client.py          # Client-side socket communication (optional)
├── users.json         # JSON file for storing user data
├── index.html         # Frontend HTML file
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies
```
## 📝 Usage

### 🆕 Register a New User
1. Enter a username in the "Register or Login" section and click **"Register"**.
2. If the username already exists, you will be prompted to choose a different one. ❗

### 🔑 Login
1. Enter your registered username and click **"Login"**.
2. Upon successful login, the **"Add Task"** and **"Your Tasks"** sections will become visible. 🎉

### ➕ Add a Task
1. Enter a task description in the **"Add Task"** section and click **"Add Task"**.
2. The task will be added to your list and synchronized in real-time across all connected devices. ⚡

### ✏️ Edit a Task
1. Click the **"Edit"** button next to the task you want to modify.
2. Enter the new task description in the prompt and click **"OK"**.
3. The task will be updated in real-time. 🔄

### ❌ Delete a Task
1. Click the **"Delete"** button next to the task you want to remove.
2. The task will be deleted and the list will be updated in real-time. 🗑️

### 👀 View Tasks
1. All tasks for the logged-in user are displayed in the **"Your Tasks"** section.
2. Tasks are automatically updated when changes are made. 📋

---

## 🔧 Troubleshooting

### 🚨 Socket Server Not Running
- Ensure that the socket server (`server.py`) is running on port `12346`.
- Check for any port conflicts or firewall issues. 🔍

### 🚨 Flask Server Not Running
- Ensure that the Flask server (`app.py`) is running on port `5000`.
- Check for any port conflicts or firewall issues. 🔍

### 🚨 Real-Time Sync Not Working
- Ensure both the Flask server and the socket server are running.
- Check the browser console for any JavaScript errors. 🛠️
