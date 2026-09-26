import pytest
from task_manager import add_task


def test_add_task(initial_tasks):
    assert add_task(initial_tasks, "Walk the dog") == ["Buy groceries", "Read book", "Walk the dog"]


@pytest.mark.parametrize("tasks, new_task", [
    (["Go home"], ""),
    (["Go home"], 123),
    (["Go home"], None),
])
def test_add_task_failure(tasks, new_task):
    with pytest.raises(ValueError):
        add_task(tasks, new_task)