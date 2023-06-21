from main import BooksCollector

import pytest

class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    def test_set_book_rating_add_rating(self):

        collector = BooksCollector()
        collector.add_new_book('Черный обелиск')
        collector.set_book_rating('Черный обелиск', 5)

        assert collector.get_book_rating('Черный обелиск') == 5, 'Рейтинг не соответствует ожидаемому'

    @pytest.mark.parametrize('rating', [11, 0])
    def test_set_book_rating_add_rating_over_10_and_less_1(self,rating):

        collector = BooksCollector()
        collector.add_new_book('Тихий Дон')
        collector.set_book_rating('Тихий Дон', rating)

        assert collector.get_book_rating('Тихий Дон') == 1

    def test_get_book_rating_not_book_not_rating(self):
            collector = BooksCollector()
            collector.set_book_rating('Евгений Онегин', 2)

            assert collector.get_book_rating('Евгений Онегин') == None

    def test_get_books_with_specific_rating(self):
            collector = BooksCollector()
            collector.add_new_book('Бесы')
            collector.add_new_book('Братья Карамазовы')
            collector.add_new_book('Мы')
            collector.set_book_rating('Бесы', 8)
            collector.set_book_rating('Братья Карамазовы', 8)
            collector.set_book_rating('Мы', 9)

            assert collector.get_books_with_specific_rating(8) == ['Бесы','Братья Карамазовы']

    def test_add_book_in_favorites(self):
            collector = BooksCollector()
            collector.add_new_book('Цветы для Элджернона')
            collector.add_book_in_favorites('Цветы для Элджернона')

            assert collector.get_list_of_favorites_books() == ['Цветы для Элджернона']

    def test_add_book_in_favorites_identical_books(self):
            collector = BooksCollector()
            collector.add_new_book('Цветы для Элджернона')
            collector.add_new_book('Цветы для Элджернона')
            collector.add_book_in_favorites('Цветы для Элджернона')

            assert collector.get_list_of_favorites_books() != ['Цветы для Элджернона','Цветы для Элджернона']

    def test_delete_book_from_favorites(self):
            collector = BooksCollector()
            collector.add_new_book('Цветы для Элджернона')
            collector.add_book_in_favorites('Цветы для Элджернона')
            collector.delete_book_from_favorites('Цветы для Элджернона')

            assert collector.get_list_of_favorites_books() == []