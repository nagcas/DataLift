# 🌟 **DataLift** 🌟  
**DataLift** è un'applicazione web avanzata per l'importazione, l'elaborazione e la visualizzazione di dati topografici generati da stazioni totali.  
Offre strumenti per analisi approfondite e una rappresentazione visiva chiara e intuitiva.

---

## 🚀 **Caratteristiche**
- 📂 Importazione file CSV con dati topografici.  
- 📊 Calcolo di distanza ridotta, dislivelli e visualizzazione 3D.  
- 🌍 Mappe interattive basate su Leaflet.  
- 🔐 Sistema di autenticazione sicuro.  
- 📈 Grafici intuitivi per analisi dettagliate.  

---

## 🛠️ **Tecnologie Utilizzate**
### **Frontend**  
- ⚛️ **React.js**  
- 📦 Librerie principali:  
  - [Bootstrap](https://getbootstrap.com/) per lo styling e i componenti UI.   
  - [Axios](https://axios-http.com/) per le richieste API.  
  - [React-Leaflet](https://react-leaflet.js.org/) per le mappe.  
  - [Chart.js](https://www.chartjs.org/) per i grafici.  

### **Backend**  
- 🚀 **FastAPI**: Framework moderno per API RESTful.  
- 🐍 Librerie principali:  
  - [Pandas](https://pandas.pydata.org/) per l'elaborazione dati.  
  - [SQLAlchemy](https://www.sqlalchemy.org/) per la gestione del database.  
  - [Uvicorn](https://www.uvicorn.org/) per l'avvio del server.  

---

## 📦 **Dipendenze**
### **Frontend**  
```json
{
  "dependencies": {
    "@testing-library/jest-dom": "^5.17.0",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "antd": "^5.22.1",
    "axios": "^1.7.7",
    "bootstrap": "^5.3.3",
    "bootstrap-icons": "^1.11.3",
    "chart.js": "^4.4.6",
    "react": "^18.3.1",
    "react-bootstrap": "^2.10.5",
    "react-dom": "^18.3.1",
    "react-leaflet": "^4.2.1",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4"
  }
}
```

### **Backend**  
- `fastapi[standard]`  
- `uvicorn`  
- `pandas`  
- `sqlalchemy`  

---

## 🛠️ **Installazione**

### **Backend**
1. Clona il repository:  
   ```bash
   git clone https://github.com/tuo-utente/datalift.git
   cd datalift/backend
   ```
2. Crea un ambiente virtuale:  
   ```bash
   python -m venv env
   source env/bin/activate  # Su Windows: .\env\Scripts\activate
   ```
3. Installa le dipendenze:  
   ```bash
   pip install "fastapi[standard]" uvicorn pandas sqlalchemy
   ```
4. Avvia il server:  
   ```bash
   uvicorn main:app --reload
   ```

---

### **Frontend**
1. Vai nella directory del frontend:  
   ```bash
   cd ../frontend
   ```
2. Installa le dipendenze:  
   ```bash
   npm install
   ```
3. Avvia l'app React:  
   ```bash
   npm start
   ```

---

## 🌐 **Struttura del Progetto**
```
DataLift/
│
├── backend/
│   ├── main.py         # File principale per il server FastAPI
│   ├── models.py       # Definizioni dei modelli
│   ├── routers/        # Endpoint delle API
│   ├── services/       # Logica di elaborazione dati
│   └── requirements.txt # Dipendenze del backend
│
├── frontend/
│   ├── public/         # File statici
│   ├── src/            # Componenti React
│   │   ├── components/ # Componenti principali
│   │   ├── pages/      # Pagine dell'app
│   │   ├── App.js      # File principale React
│   └── package.json    # Dipendenze del frontend
│
└── README.md           # Documentazione del progetto
```

---

## 🧪 **Test**
### **Backend**  
Utilizza **Postman** per testare gli endpoint API di FastAPI.  

### **Frontend**  
Esegui i test di React:  
```bash
npm test
```

## 📜 **Licenza**  
Distribuito sotto licenza **GNU Affero General Public License v3.0**

---

Grazie per aver scelto **DataLift**! 😊
