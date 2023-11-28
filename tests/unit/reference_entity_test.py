""" tests/unit/reference_entity_test.py """

import unittest

from viiteri.entities.references import Article, Book, Inproceeding


class TestReferenceEntity(unittest.TestCase):
    """ Test class for Reference - entities """

    def setUp(self):
        self.test_article = Article(cite_key="petpet", author="Petteri",
                                    title="Petterin Kirja",
                                    journal="Petterin Kirjakokoelma", year="2003", volume="1")
        self.test_book = Book(cite_key="petkir", author="Petteri",
                              editor="Petteri", title="Petterin Kirja vol 2",
                              publisher="WSOY", year="2004")
        self.test_inproceeding = Inproceeding(cite_key="johinp", author="John Doe",
                                              title="An Analysis of Example",
                                              booktitle="Sample Text",
                                              year="2002", editor="Ex Ample")

    def test_article_constructor(self):
        """ Test that Article entity is correctly instantiated """
        # Test that abstract fields are set
        self.assertEqual(self.test_article.type, "article")
        self.assertEqual(self.test_article.cite_key, "petpet")

        # Test that required fields are set
        self.assertEqual(self.test_article.author, "Petteri")
        self.assertEqual(self.test_article.title, "Petterin Kirja")
        self.assertEqual(self.test_article.journal, "Petterin Kirjakokoelma")
        self.assertEqual(self.test_article.year, "2003")

        # Test that optional fields are set
        self.assertEqual(self.test_article.volume, "1")

    def test_book_constructor(self):
        """ Test that Book-entity is correctly instantiated """
        # Test that abstract fields are set
        self.assertEqual(self.test_book.type, "book")
        self.assertEqual(self.test_book.cite_key, "petkir")

        # Test that required fields are set
        self.assertEqual(self.test_book.author, "Petteri")
        self.assertEqual(self.test_book.editor, "Petteri")
        self.assertEqual(self.test_book.title, "Petterin Kirja vol 2")
        self.assertEqual(self.test_book.publisher, "WSOY")
        self.assertEqual(self.test_book.year, "2004")

    def test_inproceeding_constructor(self):
        """ Test that Inproceeding-entity is correctly instantiated """
        # Test that abstract fields are set
        self.assertEqual(self.test_inproceeding.type, "inproceeding")
        self.assertEqual(self.test_inproceeding.cite_key, "johinp")

        # Test that required fields are set
        self.assertEqual(self.test_inproceeding.author, "John Doe")
        self.assertEqual(self.test_inproceeding.title,
                         "An Analysis of Example")
        self.assertEqual(self.test_inproceeding.booktitle, "Sample Text")
        self.assertEqual(self.test_inproceeding.year, "2002")

        # Test that optional fields are set
        self.assertEqual(self.test_inproceeding.editor, "Ex Ample")

    def test_init_article_with_missing_required_arguments(self):
        """ Test that Article entity raises ValueError with invalid arguments """

        with self.assertRaises(ValueError):
            Article(cite_key="petpet", author="Petteri",
                    title="Petterin Kirja", journal="Petterin Kirjakokoelma")

    def test_init_book_with_missing_required_arguments(self):
        """ Test that Book-entity raises ValueError with invalid arguments """

        with self.assertRaises(ValueError):
            Book(cite_key="petkir", author="Petteri",
                 editor="Petteri", publisher="WSOY",
                 year="2004")

    def test_init_inproceeding_with_missing_required_arguments(self):
        """ Test that Inproceeding-entity raises ValueError with invalid arguments  """

        with self.assertRaises(ValueError):
            Inproceeding(cite_key="johinp", author="John Doe",
                         title="An Analysis of Example", booktitle="Sample Text",
                         editor="Ex Ample")

    def test_article_str_method(self):
        """ Test that Article entitys str method returns correct string """
        article_str = str(self.test_article)
        self.assertEqual(article_str, ("{'_type': 'article', "
                                       "'_cite_key': 'petpet', "
                                       "'author': 'Petteri', "
                                       "'title': 'Petterin Kirja', "
                                       "'journal': 'Petterin Kirjakokoelma', "
                                       "'year': '2003', "
                                       "'volume': '1', "
                                       "'number': None, "
                                       "'pages': None, "
                                       "'month': None, "
                                       "'doi': None, "
                                       "'note': None, "
                                       "'issn': None, "
                                       "'zblnumber': None, "
                                       "'eprint': None}"))

    def test_book_str_method(self):
        """ Test that Book entitys str method returns correct string """
        book_str = str(self.test_book)
        self.assertEqual(book_str, ("{'_type': 'book', "
                                    "'_cite_key': 'petkir', "
                                    "'author': 'Petteri', "
                                    "'editor': 'Petteri', "
                                    "'title': 'Petterin Kirja vol 2', "
                                    "'publisher': 'WSOY', "
                                    "'year': '2004', "
                                    "'number': None, "
                                    "'volume': None, "
                                    "'pages': None, "
                                    "'month': None, "
                                    "'note': None, "
                                    "'doi': None, "
                                    "'issn': None, "
                                    "'isbn': None}"))

    def test_inproceeding_str_method(self):
        """ Test that Inproceeding entitys str method returns correct string """
        inproceeding_str = str(self.test_inproceeding)
        self.assertEqual(inproceeding_str, ("{'_type': 'inproceeding', "
                                            "'_cite_key': 'johinp', "
                                            "'author': 'John Doe', "
                                            "'title': 'An Analysis of Example', "
                                            "'booktitle': 'Sample Text', "
                                            "'year': '2002', "
                                            "'editor': 'Ex Ample', "
                                            "'volume': None, "
                                            "'number': None, "
                                            "'series': None, "
                                            "'pages': None, "
                                            "'month': None, "
                                            "'address': None, "
                                            "'organization': None, "
                                            "'publisher': None, "
                                            "'note': None, "
                                            "'annote': None}"))
