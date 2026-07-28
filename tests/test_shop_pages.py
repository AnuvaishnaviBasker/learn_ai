import pytest
from playwright.sync_api import Page

from src.page_objects.about_page import AboutPage
from src.page_objects.blog_page import BlogPage
from src.page_objects.cart_page import CartPage
from src.page_objects.catalog_page import CatalogPage
from src.page_objects.home_page import HomePage
from src.page_objects.login_page import LoginPage
from src.page_objects.register_page import RegisterPage
from src.page_objects.search_page import SearchPage


@pytest.mark.parametrize(
    'page_object_cls, path, expected_text',
    [
        (HomePage, '/', 'Just a demo site showing off what Sauce can do.'),
        (CatalogPage, '/collections/all', 'Products'),
        (AboutPage, '/pages/about-us', 'About Us'),
        (BlogPage, '/blogs/news', 'First Post'),
        (SearchPage, '/search', 'Search Results'),
        (LoginPage, '/account/login', 'Customer Login'),
        (RegisterPage, '/account/register', 'Create account'),
        (CartPage, '/cart', 'My Cart'),
    ],
)
def test_shop_pages_load(page: Page, page_object_cls, path: str, expected_text: str):
    page_object = page_object_cls(page)
    page_object.open(path)
    page_object.expect_text(expected_text)
