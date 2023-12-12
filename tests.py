import pytest

from main import BooksCollector
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_more_than_40symbols(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка на лунеНезнайка на лунеНезнайка ')

        assert collector.books_genre == {}
    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Незнайка на луне','Мультфильмы'],
            ['Кошмар на улице вязов', 'Ужасы']
        ]
    )
    def test_set_book_genre_correct_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка на луне')
        collector.set_book_genre('Незнайка на луне', 'Мультфильмы')

        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Незнайка на луне']

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка на луне')

        assert collector.get_books_genre() == {'Незнайка на луне': ''}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка на луне')
        collector.set_book_genre('Незнайка на луне', 'Мультфильмы')

        collector.add_new_book('Кошмар на улице вязов')
        collector.set_book_genre('Кошмар на улице вязов', 'Ужасы')

        assert collector.get_books_for_children() == ['Незнайка на луне']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка на луне')
        collector.add_book_in_favorites('Незнайка на луне')

        assert collector.favorites == ['Незнайка на луне']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка на луне')
        collector.delete_book_from_favorites('Незнайка на луне')

        assert collector.favorites == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка на луне')
        collector.add_book_in_favorites('Незнайка на луне')

        assert collector.get_list_of_favorites_books() == ['Незнайка на луне']

