
def list_tasks(tasks):
    print(*tasks, sep='\n') if tasks else print('Nothing to list!')

def add_task(tasks, task):
    tasks.append(task)

def undo_task(tasks, undone_tasks):
    if not tasks:
        print('Nothing to undo!')
        return
    
    undone_task = tasks.pop()
    undone_tasks.append(undone_task)

def redo_task(tasks, undone_tasks):
    if not undone_tasks:
        print('Nothing to redo!')
        return
    
    last_undone_task = undone_tasks.pop()
    tasks.append(last_undone_task)

tasks = []
undone_tasks = []
commands = ['list', 'undo', 'redo']

while True:
    print()
    print('commands: list, undo, redo')
    _input = input('input a task or command: ')

    if _input not in commands:
        add_task(tasks, _input)
    elif _input == 'list':
        list_tasks(tasks)
    elif _input == 'undo':
        undo_task(tasks, undone_tasks)
    elif _input == 'redo':
        redo_task(tasks, undone_tasks)