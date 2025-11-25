import OpenAI from 'openai'

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
