import dataclasses
from enum import Enum

from models import Tasks


@dataclasses.dataclass(frozen=True)
class AllowedCommands(Enum):
    SHOW_TODAY_TASKS = "1"
    ADD_TASKS = "2"
    EDIT_TASKS = "3"
    STATS = "4"
    SHOW_TASKS_BY_DATE = "5"


def detect_command(user_answer: str) -> AllowedCommands | None:
    for command in AllowedCommands:
        if user_answer == command.value:
            return command
    return None


def print_hi_message() -> str:
    return input("Привет! Выбери команду: ").strip()


def print_hi_error_message() -> str:
    print("Ошибка ввода!")
    return print_hi_message()


def format_tasks(
        tasks: Tasks,
) -> str:  # in future add uncompleted task retriever for the current day
    message = f"%SEPARATOR%\n| Группа задач №{tasks.id}\n| Задачи на {tasks.for_what_date.to_string()}\n%SEPARATOR%"
    max_length = 0
    for t in tasks.tasks:
        part_1 = f"\n| №{t.id}: [{t.start_time.to_string()} - {t.finish_time.to_string()}] {t.name}\n"
        part_2 = f"| Описание: {t.description}\n"
        part_3 = f"| Статус выполнения: {t.is_completed}\n"
        max_l = max(max(len(part_1), len(part_2)), len(part_3))
        if max_length < max_l:
            max_length = max_l
        message += part_1 + part_2 + part_3 + "%SEPARATOR%"
    message = message.replace("%SEPARATOR%", "+" + (max_length - 1) * "-" + "+")

    new_message = ""
    for line in message.split("\n"):
        if line[-1] != "+":
            new_message = new_message + line + (max_length - len(line)) * " " + "|\n"
        else:
            new_message = new_message + line + "\n"
    return new_message


def print_today_tasks(message: str) -> str:
    return input(message)
