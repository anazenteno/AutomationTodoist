# Created by Windows at 7/16/2024
Feature: Gestion de tareas in Todoist

  Scenario: Verificar que se pueda agregar una nueva tarea.
    Given que estoy en la pagina donde se agregar tarea de hoy
    When ingreso el nombre de la tarea con 'Mensajes Empresa'
    And ingreso la descripcion de la tarea con 'desde hace mucho tiempo que no se envio los correos'
    And hacer clic agregar tarea
    Then la tarea 'Mensajes Empresa' debería registrarse exitosamente


  @create_task
  Scenario: Verificar que se pueda editar una tarea existente.
    Given que estoy en la pagina de registro tareas, hacer clic en  mas acciones tareas
    And seleccionar la opcion editar una tarea
    When cambio el nombre de la tarea a 'Compras en tiendas en lineas'
    And guardo los cambios de la tarea
    Then la tarea debería actualizarse correctamente con el nombre 'Compras en tiendas en lineas'


  @create_task
  Scenario: Verificar que se pueda eliminar una tarea.
    Given que estoy en la pagina de registro tareas, hacer clic en  mas acciones tareas
    When selecciono y elimino la tarea
    And confirmo la eliminación haciendo clic en el botón correspondiente
    Then la tarea deberia eliminarse correctamente