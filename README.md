Write a CRUD operation using FastAPI (use a list to store the todo details).

 

The API should have the following endpoints:

 

1. GET "/todos" endpoint that allowes a user to get a list of todos.

2. GET "/todos/{id}" that allows a user to get a single e todo.

3. POST "/todos" that allows a user to create a new todo.

4. PUT "/todos/{id}" that allows a user to update a todo.

5. DELETE "/todos/{id}" that allows a user to delete a todo.

 

Each todo should have a title, description and status. The status can be either "pending" or "in-progress" or "completed".