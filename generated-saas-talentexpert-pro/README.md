# TalentExpert Pro

Plateforme IA pour optimiser les candidatures et accélérer l'employabilité

## 🚀 Fonctionnalités Principales

- Optimisation de CV avec IA
- Simulation d'entretien intelligente
- Analyse de marché en temps réel

## 📦 Installation

```bash
# Installer les dépendances
npm install

# Copier le fichier d'environnement
cp .env.example .env

# Configurer les variables d'environnement dans .env
```

## 🔧 Configuration

### 1. Supabase

1. Créez un projet sur [Supabase](https://supabase.com)
2. Exécutez le script SQL de configuration : `database-setup.sql`
3. Copiez l'URL et les clés API dans `.env`

### 2. OpenAI

1. Obtenez une clé API sur [OpenAI](https://platform.openai.com)
2. Ajoutez-la dans `.env` : `OPENAI_API_KEY=your_key`

## 🏃 Démarrage

```bash
# Développement
npm run dev

# Build production
npm run build

# Démarrer en production
npm start
```

L'application sera accessible sur [http://localhost:3000](http://localhost:3000)

## 📊 Structure du Projet

```
TalentExpert Pro/
├── src/
│   ├── app/
│   │   ├── api/          # Routes API
│   │   ├── page.tsx      # Page principale
│   │   └── layout.tsx    # Layout global
│   ├── components/       # Composants React
│   └── lib/              # Utilitaires (OpenAI, etc.)
├── public/               # Assets statiques
├── database-schema.json  # Schéma de BDD
└── database-setup.sql    # Script SQL
```

## 🤖 Automatisations IA

Ce Micro-SaaS utilise OpenAI pour :

- Traitement intelligent des données
- Génération de contenu
- Analyse et insights automatiques

Toutes les automatisations sont configurées dans `src/lib/openai.ts`

## 🔐 Authentification

✅ Système d'authentification activé via Supabase Auth

## 🚀 Déploiement

### Vercel (Recommandé)

```bash
npm install -g vercel
vercel
```

### Docker

```bash
docker build -t talentexpert-pro .
docker run -p 3000:3000 talentexpert-pro
```

## 📝 License

MIT

## 🎉 Généré automatiquement

Ce Micro-SaaS a été généré automatiquement par **AI SaaS Builder**
Date de génération : 2025-11-25 05:52:55

---

**Bon développement ! 🚀**
