from pathlib import Path
from dotenv import load_dotenv
import os

# Carpeta raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Ruta del archivo .env
ENV_PATH = BASE_DIR / ".env"

# Cargar variables de entorno
load_dotenv(ENV_PATH)

# Leer API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError(
        f"No se encontró OPENAI_API_KEY en {ENV_PATH}"
    )

# Rutas del proyecto
DATA_DIR = BASE_DIR / "data"
VECTOR_DB_DIR = BASE_DIR / "vector_db"

# Parámetros de chunking
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K = 3