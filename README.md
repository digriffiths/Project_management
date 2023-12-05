# Project Management App (Backend)

This project is a backend application for a Project Management App. It provides APIs for user registration, authentication, and task management. The application is built with FastAPI and SQLAlchemy, and uses JWT for authentication.

## Features

- **User Registration and Authentication**: Users can register and authenticate themselves using a username and password. Authentication is handled with a JWT.
- **Task Management**: Users can create, read, update, and delete tasks. Each task has a title, description, status (e.g., pending, completed), and a due date.
- **Task Prioritization**: Users can prioritize tasks.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Docker
- PostgreSQL

### Installation

1. Clone the repository:
   bash
   git clone https://github.com/yourusername/todo-list-app-backend.git

2. Navigate to the project directory:
   bash
   cd todo-list-app-backend

3. Build the Docker image:
   bash
   docker-compose build

4. Run the Docker container:
   bash
   docker-compose up

The application will be available at `http://localhost:8000`.

## Usage

You can interact with the application using any HTTP client like `curl` or `httpie`, or use a GUI-based tool like Postman.

Here are some example API calls:

- Register a new user:
  bash
  http POST http://localhost:8000/register username=testuser password=testpass

- Authenticate a user:
  bash
  http POST http://localhost:8000/token username=testuser password=testpass

- Add a new task:
  bash
  http POST http://localhost:8000/add_task task_name="Test Task" project="Test Project" task_due_by="2023-12-31T23:59:59Z" is_high_priority=true Authorization:"Bearer your_token"

- Get all tasks for a user:
  bash
  http GET http://localhost:8000/user_tasks Authorization:"Bearer your_token"

Replace `your_token` with the token received from the authenticate API call.

## Development

This project follows best practices for code organization, version control, error handling, and uses environment variables for sensitive information. It uses Alembic for database migrations and Docker for containerization.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
