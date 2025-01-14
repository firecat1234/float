# manages long term and short term memories

class TaskService:

    def __init__(self):
      # placeholder for scheduled task set up
      self.tasks = []

    def add_task(self, task):
        # schedule a new task in async queue
        # check if all prereq tasks have completed before adding.
      print(f"Scheduling a new task: {task}")
      self.tasks.append(task)

    def retrieve_task(self, task_id):
      # retrieve an existing task in the queue
      # may need to implement search, or task ids.
      print(f"retrieving task {task_id}")

    def complete_task(self, task_id):
      # remove task from queue, store results.
      print(f"task {task_id} has been completed.")
    
    def list_tasks(self):
      # return all pending tasks.
        return self.tasks

    def add_task(self, task, prerequisites=None):
        if prerequisites and not all(p in self.tasks for p in prerequisites):
            print(f"Cannot schedule {task}. Missing prerequisites: {prerequisites}")
            return
        self.tasks.append({"task": task, "prerequisites": prerequisites or []})
        print(f"Task scheduled: {task}")
