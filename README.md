# Shia Islamic FAQ Assistant

A Flask-based web application that provides Islamic FAQ assistance according to Ja'fari Fiqh using OpenAI's GPT models.

## 🐛 Bug Fixes Applied

### ✅ **CRITICAL - Fixed Deprecated OpenAI API Usage**
- **Issue**: Code used `openai.ChatCompletion.create()` which is deprecated in openai>=1.0.0
- **Fix**: Updated to use the new `OpenAI()` client with `client.chat.completions.create()`
- **Impact**: Application now works with latest OpenAI library versions

### ✅ **HIGH SECURITY - Fixed XSS Vulnerability**
- **Issue**: User input and API responses were directly injected into HTML using `innerHTML`
- **Fix**: Replaced with safe DOM manipulation using `textContent` and `createElement`
- **Impact**: Prevents Cross-Site Scripting (XSS) attacks

### ✅ **CONFIGURATION - Made API Endpoint Configurable**
- **Issue**: Hardcoded production URL in frontend JavaScript
- **Fix**: Added automatic detection of localhost vs production environment
- **Impact**: Application now works in both development and production environments

### ✅ **RUNTIME - Added Environment Variable Validation**
- **Issue**: No validation for required `OPENAI_API_KEY` environment variable
- **Fix**: Added startup validation with clear error messages
- **Impact**: Application fails fast with helpful error messages if misconfigured

## 🚀 Setup Instructions

### 1. Install Dependencies

Create a virtual environment and install packages:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy the example environment file:
```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```env
OPENAI_API_KEY=your_actual_openai_api_key_here
PORT=5000
FLASK_ENV=development
```

### 3. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 🔧 Technical Details

### Dependencies
- **Flask 3.1.1**: Web framework
- **openai 1.23.2**: OpenAI API client (updated to latest compatible version)
- **python-dotenv 1.0.1**: Environment variable management

### Security Features
- XSS protection through safe DOM manipulation
- Environment variable validation
- Error handling and logging

### API Endpoints
- `GET /`: Serves the main HTML interface
- `POST /ask`: Processes questions and returns AI responses
- `GET /faq-sample`: Returns sample FAQ data

## 🌍 Deployment

The application is configured for deployment on platforms like Railway, Heroku, or any platform that supports Flask applications.

Environment variables required in production:
- `OPENAI_API_KEY`: Your OpenAI API key
- `PORT`: Port number (automatically set by most platforms)

## 📝 License

This project is configured for educational and community use in accordance with Islamic principles and Ja'fari jurisprudence.