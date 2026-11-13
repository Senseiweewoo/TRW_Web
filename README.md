# 📚 School Library Web Application

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Senseiweewoo/TRW_Web)

An interactive, responsive School Library portal built with **Flask**, featuring real-time catalog search, subject category filtering, a detailed book modal, and a simulated borrowing system.

---

## ✨ Features

- **📖 Curated Catalog**: Includes literature classics, adventure novels, science publications, and computer engineering references (*Computer Networks*, *Clean Code*, *Introduction to Algorithms*).
- **🔍 Multi-Field Search & Filter**: Real-time keyword filtering across title, author, category, and ISBN with a quick-reset button.
- **🏷️ Category Filter Chips**: One-click pills (*All*, *Fiction*, *Classic Literature*, *Adventure*, *Computer Engineering*, *Science*).
- **📋 Interactive Book Modal**: View complete synopsis, shelf call number (`📍 Shelf E-01`), ISBN, page count, and real-time availability badges (🟢 *Available*, 🟡 *Borrowed*, 🔴 *Reserved*).
- **🔄 Live Borrowing Workflow**: Asynchronous `/api/borrow/<id>` toggle updating book availability with instant feedback toasts.
- **📱 Responsive Mobile Navigation**: Collapsible hamburger menu and fluid grid adapting to phones, tablets, and desktops.
- **🚀 Vercel-Ready**: Serverless configuration via `vercel.json` and `api/index.py`.

---

## 📁 Project Structure

```text
TRW_Web/
├── api/
│   └── index.py            # Vercel serverless entry point
├── TRW_Web/
│   ├── static/
│   │   ├── images/         # High-resolution book covers & library hero
│   │   └── style.css       # Design tokens & responsive styles
│   ├── templates/
│   │   └── index.html      # Accessible HTML5 template with modal
│   └── app.py              # Flask app & catalog API routes
├── requirements.txt        # Python dependencies (Flask, gunicorn)
├── vercel.json             # Vercel rewrites configuration
├── run.py                  # Local launcher script
└── README.md
```

---

## 🛠️ Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Senseiweewoo/TRW_Web.git
   cd TRW_Web
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**:
   ```bash
   python run.py
   ```

4. Open `http://127.0.0.1:5000` in your web browser.

---

## ☁️ Deploy to Vercel

### 1-Click Deploy
Click the button below to import and deploy directly to Vercel:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Senseiweewoo/TRW_Web)

### Manual Deploy via Vercel Dashboard
1. Go to [vercel.com/new](https://vercel.com/new).
2. Click **Import** next to `Senseiweewoo/TRW_Web`.
3. Click **Deploy**. Vercel will build and assign your live `.vercel.app` domain automatically.
