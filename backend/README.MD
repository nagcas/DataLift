# DataLift - Backend

Il backend di **DataLift** è costruito con **Django** e **Django REST Framework** per fornire un'API RESTful robusta e scalabile per l'importazione, l'elaborazione e la gestione dei dati topografici. Questo repository contiene il codice per la gestione del database, la logica di business e l'esposizione delle API al frontend.

## Tecnologie Utilizzate

- **Django**: Framework web Python per sviluppare applicazioni web scalabili e sicure.
- **Django REST Framework (DRF)**: Toolkit potente per la costruzione di API RESTful con Django.
- **PostgreSQL**: Database relazionale utilizzato per gestire i dati.
- **Django Channels** (opzionale): Per la gestione della comunicazione in tempo reale (se necessaria).
- **Celery** (opzionale): Per l'esecuzione di attività in background, come l'elaborazione di dati complessi.

---

## Prerequisiti

Per eseguire il backend, assicurati di avere:

- [Python 3.8+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/) o un altro database supportato
- [Pip](https://pip.pypa.io/en/stable/) per la gestione delle dipendenze Python
- [Virtualenv](https://virtualenv.pypa.io/en/stable/) per creare un ambiente virtuale (facoltativo)

---

## Installazione

### 1. Clona il repository

```bash
git clone https://github.com/tuo-username/datalift.git
cd datalift/backend
```

### 2. Crea un ambiente virtuale (opzionale, ma consigliato)

```bash
python -m venv env
source env/bin/activate  # Su macOS/Linux
env\Scripts\activate  # Su Windows
```

### 3. Installa le dipendenze

Installa tutte le dipendenze del progetto nel tuo ambiente virtuale:

```bash
pip install -r requirements.txt
```

### 4. Configura il database

#### Creazione del database (PostgreSQL)

Crea un database PostgreSQL per il progetto. Puoi farlo direttamente tramite la shell PostgreSQL:

```bash
psql -U postgres
CREATE DATABASE datalift;
```

#### Configura le variabili di ambiente

Crea un file `.env` nella cartella `backend` e definisci le seguenti variabili:

```bash
DEBUG=True
SECRET_KEY=la_tua_chiave_segreta
DATABASE_URL=postgres://user:password@localhost:5432/datalift
```

Sostituisci `user` e `password` con le credenziali del tuo database PostgreSQL.

### 5. Esegui le migrazioni

Esegui le migrazioni del database per creare le tabelle necessarie:

```bash
python manage.py migrate
```

---

## Avvia il server di sviluppo

Una volta configurato il backend, puoi avviare il server di sviluppo di Django con il seguente comando:

```bash
python manage.py runserver
```

Il server sarà disponibile su `http://localhost:8000`. Puoi iniziare a testare l'API e interagire con essa tramite Postman, Insomnia o un altro client HTTP.

---

## Struttura del Backend

```
backend/
│
├── datalift/                # La directory principale del progetto Django
│   ├── __init__.py
│   ├── settings.py          # Configurazione di Django (incluso il database)
│   ├── urls.py              # URL routing del backend
│   ├── wsgi.py              # WSGI per il deployment in produzione
│   ├── asgi.py              # ASGI per la gestione di WebSockets, se usato
│   ├── apps/                # Directory per le applicazioni Django
│   ├── migrations/          # Migrazioni del database
│   └── admin.py             # Configurazioni per l'admin di Django
│
├── manage.py                # Script di gestione di Django
├── requirements.txt         # Dipendenze Python
└── .env                     # Variabili di ambiente per la configurazione
```

---

## API

Il backend espone diverse API per interagire con i dati topografici. Ecco alcune delle principali API disponibili:

### 1. **Importa Dati**

Endpoint per caricare file di dati (CSV, JSON, XML):

```
POST /api/data/import
```

### 2. **Recupera Dati**

Endpoint per ottenere i dati caricati:

```
GET /api/data/
```

### 3. **Filtra e Elabora Dati**

Endpoint per elaborare i dati in base a parametri di filtro:

```
GET /api/data/filtered
```

---

## Testing

Per eseguire i test sul backend, puoi utilizzare `pytest` o il framework di test integrato di Django.

### Esegui i test

```bash
python manage.py test
```

I test si trovano nella cartella `datalift/tests/`.

## Licenza

Questo progetto è distribuito sotto la **GNU Affero General Public License v3.0**

---

## Autori

- **Gianluca Chiaravalloti** - Sviluppatore principale
