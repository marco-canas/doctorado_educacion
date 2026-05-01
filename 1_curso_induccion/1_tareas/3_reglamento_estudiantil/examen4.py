import sys

def simulador_cuauhtemoc_v4():
    # Banco de preguntas con justificaciones detalladas
    preguntas = [
        {
            "id": 1,
            "pregunta": "¿Cuál es el tiempo máximo de prórroga para entregar el Certificado de Bachillerato original si no se tiene al inscribirse?",
            "opciones": ["a) 30 días naturales", "b) 60 días naturales", "c) Al finalizar el primer periodo", "d) No hay prórroga"],
            "correcta": "b",
            "justificacion": "Artículo 8: El reglamento otorga un plazo máximo de 60 días naturales. Si no se entrega, se cancelan los trámites sin responsabilidad para la Universidad."
        },
        {
            "id": 2,
            "pregunta": "Un alumno de Medicina reprueba 2 materias en ordinario y 1 en extraordinario. ¿Qué sucede con su estatus?",
            "opciones": ["a) Es baja definitiva", "b) Es baja temporal", "c) Es alumno irregular", "d) Se le anula el semestre"],
            "correcta": "c",
            "justificacion": "Artículo 25: Se considera alumno irregular a quien no acredite una o más asignaturas del ciclo escolar cursado."
        },
        {
            "id": 3,
            "pregunta": "¿Qué promedio mínimo se requiere para solicitar un EXAMEN POR COMPETENCIA (Suficiencia)?",
            "opciones": ["a) 8.0", "b) 8.5", "c) 9.0", "d) No se requiere promedio"],
            "correcta": "b",
            "justificacion": "Artículo 66: Para solicitar exámenes por competencia, el alumno debe tener un promedio general mínimo de 8.5."
        },
        {
            "id": 4,
            "pregunta": "Si un alumno falta a un examen parcial por causa justificada, ¿cuántos días tiene para presentar su justificante?",
            "opciones": ["a) 24 horas", "b) 3 días hábiles", "c) 5 días hábiles", "d) 48 horas"],
            "correcta": "b",
            "justificacion": "Artículo 45: Los justificantes deben presentarse ante la Dirección de Carrera en un plazo no mayor a 3 días hábiles después de la falta."
        },
        {
            "id": 5,
            "pregunta": "¿Cuál es el límite de faltas permitidas para una materia que se imparte 2 veces por semana en un sistema de 80% de asistencia?",
            "opciones": ["a) 2 faltas", "b) 4 faltas", "c) 6 faltas", "d) 8 faltas"],
            "correcta": "c",
            "justificacion": "Cálculo basado en el Art. 40: En un cuatrimestre de 15 semanas (30 clases), el 20% permitido equivale a un máximo de 6 faltas."
        },
        {
            "id": 6,
            "pregunta": "¿Qué autoridad preside el Consejo Universitario, encargado de las sanciones más graves?",
            "opciones": ["a) El Director de Carrera", "b) El Rector", "c) El Jefe de Control Escolar", "d) El representante de docentes"],
            "correcta": "b",
            "justificacion": "Artículo 142 y definiciones: El Consejo Universitario es la máxima autoridad y es presidido por el Rector de la institución."
        },
        {
            "id": 7,
            "pregunta": "¿Se pueden revalidar materias que fueron acreditadas en otra institución mediante exámenes extraordinarios?",
            "opciones": ["a) Sí, todas", "b) No, ninguna", "c) Solo si el promedio es mayor a 9.0", "d) Solo el 50%"],
            "correcta": "b",
            "justificacion": "Artículo 93: No se otorgará equivalencia o revalidación en materias acreditadas por exámenes extraordinarios o suficiencia en otras instituciones."
        },
        {
            "id": 8,
            "pregunta": "¿Qué porcentaje de créditos debe cubrir un alumno para iniciar su SERVICIO SOCIAL?",
            "opciones": ["a) 50%", "b) 60%", "c) 70%", "d) 100%"],
            "correcta": "c",
            "justificacion": "Artículo 112: El servicio social solo puede iniciarse al haber cubierto al menos el 70% de los créditos del plan de estudios."
        },
        {
            "id": 9,
            "pregunta": "¿Cómo se considera una calificación de 5.9 en el sistema de evaluación de la universidad?",
            "opciones": ["a) Se redondea a 6.0", "b) Es reprobatoria (5.0)", "c) Es aprobatoria condicionada", "d) Depende del profesor"],
            "correcta": "b",
            "justificacion": "Artículo 56: Las calificaciones decimales se redondean solo si son superiores a 6.0. Cualquier calificación menor a 6.0 se asienta como 5.0."
        },
        {
            "id": 10,
            "pregunta": "¿Cuál es la sanción por introducir alimentos o bebidas a laboratorios o talleres?",
            "opciones": ["a) Baja definitiva", "b) Amonestación y retiro del área", "c) Multa económica", "d) Suspensión de un mes"],
            "correcta": "b",
            "justificacion": "Artículos de Disciplina: El uso inadecuado de instalaciones especiales amerita amonestación y desalojo inmediato por seguridad e higiene."
        }
    ]

    puntaje = 0
    fallas = []

    print("="*65)
    print("      SIMULADOR DE EXAMEN UC - VERSIÓN 4.0 (CASOS CRÍTICOS)")
    print("="*65)
    print("Responde con la letra correspondiente (a, b, c, d)\n")

    for p in preguntas:
        print(f"PREGUNTA {p['id']}: {p['pregunta']}")
        for opt in p['opciones']:
            print(f"  {opt}")
        
        resp = input("Tu respuesta: ").strip().lower()

        if resp == p['correcta']:
            print("¡CORRECTO! ✨\n")
            puntaje += 1
        else:
            print("INCORRECTO ❌\n")
            fallas.append(p)

    # --- RESULTADOS ---
    porcentaje = (puntaje / len(preguntas)) * 100
    print("\n" + "#"*65)
    print(f"RESUMEN DE RESULTADOS")
    print(f"Aciertos: {puntaje} / 10")
    print(f"Eficacia: {porcentaje}%")
    print("#"*65)

    # --- MÓDULO DE JUSTIFICACIONES ---
    if fallas:
        print("\nREPORTE DE JUSTIFICACIÓN DE FALLAS:")
        print("Repasa estos puntos para entender la lógica del reglamento:\n")
        for f in fallas:
            print(f"--- Pregunta {f['id']} ---")
            print(f"Tu error en: {f['pregunta']}")
            print(f"JUSTIFICACIÓN: {f['justificacion']}\n")
    else:
        print("\n¡Excelente! No tienes fallas que justificar. Tienes un dominio total.")

if __name__ == "__main__":
    simulador_cuauhtemoc_v4()  