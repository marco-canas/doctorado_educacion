import sys

def mostrar_resultado(puntaje, total, temas_repasar):
    porcentaje = (puntaje / total) * 100
    print("\n" + "="*50)
    print(f"RESUMEN DE TU DESEMPEÑO")
    print(f"Aciertos: {puntaje} de {total}")
    print(f"Eficacia: {porcentaje:.2f}%")
    print("="*50)

    if porcentaje >= 80:
        print("¡Excelente nivel! Estás listo para el examen real.")
    elif porcentaje >= 60:
        print("Buen intento, pero necesitas asegurar los puntos clave.")
    else:
        print("Atención: Debes realizar una lectura profunda del reglamento.")

    if temas_repasar:
        print("\nFOCOS DE ESTUDIO (Puntos donde fallaste):")
        # Usamos un set para no repetir el tema si falló varias del mismo tipo
        for tema in set(temas_repasar):
            print(f"-> {tema}")

def ejecutar_examen():
    # Estructura: Pregunta, Opciones, Respuesta Correcta, Retroalimentación, Categoría
    banco_preguntas = [
        {
            "pregunta": "¿Qué autoridad es la encargada de resolver una solicitud de revisión de examen?",
            "opciones": ["a) El Rector", "b) El Consejo Universitario", "c) El Director de la Carrera", "d) El Jefe de Control Escolar"],
            "correcta": "c",
            "retro": "Art. 131-133: La revisión se solicita por escrito al Director de la Carrera o Escuela.",
            "tema": "Procesos de Revisión de Calificaciones"
        },
        {
            "pregunta": "Según el reglamento, ¿cuál es una sanción considerada como grave?",
            "opciones": ["a) Amonestación verbal", "b) Suspensión de 1 a 3 días", "c) Matrícula condicionada", "d) Trabajo comunitario"],
            "correcta": "c",
            "retro": "Art. 141: La matrícula condicionada es una sanción superior a la suspensión temporal.",
            "tema": "Régimen Disciplinario y Sanciones"
        },
        {
            "pregunta": "¿Cuál es el requisito para realizar un examen extraordinario?",
            "opciones": ["a) Haber pagado la cuota y tener 60% de asistencia", "b) Tener 80% de asistencia", "c) No tener adeudos y promedio de 7.0", "d) Solo haber pagado la cuota"],
            "correcta": "a",
            "retro": "Art. 41 y 140: Se requiere pago del derecho y al menos el 60% de asistencias.",
            "tema": "Asistencias y Derechos a Examen"
        },
        {
            "pregunta": "¿Qué ocurre si un alumno es sorprendido cometiendo fraude en un examen?",
            "opciones": ["a) Se le repite el examen", "b) Se le anula el examen y se reporta a Dirección", "c) Se le baja un punto", "d) Se le suspende por un mes"],
            "correcta": "b",
            "retro": "Art. 139: El fraude implica la nulidad del examen y sanción disciplinaria.",
            "tema": "Honestidad Académica"
        },
        {
            "pregunta": "¿En qué caso un alumno causa BAJA DEFINITIVA por motivos académicos?",
            "opciones": ["a) Por reprobar una materia dos veces", "b) Por no asistir a una semana de clases", "c) Por agotar las 3 oportunidades de acreditar una asignatura", "d) Por tener promedio menor a 8.0"],
            "correcta": "c",
            "retro": "Art. 59 y 82: Al agotar las 3 oportunidades permitidas (ordinarios/extraordinarios).",
            "tema": "Permanencia y Bajas"
        }
    ]

    puntaje = 0
    temas_repasar = []

    print("=== SEGUNDO SIMULADOR: REGLAMENTO UNIVERSIDAD CUAUHTÉMOC ===\n")
    
    for i, p in enumerate(banco_preguntas, 1):
        print(f"{i}. {p['pregunta']}")
        for opt in p['opciones']:
            print(f"   {opt}")
        
        res = input("\nTu elección (a/b/c/d): ").lower().strip()
        
        if res == p['correcta']:
            print("CORRECTO. ✅\n")
            puntaje += 1
        else:
            print(f"INCORRECTO. ❌ {p['retro']}\n")
            temas_repasar.append(p['tema'])

    mostrar_resultado(puntaje, len(banco_preguntas), temas_repasar)

if __name__ == "__main__":
    ejecutar_examen()