-- Base de données pour TalentExpert Pro
-- Plateforme IA pour optimiser les candidatures et accélérer l'employabilité

-- Table: users
CREATE TABLE IF NOT EXISTS users (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  email VARCHAR(255) UNIQUE,
  name VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW()
);

-- Table: items
CREATE TABLE IF NOT EXISTS items (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  title VARCHAR(255),
  description TEXT,
  status VARCHAR(255),
  ai_processed BOOLEAN DEFAULT False,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Table: optimisation_de_cv_avec_ia
CREATE TABLE IF NOT EXISTS optimisation_de_cv_avec_ia (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name VARCHAR(255),
  data JSONB,
  ai_generated BOOLEAN DEFAULT False,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Table: simulation_d'entretien_intelligente
CREATE TABLE IF NOT EXISTS simulation_d'entretien_intelligente (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name VARCHAR(255),
  data JSONB,
  ai_generated BOOLEAN DEFAULT False,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Table: analyse_de_marché_en_temps_réel
CREATE TABLE IF NOT EXISTS analyse_de_marché_en_temps_réel (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name VARCHAR(255),
  data JSONB,
  ai_generated BOOLEAN DEFAULT False,
  created_at TIMESTAMP DEFAULT NOW()
);

