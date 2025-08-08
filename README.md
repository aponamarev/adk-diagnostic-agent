# Closed Loop: AI Diagnostic Agent

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

- **Family History (FH):** Health status of immediate family members, with a focus on heritable conditions (e.g., heart disease, cancer, genetic disorders).

- **Social History (SH):**

  - Occupation and living situation.
  - Use of tobacco, alcohol, and illicit substances.
  - Diet and exercise habits.
