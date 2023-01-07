
# Task manager

**Task Manager** is a Fullstack Task Management Application, where
people can register and login into their account. Users can perform add
their daily tasks, color-highlight any task, after done they can mark a
task as done. Also in the sidebar screen, they can see their done tasks.

## Live
**Video Demo:** https://youtu.be/4S5oi9WjbZE

**Frontend**: [Click](https://taskmanager-rahi.web.app/) or visit here: https://taskmanager-rahi.web.app/

**Backend api root**: http://taskmanage.pythonanywhere.com
## Tech Stack

**Frontend:** Reactjs,Bootstrap,Redux,Context Api,react-router-dom,react-hook,react-hook-form,react-toastify,jwt-decode,axios

**Backend:** Python,Django,Restframework,simpleJWT,cors-headers,mysqlclient

**Database:** Mysql,Sqlite3.




  
## Features

- Register with `username`,`email` and `password`
- Login with `username` and `password`
- Add Task
- All Task in a single screen
- Highlight/change color of a Task
- Make a task as `done`
- All `done task`s listed in sidebar drawer
- Delete a task parmanently from `done list`
 
## API Reference

#### Register

```http
  POST /auth/register/
```

| body | 
| :-------- | 
| `username,email,password,password2` |  

----------------------------------------
#### Login

```http
  POST /auth/login/
```
-------------------
| body |          
| :-------- |  
| `username,password`| 

----------------------------------------
#### For every request for each end point below is **Required** to pass a  Jwt token in request header with prefix `JWT`


#### GET Task Lists

```http
  GET /
```
 | Parameter | Response     |  
| :-------- | :------- |  
| ` `      | `All tasks` |  
| `query=done`| `All done tasks ` | 
| `query=undone`| `All undone tasks ` |

----------------------------------------
#### Create a new Task 

```http
  POST /
```
| body | Response     |  
| :-------- | :------- |  
| `note:str,color(option:str),is_done(optional:bool) `      | `new task` |  

----------------------------------------
#### Update a new Task 

```http
  PUT /<id>
```
| body | Response     |  
| :-------- | :------- |  
| `note:str,color(option):str,is_done(optional):bool}`      | `updated task` |  

----------------------------------------
#### Delete a new Task 

```http
  DELETE /<id>
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/icerahi/taskmanager
```

Go to the project directory

```bash
  cd taskmanager
```
### Setup backend with mysql database
- Install mysql database/Xammp server - You can follow this: https://vitux.com/ubuntu-xampp/
- After Installation open terminal and run xampp server 
```bash
sudo /opt/lampp/lampp start
```
- Then Open browser http://localhost/phpmyadmin and create a new database with name `taskmanager`

Go to project backend directory and write

```bash
  cd backend
  virtualenv -p python3 venv 
  source venv/bin/activate
  pip install -r requirements.txt
  python manage.py loaddata data.json
  python manage.py makemigrations
  python manage.py migrate 
  python manage.py runserver
```

### Setup frontend
Go to frontend directory

```bash
  cd frontend
```
And inside the src folder open the .env file and comment down `production domain` and uncomment `localdomain`

```bash
  npm start
```
It will open the Project in your default browser: http://localhost:3000

  
## Authors

- [Imran Hasan Rahi](https://linkedin.com/in/icerahi)

  
