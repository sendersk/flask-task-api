from models import Task
from storage import add_task, get_all_tasks, update_task, delete_task

# Valid task
t1 = Task(id=1, title="Buy milk", description="Go to store", status="todo")
print(t1.to_dict())

# Invalid task (status)
try:
    Task(id=2, title="Invalid", description="Wrong status", status="pending")
except ValueError as e:
    print("Error:", e)

# Create task
t2 = add_task("Buy milk", "Go to the store")
print("Added:", t1.to_dict())

# Update task
t1_updated = update_task(1, {"status": "in_progress"})
print("Updated:", t1_updated.to_dict())

# Get all tasks
print("All tasks:", [t.to_dict() for t in get_all_tasks()])

# Delete task
delete_task(1)
print("Remaining:", [t.to_dict() for t in get_all_tasks()])