from dataclasses import dataclass


def format_time_value(v: int) -> str:
    if len(str(v)) == 1:
        return "0" + str(v)
    else:
        return str(v)


@dataclass(frozen=True)
class TimeFormat:
    separator = ":"
    hours: int
    minutes: int

    def to_string(self) -> str:
        return f"{format_time_value(self.hours)}{self.separator}{format_time_value(self.minutes)}"


@dataclass(frozen=True)
class DateFormat:
    separator = "."
    day: int
    month: int
    year: int

    def to_string(self) -> str:
        return (
            f"{format_time_value(self.day)}{self.separator}"
            f"{format_time_value(self.month)}{self.separator}{self.year}"
        )


@dataclass(frozen=True)
class FileObj:
    id: int
    filename: str
    created_for: DateFormat


@dataclass(frozen=True)
class StoragePreview:
    files: list[FileObj]


@dataclass(frozen=True)
class Task:
    id: int
    name: str
    description: str
    start_time: TimeFormat
    finish_time: TimeFormat
    is_completed: bool
    creation_date: DateFormat


@dataclass(frozen=True)
class Tasks:
    id: int
    tasks: list[Task]
    for_what_date: DateFormat
