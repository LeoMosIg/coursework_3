import json


class CommentsDAO:

    def __init__(self, path):
        self.path = path

    def load_comments(self):
        """Просто загружает комментарии"""
        with open(self.path, 'r', encoding="UTF-8") as file:
            data = json.load(file)
        return data

    def get_by_post_pk(self, post_pk):
        """Получаем комментарии к определённому посту"""
        comments = self.load_comments()
        comments_by_pk = []
        for comment in comments:
            if comment["post_pk"] == post_pk:
                comments_by_pk.append(comment)
        return comments_by_pk
