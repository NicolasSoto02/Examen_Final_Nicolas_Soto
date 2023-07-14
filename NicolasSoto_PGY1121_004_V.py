import datetime as dt
import re

dptos=[#V=en venta X=vendido
['Piso  1', 'V', 'V', 'V', 'V'],
['Piso  2', 'V', 'V', 'V', 'V'],
['Piso  3', 'V', 'V', 'V', 'V'],
['Piso  4', 'V', 'V', 'V', 'V'],
['Piso  5', 'V', 'V', 'V', 'V'],
['Piso  6', 'V', 'V', 'V', 'V'],
['Piso  7', 'V', 'V', 'V', 'V'],
['Piso  8', 'V', 'V', 'V', 'V'],
['Piso  9', 'V', 'V', 'V', 'V'],
['Piso 10', 'V', 'V', 'V', 'V'],
]
pre_lis=[3800,3000,2800,3500]
con_ven=[0,0,0,0,0]
datos=[]
lib_dept={"A":1,"B":2,"C":3,"D":4,}
nombres=["A","B","C","D"]
total=0
def rutsim(rut):
    rut1=rut.replace(".","").replace("-","")
    rut1=rut1[:-1]
    return rut1   

def show():
    print("          TIPO\n        A B C D ")
    for row in reversed(dptos):
        print(" ".join(row))

def comprar():
    global datos,total
    while True:
        show()
        try: 
            sel=str(input(f"Ingrese que dpto desea comprar:\n"))
            
            let=re.findall(r'[a-zA-Z]+',sel)[0].upper()
            let1=lib_dept.get(let)

            num=int(re.findall(r'\d+',sel)[0])-1
            
            if dptos[num][let1]=="V":
                rut=str(input("Porfavor Ingrese su rut:\n"))
                rut1=int(rutsim(rut))
                
                cont=str(input(f"Su total es de: {pre_lis[let1-1]}UF\nPresione ENTER para continuar"))
                
                con_ven[let1-1]+=1#Guardando q tipo de depto se vendio en su indice correspondiente
                con_ven[4]+=1     #El indice 4 es el total de ventas
                
                datos.append([rut1,num+1,let])
                
                datos=sorted(datos, key=lambda x: x[2])#Ordenando por letra y luego por piso, dejandolo asi ordenado por piso y letra en una lista
                datos=sorted(datos, key=lambda x: x[1])
                
                dptos[num][let1]="X" #Cambiando el estado del depto a vendido

                total+=pre_lis[let1-1]#Sumando el total de ventas
                break
            else:
                print("No esta disponible")
        except:
            print("El departamento ingresado no existe")

def mostrar():
    show()
    cont=str(input("Presione ENTER para continuar"))

def compradores():
    
    for i in range(len(datos)):
        print(f"Depto: {datos[i][1]}{datos[i][2]}\nRut:{datos[i][0]}\n")
        if i==len(datos):
            break    
    else:
        print("Todos los departamentos estan disponibles")
        
def ventas():
    print("Tipo de departamento   Cantidad  Total")
    for i in range(4):
        if con_ven[i]>0:
            print(f"Tipo {nombres[i]} {pre_lis[i]}                  {con_ven[i]:>2}  {con_ven[i]*pre_lis[i]}UF")
    print(f"Total                                           {con_ven[4]:>}        {total:>6}")

def salir():
    fecha=dt.datetime.now().strftime("%d/%m/%Y")
    print(f"Hasta pronto!\nNicolás Soto\n{fecha}")

while True:#Menu
    menu=int(input("Imboiliaria MI CASA\n Seleccione una Opcion\n(1) Comprar O Arrendar\n(2) Mostrar departamentos disponibles\n(3) Mostrar listado de compradores\n(4) Mostrar ventas totales\n(5) Salir\n"))
    if menu==1:
        comprar()
    if menu==2:
        mostrar()
    if menu==3:
        compradores()
    if menu==4:
        ventas()
    if menu==5:
        salir()
        break