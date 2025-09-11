from re import Pattern

from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = page.get_by_test_id(f"{identifier}-drawer-list-item-icon")
        self.title = page.get_by_test_id(f"{identifier}-drawer-list-item-title-text")
        self.button = page.get_by_test_id(f"{identifier}-drawer-list-item-button")
        self.users_list_item = page.get_by_test_id('users-list-item')
        self.courses_list_item = page.get_by_test_id('courses-list-item')
        self.accounts_list_item = page.get_by_test_id('accounts-list-item')

    def check_visible(self, title: str):
        expect(self.icon).to_be_visible()

        expect(self.title).to_be_visible(title)
        expect(self.title).to_have_text(title)

        expect(self.button).to_be_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)


    def navigate_to_users_page(self):
        self.users_list_item.click()

    def navigate_to_courses_page(self):
        self.courses_list_item.click()

    def navigate_to_accounts_page(self):
        self.accounts_list_item.click()
