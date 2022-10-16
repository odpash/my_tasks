import json
from pathlib import Path

from models import *


def read_tasks_by_id(tasks_id: int) -> Tasks | None:
    data = _read_from_file(tasks_id)
    if not data:
        return None
    tasks = _parse_data_from_file(data)
    return tasks


def write_tasks_update(tasks: Tasks):
    pass


def write_new_tasks(tasks: Tasks):
    pass


def load_storage_preview() -> StoragePreview:
    index = 0
    data = []
    while True:
        index += 1
        task = read_tasks_by_id(index)
        if task:
            data.append(
                FileObj(
                    id=task.id, filename=f"{index}.json", created_for=task.for_what_date
                )
            )
        else:
            break
    return StoragePreview(data)


def _read_from_file(tasks_id: int) -> str | None:
    file_path = (
        f"/Users/olegpash/Developer/october2022/my_tasks/storage/{tasks_id}.json"
    )
    if Path(file_path).is_file():
        file = open(file=file_path, mode="r", encoding="UTF-8")
        data = file.read()
        file.close()
        return data
    return None


def _parse_data_from_file(data: str) -> Tasks:
    try:
        js_data = json.loads(data)
        tasks_list = []
        for js_task in js_data["tasks"]:
            tasks_list.append(
                Task(
                    id=js_task["id"],
                    name=js_task["name"],
                    description=js_task["description"],
                    start_time=TimeFormat(
                        hours=int(js_task["start_time"].split(TimeFormat.separator)[0]),
                        minutes=int(
                            js_task["start_time"].split(TimeFormat.separator)[1]
                        ),
                    ),
                    finish_time=TimeFormat(
                        hours=int(
                            js_task["finish_time"].split(TimeFormat.separator)[0]
                        ),
                        minutes=int(
                            js_task["finish_time"].split(TimeFormat.separator)[1]
                        ),
                    ),
                    is_completed=js_task["is_completed"],
                    creation_date=DateFormat(
                        day=int(
                            js_task["creation_date"].split(DateFormat.separator)[0]
                        ),
                        month=int(
                            js_task["creation_date"].split(DateFormat.separator)[1]
                        ),
                        year=int(
                            js_task["creation_date"].split(DateFormat.separator)[2]
                        ),
                    ),
                )
            )
        return Tasks(
            id=js_data["id"],
            tasks=tasks_list,
            for_what_date=DateFormat(
                day=int(js_data["for_what_date"].split(DateFormat.separator)[0]),
                month=int(js_data["for_what_date"].split(DateFormat.separator)[1]),
                year=int(js_data["for_what_date"].split(DateFormat.separator)[2]),
            ),
        )
    except Exception:
        print("err")


def _convert_to_json():
    pass


def _update_storage_file():
    pass


if __name__ == "__main__":
    print(read_tasks_by_id(1))
