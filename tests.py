from models import Task

# Valid task
t1 = Task(id=1, title="Buy milk", description="Go to store", status="todo")
print(t1.to_dict())

# Invalid task (status)
try:
    Task(id=2, title="Invalid", description="Wrong status", status="pending")
except ValueError as e:
    print("Error:", e)