# Punto 2 Entrega 4 Sistemas Opertivos
# Alejandro Peñaranda Agudelo - 201941008

nombreLectura = "inFile"

class Particion():
  def __init__(self,n,capacidad):
    self.n = n
    self.capacidad = int(capacidad)
    
  def nuevoTamaño(self,capacidad):
    self.capacidad = capacidad


class Proceso():
  def __init__(self,n,tamaño):
    self.n = n
    self.tamaño = int(tamaño)

  def nombre(self):
    res = "P" + str(self.n)
    return res

  
def input():
    readData = []
    with open(nombreLectura + ".txt", "r") as f:
        particiones = []
        procesos = []
        readData = f.read().split('\n')
        metodo = int(readData[0])
        numParticiones = int(readData[1])
        numProcesos = int(readData[numParticiones + 2])
        aux1 = numParticiones + 2
        aux2 = aux1 + numProcesos + 1
        for i in range (2,aux1):
          particiones.append(Particion(i-1,readData[i]))
        for i in range (aux1 + 1,aux2):
          procesos.append(Proceso(i - aux1-1,readData[i]))
          
    return metodo, particiones, procesos

  
#Esta función se encarga de realizar el llamado al metodo de asignacion de memoria seleccionado
def saveProcs(metodo,particiones,procesos):
  if metodo == 1:
    firstFit(particiones, procesos)
  elif metodo == 2:
      bestFit(particiones, procesos)
  elif metodo == 3:
      worstFit(particiones, procesos)
  else:
    print('Error: Escoga un metodo de asignación de memoria valido')

#Esta función implementa el metodo de asignacion de memoria FirstFit
def firstFit(particiones,procesos):
  res = ""
  for i in range(len(procesos)):
    aux = False
    for j in range(len(particiones)):
      if procesos[i].tamaño <= particiones[j].capacidad:
        res += procesos[i].nombre() + " -> " + str(procesos[i].tamaño) + " is put in " + str(particiones[j].capacidad) + ", " + str(particiones[j].n) + " partition." + "\n"
        particiones[j].nuevoTamaño(particiones[j].capacidad - procesos[i].tamaño)
        aux = True
        break
    if aux == False:
      res += procesos[i].nombre() + " -> " + str(procesos[i].tamaño) + " Not allocated"
  print(res)

#Esta función implementa el metodo de asignacion de memoria BestFit
def bestFit(particiones,procesos):
  res = ""
  for i in range(len(procesos)):
    aux = False
    index = 0
    mindif = 100000000
    for j in range(len(particiones)):
      if procesos[i].tamaño <= particiones[j].capacidad:
        aux = True
        if particiones[j].capacidad - procesos[i].tamaño < mindif:
          mindif = particiones[j].capacidad - procesos[i].tamaño
          index = j
    particiones[index].nuevoTamaño(particiones[index].capacidad - procesos[i].tamaño)
    res += procesos[i].nombre() + " -> " + str(procesos[i].tamaño) + " is put in " + str(particiones[index].capacidad + procesos[i].tamaño ) + ", " + str(particiones[index].n) + " partition." + "\n"
    if aux == False:
      res+= procesos[i].nombre() + " -> " + str(procesos[i].tamaño) + " Not allocated"
  print(res)

#Esta función implementa el metodo de asignacion de memoria WorstFit  
def worstFit(particiones,procesos):
  res = ""
  for i in range(len(procesos)):
    aux = False
    index = 0
    maxdif = 0
    for j in range(len(particiones)):
      if procesos[i].tamaño <= particiones[j].capacidad:
        aux = True
        if particiones[j].capacidad - procesos[i].tamaño > maxdif:
          maxdif = particiones[j].capacidad - procesos[i].tamaño
          index = j
    if maxdif != 0:
      particiones[index].nuevoTamaño(particiones[index].capacidad - procesos[i].tamaño)
      res += procesos[i].nombre() + " -> " + str(procesos[i].tamaño) + " is put in " + str(particiones[index].capacidad + procesos[i].tamaño ) + ", " + str(particiones[index].n) + " partition." + "\n"
    if aux == False:
      res+= procesos[i].nombre() + " -> " + str(procesos[i].tamaño) + " Not allocated"
  print(res)

#Metodo principal da inicio a la ejecucion del problema
def main():
  metodo,particiones, procesos = input()
  saveProcs(metodo,particiones,procesos)
  
  
if __name__ == "__main__":
    main()
