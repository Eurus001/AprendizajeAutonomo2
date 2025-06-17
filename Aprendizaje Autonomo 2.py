def main():
    print("Cálculo de promedio de notas")
    materias = []
    notas = []

    while True:
        materia = input("Ingresa el nombre de la materia (o escribe 'fin' para terminar): ").strip()
        if materia.lower() == "fin":
            break
        if materia == "":
            print("El nombre de la materia no puede estar vacío.")
            continue

        try:
            nota = float(input(f"Ingresa la nota de '{materia}': "))
            if nota < 0 or nota > 10:
                print("La nota debe estar entre 0 y 10.")
                continue
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        materias.append(materia)
        notas.append(nota)
        print(f"Agregado: {materia} - {nota}\n")

    if not materias:
        print("No se ingresaron materias.")
        return

    print("\nResumen de materias y notas:")
    for i in range(len(materias)):
        print(f"  {i+1}. {materias[i]}: {notas[i]}")

    promedio = sum(notas) / len(notas)
    print(f"\nPromedio general: {promedio:.2f}")
    if promedio >= 7.0:
        print("¡Felicidades! Has aprobado.\n")
    else:
        print("Debes mejorar. No has aprobado.\n")

    guardar = input("¿Deseas guardar este resultado en un archivo? (s/n): ").strip().lower()
    if guardar == "s":
        with open("resultado_notas.txt", "w") as f:
            f.write("Resumen de notas:\n")
            for i in range(len(materias)):
                f.write(f"{materias[i]}: {notas[i]}\n")
            f.write(f"\nPromedio general: {promedio:.2f}\n")
            f.write("Estado: Aprobado\n" if promedio >= 7.0 else "Estado: Reprobado\n")
        print("Resultado guardado en 'resultado_notas.txt'")

    input("Presiona enter para terminar...")

if __name__ == "__main__":
    main()
