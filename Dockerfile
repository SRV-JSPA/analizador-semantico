# Imagen base
FROM ubuntu:24.04

# Evitar prompts interactivos
ENV DEBIAN_FRONTEND=noninteractive

# Paquetes base: Python, venv, pip, Java (para ANTLR), y utilidades
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-venv \
    python3-pip \
    openjdk-17-jdk \
    curl \
    ca-certificates \
    bash-completion \
    fontconfig \
    fonts-dejavu \
 && rm -rf /var/lib/apt/lists/*

# ===== ANTLR =====
# Copia el JAR de ANTLR y los scripts antlr/grun que ya tienes en ./commands/
# Estructura esperada en tu repo:
#   antlr-4.13.1-complete.jar
#   commands/antlr
#   commands/grun
COPY antlr-4.13.1-complete.jar /usr/local/lib/antlr-4.13.1-complete.jar
COPY ./commands/antlr /usr/local/bin/antlr
COPY ./commands/grun  /usr/local/bin/grun
RUN chmod +x /usr/local/bin/antlr /usr/local/bin/grun

# Variables de entorno para que java encuentre el jar de ANTLR
ENV CLASSPATH=".:/usr/local/lib/antlr-4.13.1-complete.jar"
ENV JAVA_TOOL_OPTIONS=""

# ===== Python venv =====
# Creamos un venv en /opt/venv y lo usamos por defecto vía PATH
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"

# Asegurar pip actualizado dentro del venv
RUN pip install --no-cache-dir --upgrade pip wheel

# ===== Dependencias Python =====
# Copia primero requirements.txt para aprovechar la cache de Docker
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
 && rm -f /tmp/requirements.txt

# ===== Workspace por defecto =====
# Tu comando de ejecución monta la carpeta local ./program en /program
WORKDIR /program

# Opcional: copia un script para crear venv local si alguna vez lo necesitas dentro
# (si ya tienes python-venv.sh y lo usas, descomenta las dos líneas siguientes)
# COPY python-venv.sh /usr/local/bin/python-venv.sh
# RUN chmod +x /usr/local/bin/python-venv.sh

# Comando por defecto: shell interactivo
CMD ["bash"]
