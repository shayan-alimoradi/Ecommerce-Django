from django.test import TestCase

from shop_product.forms import (
    SearchForm,
    CommentForm,
    ReplyForm,
)


class TestSearchForm(TestCase):
    def test_valid_data(self):
        form = SearchForm(data={"search": "request"})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = SearchForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)


class TestCommentForm(TestCase):
    def test_valid_data(self):
        form = CommentForm(data={"comment": "comment"})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)


class ReplyCommentForm(TestCase):
    def test_valid_data(self):
        form = ReplyForm(data={"comment": "comment"})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = ReplyForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
