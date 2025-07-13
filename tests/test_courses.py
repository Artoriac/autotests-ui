from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_field = page.get_by_test_id('registration-form-email-input').locator('input')
        email_field.fill('user.name_arto@gmail.com')

        username_field = page.get_by_test_id('registration-form-username-input').locator('input')
        username_field.fill('username_arto')

        password_field = page.get_by_test_id('registration-form-password-input').locator('input')
        password_field.fill('password123!')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path='browser-state-for-courses.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state-for-courses.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_header = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_header).to_have_text('Courses')

        file_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(file_icon).to_be_visible()

        title_no_result = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(title_no_result).to_have_text('There is no results')

        block_no_result = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(block_no_result).to_have_text('Results from the load test pipeline will be displayed here')