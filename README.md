# API Testing Showcase

🔍 Proyecto orientado a demostrar pruebas automatizadas sobre endpoints REST usando **Pytest**, **Postman** y un client propio en Python.

Esto es una réplica personalizada para practicar software. No es copy-paste, sino una forma de iterar sobre lo aprendido.

---

## 🧰 Tecnologías y herramientas

- `Pytest` y `pytest-cov` para unit tests + reporte de cobertura
- Mock de tokens JWT para simular autenticación
- Client de consumo de API (`src/api_client.py`)
- Colección exportada de Postman (`postman/api-testing-collection.json`)
- Carpeta `tests/` con casos de prueba y configuración

---

## 📦 Estructura del Proyecto

```plaintext
📁 APITestingShowcase/
├── 🧠 src/
│   └── 📄 api_client.py                → Cliente HTTP para consumir la API
├── 🧪 tests/
│   ├── 🧪 test_endpoints.py            → Casos de prueba automatizados
│   ├── 🧪 conftest.py                  → Fixture con JWT mockeado
│   └── 📦 requirements.txt             → Dependencias de testing
├── 🧰 postman/
│   └── 📄 api-testing-collection.json  → Colección exportada desde Postman
├── 📖 README.md                        → Documentación técnica y motivacional
└── 🧙‍♂️ venv/                            → Entorno virtual de Python (ignorado en Git)

---

💡 Motivación
Este proyecto forma parte de mi portfolio técnico como desarrollador backend y QA. Busca mostrar prácticas de testing reproducible, seguridad básica en el consumo de APIs, y presentación profesional mediante estructura clara y narrativa.

🔐 En desarrollo futuro

-Integración con CI/CD para ejecución automática.

-Testeo sobre API propia (FastAPI / Spring Boot).

-Validación de response schema con JSONSchema.
