# Google ADK: AI Diagnostic Agent

## Project Goal

This project aims to build a simple AI agent designed to conduct initial medical diagnostic interviews. The agent will interact with a user (simulating a patient) in a conversational manner to gather a comprehensive medical history and relevant clinical data. The ultimate goal is to collect sufficient information to formulate a well-reasoned differential diagnosis, mirroring the initial steps of a clinical encounter.


## The Diagnostic Process

The agent will engage in a dynamic, multi-turn conversation to build a clinical picture. This process of sequential diagnosis involves:

1.  **Initiating the Encounter:** Starting with the patient's chief complaint.
2.  **Iterative Questioning:** Asking a series of targeted questions to explore the history of the present illness, review of systems, and past medical history.
3.  **Hypothesis Generation:** Internally forming and refining a list of possible diagnoses (a differential diagnosis) based on the information gathered.

The agent's objective is not to provide a final diagnosis, but to perform an efficient information-gathering process, which is a critical first step in patient care.

## Typical Diagnostic Information to be Collected

To construct a comprehensive patient case, the agent will be designed to collect the following categories of information:

- **Chief Complaint (CC):** The primary reason the patient is seeking medical attention (e.g., "chest pain," "headache for 3 days").
  - **Complaint:** The primary reason the patient is seeking medical attention (e.g., "chest pain," "headache for 3 days").
  - **Onset:** When did it start? Was it sudden or gradual?
  - **Severity:** On a scale of 1 to 10, how bad is it?
  - **Alleviating/Aggravating factors:** What makes it better or worse?

- **Past Medical History (PMH):**

  - Chronic illnesses (e.g., diabetes, hypertension)
  - Past surgeries and hospitalizations
  - Major accidents or injuries

- **Medications and Allergies:**

  - List of current medications, including dosage and frequency (prescription, over-the-counter, supplements).
  - Known allergies to medications or other substances and the nature of the reaction.

- **Social History (SH):**

  - Occupation and living situation.
  - Use of tobacco, alcohol, and illicit substances.
  - Diet and exercise habits.

## Requirements

- Python 3.12 (see `requires-python` in `pyproject.toml`)
- PDM (Python package manager)
- Docker and Docker Compose (optional, for containerized run)

---

## Environment Variables

- **GEMINI_API_KEY**: required. See `env.template` for the expected variable name.
  - Local: create a `.env` file and add your key, or export it in your shell.
  - Docker: Docker Compose will read `.env` automatically and pass the value through.

Copy the template and edit:

```bash
cp env.template .env
```

Example `.env` file:

```bash
GEMINI_API_KEY=your_api_key_here
```

Or export in your shell session:

```bash
export GEMINI_API_KEY=your_api_key_here
```

---

## Using PDM

PDM is a modern Python package/dependency manager that uses `pyproject.toml` and isolates environments. Common actions:

- Install PDM:
  - macOS/Linux via pipx: `pipx install pdm`
  - or: `python3 -m pip install --user pdm`
- Select Python 3.12 (if needed): `pdm use -f 3.12`
- Install dependencies: `pdm install`
- Run project commands: prefix with `pdm run`, e.g. `pdm run python -V`

---

## Local Installation & Run (no Docker)

1) Install dependencies

```bash
pdm install
```

2) Ensure `GEMINI_API_KEY` is set (see above).

3) Run the web UI (defaults to `localhost:8000`):

```bash
pdm run adk web src
```

Optional flags (example):

```bash
pdm run adk web src --host 0.0.0.0 --port 8000
```

4) Run the agent in interactive console mode:

```bash
pdm run adk run src/diagnostic_agent
```

## Run via Docker/Makefile

This repo includes a `Makefile` and `docker-compose.yml` to streamline builds and runs. Ensure `GEMINI_API_KEY` is available (e.g., in `.env`).

- Build images:

```bash
make build
```

- Start the web UI (exposes `${DIAGNOSTIC_AGENT_PORT:-8000}` → container `8000`):

```bash
make web
# or override the port
DIAGNOSTIC_AGENT_PORT=8080 make web
```

- Run interactive console agent:

```bash
make console
```

- Stop containers and remove orphans/volumes:

```bash
make stop
```

- Full reset (remove images/volumes, then rebuild):

```bash
make reset
```

Under the hood:
- Web uses: `pdm run adk web src --host 0.0.0.0` (see `docker-compose.yml`).
- Console uses: `pdm run adk run src/diagnostic_agent` (see `Makefile`).

---

## Notes

- The agent graph is defined in `src/diagnostic_agent/agent.py` and exposed via `root_agent` for ADK.
- The agent requires `GEMINI_API_KEY` to operate, as outlined in `env.template` and passed through in `docker-compose.yml`.
