import datetime
from tasks_storage import DateFormat, load_storage_preview, read_tasks_by_id
from printer import format_tasks, print_today_tasks


def today():
    dt = datetime.datetime.today()
    current_date = DateFormat(day=dt.day, month=dt.month, year=dt.year)
    storage_preview = load_storage_preview()
    is_founded = False
    tasks_id = None
    for preview in storage_preview.files:
        if preview.created_for == current_date:
            is_founded = True
            tasks_id = preview.id

    if is_founded:
        tasks = read_tasks_by_id(tasks_id)
        formatted_tasks = format_tasks(tasks)
        user_command = print_today_tasks(formatted_tasks)  # TODO: здесь закончил
        input("Хароош пока хватит на этом")
    else:
        print("Заглушка тасков не найдено")


def by_date():
    pass