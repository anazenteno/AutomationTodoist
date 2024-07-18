from playwright.sync_api import Page


class Utilities:
    def __init__(self, page: Page):
        self.page = page

    def click_element(self, element, force=False):
        self.page.is_visible(element)
        self.page.locator(element).click(force=force)
        self.page.wait_for_load_state()

    def fill_input_element(self, element, text, force=False):
        if not force:
            self.page.is_visible(element)
            self.page.locator(element).click()
        self.page.locator(element).fill(text, force=force)

    def fill_on_frame(self, element_frame, element, text):
        self.page.frame_locator(element_frame).locator(element).fill(text)

    def get_text_element(self, element):
        return self.page.locator(element).inner_text()

    def click_and_select_option(self, element, option_element):
        self.click_element(element)
        self.click_element(option_element)