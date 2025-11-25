import { useState } from 'react'
import Dashboard from '@/components/Dashboard'
import AuthForm from '@/components/AuthForm'

export default function Home() {
  const [isAuthenticated, setIsAuthenticated] = useState(false)

  return (
    <main className="min-h-screen bg-gradient-to-br from-purple-600 to-blue-500">
      <div className="container mx-auto px-4 py-8">
        <header className="text-center mb-12">
          <h1 className="text-5xl font-bold text-white mb-4">
            TalentExpert Pro
          </h1>
          <p className="text-xl text-white/90">
            Plateforme IA pour optimiser les candidatures et accélérer l'employabilité
          </p>
        </header>

        {
          isAuthenticated ? <Dashboard /> : <AuthForm onAuth={() => setIsAuthenticated(true)} />
        }
      </div>
    </main>
  )
}
