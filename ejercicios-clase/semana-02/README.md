# Semana 02 — Configuración del entorno de trabajo

## Crear y activar el entorno virtual (raíz del repositorio)

```bash
python3 -m venv venv
source venv/bin/activate
```

El prompt debe mostrar el prefijo `(venv)`. Para salir: `deactivate`.

## Instalar dependencias y registrar versiones

```bash
pip install matplotlib
pip freeze > requirements.txt
```

## Reproducir el entorno en otra máquina

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```