Cosas a tener en cuenta

    No es imprescindible terminar todo, se valorará el código y su presentación (poco pero hecho lo mejor posible, mejor que mucho y sin terminar)
    Como corolario a lo anterior, se recomienda hacer lo que tengas más controlado
    Se valorará:
        buenas prácticas aplicadas (commit conventions, linting, pre-commits, etc...)
        un pipeline de CI (Github Actions o similar)
        despliegue del producto en Openshift / Kubernetes / DockerSwarm
        documentación asociada al proyecto. Asumiremos que el laboratorio es para una persona con concomientos básicos.
    Se marcan los pasos que se consideran mínimos (Req) en cada sección

Prueba
Ansible

    (Req) Uso de docker para levantar una instancia de Sonatype Nexus
    (Req) Lectura de todos los repositorios existentes
    Borrado de los repositorios
    Generación de los repositorios como estaban inicialmente

Python / TypeScript (Deno)

    (Req) Partiendo de una instancia de Nexus levantada
    (Req) Lectura del listado de repositorios
    Creación de un nuevo repositorio
    Subida de un artefacto a mano al repositorio (Necesario para la siguiente)
    Listado de los assets del repositorio
