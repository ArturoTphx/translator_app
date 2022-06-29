NOTA:  
Se debe tener instalado docker en la máquina a probar  
Para más información, consultar: https://docs.docker.com/engine/install/  

PASOS (manuales):  
1. Clonar el repositorio, la carpeta tendrá el nombre de: 'translator_app'  
2. Abrir la terminal donde se clonó la carpeta, y trasladarse al proyecto: 'cd translator_app'  
3. Poner el siguiente comando en la terminal: 'docker image build -t translator .' (Esto construye la imagen)  
3.1 Si ocurre un error, poner en la terminal: 'sudo chmod 666 /var/run/docker.sock', y volver al paso 3  
4. Poner el siguiente comando en la terminal: 'docker run -p 5000:5000 -d translator' (Esto corre un contenedor con la imagen)  

PASOS (automáticos):
1. Clonar el repositorio, la carpeta tendrá el nombre de: 'translator_app'  
2. Abrir la terminal donde se clonó la carpeta, y trasladarse al proyecto: 'cd translator_app'  
3. Poner el siguiente comando en la terminal: 'chmod +x init.sh' (Esto da permisos de ejecución)  
4. Poner el siguiente comando en la terminal: './init.sh' (Esto corre un script de bash que hace el proceso automáticamente)  

COMPROBACIONES:  
1. Escribir en la terminal: 'docker ps' (Muestra los procesos de docker en ejecución)  
1.1 Se debe poner observar un contenedor con una imagen llamada 'translator'  
2. Puede hacer una petición al programa con el siguiente comando: 'echo $(curl -X POST -H "Content-Type: application/json" -d '{"name": "SMITH"}' http://127.0.0.1:5000/traductor?palabra=nombre)'  (Se puede cambiar la palabra nombre por: 'nombre', 'casa', 'gato', 'perro', 'chocolate', 'hola'. Si pone alguna palabra no reconocida, la petición devolverá 'default')  
3. Si posee instalado Apache Bench para probar el rendimiento del servidor, puede correr el comando: 'ab -T application/json -c 1000 -n 1000 -p profile.txt 'http://127.0.0.1:5000/traductor?palabra=nombre'' (Este comando hace mil peticiones concurrentes al servidor web)  
4. Si se desea ver lo que contiene el archivo 'server.log', se puede  correr el siguiente comando: 'curl -X GET -H "Accept: text/plain" http://127.0.0.1:5000/file > server.log' (El cual crea un archivo localmente con una copia del archivo original en un archivo del mismo nombre)
5. Si desea ver el registro de las peticiones en la aplicación, debe correr nuevamente: 'docker ps'. Copiar el ID del contenedor con la imagen de 'translator', y contiuar al paso 5  
6. Con el ID previamente copiado, debe ejecutar el comando: 'docker logs ID_DEL_CONTENEDOR' (Remplazando la palabra ID_DEL_CONTENEDOR por el ID mencionado)  
