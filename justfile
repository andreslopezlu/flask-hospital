# Justfile Maestro para Python (uv + ruff + mypy)
# -----------------------------------------------------------------------------
# Jerarquía: Proto -> Light -> Ready -> Review -> Strict
# -----------------------------------------------------------------------------

# --- Variables ---
python  := "uv run python"
pytest  := "uv run pytest"
ruff    := "uv run ruff"
mypy    := "uv run mypy"
pc      := "uv run pre-commit"
ipython := "uv run ipython"
ptw     := "uv run ptw"

# --- Ayuda ---

# Muestra la lista de comandos disponibles y sus descripciones
# Uso: $ just
default:
    @just --list

# --- Inicialización ---

# Configura el proyecto desde cero (Git, venv y TODAS las librerías de desarrollo)
# Uso: $ just init
init:
    git init
    uv sync --all-groups
    @echo "📦 Instalando ecosistema de desarrollo..."
    uv add --dev ruff mypy pytest pytest-cov pytest-watch pre-commit ipython
    @just pc-install
    @echo "✅ Repositorio Git inicializado y entorno sincronizado."
    @echo "🚀 Proyecto listo para el desarrollo profesional."

# --- Gestión de Dependencias ---

# Sincroniza el entorno virtual con el archivo de bloqueo
# Uso: $ just sync
sync:
    uv sync --all-groups

# Actualiza o genera el archivo de bloqueo uv.lock
# Uso: $ just lock
lock:
    uv lock

# Instala una dependencia de producción
# Uso: $ just install pandas
install package:
    uv add "{{package}}"

# Instala una dependencia de desarrollo
# Uso: $ just dev-add ipykernel
dev-add package:
    uv add --dev "{{package}}"

# Muestra el árbol de dependencias para detectar conflictos
# Uso: $ just dev-tree
dev-tree:
    uv tree

# --- Calidad de Código (Ruff) ---

# Revisa errores de lógica y estilo (solo lectura)
# Uso: $ just lint
lint:
    {{ ruff }} check .

# Formatea el código siguiendo el estándar del proyecto
# Uso: $ just format
format:
    {{ ruff }} format .

# REPARA Y FORMATEA: Solo continúa al formato si el linter no encuentra errores fatales
# Uso: $ just fix
fix:
    {{ ruff }} check --fix . && {{ ruff }} format .

# --- Tipado Estático (Mypy) ---

# Nivel 0: Sin validación de tipos (chequeo sintáctico)
# Uso: $ just type-none
type-none:
    {{ mypy }} . --ignore-errors --follow-imports=skip

# Nivel 1: Validación baja (rápida, ignora imports faltantes)
# Uso: $ just type-low
type-low:
    {{ mypy }} . --ignore-missing-imports --follow-imports=silent

# Nivel 2: Validación intermedia (recomendada para desarrollo diario)
# Uso: $ just type-medium
type-medium:
    {{ mypy }} . --ignore-missing-imports --warn-unused-ignores --warn-redundant-casts --warn-return-any

# Nivel 3: Validación alta (exige tipos en todas tus funciones)
# Uso: $ just type-high
type-high:
    {{ mypy }} . --disallow-untyped-defs --check-untyped-defs --warn-unused-ignores --warn-redundant-casts --warn-return-any --no-implicit-optional

# Nivel 4: Validación estricta total (modo CI serio)
# Uso: $ just type-strict
type-strict:
    {{ mypy }} . --strict

# --- Testing (Pytest) ---

# Ejecuta todos los tests de forma rápida
# Uso: $ just test
test:
    {{ pytest }}

# Ejecuta tests con reporte de cobertura en terminal
# Uso: $ just test-cov
test-cov:
    {{ pytest }} --cov=. --cov-report=term-missing

# Ejecuta tests de un archivo específico
# Uso: $ just test-file tests/test_logic.py
test-file file:
    {{ pytest }} {{ file }}

# --- Pre-commit ---

# Instala los hooks de git en el repositorio
# Uso: $ just pc-install
pc-install:
    {{ pc }} install

# Ejecuta todos los hooks en todos los archivos
# Uso: $ just pc-run
pc-run:
    {{ pc }} run --all-files

# Ejecuta hooks en modo estricto (muestra diferencias al fallar)
# Uso: $ just pc-strict
pc-strict:
    {{ pc }} run --all-files --show-diff-on-failure

# Commit saltando validaciones de hooks (emergencias)
# Uso: $ just commit-lazy "mensaje"
commit-lazy msg:
    git commit -m "{{ msg }}" --no-verify

# --- Pipelines de Validación (Jerarquía de Rigor) ---

# 1. PROTO: "Limpiar y Seguir". Auto-reparación rápida de estética.
# Uso: $ just check-proto
check-proto:
    @echo "🧹 Nivel PROTO: Auto-reparando..."
    @just fix

# 2. LIGHT: Verificación rápida de lógica y sintaxis básica.
# Uso: $ just check-light
check-light:
    @echo "🚀 Nivel LIGHT: Verificación rápida + Tests..."
    @just lint
    @just type-low
    @just test

# 3. READY: Calidad estándar antes de registrar cambios (Commit).
# Uso: $ just check-ready
check-ready:
    @echo "⚖️ Nivel READY: Calidad estándar + Cobertura + Hooks..."
    @just lint
    @just type-medium
    @just test-cov
    @just pc-run

# 4. REVIEW: Rigor para revisiones de código o Pull Requests.
# Uso: $ just check-review
check-review:
    @echo "🔍 Nivel REVIEW: Alta exigencia de tipos + Hooks..."
    @just lint
    @just type-high
    @just test-cov
    @just pc-run

# 5. STRICT: Validación implacable para CI/CD y Producción.
# Uso: $ just check-strict
check-strict:
    @echo "🛡️ Nivel STRICT: Rigor máximo de CI..."
    uv sync --locked
    {{ ruff }} format --check .
    @just lint
    @just type-strict
    @just test
    @just pc-strict

# --- Desarrollo Interactivo (Watch Mode) ---

# Monitorea cambios y ejecuta Ruff automáticamente
# Uso: $ just watch-lint
watch-lint:
    {{ ruff }} check --watch .

# Monitorea cambios y ejecuta Pytest automáticamente
# Uso: $ just watch-test
watch-test:
    {{ ptw }} .

# Monitorea cambios y aplica formato automáticamente (requiere 'entr')
# Uso: $ just watch-format
watch-format:
    @echo "👀 Observando archivos para auto-formatear..."
    find . -name "*.py" | entr {{ ruff }} format /_

# --- Ejecución ---

# Lanza el REPL de Python estándar
# Uso: $ just repl
repl:
    {{ python }}

# Lanza la consola interactiva IPython
# Uso: $ just shell
shell:
    {{ ipython }}

# Ejecuta un script directo
# Uso: $ just run main.py
run script:
    {{ python }} {{ script }}

# Ejecuta un paquete como módulo con argumentos
# Uso: $ just mod my_app.api --port 8000
mod module *args:
    {{ python }} -m {{ module }} {{ args }}

# --- Mantenimiento ---

# Limpieza total de archivos temporales y cachés
# Uso: $ just clean
clean:
    rm -rf .pytest_cache .mypy_cache .ruff_cache .venv dist
    find . -type d -name "__pycache__" -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete
    @echo "✨ Proyecto limpio."
