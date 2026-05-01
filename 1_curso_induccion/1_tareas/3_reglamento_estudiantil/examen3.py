import sys

def examen_simulacion_final():
    # Banco de 10 preguntas basadas estrictamente en el Reglamento de Alumnos
    preguntas = [
        {
            "id": 1,
            "pregunta": "¿Cuál es la calificación mínima aprobatoria para el nivel de POSGRADO?",
            "opciones": ["a) 7.0", "b) 8.0", "c) 6.0", "d) 8.5"],
            "correcta": "b",
            "explicacion": "Artículo 58: En Posgrado la mínima es 8.0, a diferencia de Licenciatura que es 6.0 (o 7.0 en Medicina)."
        },
        {
            "id": 2,
            "pregunta": "¿Cuántos exámenes extraordinarios acumulados causan BAJA automática en la Lic. de MÉDICO CIRUJANO?",
            "opciones": ["a) 14", "b) 5", "c) 10", "d) 12"],
            "correcta": "c",
            "explicacion": "Artículo 82: Para Medicina el límite son 10 extraordinarios; para las demás licenciaturas son 14."
        },
        {
            "id": 3,
            "pregunta": "¿Qué porcentaje de asistencia se requiere para tener derecho a examen FINAL?",
            "opciones": ["a) 60%", "b) 70%", "c) 85%", "d) 80%"],
            "correcta": "d",
            "explicacion": "Artículo 40: El reglamento exige el 80% de asistencia para ordinarios (finales)."
        },
        {
            "id": 4,
            "pregunta": "En el sistema CUATRIMESTRAL, ¿cuál es el valor porcentual del examen FINAL?",
            "opciones": ["a) 30%", "b) 40%", "c) 50%", "d) 20%"],
            "correcta": "b",
            "explicacion": "Artículo 47: Se compone de dos parciales (30% c/u) y un final del 40%."
        },
        {
            "id": 5,
            "pregunta": "¿Cuántas fotografías y de qué tipo se requieren para la inscripción a Licenciatura?",
            "opciones": ["a) 4 a color", "b) 6 blanco y negro, papel mate", "c) 2 digitales", "d) 8 blanco y negro"],
            "correcta": "b",
            "explicacion": "Artículo 6, Fracción III: Se requieren 6 fotografías tamaño infantil, blanco y negro, papel mate."
        },
        {
            "id": 6,
            "pregunta": "¿Qué plazo tiene el alumno para solicitar una REVISIÓN de examen tras conocer su nota?",
            "opciones": ["a) 24 horas", "b) 48 horas", "c) 3 días hábiles", "d) 12 horas"],
            "correcta": "a",
            "explicacion": "Artículo 131: El alumno debe solicitar la revisión en un plazo no mayor a 24 horas."
        },
        {
            "id": 7,
            "pregunta": "¿Cuál es el periodo máximo de PERMANENCIA para terminar una carrera?",
            "opciones": ["a) 10 años", "b) El doble de la duración del plan de estudios", "c) 6 años", "d) La duración del plan más 2 años"],
            "correcta": "b",
            "explicacion": "Artículo 78: No puedes exceder el doble del tiempo que dura oficialmente tu carrera."
        },
        {
            "id": 8,
            "pregunta": "¿Cuántas materias reprobadas al final de un ciclo causan BAJA DEFINITIVA?",
            "opciones": ["a) 2 materias", "b) 3 materias", "c) 4 materias o más", "d) 5 materias"],
            "correcta": "c",
            "explicacion": "Artículo 80: Quedar reprobado en 4 o más materias al término de un ciclo es motivo de baja."
        },
        {
            "id": 9,
            "pregunta": "¿Qué porcentaje de créditos de la primera carrera debe tener un alumno para cursar una SIMULTÁNEA?",
            "opciones": ["a) 25%", "b) 75%", "c) 50%", "d) 100%"],
            "correcta": "c",
            "explicacion": "Artículo 96: Es requisito haber aprobado al menos el 50% de los créditos de la primera carrera."
        },
        {
            "id": 10,
            "pregunta": "¿Cuál de estas es una SANCIÓN considerada grave en el reglamento?",
            "opciones": ["a) Amonestación verbal", "b) Matrícula condicionada", "c) Suspensión de un día", "d) Llamada de atención escrita"],
            "correcta": "b",
            "explicacion": "Artículo 141, Inciso D: La Matrícula Condicionada es una sanción mayor impuesta por la Dirección General."
        }
    ]

    puntaje = 0
    erradas = []

    print("="*60)
    print("SIMULADOR FINAL: REGLAMENTO UNIVERSIDAD CUAUHTÉMOC")
    print("="*60)
    print("Instrucciones: Escribe la letra (a, b, c o d) y pulsa Enter.\n")

    for p in preguntas:
        print(f"{p['id']}. {p['pregunta']}")
        for opcion in p['opciones']:
            print(f"   {opcion}")
        
        respuesta = input("Tu respuesta: ").lower().strip()
        
        if respuesta == p['correcta']:
            print("CORRECTO ✅\n")
            puntaje += 1
        else:
            print(f"INCORRECTO ❌ (La respuesta era {p['correcta']})")
            print(f"INFO: {p['explicacion']}\n")
            erradas.append(p['id'])

    # Cálculo de estadísticas
    total = len(preguntas)
    porcentaje = (puntaje / total) * 100

    print("="*60)
    print(f"RESULTADO DE LA PRUEBA")
    print(f"Puntaje: {puntaje} / {total}")
    print(f"Porcentaje de Acierto: {porcentaje}%")
    print("="*60)

    if porcentaje == 100:
        print("¡Perfecto! Estás totalmente listo para el examen.")
    elif porcentaje >= 70:
        print("Buen trabajo. Solo ajusta los detalles de las preguntas que fallaste.")
    else:
        print("Necesitas repasar más. El reglamento es estricto en estos puntos.")

    if erradas:
        print(f"\nDEBES REPASAR LOS TEMAS DE LAS PREGUNTAS: {erradas}")

if __name__ == "__main__":
    examen_simulacion_final() 