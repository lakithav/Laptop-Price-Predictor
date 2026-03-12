# Complete Guide: Deploy Laptop Price Predictor to Render

This guide will walk you through deploying your Flask-based Laptop Price Predictor website to Render, a cloud platform that offers free web service hosting.

## 📋 Prerequisites

- A GitHub account
- Your project code ready to push to GitHub
- A Render account (free - sign up at [render.com](https://render.com))

---

## 🚀 Step-by-Step Deployment Process

### Step 1: Prepare Your Project Structure

Your project should have the following structure:

```
Laptop-Price-Predictor/
├── website/
│   ├── app.py
│   ├── model/
│   │   └── predictor.pickle
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   └── Procfile (optional for Render)
├── requirements.txt
└── README.md
```

**Important:** Render will run from the root of your repository, so we need to ensure paths are correct.

### Step 2: Update Your Files

#### ✅ Already Done:

- `requirements.txt` includes `gunicorn` (required for production)
- `app.py` updated to use PORT environment variable

#### 📝 Create a Start Script (Recommended)

Create a file named `start.sh` in your project root:

```bash
#!/bin/bash
cd website
gunicorn app:app
```

Make it executable (if on Linux/Mac):

```bash
chmod +x start.sh
```

**Alternative:** You can skip the start script and configure the start command directly in Render dashboard.

### Step 3: Push Your Code to GitHub

1. **Initialize Git repository** (if not already done):

```bash
git init
```

2. **Create a `.gitignore` file** in the root directory:

```
# Virtual environments
env/
.venv/
venv/
ENV/

# Python cache
__pycache__/
*.py[cod]
*$py.class
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Local test files
*.log
```

3. **Add and commit your files**:

```bash
git add .
git commit -m "Initial commit for Render deployment"
```

4. **Create a new repository on GitHub**:
   - Go to [github.com](https://github.com)
   - Click "New repository"
   - Name it (e.g., "laptop-price-predictor")
   - Don't initialize with README (since you already have files)
   - Click "Create repository"

5. **Push to GitHub**:

```bash
git remote add origin https://github.com/YOUR_USERNAME/laptop-price-predictor.git
git branch -M main
git push -u origin main
```

### Step 4: Sign Up for Render

1. Go to [render.com](https://render.com)
2. Click "Get Started for Free"
3. Sign up with GitHub (recommended for easier integration)
4. Authorize Render to access your GitHub repositories

### Step 5: Create a New Web Service on Render

1. **From Render Dashboard**:
   - Click "New +" button
   - Select "Web Service"

2. **Connect Your Repository**:
   - Find your `laptop-price-predictor` repository
   - Click "Connect"

3. **Configure Your Web Service**:

   Fill in the following settings:

   | Setting            | Value                                                      |
   | ------------------ | ---------------------------------------------------------- |
   | **Name**           | `laptop-price-predictor` (or your preferred name)          |
   | **Region**         | Choose closest to you (e.g., Oregon, Frankfurt, Singapore) |
   | **Branch**         | `main`                                                     |
   | **Root Directory** | Leave blank (uses repository root)                         |
   | **Runtime**        | `Python 3`                                                 |
   | **Build Command**  | `pip install -r requirements.txt`                          |
   | **Start Command**  | `cd website && gunicorn app:app`                           |
   | **Plan**           | `Free`                                                     |

4. **Advanced Settings** (Optional but Recommended):
   - Click "Advanced"
   - Add Environment Variable:
     - **Key**: `PYTHON_VERSION`
     - **Value**: `3.11.0` (or your Python version)

5. **Create Web Service**:
   - Click "Create Web Service"
   - Render will start building and deploying your app

### Step 6: Monitor Deployment

1. **Watch the Build Logs**:
   - You'll see real-time logs as Render:
     - Installs Python
     - Installs dependencies from requirements.txt
     - Starts your application with gunicorn

2. **Wait for Deployment**:
   - Initial deployment takes 2-5 minutes
   - You'll see "Your service is live 🎉" when complete

3. **Get Your URL**:
   - Your app will be available at: `https://laptop-price-predictor.onrender.com`
   - (URL will be shown in the dashboard)

---

## 🔧 Troubleshooting Common Issues

### Issue 1: Build Fails with Module Not Found

**Solution**: Make sure all required packages are in `requirements.txt`

```bash
# In your local environment, generate fresh requirements
pip freeze > requirements.txt
```

### Issue 2: Application Error - Port Binding

**Solution**: Ensure your `app.py` uses the PORT environment variable:

```python
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

### Issue 3: Model File Not Found

**Solution**: Verify the model path in `app.py`:

- If you get "model/predictor.pickle not found"
- Check that the file exists in your GitHub repository
- Ensure Git isn't ignoring `.pickle` files

```bash
# Force add the pickle file if needed
git add -f website/model/predictor.pickle
git commit -m "Add model file"
git push
```

### Issue 4: Static Files Not Loading

**Solution**: Use Flask's url_for in templates:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
```

### Issue 5: Large Dependencies Causing Build Timeout

**Solution**: Render free tier has build time limits. If scipy/numpy cause issues:

- Use pre-built wheels
- Consider upgrading to paid tier for faster builds

---

## 🔄 Updating Your Deployed Application

When you make changes to your code:

1. **Commit and push changes**:

```bash
git add .
git commit -m "Description of changes"
git push origin main
```

2. **Automatic Deployment**:
   - Render automatically detects the push
   - Rebuilds and redeploys your application
   - Takes 2-3 minutes

3. **Manual Deployment** (if needed):
   - Go to your Render dashboard
   - Click your service
   - Click "Manual Deploy" → "Deploy latest commit"

---

## 📊 Monitoring Your Application

### View Logs

1. Go to your Render dashboard
2. Click on your service
3. Click "Logs" tab
4. See real-time application logs

### Check Metrics

1. In your service dashboard
2. View "Metrics" tab
3. Monitor:
   - CPU usage
   - Memory usage
   - Response times
   - HTTP requests

---

## 💡 Important Notes About Render Free Tier

### Advantages:

- ✅ Completely free
- ✅ Automatic HTTPS
- ✅ Automatic deployments from GitHub
- ✅ 750 hours/month (enough for continuous hosting)
- ✅ Custom domains supported

### Limitations:

- ⚠️ **Services spin down after 15 minutes of inactivity**
- ⚠️ First request after inactivity takes 30-60 seconds (cold start)
- ⚠️ 512 MB RAM limit
- ⚠️ Limited build minutes

### Keeping Your Service Active:

If you want to avoid cold starts, consider:

1. Using a free uptime monitoring service (e.g., UptimeRobot)
2. Upgrading to Render's paid tier ($7/month for always-on)

---

## 🌐 Custom Domain Setup (Optional)

1. **In Render Dashboard**:
   - Go to your service
   - Click "Settings"
   - Scroll to "Custom Domain"
   - Click "Add Custom Domain"

2. **Add Your Domain**:
   - Enter your domain (e.g., `laptops.yoursite.com`)
   - Render provides DNS instructions

3. **Update DNS**:
   - Add CNAME record at your domain registrar
   - Point to the provided Render URL
   - Wait for DNS propagation (up to 48 hours)

---

## 🎯 Final Checklist

Before deploying, ensure:

- [ ] All code is committed and pushed to GitHub
- [ ] `requirements.txt` is complete and accurate
- [ ] `app.py` uses PORT environment variable
- [ ] Model file (`predictor.pickle`) is in the repository
- [ ] `.gitignore` excludes virtual environments
- [ ] Templates and static files are included
- [ ] Render account is created and verified

---

## 📚 Additional Resources

- [Render Documentation](https://render.com/docs)
- [Render Python Guide](https://render.com/docs/deploy-flask)
- [Render Community Forum](https://community.render.com/)

---

## 🎉 Success!

Once deployed, your Laptop Price Predictor will be accessible at:

```
https://your-service-name.onrender.com
```

Share this URL with anyone to use your price predictor!

---

## 📞 Need Help?

If you encounter issues:

1. Check Render logs for error messages
2. Review the troubleshooting section above
3. Search Render community forum
4. Check that all steps were followed correctly

Good luck with your deployment! 🚀
