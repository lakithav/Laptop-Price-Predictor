# Quick Start: Deploy to Render

## 🚀 Fast Track Deployment (5 Minutes)

### 1. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit for Render deployment"
git remote add origin https://github.com/YOUR_USERNAME/laptop-price-predictor.git
git push -u origin main
```

### 2. Create Web Service on Render

- Go to [render.com](https://render.com) and sign up
- Click **New +** → **Web Service**
- Connect your GitHub repository
- Configure:
  - **Name**: laptop-price-predictor
  - **Build Command**: `pip install -r requirements.txt`
  - **Start Command**: `cd website && gunicorn app:app`
  - **Plan**: Free
- Click **Create Web Service**

### 3. Wait & Access

- Wait 3-5 minutes for build
- Access at: `https://your-app-name.onrender.com`

---

## ⚡ Key Commands

### Build Command:

```
pip install -r requirements.txt
```

### Start Command:

```
cd website && gunicorn app:app
```

---

## 🔄 Update Deployed App

```bash
git add .
git commit -m "Your changes"
git push origin main
```

Render auto-deploys on push!

---

## ⚠️ Remember:

- Free tier spins down after 15 min inactivity
- First request after sleep: 30-60 sec delay
- Check logs in Render dashboard for errors

See **RENDER_DEPLOYMENT_GUIDE.md** for complete guide!
