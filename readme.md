instalar con 3.6, el 3.5 no sirve
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

crear ambiente virtual:
```
pipenv shell --python=python3.6
```
ya habiendolo creado el ambiente en ese bash es el instalado en el ambiente virtual:
```
$python -V
Python 3.6.10
```
remover ambiente virtual, con esto desaparecen todos los paquetes instalados en ese ambiente virtual:
```
pipenv --rm
```

instalar paquetes:
```
pipenv install paquete
```

instalar ursina:
https://www.ursinaengine.org/
```
```



