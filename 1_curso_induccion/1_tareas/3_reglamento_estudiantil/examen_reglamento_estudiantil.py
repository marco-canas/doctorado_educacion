import sys

def realizar_examen():
    preguntas = [
        {
            "id": 1,
            "pregunta": "¿Cuál es el porcentaje mínimo de asistencia para tener derecho a presentar un examen FINAL?",
            "opciones": ["a) 60%", "b) 70%", "c) 80%", "d) 90%"],
            "correcta": "c",
            "referencia": "Artículo 40: Se requiere un 80% de asistencia para el examen final."
        },
        {
            "id": 2,
            "pregunta": "¿Qué sucede si un alumno de Licenciatura acumula 14 exámenes extraordinarios?",
            "opciones": ["a) Se le condiciona la matrícula", "b) Es dado de baja automáticamente", "c) Debe pagar una multa", "d) Pierde el derecho a beca"],
            "correcta": "b",
            "referencia": "Artículo 82: Alumnos de licenciatura que acumulen 14 extraordinarios serán dados de baja (excepto Medicina que son 10)."
        },
        {
            "id": 3,
            "pregunta": "¿Cuál es la calificación mínima aprobatoria para la licenciatura en Médico Cirujano Integral?",
            "opciones": ["a) 6.0", "b) 7.0", "c) 8.0", "d) 6.5"],
            "correcta": "b",
            "referencia": "Artículo 57: La mínima es 6, excepto en Medicina donde es 7.0."
        },
        {
            "id": 4,
            "pregunta": "¿Cuántas oportunidades totales tiene un alumno de licenciatura para acreditar una asignatura sin causar baja?",
            "opciones": ["a) Dos", "b) Tres", "c) Cuatro", "d) Cinco"],
            "correcta": "b",
            "referencia": "Artículo 59: El alumno tiene 3 oportunidades (combinación de ordinarios y extraordinarios)."
        },
        {
            "id": 5,
            "pregunta": "En el sistema cuatrimestral, ¿cuál es la ponderación del examen FINAL?",
            "opciones": ["a) 30%", "b) 50%", "c) 40%", "d) 20%"],
            "correcta": "c",
            "referencia": "Artículo 47: Dos parciales de 30% cada uno y un final del 40%."
        },
        {
            "id": 6,
            "pregunta": "¿Cuál es el plazo máximo para solicitar la revisión de un examen tras notificarse las calificaciones?",
            "opciones": ["a) 24 horas", "b) 48 horas", "c) 3 días hábiles", "d) 12 horas"],
            "correcta": "a",
            "referencia": "Artículo 131: El plazo no podrá ser mayor a 24 horas después de la notificación."
        },
        {
            "id": 7,
            "pregunta": "¿Qué tipo de materias NO pueden acreditarse mediante examen extraordinario?",
            "opciones": ["a) Materias teóricas", "b) Idiomas", "c) Clínicas, talleres y laboratorios", "d) Materias seriadas"],
            "correcta": "c",
            "referencia": "Artículo 63: Las materias prácticas (clínicas, talleres, etc.) solo se aprueban en ordinario o cursos especiales."
        },
        {
            "id": 8,
            "pregunta": "¿Cuál es el periodo máximo de permanencia para acreditar un plan de estudios?",
            "opciones": ["a) 5 años", "b) El doble de la duración del plan", "c) La duración del plan más 2 años", "d) No hay límite"],
            "correcta": "b",
            "referencia": "Artículo 78: El periodo máximo es el doble de la duración del plan de estudios."
        },
        {
            "id": 9,
            "pregunta": "¿Cuántas materias reprobadas (máximo) permiten la reinscripción condicionada de un alumno irregular?",
            "opciones": ["a) 1 materia", "b) 2 materias", "c) 3 materias", "d) 5 materias"],
            "correcta": "c",
            "referencia": "Artículo 26: Máximo 3 materias reprobadas del mismo ciclo para reinscribirse."
        },
        {
            "id": 10,
            "pregunta": "¿Qué porcentaje de asistencia se requiere como mínimo para tener derecho a un examen EXTRAORDINARIO?",
            "opciones": ["a) 50%", "b) 80%", "c) 60%", "d) 70%"],
            "correcta": "c",
            "referencia": "Artículo 41 y 140: Se requiere al menos el 60% de asistencia."
        }
    ]

    puntaje = 0
    errores = []

    print("--- SIMULADOR DE EXAMEN: REGLAMENTO UNIVERSIDAD CUAUHTÉMOC ---")
    print("Responde con la letra de la opción correcta (a, b, c o d)\n")

    for p in preguntas:
        print(f"Pregunta {p['id']}: {p['pregunta']}")
        for opcion in p['opciones']:
            print(opcion)
        
        respuesta = input("Tu respuesta: ").lower().strip()
        
        if respuesta == p['correcta']:
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta era {p['correcta']}.\n")
            errores.append(p)

    # Resultados
    porcentaje = (puntaje / len(preguntas)) * 100
    print("-" * 30)
    print(f"RESULTADOS FINALES:")
    print(f"Puntaje: {puntaje}/{len(preguntas)}")
    print(f"Eficacia: {porcentaje}%")
    print("-" * 30)

    if errores:
        print("\nTEMAS A REPASAR PARA MEJORAR:")
        for error in errores:
            print(f"- En la pregunta {error['id']}: {error['referencia']}")
    else:
        print("\n¡Excelente! Conoces perfectamente el reglamento.")

if __name__ == "__main__":
    realizar_examen()