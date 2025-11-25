# 🚀 AI SaaS Builder

**Créez un Micro-SaaS fonctionnel en 27 minutes** en répondant simplement à 4 questions !

Inspiré du post LinkedIn viral, ce builder génère automatiquement une application complète avec :
- ✅ Base de données (schéma + SQL)
- ✅ Automatisations IA (OpenAI)
- ✅ Interface utilisateur (React/Next.js)
- ✅ Système d'authentification (optionnel)
- ✅ API Routes prêtes à l'emploi
- ✅ Configuration Docker complète

## 🎯 Les 4 Questions

Le builder vous pose simplement 4 questions pour générer votre application :

1. **Quel est le nom de ton Micro-SaaS ?**
   - Exemple: TalentTracker, LeadGen Pro, ContentWizard...

2. **Quelle est sa description en quelques lignes ?**
   - Décrivez le problème résolu et la valeur apportée

3. **Quelles sont les 3 fonctionnalités principales ?**
   - Les features qui rendent votre SaaS unique

4. **As-tu besoin d'un système d'authentification utilisateur ?**
   - Oui/Non pour activer la gestion de comptes

## 🚀 Utilisation Rapide

### Option 1: Interface Web (HTML)

```bash
# Ouvrir l'interface dans votre navigateur
open ai-saas-builder.html
```

Remplissez les 4 questions dans l'interface web et cliquez sur "Générer mon SaaS" !

### Option 2: Ligne de Commande (CLI)

```bash
# Lancer le builder interactif
python3 cli-builder.py
```

Suivez les questions dans le terminal et votre application sera générée automatiquement.

### Option 3: En Python (Programmation)

```python
from saas_generator import MicroSaaSGenerator

# Définir les données de votre SaaS
saas_data = {
    "name": "MonSuperSaaS",
    "description": "Une application qui résout X problème pour Y audience",
    "features": [
        "Fonctionnalité 1",
        "Fonctionnalité 2",
        "Fonctionnalité 3"
    ],
    "auth": True  # True si authentification nécessaire
}

# Générer l'application
generator = MicroSaaSGenerator(saas_data)
generator.generate_all()
```

## 📦 Ce qui est généré automatiquement

Une fois les 4 questions répondues, le builder génère :

### Structure Complète du Projet

```
generated-saas-[nom]/
├── src/
│   ├── app/
│   │   ├── api/                  # Routes API pour chaque fonctionnalité
│   │   │   ├── items/route.ts
│   │   │   ├── auth/route.ts     (si auth activée)
│   │   │   └── [feature]/route.ts (pour chaque fonctionnalité)
│   │   ├── page.tsx              # Page principale
│   │   ├── layout.tsx            # Layout global
│   │   └── globals.css           # Styles Tailwind
│   ├── components/
│   │   ├── Dashboard.tsx         # Tableau de bord principal
│   │   └── AuthForm.tsx          (si auth activée)
│   ├── lib/
│   │   └── openai.ts             # Intégration OpenAI
│   └── types/                    # Types TypeScript
├── public/                       # Assets statiques
├── database-schema.json          # Schéma de base de données
├── database-setup.sql            # SQL pour Supabase/PostgreSQL
├── package.json                  # Dépendances npm
├── .env.example                  # Variables d'environnement
├── Dockerfile                    # Configuration Docker
├── tailwind.config.js           # Config Tailwind CSS
├── tsconfig.json                # Config TypeScript
└── README.md                     # Documentation du SaaS généré
```

### Technologies Utilisées

- **Frontend**: Next.js 14 + React 18 + TypeScript
- **Styling**: Tailwind CSS
- **Base de données**: Supabase (PostgreSQL)
- **IA**: OpenAI GPT-4
- **Auth**: Supabase Auth (optionnel)
- **Déploiement**: Vercel / Docker

## 🛠️ Configuration et Démarrage

Une fois votre SaaS généré :

### 1. Installation des dépendances

```bash
cd generated-saas-[nom-de-votre-saas]
npm install
```

### 2. Configuration Supabase

