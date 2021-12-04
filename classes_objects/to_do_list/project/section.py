from project.task import Task


class Section:
    def __init__(self, name):
        self.completed = False
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for t in self.tasks:
            if new_task == t:
                return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.name} is added to the section"

    def complete_task(self, task_name):

        for t in self.tasks:
            if not task_name == t:
                return f"Could not find task with the name {task_name}"
        self.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        return f"Cleared {len(self.tasks[self.completed])} tasks."

    def view_section(self):
        return f"Section {self.name}:\n {[x for x in self.tasks]}"


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())