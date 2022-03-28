# practicas_bio
1. Primero debemos instalar anaconda(https://www.anaconda.com/) en linux.
   1.1 Ejecutamos el sh y despues creamos un entorno virtual : conda install -n nombredelentorno -c anaconda python .
        1.1.1Nota : Si quisiera una version de python en especifico : python=3.9 .
   1.2 Para acceder al entorno creado : conda activate nombredelentorno .
        1.2.1Para salir del entorno : conda deactivate nombredelentorno .
2. Ahora un vez en el entorno, instalaremos:
   2.1 Ahora instalaremos Flask mediante anaconda(https://anaconda.org/anaconda/flask) : conda install -c anaconda flask .
   2.2 Recomendación : instalar pip en anaconda : https://anaconda.org/anaconda/pip : conda install -c anaconda pip
   2.3 Instalar pymongo : pip install flask pymongo
   2.4 Instalamos mongoengine : python -m pip install -U mongoengine
   2.5 Instalamos flask_mongoengine : pip install flask-mongoengine
   2.6 Instalamos mongodb : sudo apt-get install -y mongodb-org
3. Una vez instalador mongodb, para iniciarlo debemos usar el siguiente comando : systemctl start mongod .
   3.1 Otros comandos utiles serian : systemctl status mongod , systemctl sttop mongod .
   3.2 Para acceder a mongodb desde terminal : mongo .
4. Luego instalaremos postman(https://www.postman.com/downloads/).
5. Por ultimo descargaremos visual studio code(https://code.visualstudio.com/).

