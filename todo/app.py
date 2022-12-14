import pandas as pd

from .constants import *
from .utils import *


class Todo:
    def __init__(self, active_csv, archive_csv) -> None:
        self.active_csv = f"data/{active_csv}"
        self.archive_csv = f"data/{archive_csv}"

    def add_task(self, name, category, note):
        with open(self.active_csv, "a") as f:
            f.write(f"{name},{category},{note}\n")
        with open(self.archive_csv, "a") as f:
            f.write(f"{name},{category},{note}\n")

    def show_tasks(self):
        print(pd.read_csv(self.active_csv, index_col="Task Name"))

    def delete_task(self, task_name):
        df = pd.read_csv(self.active_csv)
        df.drop(df[df["Task Name"] == task_name].index, inplace=True)
        df.to_csv(self.active_csv, index=False)
