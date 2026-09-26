def add_task(tasks: list[str], new_task: str) -> list[str]:
    if not isinstance(new_task, str) or not new_task:
        raise ValueError
    tasks.append(new_task)
    return tasks
