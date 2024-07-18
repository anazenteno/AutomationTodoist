from playwright.sync_api import sync_playwright

from configure.global_variables import ENVIRONMENT, TASK_NAME
from page_object.login_page import LoginPage
from page_object.task_page import TaskPage


def before_all(context):
    context.playwright = sync_playwright().start()
    browser = context.playwright.chromium.launch(headless=False, args=['--start-maximized'])
    context.browser = browser.new_context(no_viewport=True)
    context.page = context.browser.new_page()


def before_feature(context, feature):
    context.env = 'Todoist'
    username = ENVIRONMENT["QA"]['Todoist']['account']['username']
    password = ENVIRONMENT["QA"]['Todoist']['account']['password']
    context.page.goto(ENVIRONMENT["QA"][context.env]['URI'])
    loginPage = LoginPage(context.page)
    loginPage.click_login_link()
    loginPage.set_text_username_input(username)
    loginPage.set_text_password_input(password)
    loginPage.click_login_btn()


def before_scenario(context, scenario):
    if 'create_task' in scenario.tags:
        task_page = TaskPage(context.page)
        task_page.click_in_add_task()
        task_page.set_text_task_name_input(TASK_NAME)
        task_page.set_text_description_task_input("Recordatorio a los clientes sobre la reunion del viernes")
        task_page.click_in_add_tasks_btn()
        task_page.click_for_cancel_btn()
