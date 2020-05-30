
### uso de ambientes virtuales Pipenv

instalar ursina con la version 3.6, el 3.5 no sirve
https://realpython.com/intro-to-pyenv/
```bash
curl https://pyenv.run | bash #descargar

pyenv install --list | grep " 3\.[678]" #ver versiones a instalar

pyenv install 3.6.10 #quiero instalar esta

pyenv global 3.6.10 #debo agregarla al path


```
y ya es posible usarlo
```sh
$ python3.6 -V
Python 3.6.10
```
### pipenv
verifica que tienes pip en python e instalar pipenv
```python
$pip install pipenv 
```
eso te permitira instalar ambientes virtuales, si not tienes pip me parece que se instala con apt-get, prueba tambien escribiendo `python3 pip install pipenv ` si no llega a funcionar, en todo caso ahi podria haber errores dependientes de tu maquina que no son graves, puedes googlear para resolverlos
ya instalado pipenv sera posible acceder al comando pipenv desde cualquier carpeta

me ubico en la carpeta en la que trabajare y crear un ambiente virtual con la version que quiero usar:
```sh
pipenv shell --python=python3.6
```
ya habiendolo creado el ambiente en ese bash es el instalado en el ambiente virtual, todo lo que corra ahi correra con esa version de python, sin afectar a carpetas arriba de esta, eso permite evitar errores de dependencias:
```sh
$python -V
Python 3.6.10
```
si quieres remover el ambiente virtual, con esto desaparecen todos los paquetes instalados en ese ambiente virtual:
```sh
pipenv --rm
```

instalar paquetes:
```sh
pipenv install paquete
```

para salir del shell de ese ambiente virtual teclear:
```
exit
```

para volver a entrar a ese ambiente hay que ubicarnos en la carpeta en la que se creo y teclear:
```sh
pipenv shell
```
puede haber mas de un ambiente virtual abierto del mismo proyecto al mismo tiempo, pero pues rara vez lo haras

### ejecutar codigo


ya en el ambiente virtual en la carpeta donde este nuestro ambiente creamos un archivo `mi_primer_programa.py` y en el escribimos
```python
print("hello world")
```
lo guardamos y para ejecutar ese codigo escribimos en la consola del ambiente virtual
```sh
$ python mi_primer_programa.py
```
y eso hara funcionar el programa

### Ursina 
instalar ursina:
https://www.ursinaengine.org/
```sh
pip install git+https://github.com/pokepetter/ursina.git
```

creamos un archivo test_ursina.py: 
```py
from ursina import *

app = Ursina()

player = Entity(model='cube', color=color.orange, scale_y=2)

def update():   # update gets automatically called.
    player.x += held_keys['d'] * .1
    player.x -= held_keys['a'] * .1

app.run() 
```

y ejecutamos:
```py
python test_ursina.py 
```





