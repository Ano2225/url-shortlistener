# URL Shortener

Un service de raccourcissement d'URL  qui transforme vos longs liens en URLs courts et faciles à partager. Construit avec Flask, MongoDB et TailwindCSS.

## ✨ Fonctionnalités

- 🔗 Raccourcissement d'URL instantané
- 🎨 Interface utilisateur moderne et responsive
- 📱 Génération automatique de QR codes
- 🎯 URLs personnalisés
- 🔒 Protection par mot de passe (optionnel)
- ⏰ Dates d'expiration configurables
- 📊 Suivi des statistiques de clics ( A venir )

## 🚀 Technologies Utilisées

- **Backend:** Flask (Python)
- **Base de données:** MongoDB Atlas
- **Frontend:** HTML, TailwindCSS, JavaScript

## 📦 Installation

1. **Clonez le repository**
```bash
git clone https://github.com/votre-username/url-shortener.git
cd url-shortener
```

2. **Créez un environnement virtuel**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Installez les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configurez les variables d'environnement**
Créez un fichier `.env` à la racine du projet :
```env
MONGO_URI=votre_uri_mongodb
```

5. **Lancez l'application**
```bash
python main.py
```

## 📝 Configuration MongoDB

1. Créez un compte sur [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Créez un nouveau cluster
3. Dans "Database Access", créez un nouvel utilisateur
4. Dans "Network Access", autorisez votre IP
5. Récupérez votre URI de connexion et ajoutez-la dans le fichier `.env`

## 🛠️ Structure du Projet

```
project/
├── main.py          # Application Flask
├── templates/       # Templates HTML
├── requirements.txt # Dépendances
└── .env            # Variables d'environnement
```

## 💻 Utilisation

1. Collez votre URL long dans le champ de saisie
2. (Optionnel) Configurez les options avancées :
   - URL personnalisé
   - Protection par mot de passe
   - Date d'expiration
3. Cliquez sur "Raccourcir"
4. Copiez votre URL court ou telecharger la photo du QR code

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push sur la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT.

## 👥 Auteur

- OUATTARA Arouna - (Young_Geek)

## 📞 Contact

- GitHub: [@Ano2225](https://github.com/Ano2225)
- Email: ouatt0767@gmail.com
