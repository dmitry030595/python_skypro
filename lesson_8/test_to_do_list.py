from to_do_list import ToDoList

base_url = 'https://todo-app-sky.herokuapp.com/'

tasks = ToDoList(base_url)
title_task = 'my_little_task'
title2_task = 'my_big_task'


def test_to_do_list():
    # создание задачи
    my_task = tasks.add_task(title_task)
    task_id = my_task.json()['id']

    # проверяем, что задача в списке
    id_list = []
    for i in tasks.get_list_of_tasks().json():
        id_list.append(i['id'])
    assert task_id in id_list, 'task not in to-do list'

    # переименовываем задачу
    tasks.change_title_task(task_id, title2_task)

    # проверка, что задача переименована
    rename_task = tasks.get_task(task_id)
    assert rename_task.json()['title'] == title2_task

    # отмечаем задачу выполненной
    tasks.task_completed(task_id)

    # проверяем, что задача выполнена
    tasks.task_completed(task_id)
    assert tasks.get_task(task_id).json()['completed'] is True

    # снимаем отметку о выполнении задачи
    tasks.task_uncompleted(task_id)

    # проверяем, что задача не выполнена
    assert tasks.get_task(task_id).json()['completed'] is False

    # удаляем задачу
    tasks.delete_task(task_id)

    # проверяем, что задачи нет в списке
    id_list = []
    for i in tasks.get_list_of_tasks().json():
        id_list.append(i['id'])
    assert task_id not in id_list, 'task in to-do list'
