from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test

class TestBooksCollector:
#Тест на добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    import pytest
# Тест проверяет, что можно добавить книге любой рейтинг  от 1 до 10ти
    @pytest.mark.parametrize('rating', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_set_book_rating_add_rating(self,rating):

        collector = BooksCollector()
        collector.add_new_book('Черный обелиск')
        collector.set_book_rating('Черный обелиск', rating)

        assert collector.get_book_rating('Черный обелиск') == rating

# Тест проверяет, что нельзя установить рейтинг выше 10
    def test_set_book_rating_add_rating_over_10(self):

        collector = BooksCollector()
        collector.add_new_book('Тихий Дон')
        collector.set_book_rating('Тихий Дон', 11)

        assert collector.get_book_rating('Тихий Дон') == 1

# Тест проверяет, что нельзя установить рейтинг ниже 1
    def test_set_book_rating_add_rating_less_1(self):
            collector = BooksCollector()
            collector.add_new_book('Евгений Онегин')
            collector.set_book_rating('Евгений Онегин', 0)

            assert collector.get_book_rating('Евгений Онегин') == 1

 # Тест проверяет, что у не добавленной книги нет рейтинга
    def test_get_book_rating_not_book_not_rating(self):
            collector = BooksCollector()
            collector.set_book_rating('Евгений Онегин', 2)

            assert collector.get_book_rating('Евгений Онегин') == None

#Тест проверяет вывод всех книг с одинаковым рейтингом
    def test_get_books_with_specific_rating(self):
            collector = BooksCollector()
            collector.add_new_book('Бесы')
            collector.add_new_book('Братья Карамазовы')
            collector.add_new_book('Мы')
            collector.set_book_rating('Бесы', 8)
            collector.set_book_rating('Братья Карамазовы', 8)
            collector.set_book_rating('Мы', 9)

            assert collector.get_books_with_specific_rating(8) == ['Бесы','Братья Карамазовы']

#Тест на проверку добавления книги в избранное
    def test_add_book_in_favorites(self):
            collector = BooksCollector()
            collector.add_new_book('Цветы для Элджернона')
            collector.add_book_in_favorites('Цветы для Элджернона')

            assert collector.get_list_of_favorites_books() == ['Цветы для Элджернона']

# Тест на проверку добавления одной и той же книги в избранное
    def test_add_book_in_favorites_identical_books(self):
            collector = BooksCollector()
            collector.add_new_book('Цветы для Элджернона')
            collector.add_new_book('Цветы для Элджернона')
            collector.add_book_in_favorites('Цветы для Элджернона')

            assert collector.get_list_of_favorites_books() != ['Цветы для Элджернона','Цветы для Элджернона']

# Тест на проверку удаления книги из избранного
    def test_delete_book_from_favorites(self):
            collector = BooksCollector()
            collector.add_new_book('Цветы для Элджернона')
            collector.add_book_in_favorites('Цветы для Элджернона')
            collector.delete_book_from_favorites('Цветы для Элджернона')

            assert collector.get_list_of_favorites_books() == []