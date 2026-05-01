import os
import time

def limpiar_pantalla():
    # Limpia la consola según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def examen_interactivo_uc():
    preguntas = [
        {
            "id": 1,
            "pregunta": "¿Qué sucede con los trámites de un alumno que no entrega su documentación original en el plazo de 60 días?",
            "opciones": ["a) Se le cobra una multa", "b) Se cancelan los trámites sin responsabilidad para la UC", "c) Se le permite seguir pero sin derecho a beca", "d) Se le suspende por un ciclo"],
            "correcta": "b",
            "feedback": "Artículo 8: La falta de entrega de documentos originales en el plazo previsto (60 días naturales) causará la cancelación de los trámites escolares."
        },
        {
            "id": 2,
            "pregunta": "¿Con cuánto tiempo de anticipación se debe solicitar una BAJA TEMPORAL para que no afecte el historial?",
            "opciones": ["a) 24 horas antes", "b) 15 días hábiles antes de los exámenes finales", "c) En cualquier momento del ciclo", "d) Al inicio del siguiente ciclo"],
            "correcta": "b",
            "feedback": "Artículo 84: La solicitud de baja temporal debe hacerse por escrito al menos 15 días hábiles antes del periodo de exámenes finales."
        },
        {
            "id": 3,
            "pregunta": "¿A quién debe dirigirse el alumno para solicitar una baja definitiva voluntaria?",
            "opciones": ["a) Al Rector", "b) Al profesor titular", "c) Al Departamento de Control Escolar", "d) Al Consejo Universitario"],
            "correcta": "c",
            "feedback": "Artículo 87: Todo alumno que desee darse de baja definitiva voluntariamente debe solicitarlo por escrito ante Control Escolar."
        },
        {
            "id": 4,
            "pregunta": "¿Qué requisito es indispensable para realizar actividades en laboratorios y clínicas?",
            "opciones": ["a) Tener promedio de 9.0", "b) Portar el uniforme y equipo de protección completo", "c) Haber pagado el seguro de vida", "d) Ser alumno de último año"],
            "correcta": "b",
            "feedback": "Artículos de Uso de Instalaciones: Es obligatorio el uso de uniforme, gafete y equipo de protección personal para ingresar y permanecer en áreas técnicas."
        },
        {
            "id": 5,
            "pregunta": "En el sistema SEMESTRAL, ¿cuántos exámenes parciales se aplican antes del final?",
            "opciones": ["a) Dos", "b) Tres", "c) Cuatro", "d) Uno"],
            "correcta": "b",
            "feedback": "Artículo 48: El sistema semestral contempla tres periodos de evaluaciones parciales y una evaluación final."
        },
        {
            "id": 6,
            "pregunta": "¿Cuál es la vigencia de un dictamen de REVALIDACIÓN o equivalencia?",
            "opciones": ["a) Un año", "b) Toda la carrera", "c) El ciclo escolar en que se emite", "d) No tiene vigencia"],
            "correcta": "c",
            "feedback": "Artículo 95: Los dictámenes de equivalencia tienen vigencia únicamente por el ciclo escolar para el cual fueron emitidos."
        },
        {
            "id": 7,
            "pregunta": "¿Qué documento es OBLIGATORIO presentar para poder realizar cualquier examen?",
            "opciones": ["a) El recibo de pago", "b) Identificación oficial o credencial de la Universidad", "c) El reglamento firmado", "d) Una carta del director"],
            "correcta": "b",
            "feedback": "Artículo 42: Para tener derecho a examen, el alumno deberá presentar su credencial de la Universidad o identificación oficial vigente."
        },
        {
            "id": 8,
            "pregunta": "¿Puede un alumno irregular solicitar una BECA académica?",
            "opciones": ["a) Sí, si tiene necesidad económica", "b) No, debe ser alumno regular", "c) Solo si el Director lo autoriza", "d) Sí, con promedio de 8.0"],
            "correcta": "b",
            "feedback": "Reglamento de Becas/Permanencia: Uno de los requisitos generales para mantener o solicitar apoyos es mantener el estatus de alumno regular (no adeudar materias)."
        },
        {
            "id": 9,
            "pregunta": "¿Quién es el responsable de cubrir los gastos médicos si un alumno sufre un accidente fuera de la Universidad sin relación a actividades académicas?",
            "opciones": ["a) La Universidad", "b) El Seguro Estudiantil (si aplica)", "c) El alumno/padres", "d) El Consejo Universitario"],
            "correcta": "c",
            "feedback": "Artículo 105-107: La Universidad solo responde por incidentes dentro de sus instalaciones o en actividades oficiales autorizadas bajo el amparo del seguro contratado."
        },
        {
            "id": 10,
            "pregunta": "Si un alumno reprueba un examen EXTRAORDINARIO de una materia seriada, ¿qué sucede?",
            "opciones": ["a) Puede cursar la siguiente materia", "b) No puede cursar la materia consecuente", "c) Se le da de baja inmediata", "d) Debe pagar una multa"],
            "correcta": "b",
            "feedback": "Artículo 31: El alumno no podrá cursar asignaturas que tengan como antecedente una materia no acreditada (seriación)."
        }
    ]

    puntaje = 0
    total = len(preguntas)

    limpiar_pantalla()
    print("==============================================================")
    print("   SIMULADOR UC v5.0 - APRENDIZAJE CON RETROALIMENTACIÓN")
    print("==============================================================\n")

    for p in preguntas:
        print(f"PREGUNTA {p['id']}: {p['pregunta']}")
        for opt in p['opciones']:
            print(f"  {opt}")
        
        while True:
            resp = input("\nTu respuesta (a, b, c, d): ").lower().strip()
            if resp in ['a', 'b', 'c', 'd']:
                break
            print("Por favor, elige una opción válida.")

        if resp == p['correcta']:
            print("\n✅ ¡CORRECTO!")
            puntaje += 1
        else:
            print(f"\n❌ INCORRECTO (La opción correcta era la {p['correcta']})")
        
        # Retroalimentación inmediata
        print(f"FUNDAMENTO: {p['feedback']}")
        print("\nPresiona ENTER para continuar a la siguiente pregunta...")
        input()
        limpiar_pantalla()

    # Resultado Final
    porcentaje = (puntaje / total) * 100
    print("==============================================================")
    print("                     EXAMEN FINALIZADO")
    print("==============================================================")
    print(f"Puntaje Obtenido: {puntaje} / {total}")
    print(f"Porcentaje de Acierto: {porcentaje}%")
    print("==============================================================")

    if porcentaje >= 90:
        print("Resultado: NIVEL EXPERTO. Dominas el reglamento.")
    elif porcentaje >= 70:
        print("Resultado: NIVEL COMPETENTE. Conoces lo básico, repasa los fallos.")
    else:
        print("Resultado: REPASO NECESARIO. Lee nuevamente el PDF adjunto.")

if __name__ == "__main__":
    examen_interactivo_uc()    