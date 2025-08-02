from playwright.sync_api import Page,expect
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_field = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_field = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_field = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')


    def fill_registration_form_email_field(self):
       self.email_field.fill('user.name_arto@gmail.com')

    def fill_registration_form_username_field(self):
       self.username_field.fill('username_arto')

    def fill_registration_form_password_field(self):
       self.password_field.fill('password123!')

    def click_registration_button(self):
        self.registration_button.click()

