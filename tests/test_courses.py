from playwright.sync_api import sync_playwright, expect, Page
import  pytest

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_header = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_header).to_have_text('Courses')

    file_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(file_icon).to_be_visible()

    title_no_result = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(title_no_result).to_have_text('There is no results')

    block_no_result = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(block_no_result).to_have_text('Results from the load test pipeline will be displayed here')