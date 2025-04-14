monitoring-dashboard/
│
├── backend/
│   ├── app.py                 # Flask/FastAPI main file
│   ├── routes/
│   │   └── metrics.py         # API routes for system metrics
│   └── utils/
│       ├── collect.py         # Bash/python for system data
│       └── db.py              # Database interactions
│
├── scripts/
│   ├── monitor.sh             # Shell script to collect system info
│   └── cronjob.txt            # Setup example for crontab
│
├── frontend/
│   ├── index.html             # Dashboard UI
│   ├── styles.css             # Minimalist black/white theme
│   └── scripts.js             # Fetch metrics and update DOM
│
├── static/
│   └── charts/                # Optional graphs with Chart.js
│
├── templates/                # Jinja2 if using Flask
│
├── database/
│   └── logs.db                # SQLite/MySQL database
│
└── README.md
