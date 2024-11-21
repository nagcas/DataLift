# DataLift - Frontend

Il frontend di **DataLift** è costruito con **React** e **Vite** per garantire un'esperienza utente interattiva e reattiva. Questa applicazione web permette agli utenti di importare, visualizzare e interagire con i dati topografici in modo intuitivo.

## Tecnologie Utilizzate

- **React**: Libreria JavaScript per costruire interfacce utente.
- **Vite**: Strumento di build veloce per lo sviluppo di applicazioni web.
- **React Router**: Per la gestione della navigazione tra le pagine.
- **Axios**: Per effettuare richieste HTTP verso il backend.
- **Material-UI**: Framework di componenti UI per un design moderno e reattivo.
- **Chart.js** (opzionale): Per la visualizzazione grafica dei dati.

---

## Prerequisiti

Per eseguire il frontend, assicurati di avere:

- [Node.js 16+](https://nodejs.org/)
- [npm](https://npmjs.com/) o [Yarn](https://yarnpkg.com/) per la gestione delle dipendenze

---

## Installazione

### 1. Clona il repository

```bash
git clone https://github.com/tuo-username/datalift.git
cd datalift/frontend
```

### 2. Installa le dipendenze

Installa tutte le dipendenze del progetto utilizzando npm o Yarn:

#### Usando npm:

```bash
npm install
```

#### Usando Yarn:

```bash
yarn install
```

---

## Avvia il server di sviluppo

Una volta installate le dipendenze, puoi avviare il server di sviluppo con il comando:

#### Usando npm:

```bash
npm run dev
```

#### Usando Yarn:

```bash
yarn dev
```

Il frontend sarà disponibile su `http://localhost:3000` e sarà possibile iniziare a testare l'applicazione.

---

## Struttura del Frontend

```
frontend/
│
├── public/                  # Contiene il file index.html e altre risorse statiche
│
├── src/                     # La directory principale per il codice sorgente
│   ├── assets/              # Immagini e risorse statiche
│   ├── components/          # Componenti React riutilizzabili
│   ├── pages/               # Pagine principali dell'applicazione
│   ├── services/            # Funzioni di interazione con il backend (API)
│   ├── App.js               # Componente principale dell'app
│   └── index.js             # Punto di ingresso dell'applicazione
│
├── .env                     # Variabili di ambiente per configurazioni locali
├── package.json             # Gestione delle dipendenze e degli script
└── vite.config.js           # Configurazione di Vite
```

---

## API

Il frontend interagisce con il backend attraverso diverse API. Ecco alcuni degli endpoint principali:

### 1. **Importa Dati**

Per caricare i dati:

```
POST /api/data/import
```

### 2. **Recupera Dati**

Per ottenere i dati caricati:

```
GET /api/data/
```

---

## Comandi Utili

- **Avvia il server di sviluppo**: `npm run dev` o `yarn dev`
- **Build per la produzione**: `npm run build` o `yarn build`
- **Test**: `npm run test` o `yarn test` (se configurato)

---

## Testing

Per eseguire i test, puoi utilizzare il framework di testing integrato come **Jest** o **React Testing Library**.

### Esegui i test

```bash
npm run test
```

## Licenza

Questo progetto è distribuito sotto la **GNU Affero General Public License v3.0**

---

## Autori

- **Gianluca Chiaravalloti** - Sviluppatore principale

---
