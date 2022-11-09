from db.run_sql import run_sql
from models.user import User
import repositories.task_repository as task_repository
  
def select_all():  
    users = [] 

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in users:
        user = User(row['first_name'], row['last_name'], row['id'] )
        users.append(task)
    return users

# SAVE 
def save(user):
    sql = """INSERT INTO users
    (first_name, last_name)
    VALUES (%s,%s)
    RETURNING *"""

    values = [user.first_name, user.last_name]
    results = run_sql(sql,values)
    id = results[0]['id']
    user.id = id
    return user
   
# SELECT

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"  
    values = [id] 
    results = run_sql(sql, values)
    
    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        user = User(result['first_name'], result['last_name'], result['id'] )
    return user

# DELETE ALL 

def delete_all():
     sql = "DELETE FROM users"
     run_sql(sql)

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)
   
# UPDATE 

def update(task):
    sql = "UPDATE users SET (first_name, last_name) = (%s,%s) WHERE id = %s"
    values = [users.first_name, users.last_name]
    run_sql(sql, values)


# def tasks(user):
#     sql = "SELECT * FROM tasks WHERE id=%s"
#     values = [id]
#     result = (sql, values)
     
#     if results:
#         result = results[0]
#         user = select(result['user_id'])
#         task_by_user = Task(result['description'], result['assignee'], result['duration'],user, result['completed'], result['id'] )
#     return task_by_user