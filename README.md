# TODOIST - Automatizacion pruebas WEB

Instrucciones para configurar y ejecutar pruebas automatizadas Web con:
	- Lenguaje :Python
	- Framework: Behave
	- Herramienta: Playwright y Allure

### Requisitos Previos
	1. Instalar Python puedes descargarlo desde aquí.
	2. Instalar pip que es el gestor de paquetes de Python.
	3. Instalar Node.js que requerido para Playwright. Descárgalo desde aquí.
	4. Instalar Allure para generar reportes. Instálala siguiendo las instrucciones aquí.

### Configuración del Entorno
	1. Clonar el repositorio del proyecto.
		--------------------------------------------------------------------------------------------
		- git clone <URL_DEL_REPOSITORIO>
		--------------------------------------------------------------------------------------------
	2. Crear un Entorno Virtual:
	   Crea un entorno virtual para evitar conflictos con otras versiones de paquetes.
	3. Instalar Dependencias:
	   Instala las dependencias del proyecto especificadas en el archivo requirements.txt.
	   ----------------------------------------------------------------------------------------------
	   - pip install -r requirements.txt
	   ----------------------------------------------------------------------------------------------
	4. Instalar Playwright:
	   Instala Playwright y sus dependencias.
	   ----------------------------------------------------------------------------------------------
	   - pip install playwright
	   - playwright install
	   -----------------------------------------------------------------------------------------------
	5. Configurar Allure:
	   Asegúrate de que Allure esté instalado y configurado correctamente en tu sistema.
	   -----------------------------------------------------------------------------------------------
	   - npm install -g allure-commandline --save-dev
	   -----------------------------------------------------------------------------------------------

### Estructura del Proyecto
	1. Carpetas y Archivos Principales:
		- features/: Contiene los archivos .feature con los escenarios de prueba.
		- steps/: Contiene los archivos Python con los steps definitions.
		- pages_object/: Contiene los archivos Python que representan las páginas de la aplicación web (patrón Page Object Model).
		- configure/: Contiene el archivo para configurar el ambiente. usuario y contrasenia
		  que se encuentran establecidas dentro de file que como son publicas pueden usarlo.
		- reports/: Carpeta donde se almacenarán los reportes generados por Allure.

### Ejecución de Pruebas
	1. Ejecución de Pruebas con Behave: Ejecuta las pruebas utilizando Behave.
	   ------------------------------------------------------------------------------------------------
	   - behave
	   ------------------------------------------------------------------------------------------------
	2. Generación de Reportes con Allure: 
	   - Ejecuta las pruebas y genera reportes Allure.
	     ------------------------------------------------------------------------------------------------
	     - behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results --no-capture
	     ------------------------------------------------------------------------------------------------
	   - Crear el informe temporalmente para mostrar el contenido automaticamente en un navegador web
	     ------------------------------------------------------------------------------------------------
	     - allure serve reports/allure-results
	     ------------------------------------------------------------------------------------------------

### Notas Adicionales
	1. Soporte: Si encuentras problemas o tienes preguntas, no dudes en contactar con 
	   mi persona.