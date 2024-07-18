import time
from playwright.sync_api import Page

from configure.global_variables import TASK_NAME
from page_object.utilities import Utilities


class TaskPage:
    # Locator general
    cancel_btn = "//button[@class='fb8d74bb _56a651f6 _3930afa0 _64ee8afd _7246d092']"
    # Locator for create a task
    add_task_btn = "//button[contains(@class,'button')]"
    name_task_input = "//p[contains(@data-placeholder,'Nombre de la tarea')]"
    description_task_input = "//p[contains(@data-placeholder,'Descripción')]"
    create_task_btn = "//button[@class='fb8d74bb _56a651f6 _3930afa0 _7ea1378e _7246d092']"
    # Locator for update a tasks
    more_action_btn = "//div[contains(text(), '{}')]//ancestor::li//descendant::button[contains(@aria-label,'Más acciones de tarea')]"
    more_action_btn_over = "//div[contains(text(), '{}')]//ancestor::li"
    edit_btn = "//div[@class='a83bd4e0 a8d37c6e _2f303ac3 fb8d74bb _211eebc7'][contains(.,'Editar')]"
    edit_name_task_input = "//p[contains(.,'{}')]"
    save_btn = "//button[@data-testid='task-editor-submit-button']"
    # Locator for delete a tasks
    delete_btn = "//div[@class='a83bd4e0 a8d37c6e _2f303ac3 fb8d74bb _211eebc7'][contains(.,'Eliminar')]"
    delete_confirm_btn = "//button[@class='fb8d74bb _56a651f6 _3930afa0 _7ea1378e _7246d092']"

    task_list = '//li[contains(@id,"task")]//div[contains(@class,"task_content")]'

    def __init__(self, page: Page):
        self.page = page
        self.utilities = Utilities(page)

    def click_in_add_task(self):
        """
        This method clicks the button to add a task.
        """
        self.utilities.click_element(self.add_task_btn)

    def set_text_task_name_input(self, text):
        """
        This method sets the text in the text input field of the task
        :param text:        The name of the task to enter.
        """
        self.utilities.fill_input_element(self.name_task_input, text)

    def set_text_description_task_input(self, text):
        """
        This method sets the text in the text input field of the task
        :param text:        The description of the task to enter.
        """
        self.utilities.fill_input_element(self.description_task_input, text)

    def click_in_add_tasks_btn(self):
        """
        This method clicks the button to create a task.
        """
        self.utilities.click_element(self.create_task_btn)

    def click_more_action_btn(self):
        """
        This method clicks the button more action of a task.
        """
        self.page.hover(self.more_action_btn_over.format(TASK_NAME))
        time.sleep(2)
        self.utilities.click_element(self.more_action_btn.format(TASK_NAME))

    def click_edit_task_btn(self):
        """
        This method clicks the button to edit a task.
        :return:
        """
        self.utilities.click_element(self.edit_btn)

    def set_text_task_name_edit_input(self, text):
        """
        This method sets when new name task
        :param text:
        """
        self.utilities.fill_input_element(self.edit_name_task_input.format(TASK_NAME), text)

    def click_save_btn(self):
        """
        This method do click save button.
        """
        self.utilities.click_element(self.save_btn)

    def click_delete_btn(self):
        """
        This method clicks the button to delete a task.
        :return:
        """
        self.utilities.click_element(self.delete_btn)

    def click_delete_confirm_btn(self):
        """
        This method clicks in the button to delete for confirm that is deleted a task.
        :return:
        """
        self.utilities.click_element(self.delete_confirm_btn)

    def obtain_last_element_task(self):
        """
        This method obtains the last element created of the task.
        :return:    The last element created of the task.
        """
        elements = self.page.locator(self.task_list)
        last_element = elements.nth(elements.count() - 1)
        return last_element.inner_text()

    def click_for_cancel_btn(self):
        self.utilities.click_element(self.cancel_btn)
