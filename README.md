Task API

A simple CRUD (Create, Read, Update, Delete) REST API for managing a to-do list, built with FastAPI and Python. Data is stored in memory only (no database) — this was a learning assignment focused on HTTP, CRUD, status codes, and Swagger UI.

What this project is

This API lets a client:

· Create a new task
· Read all tasks or a single task
· Update a task's title or completed status
· Delete a task

All data lives in a Python list in memory, so it resets every time the server restarts.

How to install and run it

1. Clone this repository:
   
   git clone https://github.com/Malaika-CS/task-crud-api.git
   cd task-crud-api
   
2. Install the dependencies:
   
   pip install fastapi uvicorn
   
3. Start the server:
   
   uvicorn main:app --reload
   
4. The API will be running at http://localhost:8000.
5. Open the interactive Swagger UI documentation at:
   
   http://localhost:8000/docs
   

Endpoints

Method Endpoint Description Success Code Error Codes
GET / API info 200 -
GET /health Health check 200 -
GET /tasks List all tasks 200 -
GET /tasks/{task_id} Get a single task by ID 200 404
POST /tasks Create a new task 201 400
PUT /tasks/{task_id} Update a task's title and/or status 200 400, 404
DELETE /tasks/{task_id} Delete a task 204 404

Example request (curl)


curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d '{"title":"Buy milk"}'


Example response:


HTTP/1.1 201 Created
content-type: application/json

{"id":4,"title":"Buy milk","done":false}


Swagger UI — Full Testing Walkthrough

Every endpoint was tested through the interactive Swagger UI (/docs) using "Try it out". Screenshots for each step are below.

GET / (root)

screenshot-root1.png
screenshot-root2.png
screenshot-root3.png

GET /health

screenshot-health1.png
screenshot-health2.png

GET /tasks

screenshot-get-tasks1.png
screenshot-get-tasks2.png
screenshot-get-tasks3.png

GET /tasks/{task_id}

screenshot-get-task_by_id1.png
screenshot-get-task_by_id2.png
screenshot-get-task_by_id3.png
screenshot-get-task_by_id4.png
screenshot-get-task_by_id5.png

POST /tasks

screenshot-post1.png
screenshot-post2.png
screenshot-post3.png
screenshot-post4.png

PUT /tasks/{task_id}

screenshot-put1.png
screenshot-put2.png
screenshot-put3.png

DELETE /tasks/{task_id}

screenshot-delete1.png
screenshot-delete2.png

Notes

· Data is stored only in memory. Restarting the server resets it back to the 3 example tasks.
· Input is validated: creating or updating a task with an empty title returns a 400 error.
· Requesting a task ID that doesn't exist returns a 404 error with a JSON message.
