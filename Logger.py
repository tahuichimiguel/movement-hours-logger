import json
import pandas as pd
from typing import List

class Logger:

    def __init__(self):
        self.data = pd.DataFrame()
        self.newentries: List[dict] = []
        self.keys: List[str] = []

    def loadJSONData(self, path: str) -> None:
        data = pd.read_json(path)

    def loadCSVData(self, path: str) -> None:
        data = pd.read_csv(path)

    #do i need this?
    def setKeys(self, keyvals: List[str] = []) -> None:
        if len(keyvals) != 0:
            self.keys = keyvals
        else:
            self.keys = list(self.data.columns)

    # keys = ['facility', 'class_type', 'city',
    #         'state', 'class_title', 'instructors',
    #         'date', 'start_time', 'end_time']
    def promptEntry(self) -> None:
        entry = {}
        for key in self.keys:
            entry[key] = input(key + ": ")

        for key in self.data:
            self.data[key] = self.data[key].append(entry[key])

    def write2csv(self, output_path):
        self.data.to_csv(output_path, index=False)


