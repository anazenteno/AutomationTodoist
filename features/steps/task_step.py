from behave import given, Step

from configure.global_variables import TASK_NAME
from page_object.task_page import TaskPage


@given("que estoy en la pagina donde se agregar tarea de hoy")
def goto_click_on_add_tasks(context):
    """
    This step navigate to the page where you can create a new task.
    :type context: behave.runner.Context
    """
    task_page = TaskPage(context.page)
    task_page.click_in_add_task()


@Step("ingreso el nombre de la tarea con '{task_name}'")
def fill_name_task_(context, task_name):
    """
    This step, enter the name of the task in the input field.
    :param task_name:       The name of the task to enter.
    :param context:         The context of the test.
    """
    task_page = TaskPage(context.page)
    task_page.set_text_task_name_input(task_name)


@Step("ingreso la descripcion de la tarea con '{task_description}'")
def fill_description_task(context, task_description):
    """
    This step, enter the description of the task in the input field.
    :param task_description: The description of the task.
    :param context:         The context of the test.
    """
    task_page = TaskPage(context.page)
    task_page.set_text_description_task_input(task_description)


@Step("hacer clic agregar tarea")
def click_element_add_task(context):
    """
    This step navigate to the page where you can create a new task.
    :type context: behave.runner.Context
    """
    task_page = TaskPage(context.page)
    task_page.click_in_add_tasks_btn()
    task_page.click_for_cancel_btn()


@Step("la tarea '{task_name}' debería registrarse exitosamente")
def validate_add_task(context, task_name):
    """
    This step verify that the task is created.
    :param task_name:       The name of the task.
    :param context:         The context of the test.
    """
    task_page = TaskPage(context.page)
    last_element = task_page.obtain_last_element_task()
    assert last_element == task_name, f"Error: last_element ({last_element}) is not equal to task_name ({task_name})"


@given("que estoy en la pagina de registro tareas, hacer clic en  mas acciones tareas")
def goto_more_action_task(context):
    """
    This step navigate to the page where register tasks and do click en more action tasks.
    :type context: behave.runner.Context
    """
    task_page = TaskPage(context.page)
    task_page.click_more_action_btn()


@Step("seleccionar la opcion editar una tarea")
def goto_select_element_update(context):
    """
    This Step navigate to the page where  selection action update a tasks.
    :type context: behave.runner.Context
    """
    task_page = TaskPage(context.page)
    task_page.click_edit_task_btn()


@Step("cambio el nombre de la tarea a '{edit_task_name}'")
def fill_new_name_task(context, edit_task_name):
    """
    This step change the name of the task.
    :param edit_task_name:    The name of the task.
    :param context:         The context of the test.
    """
    task_page = TaskPage(context.page)
    task_page.set_text_task_name_edit_input(edit_task_name)


@Step("guardo los cambios de la tarea")
def step_impl(context):
    """
    This step do click for save the change with update of name task.
    :type context: behave.runner.Context
    """
    task_page = TaskPage(context.page)
    task_page.click_save_btn()


@Step("la tarea debería actualizarse correctamente con el nombre '{edit_task_name}'")
def validate_new_name_task_when_edit(context, edit_task_name):
    """
    This step update the name of the task.
    :param edit_task_name:    The name of the task.
    :type context: behave.runner.Context
    """
    task_page = TaskPage(context.page)
    last_element_edit = task_page.obtain_last_element_task()
    assert last_element_edit == edit_task_name, f"Error: last_element ({last_element_edit}) is not equal to task_name ({edit_task_name})"


@Step("selecciono y elimino la tarea")
def goto_delete_task(context):
    """
    This step navigate to the page where selection action delete a tasks.
    :type context: behave.runner.Context
    """
    task_page = TaskPage(context.page)
    task_page.click_delete_btn()


@Step("confirmo la eliminación haciendo clic en el botón correspondiente")
def goto_confirm_delete_task(context):
    """
    This step navigate to the page when confirm delete a tasks.
    :type context: behave.runner.Context
    """
    task_page = TaskPage(context.page)
    task_page.click_delete_confirm_btn()


@Step("la tarea deberia eliminarse correctamente")
def validate_that_tasks_delete(context):
    """
    This step validate that the task is eliminated correctly.
    :type context: behave.runner.Context
    """
    task_page = TaskPage(context.page)
    element = task_page.obtain_last_element_task()
    assert element != TASK_NAME, f"Task {TASK_NAME} is still on the list."

