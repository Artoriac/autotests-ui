from playwright.sync_api import Page, expect
from dataclasses import dataclass

from components.coursepage.course_component import CreateCourseFormComponent
from components.navigation.SidebarComponent import SidebarComponent
from components.navigation.navbar_component import NavbarComponent
from pages.base_page import BasePage

@dataclass
class CheckVisibleCoursesParams:
    index: int
    title: str
    max_score: str
    min_score: str
    estimated_time: str

class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.create_course_form =CreateCourseFormComponent(self.page)
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.create_courses_button = self.page.get_by_test_id('create-course-button')


        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_courses_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

        self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')

        self.course_title = page.get_by_test_id('course-widget-title-text')
        self.course_image = page.get_by_test_id('course-preview-image')
        self.course_max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.course_min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.course_estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')

        self.course_menu_button = page.get_by_test_id('MoreVertIcon')
        self.course_edit_icon = page.get_by_test_id('course-view-edit-menu-item')
        self.course_edit_button = page.get_by_test_id('course-view-edit-menu-item-text')
        self.course_delete_icon = page.get_by_test_id('DeleteOutlineOutlinedIcon')
        self.course_delete_button = page.get_by_test_id('course-view-delete-menu-item-text')


    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_empty_view(self):
        expect(self.empty_view_icon).to_be_visible()

        expect(self.empty_view_title).to_be_visible()
        expect(self.empty_view_title).to_have_text('There is no results')

        expect(self.empty_view_description).to_be_visible()
        expect(self.empty_view_description).to_have_text(
            'Results from the load test pipeline will be displayed here'
        )

    def check_visible_create_course_button(self):
        expect(self.create_courses_button).to_be_visible()

    def click_create_course_button(self):
        self.create_courses_button.click()

    def check_visible_course_card(self, params: CheckVisibleCoursesParams):
        expect(self.course_image.nth(params.index)).to_be_visible()

        expect(self.course_title.nth(params.index)).to_be_visible()
        expect(self.course_title.nth(params.index)).to_have_text(params.title)

        expect(self.course_max_score_text.nth(params.index)).to_be_visible()
        expect(self.course_max_score_text.nth(params.index)).to_have_text(
            f'Max score: {params.max_score}'
        )

        expect(self.course_min_score_text.nth(params.index)).to_be_visible()
        expect(self.course_min_score_text.nth(params.index)).to_have_text(
            f'Min score: {params.min_score}'
        )

        expect(self.course_estimated_time_text.nth(params.index)).to_be_visible()
        expect(self.course_estimated_time_text.nth(params.index)).to_have_text(
            f'Estimated time: {params.estimated_time}'
        )

    def visible_edit_icon(self, index: int):
        expect(self.course_edit_icon.nth(index)).to_be_visible()

    def visible_delete_icon(self, index: int):
        expect(self.course_delete_icon.nth(index)).to_be_visible()

    def click_edit_course(self, index:int):
        self.course_edit_button.nth(index).click()

        expect(self.course_edit_icon.nth(index)).to_be_visible()
        expect(self.course_edit_button.nth(index)).to_have_text('Edit')
        self.course_edit_button.nth(index).click()

    def click_delete_course(self, index: int):
        self.course_edit_button.nth(index).click()

        expect(self.course_delete_icon.nth(index)).to_be_visible()
        expect(self.course_delete_button.nth(index)).to_have_text('Delete')
        self.course_delete_button.nth(index).click()