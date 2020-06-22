import json
from typing import List

class JSONLogger:

    def __init__(self, target_json_filename: str, config_filename: str):
        ''' target_json_filename: target JSON file to add records to
        config_filename: file that specifies fields to be used
        keys: list of fields to use as JSON names (specify via config)
        '''

        self.target_json_filename: str = target_json_filename
        self.config_filename: str = config_filename

        self.keys: List[str] = []
        self.fields: dict = {}
        self.data: dict = {}

    def loadJSON(self) -> None:
        '''Load JSON and store as dict'''
        with open(self.target_json_filename) as json_file:
            data = json.load(json_file)


    def promptInput(self) -> None:
        # userinput: str = input("enter text")
        # while userin != "done":
        #     print("You just entered " + userin)
        #     userin = input("enter text")
        pass
