# 🔗 URL Shortener

A powerful URL shortening service that transforms long URLs into short, shareable links. Built with Flask, MongoDB, and TailwindCSS.

## ✨ Features

- **🔗 Instant URL Shortening**
  - Convert long URLs to concise, easy-to-share links
  - Supports various URL formats and protocols

- **🎨 Modern User Interface**
  - Responsive design
  - Clean and intuitive user experience
  - Mobile-friendly layout

- **📱 QR Code Generation**
  - Automatic QR code creation for each shortened URL
  - Easy download and sharing of QR codes

- **🎯 Custom URL Options**
  - Create custom aliases for your shortened links
  - Personalize links to make them more memorable

- **🔒 Advanced Security**
  - Optional password protection for links
  - Restrict access to specific shortened URLs

- **⏰ Flexible Link Management**
  - Configurable expiration dates
  - Automatic link deactivation after specified period

- **📊 Analytics (Upcoming)**
  - Click tracking
  - Basic link performance metrics

## 🚀 Technology Stack

- **Backend:** Flask (Python)
- **Database:** MongoDB Atlas
- **Frontend:** 
  - HTML
  - TailwindCSS
  - JavaScript
- **Additional Tools:**
  - QR Code Generation Library
  - URL Validation

## 📦 Installation and Setup

### Prerequisites
- Python 3.8+
- pip
- MongoDB Atlas account

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Ano2225/url-shortener.git
   cd url-shortener
   ```

2. **Create Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the project root:
   ```env
   MONGO_URI=your_mongodb_connection_string
   SECRET_KEY=your_flask_secret_key
   DEBUG=True  # Set to False in production
   ```

5. **Run the Application**
   ```bash
   python main.py
   ```

## 📝 MongoDB Configuration

1. Sign up for [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a new cluster
3. Configure Database Access
   - Create a database user
   - Set appropriate permissions
4. Configure Network Access
   - Whitelist your IP address
5. Retrieve Connection URI
   - Replace in `.env` file

## 🛠️ Project Structure

```
url-shortener/
│
├── main.py              # Main Flask application
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates
│   ├── index.html
│   └── password_protection.html
│
└── .env                 # Environment variables
```

## 💻 Usage Guide

1. **Shorten URL**
   - Open the application
   - Paste your long URL
   - (Optional) Configure advanced settings
     * Custom alias
     * Password protection
     * Expiration date
   - Click "Shorten"

2. **Link Management**
   - Copy shortened URL
   - Download QR code
   - Share link across platforms

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository
2. Create a feature branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit changes
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to branch
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request

## 🔒 Security Considerations

- Use HTTPS
- Implement rate limiting
- Sanitize and validate all inputs
- Use secure MongoDB connection
- Protect against common web vulnerabilities

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👥 Author

**OUATTARA Arouna** (Young_Geek)
- GitHub: [@Ano2225](https://github.com/Ano2225)
- Email: ouatt0767@gmail.com

## 📞 Contact & Support

- Open an issue on GitHub
- Send an email for support

---

**Happy URL Shortening! 🚀**
