
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

crear ambiente virtual con la version que quiero usar:
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





