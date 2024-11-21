# DataLift

**DataLift** è un'applicazione web avanzata progettata per l'importazione, l'elaborazione e la visualizzazione di dati topografici. Con un backend potente basato su Django e un frontend intuitivo creato con React e Vite, questa piattaforma è pensata per offrire un'esperienza utente fluida e scalabile, ideale per i professionisti del settore.

---

## Features

- **Importazione Dati**: Carica dati topografici in vari formati (CSV, JSON, XML) per un'elaborazione avanzata.
- **Elaborazione Dati**: Manipola, filtra e analizza i dati per ottenere informazioni dettagliate sulla topografia.
- **Visualizzazione Dati**: Visualizza i dati su mappe interattive, grafici e tabelle personalizzabili.
- **API REST**: Interagisci con il backend tramite un'API RESTful costruita con Django REST Framework.

---

## Tecnologie Utilizzate

- **Backend**:
  - [Django](https://www.djangoproject.com/) - Framework Python per lo sviluppo di applicazioni web robuste.
  - [Django REST Framework](https://www.django-rest-framework.org/) - Toolkit potente per la creazione di API RESTful.
  - [PostgreSQL](https://www.postgresql.org/) - Database relazionale per gestire i dati.
  
- **Frontend**:
  - [React](https://reactjs.org/) - Libreria JavaScript per costruire interfacce utente interattive.
  - [Vite](https://vitejs.dev/) - Build tool veloce e moderno per React.
  - [Leaflet](https://leafletjs.com/) - Libreria per la creazione di mappe interattive.

- **Altre Tecnologie**:
  - [Docker](https://www.docker.com/) - Containerizzazione dell'applicazione per un ambiente di sviluppo uniforme.
  - [Nginx](https://www.nginx.com/) - Web server per la gestione delle richieste di produzione.

---

## Prerequisiti

Assicurati di avere i seguenti strumenti installati:

- [Python 3.8+](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/en/download/)
- [Docker](https://www.docker.com/get-started) (facoltativo per l'esecuzione tramite container)

---

## Installazione

### 1. Clona il repository

```bash
git clone https://github.com/tuo-username/datalift.git
cd datalift
```

### 2. Configura l'ambiente virtuale per il backend (Django)

```bash
cd backend
python -m venv env
source env/bin/activate  # Su macOS/Linux
env\Scripts\activate  # Su Windows
```

### 3. Installa le dipendenze del backend

```bash
pip install -r requirements.txt
```

### 4. Configura il frontend (React con Vite)

```bash
cd frontend
npm install
```

### 5. Configura le variabili di ambiente

Nel backend, crea un file `.env` con le seguenti variabili:

```bash
DEBUG=True
SECRET_KEY=la_tua_chiave_segreta
DATABASE_URL=postgres://user:password@localhost:5432/datalift
```

Nel frontend, configura le variabili di ambiente per Vite creando un file `.env` con:

```bash
VITE_API_URL=http://localhost:8000/api
```

### 6. Avvia il server

#### Backend (Django)

```bash
cd backend
python manage.py migrate
python manage.py runserver
```

#### Frontend (React con Vite)

```bash
cd frontend
npm run dev
```

Ora puoi accedere all'app dal tuo browser su `http://localhost:3000` (frontend) e `http://localhost:8000` (backend).

---

## Struttura del Progetto

```
datalift/
│
├── backend/                # Contiene il codice backend Django
│   ├── datalift/           # Directory principale del progetto Django
│   ├── manage.py           # Script di gestione Django
│   ├── requirements.txt    # Dipendenze Python
│   └── .env                # Variabili di ambiente backend
│
├── frontend/               # Contiene il codice frontend React
│   ├── src/                # Codice sorgente React
│   ├── public/             # File pubblici (index.html, etc.)
│   ├── package.json        # Configurazione npm e dipendenze
│   └── .env                # Variabili di ambiente frontend
│
└── .gitignore              # File per ignorare file inutili su Git
```

---

## Contribuire

1. Fork questo repository.
2. Crea un branch per la tua feature (`git checkout -b feature-nome`).
3. Commit i tuoi cambiamenti (`git commit -am 'Aggiungi nuova feature'`).
4. Pusha nel tuo branch (`git push origin feature-nome`).
5. Crea una pull request.

---

## Licenza

Questo progetto è distribuito sotto la **GNU Affero General Public License v3.0**

---

## Autori

- **Gianluca Chiaravalloti** - Sviluppatore principale

---
