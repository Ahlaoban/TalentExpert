import { NextRequest, NextResponse } from 'next/server'
import { createClient } from '@supabase/supabase-js'
import { processWithAI } from '@/lib/openai'

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY!
)

export async function POST(request: NextRequest) {
  try {
    const body = await request.json()

    // Traitement IA spécifique pour: Analyse de marché en temps réel
    const prompt = `Traite cette requête pour la fonctionnalité Analyse de marché en temps réel: ${JSON.stringify(body)}`
    const aiResult = await processWithAI({ prompt, data: body })

    return NextResponse.json({
      success: true,
      feature: 'Analyse de marché en temps réel',
      result: aiResult
    })
  } catch (error) {
    return NextResponse.json({ error: 'Failed to process Analyse de marché en temps réel' }, { status: 500 })
  }
}
