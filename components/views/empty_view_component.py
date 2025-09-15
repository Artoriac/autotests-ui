from components.base_component import BaseComponent

from  playwright.sync_api import Page, expect

class EmptyViewComponent(BaseComponent, ):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = page.get_by_test_id(f'{identifier}-icon')
        self.title = page.get_by_test_id('{identifier}-title-text')
        self.description = page.get_by_test_id('{identifier}-description-text')

    def check_visible(self, title: str, desription: str):
        expect(self.icon).to_be_visible()

        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

        expect(self.description).to_be_visible()
        expect(self.description).to_have_text(desription)