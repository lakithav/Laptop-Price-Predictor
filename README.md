# Laptop Price Predictor 💻

A machine learning-powered web application that predicts laptop prices based on specifications like RAM, weight, processor, GPU, and other features.

## 🌟 Features

- **Interactive Web Interface**: User-friendly form to input laptop specifications
- **ML-Powered Predictions**: Uses scikit-learn trained model for accurate price predictions
- **Real-time Results**: Instant price estimates based on your inputs
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **ML Library**: scikit-learn, numpy
- **Frontend**: HTML, CSS (Jinja2 templates)
- **Deployment**: Render (free tier)
- **Production Server**: Gunicorn

## 📁 Project Structure

```
Laptop-Price-Predictor/
├── website/
│   ├── app.py                 # Flask application
│   ├── model/
│   │   └── predictor.pickle   # Trained ML model
│   └── templates/
│       ├── index.html         # Input form
│       └── result.html        # Prediction results
├── model building/
│   └── Laptop_price_predictor.ipynb  # Model training notebook
├── requirements.txt
└── README.md
```

## 🚀 Deployment

This project is deployed on **Render** (free hosting).

### Quick Deploy Instructions:

1. **Push to GitHub**
2. **Sign up at [render.com](https://render.com)**
3. **Create New Web Service** with these settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `cd website && gunicorn app:app`

📖 **See [RENDER_DEPLOYMENT_GUIDE.md](RENDER_DEPLOYMENT_GUIDE.md) for complete step-by-step instructions.**

⚡ **See [QUICK_START_RENDER.md](QUICK_START_RENDER.md) for rapid deployment.**

## 💻 Local Development

### Prerequisites

- Python 3.8+
- pip

### Setup

1. **Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/laptop-price-predictor.git
cd laptop-price-predictor
```

2. **Create virtual environment**

```bash
python -m venv .venv
```

3. **Activate virtual environment**

- Windows:

```bash
.venv\Scripts\activate
```

- Mac/Linux:

```bash
source .venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Run the application**

```bash
cd website
python app.py
```

6. **Access the app**
   Open your browser and go to: `http://localhost:5000`

## 📊 Model Information

The prediction model is trained on laptop specifications including:

- RAM (GB)
- Weight (kg)
- Company (Acer, Apple, Asus, Dell, HP, Lenovo, MSI, Toshiba)
- Type (2-in-1, Gaming, Netbook, Notebook, Ultrabook, Workstation)
- Operating System (Windows, Mac, Linux)
- CPU (Intel Core i3/i5/i7, AMD)
- GPU (Intel, AMD, Nvidia)
- Touchscreen (Yes/No)
- IPS Display (Yes/No)

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Made with ❤️ for ML enthusiasts**
