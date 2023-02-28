from run import app


class TestAPI:

    def test_app_all_posts_status_code(self):
        """Проверяем, получается ли нормальный список"""
        response = app.test_client().get('/api/posts', follow_redirects=True)

        print(response.status_code)
        print(response.mimetype)

        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        assert response.mimetype == "application/json", "Получен не JSON"

    def test_app_one_post_status_code(self):
        """Проверяем, получается ли нормальный список по одному посту"""
        response = app.test_client().get('/api/posts/1', follow_redirects=True)

        print(response.status_code)
        print(response.mimetype)

        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        assert response.mimetype == "application/json", "Получен не JSON"
