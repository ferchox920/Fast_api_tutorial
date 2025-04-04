### 📄 `README.md`

```markdown
# 🚀 FastAPI + PostgreSQL Starter

Proyecto base para construir una API REST usando **FastAPI**, **SQLAlchemy** y **PostgreSQL** con una estructura modular y escalable.

---

## 📁 Estructura del proyecto

```
fast-api/
│
├── app/
│   ├── api/               # Rutas (endpoints)
│   ├── core/              # Configuración y variables de entorno
│   ├── db/                # Conexión y sesión de base de datos
│   ├── models/            # Modelos de SQLAlchemy
│   ├── schemas/           # Validaciones con Pydantic
│   ├── services/          # Lógica de negocio
│   └── main.py            # Punto de entrada de la aplicación
│
├── .env                   # Variables de entorno (no subir a Git)
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Este archivo
```

---

## ⚙️ Requisitos

- Python 3.11 o superior
- PostgreSQL 12+
- pip

---

## 🧪 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/fastapi-postgres.git
cd fastapi-postgres
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

- En Windows:

```bash
venv\Scripts\activate
```

- En Unix/Mac:

```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Configurar variables de entorno

Crear un archivo `.env` en la raíz con este contenido:

```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=tu_contraseña
DB_NAME=fastapi_db
```

### 6. Crear la base de datos (si no existe)

```sql
-- Desde psql:
CREATE DATABASE fastapi_db;
```

Opcional: crear un usuario exclusivo para esta base.

---

## 🛠 Inicializar tablas

Desde `app/main.py`, se puede importar una función temporal de `init_db` para crear las tablas automáticamente:

```python
from app.db.init_db import init_db
init_db()
```

¡Recordá luego sacarlo!

---

## 🚀 Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```

La API estará disponible en: [http://localhost:8000](http://localhost:8000)

Documentación automática:
- Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📫 Endpoints disponibles

```
GET     /api/v1/users/        → Listar usuarios
POST    /api/v1/users/        → Crear nuevo usuario
```

Ejemplo para crear usuario:

```json
{
  "name": "Fernando Ramones",
  "email": "ferchox@example.com"
}
```

---

## 🧩 To-Do

- [ ] Endpoint para obtener usuario por ID o email
- [ ] Autenticación con JWT
- [ ] Pruebas unitarias
- [ ] Dockerización

---

## 👨‍💻 Autor

Desarrollado por **Fernando Ramones** 🧠  
Contacto: [fernandoramones92@gmail.com]

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Libre de usar, modificar y mejorar.
```

---

¿Querés que agreguemos una sección con instrucciones para Docker más adelante? ¿O lo dejamos así de liviano por ahora?