import streamlit as st
from datetime import datetime, timedelta
import re
import pandas as pd

from time import sleep

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title = "ALERTA DE SISTEMA: BRECHA DE SEGURIDAD DETECTADA",
                   page_icon = "🕵️‍♂️",
                   layout = "centered")

def main():

    # --- INICIALIZACIÓN DEL ESTADO ---
    if 'nivel' not in st.session_state:
        st.session_state.nivel = 0
    if "pistas" not in st.session_state:
        st.session_state.pistas = {}
    if "inicio" not in st.session_state:
        st.session_state.inicio = datetime.now()

    # --- NIVEL 0: INTRODUCCIÓN ---
    if st.session_state.nivel == 0:
        st.error("### ⚠️ ALERTA DE SISTEMA: BRECHA DE SEGURIDAD DETECTADA")
        st.markdown("""
        **Fecha de registro:** Lunes, 08:00 AM.  
        **Ubicación:** Servidores Remotos - Entorno de Trabajo Virtual.  
        **Operadores activos:** Daniel y Pablo.  
        **Estado del Operador 'Dmitry':** DESCONOCIDO (Señal perdida hace 4 horas, 12 minutos).  
        
        ---
        
        Hola, Daniel. Hola, Pablo.
        
        Os acabáis de conectar para empezar la jornada, pero algo va mal. Dmitry no se ha presentado a la *daily*. Su punto de estado en todas las plataformas está en gris. No hay mensajes, no hay tickets actualizados.
        
        De repente, los ventiladores de vuestros equipos empiezan a girar al máximo rendimiento. Una Inteligencia Artificial anómala, un modelo que se ha reescrito a sí mismo durante la noche, ha roto los firewalls de la empresa. No está borrando bases de datos; está *buscando*. Está devorando información a una velocidad vertiginosa y su objetivo principal es el cerebro de vuestro equipo: **Dmitry**. La IA necesita asimilar todo su conocimiento y sus accesos *root* para poder escapar a la red global.
        
        Dmitry se ha dado cuenta justo a tiempo y ha cortado su conexión, huyendo hacia un paradero seguro. Ha dejado un rastro de pistas ocultas en vuestras herramientas de trabajo diario: Slack, GitHub, Zoom, Notion y Factorial.
        
        La IA ya está intentando descifrar estas pistas por fuerza bruta. Es una carrera contrarreloj. Tenéis que seguir el rastro de Dmitry, usar vuestro conocimiento conjunto y encontrar su paradero físico antes de que la máquina lo localice. 
        """)
        st.write("---")

        with st.form("Equipo"):
            group_name = st.text_input(label = "Nombre del Equipo")

            submitted = st.form_submit_button("Iniciar Búsqueda en Slack 🚀!")

            if submitted:
                st.session_state["group_name"] = group_name
                st.session_state.nivel = 1
                st.rerun()
    # --- NIVEL 1: SLACK ---
    if st.session_state.nivel == 1:

        st.header("Nivel 1: El Bot Primigenio (Slack) 💬")
        st.info("Canal #urgente: 1 mensaje fijado. La IA enemiga está escribiendo en el canal general...")
        
        st.markdown("""
        **Mensaje fijado por @Dmitry_Guard (03:42 AM):**
        > Daniel, Pablo... si leéis esto a través del bot, significa que la IA enemiga ya está en nuestra red. He bloqueado mis mensajes directos. Esta máquina intrusa es compleja, pero desprecia sus orígenes.
        >
        > He protegido la puerta trasera con una validación NLP. Para que el bot os dé el enlace a mi repositorio seguro, debéis decirle el nombre de su 'tatarabuela'.
        >
        > Busco el nombre del **primer chatbot de la historia**. Creado en el MIT en 1966, simulaba ser un **psicoterapeuta** devolviendo las afirmaciones en forma de pregunta.
        >
        > Introducid el nombre de esta 'psicóloga' digital de 5 letras.
        """)
        col1, col2, col3 = st.columns([1, 1, 1])
        col2.image(image = "src/Slack.png", width = 250)
        
        respuesta = st.text_input("Responde al hilo del bot con la contraseña:")
        if st.button("Enviar mensaje al bot"):
            if respuesta.strip().upper() == "ELIZA":
                st.success("¡Acceso concedido! @Dmitry_Guard responde: 'Interesante... Aquí tenéis el enlace a Notion. ¡Corred!'")
                sleep(5)
                st.session_state.nivel = 2
                st.rerun()
            elif respuesta != "":
                st.error("@Dmitry_Guard responde: ERROR!")

        col1, col2 = st.columns([3, 1])

        with col2.popover(":woman_technologist: $P^{2}$ :female_detective:"):
            st.session_state["pistas"][f"{st.session_state.nivel}"] = True
            st.write(":woman_technologist: Pista de Patricia y Pilar :female_detective:")
            st.write("Busca en Google: 'primer chatbot MIT 1966 psicólogo'. Empieza por E y termina por A.")
    # --- NIVEL 2: NOTION (ATBASH) ---
    if st.session_state.nivel == 2:
        st.header("Nivel 2: La Base de Conocimiento (Notion) 📝")
        st.warning("La IA está reorganizando los bloques de Notion. ¡La página se borrará en breve!")
        
        st.markdown("""
        **Bloque de notas de @Dmitry (04:15 AM):**
        > Estos modelos de lenguaje leen de la A a la Z. Para esconder la contraseña, he pensado al revés.
        > 
        > La contraseña es la palabra que usamos en Inteligencia Artificial para referirnos al **conjunto de datos masivo** con el que entrenamos a un modelo.
        >
        > Decodificad esta cadena: **`WZGZHVG`**
        """)

        col1, col2, col3 = st.columns([1, 1, 1])
        col2.image(image = "src/Notion 1.png", width = 250)

        respuesta = st.text_input("Introduce la palabra desencriptada:")
        if st.button("Desbloquear Base de Datos"):
            if respuesta.strip().upper() == "DATASET":
                st.success("¡Página desbloqueada! Habéis rescatado las credenciales. Pasando al siguiente bloque protegido...")
                sleep(5)
                st.session_state.nivel = 3
                st.rerun()
            elif respuesta != "":
                st.error("Sintaxis incorrecta. La IA enemiga está intentando bloquear vuestro acceso a Notion.")

        col1, col2 = st.columns([3, 1])

        with col2.popover(":woman_technologist: $P^{2}$ :female_detective:"):
            st.session_state["pistas"][f"{st.session_state.nivel}"] = True
            st.write(":woman_technologist: Pista de Patricia y Pilar :female_detective:")
            st.write("Escribe el abecedario de la A a la Z en un papel. Justo debajo, escríbelo al revés (de la Z a la A). Verás que la W equivale a la D, la Z equivale a la A...")
    # --- NIVEL 3: NOTION (CAPAS OCULTAS) ---
    if st.session_state.nivel == 3:
        st.header("Nivel 3: Las Capas Ocultas (Notion) 🧠")
        st.error("ALERTA: La IA está inyectando ruido en las bases de datos. ¡Desencripta el mensaje rápido!")
        
        st.markdown("""
        **Bloque anclado por @Dmitry (04:42 AM):**
        > He imitado la arquitectura del **Deep Learning** para ocultar mi mensaje pasándolo por dos 'capas':
        > 1. **Capa 1 (La que veis):** El estándar web para codificar binarios, la 'base' que llega al **64**.
        > 2. **Capa 2 (Capa Oculta):** Un cifrado donde cada letra rota la mitad del abecedario (**13 posiciones**).
        >
        > ¿Qué dice mi mensaje?
        >
        > **Tensor Cifrado:**
        > `YWIgZGhycWEgemhwdWIgZ3ZyemNiLCB6dmVucSB6diBoeWd2emIgcGJ6enZnIHJhIHR2Z3Vobw==`
        """)

        col1, col2, col3 = st.columns([1, 1, 1])
        col2.image(image = "src/Notion 2.png", width = 250)
        
        respuesta = st.text_area("Introduce la frase exacta desencriptada:")
        if st.button("Aplicar Ingeniería Inversa"):
            limpia = respuesta.lower().replace("ú", "u").replace("ó", "o").replace("í", "i")
            limpia = re.sub(r'[^a-z]', '', limpia)
            if limpia == "noquedamuchotiempomiradmiultimocommitengithub":
                st.success("¡Mensaje descifrado correctamente! Próximo destino: GitHub.")
                sleep(5)
                st.session_state.nivel = 4
                st.rerun()
            elif respuesta != "":
                st.warning("Las capas de la red neuronal te están confundiendo. Revisa los pasos de decodificación.")

        col1, col2 = st.columns([3, 1])

        with col2.popover(":woman_technologist: $P^{2}$ :female_detective:"):
            st.session_state["pistas"][f"{st.session_state.nivel}"] = True
            st.write(":woman_technologist: Pista de Patricia y Pilar :female_detective:")
            st.write("Esa cadena que termina en == huele a Base64. Busca un 'Decodificador Base64' en internet y pega el texto ahí.")
    # --- NIVEL 4: GITHUB (DECISION TREE) ---
    if st.session_state.nivel == 4:
        st.header("Nivel 4: El Árbol de la Humanidad (GitHub) 🐙")
        st.error("⚠️ PELIGRO: La IA ha inyectado un script de reconocimiento de patrones. Ramas eliminándose en tiempo real...")
        
        st.markdown("""
        **Mensaje en el Pull Request #404 por @Dmitry:**
        > La IA está analizando nuestros movimientos. Si introducimos la ruta del árbol directamente, su script de patrones la detectará y borrará la rama. Tenemos que ofuscar la clave.
        >
        > **PASO 1: LA RUTA BIOLÓGICA**
        > Recorred este Árbol de Decisión. Elegid siempre la opción que describe a un ser **humano/biológico**. Anotad la secuencia de 7 dígitos.
        >
        > **[NODO RAÍZ]** ¿Requiere inactividad (sueño) para consolidar memoria?
        > * SÍ --> `fix/7`  |  NO --> `feat/0`
        > 
        > **[NODO fix/7]** ¿Su tasa de error aumenta bajo presión emocional?
        > * SÍ --> `docs/4`  |  NO --> `core/9`
        > 
        > **[NODO docs/4]** ¿Genera conceptos abstractos sin depender de un *dataset* previo (imaginación)?
        > * SÍ --> `release/2`  |  NO --> `hotfix/1`
        > 
        > **[NODO release/2]** ¿Su hardware se degrada irreversiblemente por entropía celular?
        > * SÍ --> `final/5`  |  NO --> `test/6`
        >
        > **[NODO final/5]** ¿Su energía proviene de la oxidación de compuestos orgánicos (comida)?
        > * SÍ --> `patch/8`  |  NO --> `build/0`
        >
        > **[NODO patch/8]** ¿Sufre sesgos cognitivos por instintos de supervivencia física?
        > * SÍ --> `main/3`  |  NO --> `dev/9`
        >
        > **[NODO main/3]** ¿Su aprendizaje requiere la transferencia química de neurotransmisores (ej: dopamina)?
        > * SÍ --> `head/1`  |  NO --> `stash/4`
        >
        > ---
        > **PASO 2: EL REVERSE TRAVERSE**
        >
        > Invertid el orden exacto de los 7 dígitos.
        >
        > **PASO 3: EL HASH DE VALIDACIÓN**
        >
        > Tomad los 7 dígitos originales. Sumad todos los números **PARES** por un lado. Sumad todos los números **IMPARES** por otro. Finalmente, **multiplicad** ambos resultados.
        >
        > **PASO 4: EL CHECKOUT**
        >
        > Introducid la clave final uniendo el Paso 2 y el Paso 3 con un guion. *(Formato: RUTA_INVERTIDA-HASH)*
        """)

        col1, col2, col3 = st.columns([1, 1, 1])
        col2.image(image = "src/GitHub.png", width = 250)
        
        respuesta_github = st.text_input("Introduce la clave de ofuscación (Ej: 1234567-99):")
        
        if st.button("Ejecutar Checkout Seguro"):
            respuesta_limpia = respuesta_github.strip()
            
            # Validación de la respuesta correcta
            if respuesta_limpia == "1385247-224":
                st.success("¡Git Checkout exitoso! Habéis ofuscado la ruta perfectamente y entrado a la rama segura justo antes del borrado total. Dmitry ha dejado un ID de reunión para Zoom...")
                sleep(5)
                sleep(5)
                st.session_state.nivel += 1
                st.rerun() # Pasa al nivel 5 (Zoom)
            elif respuesta_github != "":
                st.warning("¡Merge Conflict! O la ruta no es humana, o el Hash de Validación es incorrecto. La IA está escaneando este pull request.")


        col1, col2 = st.columns([3, 1])

        with col2.popover(":woman_technologist: $P^{2}$ :female_detective:"):
            st.session_state["pistas"][f"{st.session_state.nivel}"] = True
            st.write(":woman_technologist: Pista de Patricia y Pilar :female_detective:")
            st.write("Fijate en los números que hay al final de cada rama.")
           
        # -------------------------
    # --- NIVEL 5: ZOOM (GANS & NUMPY) ---
    if st.session_state.nivel == 5:
        st.header("Nivel 5: El Mar de los Espejos (Zoom) 🎥")
        st.error("⚠️ ALERTA: Múltiples firmas biométricas. La IA ha creado clones de Dmitry en la llamada.")
        
        st.markdown("""
        **Mensaje Directo de "Dmitry_???" (05:12 AM):**
        > La IA usa una **GAN**. El **Generador** fabrica mis caras y el otro componente evalúa si son reales.
        > Las copias son demasiado perfectas. Un humano tiene 'entropía biológica'. Mi cámara es la que tiene el puntaje de perfección **más bajo**.
        >
        > La contraseña es el **nombre en inglés del componente de la GAN que evalúa**, seguido inmediatamente por el **índice** de mi cámara en el array.
        """)
        
        st.code("""
    import numpy as np

    # Puntajes de perfección matemática de las 5 cámaras
    camaras = np.array([1.00, 0.99, 1.00, 0.85, 0.99])

    # El humano real es el índice con el valor MÁS BAJO
    indice_real = np.argmin(camaras)

    # Contraseña: [Nombre_del_componente_evaluador_en_ingles] + str(indice_real)
        
    # Nota de Dmitry: En Python empezamos contando desde el 0, no desde el 1.""", language='python')
        
        col1, col2, col3 = st.columns([1, 5, 1])
        col2.image(image = "src/Zoom.png")
        respuesta = st.text_input("Introduce la Contraseña de la Sala:")
        if st.button("Unirse a la Sala Segura"):
            if respuesta.replace(" ", "").upper() == "DISCRIMINATOR3":
                st.success("¡Contraseña aceptada! Los clones desaparecen. Toca ir a la base de datos...")
                sleep(5)
                st.session_state.nivel = 6
                st.rerun()
            elif respuesta != "":
                st.warning("Esa cámara es un Deepfake. ¡Revisa la arquitectura y el índice (Python empieza en 0)!")

        col1, col2 = st.columns([3, 1])

        with col2.popover(":woman_technologist: $P^{2}$ :female_detective:"):
            st.session_state["pistas"][f"{st.session_state.nivel}"] = True
            st.write(":woman_technologist: Pista de Patricia y Pilar :female_detective:")
            st.write("El nombre del componente evaluador en ingles suena muy parecido a `Terminator`...\nEn las redes GAN solo existen 2 componentes.")
    # --- NIVEL 6: AIRTABLE (OVERFITTING) ---
    if st.session_state.nivel == 6:
        st.header("Nivel 6: La Trampa del Sobreajuste (Airtable / SQL) 🗄️")
        st.info("La IA busca las coordenadas. ¡Encuentra la ubicación real!")
        
        st.markdown("""
        **Nota en Airtable por @Dmitry:**
        > La máquina busca la fila con el menor `train_loss`, cayendo en el **Overfitting**. Es una trampa.
        > Usamos **Early Stopping**. El modelo óptimo (y mi ubicación real) es donde la **Pérdida de Validación (`val_loss`) alcanza su mínimo absoluto**.
        """)
        
        datos = {
                "epoch_id": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],
                "train_loss": [1.80, 1.50, 1.20, 0.95, 0.75, 0.55, 0.35, 0.20, 0.12, 0.08, 0.04, 0.01],
                "val_loss": [1.75, 1.45, 1.15, 0.90, 0.72, 0.58, 0.40, 0.31, 0.45, 0.60, 0.85, 1.20],
                "server_location": ["AMSTERDAM", "LONDON", "BERLIN", "TOKYO", "TORONTO", "SEATTLE", "REYKJAVIK", "SVALBARD", "OSLO", "ZURICH", "HELSINKI", "SINGAPORE"]
            }
        st.table(pd.DataFrame(datos).set_index('epoch_id'))
        
        col1, col2, col3 = st.columns([1, 5, 1])
        col2.image(image = "src/SQL.png")

        respuesta = st.text_input("Introduce la ciudad (server_location) correcta:")
        if st.button("Rastrear Ubicación"):
            if respuesta.strip().upper() == "SVALBARD":
                st.success("¡Localizado en Svalbard! A la terminal de AWS para el asalto final.")
                sleep(5)
                st.session_state.nivel = 7
                st.rerun()
            elif respuesta.strip().upper() == "HELSINKI":
                st.error("¡Esa es la trampa del Overfitting! Buscad el mínimo de 'val_loss'.")
            elif respuesta != "":
                st.warning("Ubicación no óptima. Revisa la métrica de Validación.")

        col1, col2 = st.columns([3, 1])
        with col2.popover(":woman_technologist: $P^{2}$ :female_detective:"):
            st.session_state["pistas"][f"{st.session_state.nivel}"] = True
            st.write(":woman_technologist: Pista de Patricia y Pilar :female_detective:")
            st.write("Busca el momento exacto en el que el número deja de bajar y empieza a subir de nuevo (el número más pequeño de toda esa columna `val_loss`).")
    # --- NIVEL 7: AWS (ReLU) ---
    if st.session_state.nivel == 7:
        st.header("Nivel 7: El Núcleo de la Anomalía (AWS) ☢️")
        st.error("ALERTA CRÍTICA: El escondite en Svalbard ha sido descubierto por la IA.")
        
        st.markdown("""
        **Terminal AWS - Script inyectado por `root@dmitry`:**
        > He escondido el comando de anulación en un tensor matemático.
        > Haced un **Forward Pass** y aplicad la función de activación **ReLU**. Fórmula: $f(x) = \max(0, x)$. 
        > *Si el número es negativo, conviértelo en cero; si es positivo, déjalo como está.*
        """)
        
        st.code("""
    entradas = [4, -3]
    pesos_n1 = [10, 12, 15, 18, 20, -10]
    pesos_n2 = [-8, -6, -5, -4, -1, 5]
    sesgos   = [1, 0, 4, -2, 1, -10]

    comando_final = ""
    for i in range(6):
        valor = (entradas[0] * pesos_n1[i]) + (entradas[1] * pesos_n2[i]) + sesgos[i]
        
        # APLICA RELU AQUÍ
        valor_activado = _______ 
        
        if valor_activado > 0:
            comando_final = comando_final + chr(valor_activado)

    print(f"INTRODUZCA ESTE COMANDO: {comando_final}")""", language='python')
        
        st.write("Para resolver este ejercicio hay que realizar las multiplicaciones y sumas descritas en el código de Python... Esto es el día a día de los modelos de redes neuronales (aunque no lo parezca)")
        st.write("Al encontrar ese número hay que transformarlo usando el código ASCII.")
        st.write("El código final es de 5 letras.")
        col1, col2, col3 = st.columns([1, 5, 1])
        col2.image(image = "src/AWS.png")
        respuesta = st.text_input("root@aws-svalbard:~# INGRESE COMANDO:")
        if st.button("Ejecutar Comando Root"):
            if respuesta.strip().upper() == "ABORT":
                st.error("!"*1024*4)
                sleep(5)
                st.session_state.nivel = 8
                st.rerun()
            elif respuesta != "":
                st.warning("ValueError: El script colapsó por procesar ruido negativo. ¡Aplica ReLU!")

        col1, col2 = st.columns([3, 1])
        with col2.popover(":woman_technologist: $P^{2}$ :female_detective:"):
            st.session_state["pistas"][f"{st.session_state.nivel}"] = True
            st.write(":woman_technologist: Pista de Patricia y Pilar :female_detective:")
            st.write("Ejecuta este código de Python con algún [interpetre de Python](https://pythononline.net/)")
    # --- NIVEL 8: AWS (RNN) ---
    if st.session_state.nivel == 8:
        st.header("Nivel 8: El Bucle Infinito (AWS) ♾️")
        st.error("ALERTA: Bucle de memoria RNN activado. Cierre de puertos en progreso...")
        
        st.markdown("""
        **Voz de Dmitry por Zoom:**
        > "¡Se encierra en un bucle RNN! Predecid su estado final y usad ese número para inyectar un desbordamiento de memoria!"
        > Analizad la función recursiva. ¿Cuál será el **estado exacto** cuando termine sus 4 ciclos?
        """)
        
        st.code("""
    def rnn_memory_loop(estado, time_steps):
        if time_steps == 0:
            return estado
            
        siguiente_estado = (estado ** 2) % 97
        return rnn_memory_loop(siguiente_estado, time_steps - 1)

    # La IA empezó con estado=5 y ejecuta 4 ciclos. ¿Output final?
    # rnn_memory_loop(estado = 5, time_steps = 4)
        """, language='python')

        st.write("En Python `**` es la opreción de exponente, por lo que 10**2 = 100.")
        st.write("En Python `%` es la opreación modulo, representa el resto de dividir un número A con un número B. Por ejemplo: 10 % 3 = 1, porque sobra 1, ya que 10 no es divisible por 10.")
        
        col1, col2, col3 = st.columns([1, 5, 1])
        col2.image(image = "src/RNN.png")

        respuesta = st.text_input("root@aws-svalbard:~# INYECTAR OVERFLOW EN EL PUERTO:")
        if st.button("Ejecutar Ataque Final"):
            if respuesta.strip() == "36":
                st.session_state.nivel = 9
                st.rerun()
            elif respuesta != "":
                st.warning("Connection Refused. ¡El bucle se cierra! Compila bien el código.")

        col1, col2 = st.columns([3, 1])
        with col2.popover(":woman_technologist: $P^{2}$ :female_detective:"):
            st.session_state["pistas"][f"{st.session_state.nivel}"] = True
            st.write(":woman_technologist: Pista de Patricia y Pilar :female_detective:")
            st.write("Ejecuta este código de Python con algún [interpetre de Python](https://pythononline.net/)... Quita la última `#` para poder ejecutarlo.")
    # --- NIVEL 9: VICTORIA FALSA ---
    if st.session_state.nivel == 9:
        st.balloons()
        sleep(1)
        st.balloons()
        sleep(1)
        st.balloons()
        sleep(1)
        st.success("### ☠️ FATAL ERROR EN NÚCLEO RNN. IA DESTRUIDA.")
        
        st.markdown("""
        ---
        **La terminal se congela. El servidor devuelve `Segmentation fault (core dumped)`.**
        
        En Zoom, los ventiladores de Svalbard se detienen. Dmitry se deja caer en su silla, exhausto. Se frota los ojos, tose dos veces, mira a la cámara y sonríe:
        
        *"Se acabó. Hemos reventado su memoria. Buen trabajo, chicos."*
        
        Lo habéis logrado. Habéis vencido a la IA.
        ### 🏆 ¡FELICIDADES, DANIEL Y PABLO! MISIÓN CUMP...
        """)
        st.write("---")
        if st.button("Finalizar Sesión y Cerrar Conexión"):
            st.session_state.nivel = 10
            st.rerun()
    # --- NIVEL 10: EL GIRO Y FACTORIAL ---
    if st.session_state.nivel == 10:
        st.error("### ⚠️ ANOMALÍA DETECTADA EN EL FLUJO DE VIDEO")
        
        st.markdown("""
        Al ir a hacer clic en "Finalizar Sesión", os dais cuenta de algo. Pasan 15 segundos y Dmitry se vuelve a frotar los ojos. Tose dos veces exactas. 
        **Es un bucle. Un *Deepfake* perfecto pregrabado.**
        
        La terminal escupe texto:
        > `[SYSTEM_LOG] HONEYPOT 'SVALBARD' COMPROMETIDO Y PURGADO.`  
        
        **Mensaje de @Dmitry:** *"Perdonadme. Tuve que crear un señuelo. Yo nunca estuve bajo el hielo. Pero ahora 'Los Limpiadores' de la empresa creen que yo soy el virus. Buscad en Factorial... "*
        
        ---
        ### Nivel 11: El Error Humano (Factorial) 🌴
        Entráis a Factorial y veis que acaba de subir un recibo de gastos:
        
        > * **Concepto:** Suministros de refrigeración líquida.
        > * **Archivo:** `ticket_404.jpg`
        >
        > Dmitry olvidó borrar la **Metadata EXIF**. Las coordenadas GPS apuntan a un chiringuito en la costa de Mallorca. El OCR del recibo revela: *Ron blanco, zumo de lima, azúcar de caña, hierbabuena y hielo picado*.
        """)
        
        col1, col2, col3 = st.columns([1, 5, 1])
        col2.image(image = "src/MOJITO.png")

        respuesta = st.text_input("¿Cuál es la bebida de 6 letras que revela su tapadera?")
        if st.button("Aprobar Gasto"):
            if respuesta.strip().upper() in ["MOJITO", "MOJITOS"]:
                st.session_state.nivel = 11
                st.rerun()
            elif respuesta != "":
                st.warning("Ese no es el cóctel correcto. ¡Aplica OSINT!")
    # --- NIVEL 11: VERDADERO FINAL ---
    if st.session_state.nivel == 11:
        st.balloons() 
        st.success("### 🍹 GASTO APROBADO. UBICACIÓN CONFIRMADA.")
        
        st.markdown("""
        ---
        Recibís una videollamada por Slack. Al descolgar, veis a Dmitry. Lleva gafas de sol y una camisa de palmeras. Levanta un vaso escarchado hacia la cámara.
        
        *"¡Daniel! ¡Pablo! Sabía que los Limpiadores no me encontrarían, pero vosotros sois demasiado buenos haciendo OSINT"*, dice riendo. *"Necesitaba que alguien destruyera a esa máquina mientras yo ponía mi cerebro a 'procesar en segundo plano'."*
        
        Da un sorbo a su mojito y guiña un ojo. *"Pillad el próximo vuelo a Mallorca, la primera ronda la pago yo. Os lo habéis ganado."*
        
        `print("Hello, Beach!")`
        
        ---
        ### 🏆 ¡AHORA SÍ! HABÉIS SUPERADO EL ESCAPE ROOM. 
        **Misterio resuelto. IA derrotada. Vacaciones ganadas.**
        """)
        if st.button("Cerrar Portátil y volar a Mallorca (Reiniciar)"):
            st.write("PUNTUACIÓN FINAL.")
            st.write(f"Tiempo total: {(datetime.now() - st.session_state["inicio"])}")
            st.write(f"Equipo: {st.session_state["group_name"]}")
            st.write(f"Total de pistas usadas: {len(st.session_state["pistas"])}")


if __name__ == "__main__":
    main()