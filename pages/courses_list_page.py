from playwright.sync_api import Page, expect

from components.coursepage.course_component import CreateCourseFormComponent
from components.courses.course_view_component import CourseViewComponent
from components.navigation.SidebarComponent import SidebarComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.courses_list_toolbar_view_component import CourseListToolbarViewComponent
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.page = page
        self.create_course_form = CreateCourseFormComponent(self.page)
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.create_courses_button = self.page.get_by_test_id('create-course-button')

        self.toolbar_view = CourseListToolbarViewComponent(page)

        self.empty_view = EmptyViewComponent(page, 'courses-list')
        self.course_view = CourseViewComponent(page)

        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_courses_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

        #self.course_menu_button = page.get_by_test_id('MoreVertIcon')
        self.course_edit_icon = page.get_by_test_id('course-view-edit-menu-item') #Под вопросом. Возможно это не нужно (уже используется в course_view_component)
        self.course_edit_button = page.get_by_test_id('course-view-edit-menu-item-text')
        self.course_delete_icon = page.get_by_test_id('DeleteOutlineOutlinedIcon')
        self.course_delete_button = page.get_by_test_id('course-view-delete-menu-item-text') #Под вопросом. Возможно это не нужно


    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no courses',
            description='Click on "Create course" button to create new course'
        )

    def visible_edit_icon(self, index: int):
        expect(self.course_edit_icon.nth(index)).to_be_visible()

    def visible_delete_icon(self, index: int):
        expect(self.course_delete_icon.nth(index)).to_be_visible()