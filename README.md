# Casa Vacanze - Gestione Finanziaria

Applicazione web realizzata con Django per tracciare entrate e uscite di una casa vacanze e visualizzare l'andamento del guadagno netto mensile.

## Setup del Progetto

1.  **Clona il repository:**
    ```bash
    git clone [https://github.com/maurobeltrami/gestionefinanzecasavacanze]
    ```

2.  **Crea e Attiva l'Ambiente Virtuale:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Installa le Dipendenze:**
    ```bash
    pip install django
    ```

4.  **Crea il Database e il Superutente:**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

5.  **Avvia il Server:**
    ```bash
    python manage.py runserver
    ```
