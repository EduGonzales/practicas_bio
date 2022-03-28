# practicas_bio
Primero debemos instalar anaconda(https://www.anaconda.com/) en linux.
Ejecutamos el sh y despues creamos un entorno virtual : conda install -n nombredelentorno -c anaconda python .
Nota : Si quisiera una version de python en especifico : python=3.9 .
Para acceder al entorno creado : conda activate nombredelentorno .
Para salir del entorno : conda deactivate nombredelentorno .
Ahora un vez en el entorno, instalaremos mongodb mediante anaconda(https://anaconda.org/anaconda/mongodb) : conda install -c anaconda mongodb .
Nota : En el caso de que estuvieramos en un entorno diferente o en el base podriamos instalar paquetes en otros entornos con el siguiente comando :
conda install -n nombredelentorno -c anaconda mongodb .
Una vez instalador mongodb, para iniciarlo debemos usar el siguiente comando : systemctl start mongod .
Otros comandos utiles serian : systemctl status mongod , systemctl sttop mongod .
Para acceder a mongodb desde terminal : mongo .
Ahora instalaremos Flask mediante anaconda(https://anaconda.org/anaconda/flask) : conda install -c anaconda flask .
Recomendación : instalar pip en anaconda : https://anaconda.org/anaconda/pip : conda install -c anaconda pip
Instalar pymongo : pip install flask pymongo
Instalamos mongoengine : python -m pip install -U mongoengine
Instalamos flask_mongoengine : pip install flask-mongoengine
Instalamos mongodb : sudo apt-get install -y mongodb-org
Luego instalaremos postman(https://www.postman.com/downloads/).
Por ultimo descargaremos visual studio code(https://code.visualstudio.com/).

