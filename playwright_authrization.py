from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    chrome = playwright.chromium.launch(headless=False)
    page = chrome.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.get_by_test_id('login-form-email-input').locator("input")
    email_input.fill('arty_user@gmail.com')

    password_input = page.get_by_test_id('login-form-password-input').locator("input")
    password_input.fill('QWE123qwe')

    login_button = page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_pawword_alert = page.get_by_test_id('ErrorOutlineIcon')
    expect(wrong_email_or_pawword_alert).to_be_visible()
    expect(wrong_email_or_pawword_alert).to_have_text('Wrong email 2 password')
    page.wait_for_timeout(5000)