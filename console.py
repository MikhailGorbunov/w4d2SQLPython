import pdb 
from models.task import Task
from models.user import User
import repositories.task_repository as task_repository  
import repositories.user_repository as user_repository  

task_repository.delete_all()
user_repository.delete_all()

user1 = User('Lara', 'Smith')


user2 = User('Jim', 'Walk')
user_repository.save(user1)
user_repository.save(user2)


task1 = Task('Write Emails', 'Lara', 30, user1, False)
task_repository.save(task1)

# task2 = Task('Make Dinner', 'Jim',30, False )


task2 = Task('Make Dinner', 'Jim', 30, user2, False)
task_repository.save(task2)

result = task_repository.select_all()
users = user_repository.select_all()

for task in result:
    print(task.__dict__)

pdb.set_trace()