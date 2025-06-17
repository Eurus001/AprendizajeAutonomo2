#Inicio de funcion main
def main():
    #Bienvenida
    print("Cálculo de promedio de notas")
    #Inicializar variables
    materias = []
    notas = []

    #While para ejecutar todo el programa
    while True:
        #Ingreso de materia
        materia = input("Ingresa el nombre de la materia (o escribe 'fin' para terminar): ").strip()
        #Verificacion de fin
        if materia.lower() == "fin":
            #Fin no se agrega a las materias
            break
        #Verificacion de vacio
        if materia == "":
            print("El nombre de la materia no puede estar vacío.")
            continue
        #Try de ingreso de notas, se admiten decimales
        try:
            nota = float(input(f"Ingresa la nota de '{materia}': "))
            #Verificacion de numero (positivo entre 0 y 10)
            if nota < 0 or nota > 10:
                print("La nota debe estar entre 0 y 10.")
                continue
            #Mensaje de error numero
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue
        #Agregar materia y nota segun corresponda en las listas
        materias.append(materia)
        notas.append(nota)
        #Mensaje de agregado
        print(f"Agregado: {materia} - {nota}\n")

    #Sin materias
    if not materias:
        print("No se ingresaron materias.")
        return

    #For de impresion de materias
    print("\nResumen de materias y notas:")
    for i in range(len(materias)):
        print(f"  {i+1}. {materias[i]}: {notas[i]}")

    #Calvulo de promedio
    promedio = sum(notas) / len(notas)
    print(f"\nPromedio general: {promedio:.2f}")
    #If de aprobado o no aprobado
    if promedio >= 7.0:
        print("¡Felicidades! Has aprobado.\n")
    else:
        print("Debes mejorar. No has aprobado.\n")

    #Guardar en txt o no
    guardar = input("¿Deseas guardar este resultado en un archivo? (s/n): ").strip().lower()
    if guardar == "s":
        #Aqui se abre o se crea el txt
        with open("resultado_notas.txt", "w") as f:
            #Aqui se escribe en el txt
            f.write("Resumen de notas:\n")
            for i in range(len(materias)):
                f.write(f"{materias[i]}: {notas[i]}\n")
            f.write(f"\nPromedio general: {promedio:.2f}\n")
            f.write("Estado: Aprobado\n" if promedio >= 7.0 else "Estado: Reprobado\n")
        #Mensaje de que ya se guardo
        print("Resultado guardado en 'resultado_notas.txt'")

    #Para que no se cierre la consola
    input("Presiona enter para terminar...")

if __name__ == "__main__":
    main()
