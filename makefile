datosalbum.png: datos.txt grafica.py
	python grafica.py

datos.txt: monas
	./monas>datos.txt

ejercicio16:
	c++ ejercicio.cpp -o monas
