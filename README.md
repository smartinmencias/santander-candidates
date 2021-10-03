**DESPLEGAR SONATYPE NEXUS A KUBERNETES VÍA ANSIBLE**


Para levantar una instancia de Sonatype Nexus en Kubernetes, lo primero que debemos hacer es comprobar nuestros archivos .yml (Deployment y Service) dentro de la carpeta “ansible”:

./ansible/Deployment.yml --> Usamos este archivo para crear nuestro Deploy
./ansible/Service.yml --> Usamos este archivo para desplegar nuestro Servicio

Para hacer nuestro despliegue, usaremos nuestro archivo Kube Config, ubicado en:

./ansible/files/config

Nuestro workflow desplegará, una vez aprobada nuestra PR en la rama master, nuestra instancia de Sonatype Nexus con las configuraciones realizadas en nuestros archivos Deployment.yml y Service.yml.

**ADMINISTRACIÓN DE REPOSITORIOS CON SCRIPT DE PYTHON**

En este caso, ejecutaremos nuestra Github Action manualmente. Para ello:
1.- Iremos a nuestro apartado Actions. Aquí seleccionaremos nuestro Action repomanage python.
2.- Seleccionaremos Run Workflow. En él, teclearemos las opciones:
	- Para listar repositorios, teclearemos -l. El script, nos listará los repositorios disponibles en nuestro Nexus
	- Podemos también crear repositorios apt. Para ello, introduciremos -c <nombre de repo>. El script, nos creará automáticamente nuestro repositorio
