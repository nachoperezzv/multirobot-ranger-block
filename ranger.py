from aurigapy import *
import sys


# Son lanzados por un fichero launch que les manda por parámetro el nombre de conexión

# Recibe el nombre del puerto del robot
if len(sys.argv) >= 2:
	makeblock_name = int(sys.argv[1])
else:
	sys.exit()

# Se conecta al robot
ap = AurigaPy(debug=False)
ap.connect(makeblock_name)
print("Conectado")

# Prueba iluminar LED [BORRAR]
sleep(2)
for i in range(10):
    l = i * 25
    print(l)
    ap.set_led_onboard(0, r=l, g=l, b=0)
    sleep(0.1)

#ap.move_to(command="right", degrees=2000, speed=125)


# Leen de un topic cuando tienen que empezar su movimiento

# Publican en un topic cuando han encontrado el punto de luz

# Se mueven en un bucle infinito que busca la luz. Aquí entra la 
# máquina de estados. 

print("Reset")
ap.reset_robot()
print("Closing")
ap.close()