from playwright.sync_api import Page, expect
from dataclasses import dataclass

from components.coursepage.course_component import CreateCourseFormComponent
from components.courses.course_view_component import CourseViewComponent
from components.navigation.SidebarComponent import SidebarComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.create_course_form =CreateCourseFormComponent(self.page)
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.create_courses_button = self.page.get_by_test_id('create-course-button')


        self.empty_view = EmptyViewComponent(page, 'courses-list')
        self.course_view = CourseViewComponent(page)

        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_courses_button = page.get_by_test_id('courses-list-toolbar-create-course-button')


        self.course_menu_button = page.get_by_test_id('MoreVertIcon')
        self.course_edit_icon = page.get_by_test_id('course-view-edit-menu-item')
        self.course_edit_button = page.get_by_test_id('course-view-edit-menu-item-text')
        self.course_delete_icon = page.get_by_test_id('DeleteOutlineOutlinedIcon')
        self.course_delete_button = page.get_by_test_id('course-view-delete-menu-item-text')


    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )

    def check_visible_create_course_button(self):
        expect(self.create_courses_button).to_be_visible()

    def click_create_course_button(self):
        self.create_courses_button.click()


    def visible_edit_icon(self, index: int):
        expect(self.course_edit_icon.nth(index)).to_be_visible()

    def visible_delete_icon(self, index: int):
        expect(self.course_delete_icon.nth(index)).to_be_visible()