#!/usr/bin/env python3
"""
AI SaaS Builder - Générateur Automatique de Micro-SaaS
Génère une application complète en fonction de 4 questions
"""

import json
import os
from pathlib import Path
from datetime import datetime


class MicroSaaSGenerator:
    """Générateur automatique de Micro-SaaS"""

    def __init__(self, saas_data):
        """
        Initialize the generator

        Args:
            saas_data: dict with keys: name, description, features, auth
        """
        self.name = saas_data['name']
        self.description = saas_data['description']
        self.features = saas_data['features']
        self.auth = saas_data.get('auth', False)
        self.output_dir = Path(f"generated-saas-{self.name.lower().replace(' ', '-')}")

    def generate_all(self):
        """Génère tous les fichiers du Micro-SaaS"""
        print(f"🚀 Génération du Micro-SaaS: {self.name}")
        print(f"📁 Dossier de sortie: {self.output_dir}")

        # Créer la structure de dossiers
        self.create_directory_structure()

        # Générer tous les fichiers
        self.generate_database_schema()
        self.generate_package_json()
        self.generate_env_example()
        self.generate_main_app()
        self.generate_api_routes()
        self.generate_ui_components()
        self.generate_openai_integration()

        if self.auth:
            self.generate_auth_system()

        self.generate_readme()
        self.generate_docker_files()

        print(f"\n✅ Génération terminée!")
        print(f"📦 Votre Micro-SaaS est prêt dans: {self.output_dir}")
        print(f"\n🚀 Pour démarrer:")
        print(f"   cd {self.output_dir}")
        print(f"   npm install")
        print(f"   npm run dev")

    def create_directory_structure(self):
        """Crée la structure de dossiers"""
        dirs = [
            self.output_dir,
            self.output_dir / "src",
            self.output_dir / "src" / "app",
            self.output_dir / "src" / "app" / "api",
            self.output_dir / "src" / "components",
            self.output_dir / "src" / "lib",
            self.output_dir / "src" / "types",
            self.output_dir / "public",
        ]

        for dir_path in dirs:
            dir_path.mkdir(parents=True, exist_ok=True)

    def generate_database_schema(self):
        """Génère le schéma de base de données"""
        schema = {
            "database": self.name,
            "description": self.description,
            "created_at": datetime.now().isoformat(),
            "tables": [
                {
                    "name": "users",
                    "fields": [
                        {"name": "id", "type": "uuid", "primary": True},
                        {"name": "email", "type": "string", "unique": True},
                        {"name": "name", "type": "string"},
                        {"name": "created_at", "type": "timestamp"},
                    ]
                } if self.auth else None,
                {
                    "name": "items",
                    "fields": [
                        {"name": "id", "type": "uuid", "primary": True},
                        {"name": "title", "type": "string"},
                        {"name": "description", "type": "text"},
                        {"name": "status", "type": "string"},
                        {"name": "ai_processed", "type": "boolean", "default": False},
                        {"name": "created_at", "type": "timestamp"},
                        {"name": "updated_at", "type": "timestamp"},
                    ]
                },
            ]
        }

        # Ajouter une table pour chaque fonctionnalité
        for i, feature in enumerate(self.features):
            table_name = feature.lower().replace(' ', '_')
            schema["tables"].append({
                "name": table_name,
                "fields": [
                    {"name": "id", "type": "uuid", "primary": True},
                    {"name": "name", "type": "string"},
                    {"name": "data", "type": "json"},
                    {"name": "ai_generated", "type": "boolean", "default": False},
                    {"name": "created_at", "type": "timestamp"},
                ]
            })

        # Retirer None du tableau
        schema["tables"] = [t for t in schema["tables"] if t is not None]

        # Sauvegarder le schéma
        schema_file = self.output_dir / "database-schema.json"
        with open(schema_file, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)

        # Générer le SQL pour Supabase/PostgreSQL
        sql_file = self.output_dir / "database-setup.sql"
        sql_content = self.generate_sql_from_schema(schema)
        with open(sql_file, 'w', encoding='utf-8') as f:
            f.write(sql_content)

        print(f"✅ Schéma de base de données généré")

    def generate_sql_from_schema(self, schema):
        """Génère le SQL à partir du schéma"""
        sql = f"-- Base de données pour {self.name}\n"
        sql += f"-- {self.description}\n\n"

        type_mapping = {
            'uuid': 'UUID DEFAULT gen_random_uuid()',
            'string': 'VARCHAR(255)',
            'text': 'TEXT',
            'boolean': 'BOOLEAN',
            'timestamp': 'TIMESTAMP DEFAULT NOW()',
            'json': 'JSONB'
        }

        for table in schema['tables']:
            sql += f"-- Table: {table['name']}\n"
            sql += f"CREATE TABLE IF NOT EXISTS {table['name']} (\n"

            fields = []
            for field in table['fields']:
                field_type = type_mapping.get(field['type'], 'TEXT')
                field_def = f"  {field['name']} {field_type}"

                if field.get('primary'):
                    field_def += " PRIMARY KEY"
                if field.get('unique'):
                    field_def += " UNIQUE"
                if field.get('default') is not None:
                    field_def += f" DEFAULT {field['default']}"

                fields.append(field_def)

            sql += ",\n".join(fields)
            sql += "\n);\n\n"

        return sql

    def generate_package_json(self):
        """Génère le package.json"""
        package = {
            "name": self.name.lower().replace(' ', '-'),
            "version": "1.0.0",
            "description": self.description,
            "scripts": {
                "dev": "next dev",
                "build": "next build",
                "start": "next start",
                "lint": "next lint"
            },
            "dependencies": {
                "next": "^14.0.0",
                "react": "^18.2.0",
                "react-dom": "^18.2.0",
                "@supabase/supabase-js": "^2.38.0",
                "openai": "^4.20.0",
                "axios": "^1.6.0"
            },
            "devDependencies": {
                "@types/node": "^20.0.0",
                "@types/react": "^18.2.0",
                "@types/react-dom": "^18.2.0",
                "typescript": "^5.2.0",
                "autoprefixer": "^10.4.0",
                "postcss": "^8.4.0",
                "tailwindcss": "^3.3.0"
            }
        }

        file_path = self.output_dir / "package.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(package, f, indent=2)

        print(f"✅ package.json généré")

    def generate_env_example(self):
        """Génère le fichier .env.example"""
        env_content = f"""# Configuration pour {self.name}

# Supabase Configuration
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key

# Application Configuration
NEXT_PUBLIC_APP_NAME={self.name}
NEXT_PUBLIC_APP_URL=http://localhost:3000
"""

        file_path = self.output_dir / ".env.example"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(env_content)

        print(f"✅ .env.example généré")

    def generate_main_app(self):
        """Génère l'application principale Next.js"""

        # page.tsx principale
        page_content = f'''import {{ useState }} from 'react'
import Dashboard from '@/components/Dashboard'
{"import AuthForm from '@/components/AuthForm'" if self.auth else ""}

export default function Home() {{
  {"const [isAuthenticated, setIsAuthenticated] = useState(false)" if self.auth else ""}

  return (
    <main className="min-h-screen bg-gradient-to-br from-purple-600 to-blue-500">
      <div className="container mx-auto px-4 py-8">
        <header className="text-center mb-12">
          <h1 className="text-5xl font-bold text-white mb-4">
            {self.name}
          </h1>
          <p className="text-xl text-white/90">
            {self.description}
          </p>
        </header>

        {"{" if self.auth else ""}
          {f"isAuthenticated ? <Dashboard /> : <AuthForm onAuth={{() => setIsAuthenticated(true)}} />" if self.auth else "<Dashboard />"}
        {"}" if self.auth else ""}
      </div>
    </main>
  )
}}
'''

        file_path = self.output_dir / "src" / "app" / "page.tsx"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(page_content)

        # layout.tsx
        layout_content = f'''import type {{ Metadata }} from 'next'
import './globals.css'

export const metadata: Metadata = {{
  title: '{self.name}',
  description: '{self.description}',
}}

export default function RootLayout({{
  children,
}}: {{
  children: React.ReactNode
}}) {{
  return (
    <html lang="fr">
      <body>{{children}}</body>
    </html>
  )
}}
'''

        file_path = self.output_dir / "src" / "app" / "layout.tsx"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(layout_content)

        # globals.css
        css_content = '''@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --foreground-rgb: 0, 0, 0;
  --background-start-rgb: 214, 219, 220;
  --background-end-rgb: 255, 255, 255;
}

@media (prefers-color-scheme: dark) {
  :root {
    --foreground-rgb: 255, 255, 255;
    --background-start-rgb: 0, 0, 0;
    --background-end-rgb: 0, 0, 0;
  }
}

body {
  color: rgb(var(--foreground-rgb));
  background: linear-gradient(
      to bottom,
      transparent,
      rgb(var(--background-end-rgb))
    )
    rgb(var(--background-start-rgb));
}
'''

        file_path = self.output_dir / "src" / "app" / "globals.css"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(css_content)

        print(f"✅ Application principale générée")

    def generate_api_routes(self):
        """Génère les routes API avec automatisations IA"""

        # Route principale pour les items
        api_route = '''import { NextRequest, NextResponse } from 'next/server'
import { createClient } from '@supabase/supabase-js'
import { processWithAI } from '@/lib/openai'

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY!
)

export async function GET(request: NextRequest) {
  try {
    const { data, error } = await supabase
      .from('items')
      .select('*')
      .order('created_at', { ascending: false })

    if (error) throw error

    return NextResponse.json({ data })
  } catch (error) {
    return NextResponse.json({ error: 'Failed to fetch items' }, { status: 500 })
  }
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json()

    // Traitement IA automatique
    const aiResult = await processWithAI(body)

    const { data, error } = await supabase
      .from('items')
      .insert([{
        ...body,
        ai_processed: true,
        ai_data: aiResult
      }])
      .select()

    if (error) throw error

    return NextResponse.json({ data })
  } catch (error) {
    return NextResponse.json({ error: 'Failed to create item' }, { status: 500 })
  }
}
'''

        file_path = self.output_dir / "src" / "app" / "api" / "items" / "route.ts"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(api_route)

        # Route pour chaque fonctionnalité
        for feature in self.features:
            feature_name = feature.lower().replace(' ', '-')
            feature_route = f'''import {{ NextRequest, NextResponse }} from 'next/server'
import {{ createClient }} from '@supabase/supabase-js'
import {{ processWithAI }} from '@/lib/openai'

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY!
)

export async function POST(request: NextRequest) {{
  try {{
    const body = await request.json()

    // Traitement IA spécifique pour: {feature}
    const prompt = `Traite cette requête pour la fonctionnalité {feature}: ${{JSON.stringify(body)}}`
    const aiResult = await processWithAI({{ prompt, data: body }})

    return NextResponse.json({{
      success: true,
      feature: '{feature}',
      result: aiResult
    }})
  }} catch (error) {{
    return NextResponse.json({{ error: 'Failed to process {feature}' }}, {{ status: 500 }})
  }}
}}
'''

            file_path = self.output_dir / "src" / "app" / "api" / feature_name / "route.ts"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(feature_route)

        print(f"✅ Routes API générées")

    def generate_ui_components(self):
        """Génère les composants UI"""

        # Dashboard Component - utiliser """ au lieu de f''' pour éviter les problèmes avec les accolades JSX
        dashboard_content = """import { useState, useEffect } from 'react'

interface Item {
  id: string
  title: string
  description: string
  status: string
}

export default function Dashboard() {
  const [items, setItems] = useState<Item[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchItems()
  }, [])

  const fetchItems = async () => {
    try {
      const response = await fetch('/api/items')
      const { data } = await response.json()
      setItems(data || [])
    } catch (error) {
      console.error('Error fetching items:', error)
    } finally {
      setLoading(false)
    }
  }

  const features = """ + json.dumps(self.features) + """

  return (
    <div className="max-w-6xl mx-auto">
      <div className="bg-white rounded-lg shadow-xl p-8">
        <h2 className="text-3xl font-bold mb-6 text-gray-800">
          Tableau de Bord
        </h2>

        {/* Fonctionnalités */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          {features.map((feature: string, index: number) => (
            <div
              key={index}
              className="bg-gradient-to-br from-purple-500 to-blue-500 p-6 rounded-lg text-white hover:shadow-lg transition-shadow cursor-pointer"
            >
              <h3 className="text-xl font-semibold mb-2">{feature}</h3>
              <p className="text-sm opacity-90">Cliquez pour utiliser cette fonctionnalité</p>
            </div>
          ))}
        </div>

        {/* Liste des items */}
        <div className="mt-8">
          <h3 className="text-2xl font-semibold mb-4">Éléments récents</h3>
          {loading ? (
            <p>Chargement...</p>
          ) : items.length === 0 ? (
            <p className="text-gray-500">Aucun élément pour le moment</p>
          ) : (
            <div className="space-y-4">
              {items.map(item => (
                <div key={item.id} className="border p-4 rounded-lg hover:shadow-md transition-shadow">
                  <h4 className="font-semibold">{item.title}</h4>
                  <p className="text-gray-600 text-sm">{item.description}</p>
                  <span className="text-xs text-gray-500">Statut: {item.status}</span>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
"""

        file_path = self.output_dir / "src" / "components" / "Dashboard.tsx"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(dashboard_content)

        print(f"✅ Composants UI générés")

    def generate_openai_integration(self):
        """Génère l'intégration OpenAI"""

        openai_content = '''import OpenAI from 'openai'

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
})

export async function processWithAI(data: any) {
  try {
    const completion = await openai.chat.completions.create({
      model: "gpt-4",
      messages: [
        {
          role: "system",
          content: "Tu es un assistant IA qui aide à traiter et enrichir les données d'une application SaaS."
        },
        {
          role: "user",
          content: `Traite cette donnée et retourne un résultat enrichi: ${JSON.stringify(data)}`
        }
      ],
      temperature: 0.7,
      max_tokens: 500
    })

    return {
      success: true,
      aiResponse: completion.choices[0].message.content,
      usage: completion.usage
    }
  } catch (error) {
    console.error('OpenAI Error:', error)
    return {
      success: false,
      error: 'Failed to process with AI'
    }
  }
}

export async function generateContent(prompt: string) {
  try {
    const completion = await openai.chat.completions.create({
      model: "gpt-4",
      messages: [
        {
          role: "user",
          content: prompt
        }
      ],
      temperature: 0.8,
    })

    return completion.choices[0].message.content
  } catch (error) {
    console.error('OpenAI Error:', error)
    throw error
  }
}

export async function analyzeData(data: any) {
  try {
    const completion = await openai.chat.completions.create({
      model: "gpt-4",
      messages: [
        {
          role: "system",
          content: "Analyse ces données et fournis des insights pertinents."
        },
        {
          role: "user",
          content: JSON.stringify(data)
        }
      ],
      temperature: 0.5,
    })

    return {
      insights: completion.choices[0].message.content,
      confidence: 0.85
    }
  } catch (error) {
    console.error('OpenAI Error:', error)
    throw error
  }
}
'''

        file_path = self.output_dir / "src" / "lib" / "openai.ts"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(openai_content)

        print(f"✅ Intégration OpenAI générée")

    def generate_auth_system(self):
        """Génère le système d'authentification"""

        auth_component = '''import { useState } from 'react'

interface AuthFormProps {
  onAuth: () => void
}

export default function AuthForm({ onAuth }: AuthFormProps) {
  const [isLogin, setIsLogin] = useState(true)
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)

    try {
      const response = await fetch('/api/auth', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password, action: isLogin ? 'login' : 'signup' })
      })

      if (response.ok) {
        onAuth()
      } else {
        alert('Erreur d\\'authentification')
      }
    } catch (error) {
      console.error('Auth error:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="max-w-md mx-auto bg-white rounded-lg shadow-xl p-8">
      <h2 className="text-2xl font-bold mb-6 text-center">
        {isLogin ? 'Connexion' : 'Inscription'}
      </h2>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium mb-2">Email</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-purple-500"
            required
          />
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">Mot de passe</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-purple-500"
            required
          />
        </div>

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-gradient-to-r from-purple-600 to-blue-500 text-white py-3 rounded-lg font-semibold hover:shadow-lg transition-shadow disabled:opacity-50"
        >
          {loading ? 'Chargement...' : (isLogin ? 'Se connecter' : 'S\\'inscrire')}
        </button>
      </form>

      <p className="text-center mt-4 text-sm">
        {isLogin ? 'Pas encore de compte ?' : 'Déjà un compte ?'}
        <button
          onClick={() => setIsLogin(!isLogin)}
          className="text-purple-600 font-semibold ml-2"
        >
          {isLogin ? 'S\\'inscrire' : 'Se connecter'}
        </button>
      </p>
    </div>
  )
}
'''

        file_path = self.output_dir / "src" / "components" / "AuthForm.tsx"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(auth_component)

        # Route API d'authentification
        auth_route = '''import { NextRequest, NextResponse } from 'next/server'
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY!
)

export async function POST(request: NextRequest) {
  try {
    const { email, password, action } = await request.json()

    if (action === 'signup') {
      const { data, error } = await supabase.auth.signUp({
        email,
        password,
      })

      if (error) throw error

      return NextResponse.json({ success: true, data })
    } else {
      const { data, error } = await supabase.auth.signInWithPassword({
        email,
        password,
      })

      if (error) throw error

      return NextResponse.json({ success: true, data })
    }
  } catch (error) {
    return NextResponse.json({ error: 'Authentication failed' }, { status: 401 })
  }
}
'''

        file_path = self.output_dir / "src" / "app" / "api" / "auth" / "route.ts"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(auth_route)

        print(f"✅ Système d'authentification généré")

    def generate_readme(self):
        """Génère la documentation README"""

        readme_content = f'''# {self.name}

{self.description}

## 🚀 Fonctionnalités Principales

{chr(10).join(f"- {feature}" for feature in self.features)}

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
{self.name}/
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

{"✅ Système d'authentification activé via Supabase Auth" if self.auth else "❌ Authentification désactivée"}

## 🚀 Déploiement

### Vercel (Recommandé)

```bash
npm install -g vercel
vercel
```

### Docker

```bash
docker build -t {self.name.lower().replace(' ', '-')} .
docker run -p 3000:3000 {self.name.lower().replace(' ', '-')}
```

## 📝 License

MIT

## 🎉 Généré automatiquement

Ce Micro-SaaS a été généré automatiquement par **AI SaaS Builder**
Date de génération : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

**Bon développement ! 🚀**
'''

        file_path = self.output_dir / "README.md"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)

        print(f"✅ README généré")

    def generate_docker_files(self):
        """Génère les fichiers Docker"""

        dockerfile = '''FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
'''

        file_path = self.output_dir / "Dockerfile"
        with open(file_path, 'w') as f:
            f.write(dockerfile)

        dockerignore = '''node_modules
.next
.env
.env.local
.git
.gitignore
README.md
'''

        file_path = self.output_dir / ".dockerignore"
        with open(file_path, 'w') as f:
            f.write(dockerignore)

        # tailwind.config.js
        tailwind_config = '''/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
'''

        file_path = self.output_dir / "tailwind.config.js"
        with open(file_path, 'w') as f:
            f.write(tailwind_config)

        # next.config.js
        next_config = '''/** @type {import('next').NextConfig} */
const nextConfig = {}

module.exports = nextConfig
'''

        file_path = self.output_dir / "next.config.js"
        with open(file_path, 'w') as f:
            f.write(next_config)

        # tsconfig.json
        tsconfig = '''{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
'''

        file_path = self.output_dir / "tsconfig.json"
        with open(file_path, 'w') as f:
            f.write(tsconfig)

        # postcss.config.js
        postcss_config = '''module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
'''

        file_path = self.output_dir / "postcss.config.js"
        with open(file_path, 'w') as f:
            f.write(postcss_config)

        print(f"✅ Fichiers de configuration générés")


def main():
    """Exemple d'utilisation du générateur"""

    # Exemple de données (normalement reçues du frontend)
    example_data = {
        "name": "TalentExpert Pro",
        "description": "Plateforme IA pour optimiser les candidatures et accélérer l'employabilité",
        "features": [
            "Optimisation de CV avec IA",
            "Simulation d'entretien intelligente",
            "Analyse de marché en temps réel"
        ],
        "auth": True
    }

    # Générer le SaaS
    generator = MicroSaaSGenerator(example_data)
    generator.generate_all()


if __name__ == "__main__":
    main()
