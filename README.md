Task API
A simple CRUD (Create, Read, Update, Delete) REST API for managing a to-do list, built with FastAPI and Python. Data is stored in memory only (no database) — this was a learning assignment focused on HTTP, CRUD, status codes, and Swagger UI.
What this project is
This API lets a client:
Create a new task
Read all tasks or a single task
Update a task's title or completed status
Delete a task
All data lives in a Python list in memory, so it resets every time the server restarts.
How to install and run it
Clone this repository:
Code
Install the dependencies:
Code
Start the server:
Code
The API will be running at http://localhost:8000.
Open the interactive Swagger UI documentation at:
Code
Endpoints
Method
Endpoint
Description
Success Code
Error Codes
GET
/
API info
200
-
GET
/health
Health check
200
-
GET
/tasks
List all tasks
200
-
GET
/tasks/{task_id}
Get a single task by ID
200
404
POST
/tasks
Create a new task
201
400
PUT
/tasks/{task_id}
Update a task's title and/or status
200
400, 404
DELETE
/tasks/{task_id}
Delete a task
204
404
Example request (curl)
Code
Example response:
Code
Swagger UI — Full Testing Walkthrough
Every endpoint was tested through the interactive Swagger UI (/docs) using "Try it out". Screenshots for each step are below.
GET / (root)
screenshot-root1
screenshot-root2
screenshot-root3
GET /health
screenshot-health1
screenshot-health2
GET /tasks
screenshot-get-tasks1
screenshot-get-tasks2
screenshot-get-tasks3
GET /tasks/{task_id}
screenshot-get-task_by_id1
screenshot-get-task_by_id2
screenshot-get-task_by_id3
screenshot-get-task_by_id4
screenshot-get-task_by_id5
POST /tasks
screenshot-post1
screenshot-post2
screenshot-post3
screenshot-post4
PUT /tasks/{task_id}
screenshot-put1
screenshot-put2
screenshot-put3
DELETE /tasks/{task_id}
screenshot-delete1
screenshot-delete2
Notes
Data is stored only in memory. Restarting the server resets it back to the 3 example tasks.
Input is validated: creating or updating a task with an empty title returns a 400 error.
Requesting a task ID that doesn't exist returns a 404 error with a JSON message.