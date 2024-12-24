# main.py
from flask import Flask, request, redirect, render_template, jsonify
import os
from pymongo import MongoClient
from datetime import datetime
import random
import string
import qrcode
from io import BytesIO
import base64
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Optimisation de la connexion MongoDB pour Vercel
def get_database():
    MONGO_URI = os.getenv('MONGO_URI')
    client = MongoClient(MONGO_URI)
    return client.urlshortener

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    try:
        db = get_database()
        data = request.json
        original_url = data.get('url')
        custom_code = data.get('customCode')
        password = data.get('password')
        expiration_date = data.get('expirationDate')
        
        if not original_url:
            return jsonify({'error': 'URL requise'}), 400

        # Générer code court
        short_code = custom_code if custom_code else ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        
        # Vérifier si le code existe
        if db.urls.find_one({"short_code": short_code}):
            return jsonify({'error': 'Code déjà utilisé'}), 400

        # Créer l'URL courte
        short_url = f"{request.host_url}{short_code}"

        # Générer QR Code de manière optimisée
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4,
            error_correction=qrcode.constants.ERROR_CORRECT_L
        )
        qr.add_data(short_url)
        qr.make(fit=True)

        # Convertir en base64 avec une taille optimisée
        buffer = BytesIO()
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.save(buffer, format='PNG', optimize=True, quality=70)
        qr_base64 = base64.b64encode(buffer.getvalue()).decode()

        # Insérer dans la base de données
        url_data = {
            "original_url": original_url,
            "short_code": short_code,
            "password": password,
            "expiration_date": expiration_date,
            "created_at": datetime.utcnow(),
            "click_count": 0
        }
        
        db.urls.insert_one(url_data)
        
        return jsonify({
            'original_url': original_url,
            'short_url': short_url,
            'qr_code': f"data:image/png;base64,{qr_base64}",
            'expiration_date': expiration_date
        })

    except Exception as e:
        print(f"Erreur : {e}") 
        return jsonify({'error': str(e)}), 500
    

@app.route('/<short_code>')
def redirect_to_url(short_code):
    try:
        db = get_database()
        url_data = db.urls.find_one({"short_code": short_code})
        
        if not url_data:
            return "URL non trouvée", 404

        # Incrémenter le compteur
        db.urls.update_one(
            {"short_code": short_code},
            {"$inc": {"click_count": 1}}
        )

        return redirect(url_data['original_url'])

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)