from PySide2.QtGui import QStandardItemModel, QStandardItem
from pubsub import pub


class AdventureModel():
    def __init__(self, json_model):
        self.json_model = json_model

        self.page_list = QStandardItemModel()
        for page in self.json_model["pages"]:
            item = QStandardItem(page["area"] + ": " + page["label"])
            self.page_list.appendRow(item)

        pub.subscribe(self.model_update_event, "model_updated")
        pub.subscribe(self.update_page_list, "page_search_event")

        self.area_search = ""
        self.label_search = ""
        self.text_search = ""

    def pages(self):
        return self.page_list

    def add_page(self):
        page = {"label": "Unnamed", "area": "", "text": ""}
        self.json_model["pages"].append(page)
        return page

    def lookup_page(self, index: int):
        return self.page_list.itemFromIndex(index)

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

    def update_page_list(self, arg1):
        self.area_search = arg1["area"]
        self.label_search = arg1["label"]
        self.text_search = arg1["text"]
        self.rebuild_page_list()

    def rebuild_page_list(self):
        self.page_list.clear()
        for page in self.json_model["pages"]:
            if (not self.area_search or self.area_search in page["area"]) \
                    and (not self.label_search or self.label_search in page["label"])\
                    and (not self.text_search or self.text_search in page["text"]):
                item = QStandardItem(page["area"] + ": " + page["label"])
                self.page_list.appendRow(item)

    def model_update_event(self):
        self.rebuild_page_list()
