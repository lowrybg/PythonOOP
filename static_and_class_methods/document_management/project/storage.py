from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if any([x for x in self.categories if x.id == category.id]):
            return
        self.categories.append(category)

    def add_topic(self, topic: Topic):
        if any([x for x in self.topics if x.id == topic.id]):
            return
        self.topics.append(topic)

    def add_document(self, document: Document):
        if any([x for x in self.documents if x.id == document.id]):
            return
        self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for c in self.categories:
            if c.id == category_id:
                c.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for t in self.topics:
            if t.id == topic_id:
                return self.edit_topic(topic_id, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        for d in self.documents:
            if d.id == document_id:
                d.file_name = new_file_name

    def delete_category(self, category_id):
        for c in self.categories:
            if c.id == category_id:
                self.categories.remove(c)

    def delete_document(self, document_id):
        for d in self.documents:
            if d.id == document_id:
                self.documents.remove(d)

    def delete_topic(self, topic_id):
        for t in self.topics:
            if t.id == topic_id:
                self.topics.remove(t)

    def get_document(self, document_id):
        for d in self.documents:
            if d.id == document_id:
                return d

    def __repr__(self):
        return '\n'.join([str(d) for d in self.documents])