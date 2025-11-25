import { useState, useEffect } from 'react'

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

  const features = ["Optimisation de CV avec IA", "Simulation d'entretien intelligente", "Analyse de march\u00e9 en temps r\u00e9el"]

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
