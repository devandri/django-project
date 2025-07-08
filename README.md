# ⚙️ Installation Guide

## 📦 Step 1: Create Virtual Environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
````

## 📦 Step 2: Install Requirements

```bash
pip install -r requirements.txt
```

## 🛠️ Step 3: Set Up `.env` File

Create a `.env` file in the project root:

```env
DB_NAME=restaurant_db
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=3306
```

## ⚡ Step 4: Run Migrations

```bash
python manage.py migrate
```

## ✅ Step 5: Start Development Server

```bash
python manage.py runserver
```