1. Créez un projet sur [Supabase](https://supabase.com)
2. Exécutez le script SQL : `database-setup.sql` dans l'éditeur SQL
3. Récupérez vos clés API (Project Settings → API)

### 3. Configuration OpenAI

1. Obtenez une clé API sur [OpenAI Platform](https://platform.openai.com)
2. Ajoutez-la dans votre fichier `.env`

### 4. Variables d'environnement

```bash
cp .env.example .env
```

Modifiez `.env` avec vos vraies clés :

```env
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
OPENAI_API_KEY=your_openai_api_key
```

### 5. Lancer l'application

```bash
# Développement
npm run dev

# Build production
npm run build
npm start
```

Votre application sera disponible sur [http://localhost:3000](http://localhost:3000)

## 🤖 Automatisations IA Intégrées

Chaque Micro-SaaS généré inclut des automatisations IA prêtes à l'emploi :

### 1. Traitement de données avec IA

```typescript
// Traite automatiquement les données avec GPT-4
const result = await processWithAI(data)
```

### 2. Génération de contenu

```typescript
// Génère du contenu basé sur un prompt
const content = await generateContent("Écris une description...")
```

### 3. Analyse de données

```typescript
// Analyse des données et génère des insights
const insights = await analyzeData(yourData)
```

Toutes ces fonctions sont disponibles dans `src/lib/openai.ts`

## 🎨 Personnalisation

### Modifier les couleurs

Éditez `tailwind.config.js` pour personnaliser le thème :

```js
theme: {
  extend: {
    colors: {
      primary: '#667eea',
      secondary: '#764ba2',
    }
  }
}
```

### Ajouter des fonctionnalités

1. Créez une nouvelle route API dans `src/app/api/[nom]/route.ts`
2. Ajoutez un composant UI dans `src/components/`
3. Intégrez-le dans le Dashboard

## 🚢 Déploiement

### Vercel (Recommandé - 1 clic)

```bash
npm install -g vercel
vercel
```

### Docker

```bash
docker build -t mon-saas .
docker run -p 3000:3000 mon-saas
```

### Variables d'environnement en production

N'oubliez pas de configurer vos variables d'environnement sur votre plateforme de déploiement !

## 📊 Schéma de Base de Données

Le builder génère automatiquement :

- **Table users** (si auth activée) : Gestion des utilisateurs
- **Table items** : Entités principales de votre SaaS
- **Tables personnalisées** : Une table par fonctionnalité définie

Schéma complet disponible dans `database-schema.json`

## 🎯 Exemples de Micro-SaaS Générés

### Exemple 1: TalentTracker

```python
{
    "name": "TalentTracker",
    "description": "Optimisez vos candidatures avec l'IA",
    "features": [
        "Optimisation de CV par IA",
        "Simulation d'entretien",
        "Analyse de marché"
    ],
    "auth": True
}
```

### Exemple 2: ContentWizard

```python
{
    "name": "ContentWizard",
    "description": "Générez du contenu marketing en un clic",
    "features": [
        "Génération d'articles de blog",
        "Posts réseaux sociaux",
        "Email marketing"
    ],
    "auth": True
}
```

### Exemple 3: LeadScoreAI

```python
{
    "name": "LeadScoreAI",
    "description": "Scorez vos leads automatiquement",
    "features": [
        "Scoring automatique des leads",
        "Enrichissement de données",
        "Prédiction de conversion"
    ],
    "auth": True
}
```

## 🔧 Dépannage

### Erreur de build

```bash
rm -rf node_modules package-lock.json
npm install
```

### Problèmes avec Supabase

Vérifiez que :
- Les tables sont bien créées (exécutez le SQL)
- Les clés API sont correctes
- RLS (Row Level Security) est configuré

### Problèmes avec OpenAI

- Vérifiez votre clé API
- Vérifiez vos crédits OpenAI
- Testez avec un modèle moins coûteux (gpt-3.5-turbo)

## 📚 Ressources

- [Documentation Next.js](https://nextjs.org/docs)
- [Documentation Supabase](https://supabase.com/docs)
- [Documentation OpenAI](https://platform.openai.com/docs)
- [Documentation Tailwind CSS](https://tailwindcss.com/docs)

## 🤝 Contribution

Ce builder est open source ! N'hésitez pas à :
- Reporter des bugs
- Proposer des améliorations
- Ajouter des templates

## 📝 License

MIT License - Utilisez librement pour vos projets !

## 🎉 Inspiré par

Ce projet est inspiré du post LinkedIn viral sur la création de Micro-SaaS en 27 minutes.

Le concept : Poser 4 questions simples et générer automatiquement une application complète et fonctionnelle.

---

**Créé avec ❤️ par l'AI SaaS Builder**

*Générez des Micro-SaaS en quelques minutes, pas en quelques semaines !*
