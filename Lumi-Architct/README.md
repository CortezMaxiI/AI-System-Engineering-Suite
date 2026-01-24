# 🏗️ Lumi: Architect
### AI-Powered Infrastructure Forge for Windows

![IaC Architect](https://img.shields.io/badge/Role-IaC_Architect-magenta?style=for-the-badge&logo=terraform)
![AI-Driven Automation](https://img.shields.io/badge/Logic-AI--Driven_Automation-cyan?style=for-the-badge&logo=openai)
![Windows System Engineer](https://img.shields.io/badge/System-Windows_System_Engineer-blue?style=for-the-badge&logo=windows)

**Lumi: Architect** es un agente de software avanzado que transforma requerimientos en lenguaje natural en entornos de desarrollo listos para usar. Utilizando Inteligencia Artificial y una capa de ejecución idempotente, Lumi permite que cualquier programador configure su estación de trabajo en minutos, garantizando seguridad y consistencia.

---

## 🧠 El Concepto

El despliegue de entornos de desarrollo suele ser un proceso manual, propenso a errores y que consume mucho tiempo. Lumi actúa como un **Arquitecto de Sistemas** que:

1. **Razona** sobre las herramientas necesarias.
2. **Valida** la compatibilidad y el estado actual del sistema.
3. **Ejecuta** la instalación de forma automatizada y segura.

---

## 🚀 The Neural-to-Script Pipeline

Lumi no es un simple instalador; es un sistema experto que procesa el conocimiento técnico a través de varias capas:

1.  **Neural Processor (Brain):** Recibe el lenguaje natural (ej: *"Necesito un entorno para Data Science con Python"*) y utiliza **Chain-of-Thought (CoT)** para inferir no solo el lenguaje, sino también las Build Tools, extensiones de VS Code y variables de entorno necesarias.
2.  **Architecture Manifest:** La IA genera un JSON estructurado y validado bajo un esquema estricto que define el plan de ejecución.
3.  **The Forge (Executor):** Un motor de PowerShell procesa el manifiesto, realizando una **Discovery Phase** para asegurar la idempotencia.
4.  **Health Check:** Una validación post-instalación que asegura que todos los binarios están en el PATH y operativos.

---

## 🛠️ Stack Tecnológico & Arquitectura

El sistema se basa en una arquitectura de **"Separación de Preocupaciones" (SoC)** dividida en tres capas core:

### 1. The Brain (Capa de IA) - `Python`
*   **Prompt Engineering:** Implementa *Chain-of-Thought (CoT)* para forzar a la IA a razonar antes de generar código.
*   **JSON Schema:** Los planes de arquitectura se validan contra un esquema estricto para asegurar que la ejecución sea predecible.

### 2. The Forge (Capa de Ejecución) - `PowerShell`
*   **Idempotencia:** Antes de instalar, el sistema realiza una *Discovery Phase*. Si el binario ya existe, se omite para evitar redundancia.
*   **Safety Gate:** Sistema de filtrado de comandos para prevenir ejecuciones maliciosas o no deseadas.

### 3. The Orchestrator - `Python & Rich`
*   **Interfaz de usuario (CLI):** Estilo Cyberpunk mediante la librería `Rich`.
*   **Soporte Multi-Gestor:** Integración nativa con `Winget` y `Chocolatey`.

---

## ✨ Características Principales

*   ✅ **Instalación Inteligente:** Detecta dependencias cruzadas (ej: no instala un IDE de C# sin el SDK de .NET).
*   ✅ **Detección Automática:** Si ya tenés Git o VS Code, Lumi lo reconoce y sigue adelante.
*   🔍 **Health Check (Reporte de Salud):** Valida que los binarios instalados respondan correctamente en la terminal después de la forja.
*   🧪 **Modo Demo:** Incluye un flag `--demo` para demostraciones técnicas sin consumo de API real.

---

## 📂 Estructura del Proyecto

```text
Lumi-Architect/
├── brain/      # Lógica de razonamiento e integración con LLM
├── forge/      # Scripts de automatización en PowerShell (Idempotentes)
├── docs/       # Documentación técnica y SRS
├── schemas/    # Contratos de datos (JSON Schema)
├── output/     # Historial de manifiestos generados
└── main.py     # Punto de entrada del sistema
```

---

## 💻 Cómo ejecutarlo

### 1. Requisitos
*   Python 3.10+
*   PowerShell 7 (Recomendado)
*   Conexión a Internet

### 2. Instalación
```bash
git clone https://github.com/tu-usuario/Lumi-Architect.git
cd Lumi-Architect/Lumi-Architect
pip install -r requirements.txt
```

### 3. Lanzamiento
```bash
# Modo interactivo (Requiere API Key)
python main.py

# Modo demostración (Sin API Key)
python main.py --demo
```

---

## 🎓 Perfil del Desarrollador
Este proyecto demuestra habilidades avanzadas en:
*   **IA & Agentes:** Orquestación de modelos de lenguaje para tareas operativas complejas.
*   **DevOps & Automatización:** Gestión de infraestructura como código (IaC) a nivel local.
*   **Arquitectura de Software:** Diseño modular, manejo de errores robusto y validación de esquemas.

---

> **Nota para el Reclutador:** Lumi: Architect no es solo un script de instalación; es una prueba de concepto sobre cómo los Agentes de IA pueden eliminar la fricción técnica en los equipos de ingeniería, permitiendo que el talento humano se enfoque en crear valor, no en configurar herramientas.
