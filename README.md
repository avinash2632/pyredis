# pyredis

<b>How Pyredis Works</b>

This Python application uses Redis to store the names of users in a database. Redis is an in-memory data store, which means that it stores data in memory instead of on disk. This makes it very fast for retrieving data.

The application has two endpoints:

localhost:5000/users - This endpoint retrieves the number of users in the database.
<br></br>

localhost:5000/id - This endpoint retrieves the name of the user with the specified ID.
<br></br>
The application uses the following steps to retrieve the number of users in the database:

Connect to the Redis database.
Use the KEYS command to get a list of all the keys in the database.
Return the number of users.
The application uses the following steps to retrieve the name of the user with the specified ID:

Connect to the Redis database.
Use the GET command to get the value of the key with the specified ID.
Return the value of the key.
The application is very simple to use. To run the application, you will need to have Python and Redis installed. Once you have installed the dependencies, you can run the application by executing the python files in the repo
<br>

The application will start listening on port 5000. You can then access the endpoints by visiting the following URLs in your browser:
<br>
localhost:5000/users
<br></br>
localhost:5000/id
<br>


