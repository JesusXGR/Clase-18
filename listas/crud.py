

animales=["cocodrilo", "conejo", "elefante", "gato"]
opciones=0


running = True

while running:

    print("Mi zoologico \n")
    print("Opciones: \n")
    opciones= int(input("Ingresa una opción: \n1. Agregar\n2. Mostrar \n3. Eliminar por índice \n4. Eliminar por nombre \n5. Salir \n"))


    if opciones == 1:

        animal= input("Ingresa un animal ")
        animales.append(animal)

    if opciones == 2:

        print(animales)

    if opciones == 3:
        eliminar_index= int(input("Ingresa el indice "))
        animales.pop(eliminar_index)

    if opciones == 4:
        eliminar_palabra= input("Ingresa el animal a eliminar: ")
        animales.remove(eliminar_palabra)

        runnig = False

    print("\n")
    



