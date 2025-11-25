import { useState } from 'react'

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
        alert('Erreur d\'authentification')
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
          {loading ? 'Chargement...' : (isLogin ? 'Se connecter' : 'S\'inscrire')}
        </button>
      </form>

      <p className="text-center mt-4 text-sm">
        {isLogin ? 'Pas encore de compte ?' : 'Déjà un compte ?'}
        <button
          onClick={() => setIsLogin(!isLogin)}
          className="text-purple-600 font-semibold ml-2"
        >
          {isLogin ? 'S\'inscrire' : 'Se connecter'}
        </button>
      </p>
    </div>
  )
}
