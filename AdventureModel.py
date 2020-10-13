from PySide2.QtGui import QStandardItemModel, QStandardItem
from pubsub import pub


class AdventureModel():
    def __init__(self, json_model):
        self.json_model = json_model

    def pages(self):
        return self.json_model["pages"]

    def add_page(self):
        page = {"label": "Unnamed", "area": "", "text": ""}
        self.json_model["pages"].append(page)
        return page

    def find_page(self, page_name):
        for page in self.json_model["pages"]:
            name = ""
            if page["area"]:
                name = page["area"] + ": " + page["label"]
            else:
                name = page["label"]
            if name == page_name:
                return page
        return None
