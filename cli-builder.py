#!/usr/bin/env python3
"""
AI SaaS Builder - Interface en Ligne de Commande Interactive
Posez 4 questions et générez un Micro-SaaS complet
"""

import sys
from saas_generator import MicroSaaSGenerator


def print_header():
    """Affiche l'en-tête du builder"""
    print("\n" + "="*70)
    print("🚀 AI SAAS BUILDER - Créez votre Micro-SaaS en quelques minutes")
    print("="*70 + "\n")


def print_progress(step, total=4):
    """Affiche la progression"""
    bar_length = 40
    filled = int(bar_length * step / total)
    bar = "█" * filled + "░" * (bar_length - filled)
    percentage = int(100 * step / total)
    print(f"\nProgression: [{bar}] {percentage}%\n")


def ask_question_1():
    """Question 1: Nom du Micro-SaaS"""
    print("━" * 70)
    print("📝 Question 1/4")
    print("━" * 70)
    print("\n🎯 Quel est le nom de ton Micro-SaaS ?")
    print("💡 Exemple: TalentTracker, LeadGen Pro, ContentWizard...\n")

    while True:
        name = input("➜ Nom: ").strip()
        if name:
            return name
        print("⚠️  Le nom ne peut pas être vide. Réessayez.\n")


def ask_question_2():
    """Question 2: Description"""
    print("\n" + "━" * 70)
    print("📝 Question 2/4")
    print("━" * 70)
    print("\n📖 Quelle est sa description en quelques lignes ?")
    print("💡 Décrivez en 2-3 phrases ce que fait votre SaaS et le problème qu'il résout\n")

    while True:
        description = input("➜ Description: ").strip()
        if description:
            return description
        print("⚠️  La description ne peut pas être vide. Réessayez.\n")


def ask_question_3():
    """Question 3: 3 fonctionnalités principales"""
    print("\n" + "━" * 70)
    print("📝 Question 3/4")
    print("━" * 70)
    print("\n⚡ Quelles sont les 3 fonctionnalités principales ?\n")

    features = []
    for i in range(1, 4):
        while True:
            feature = input(f"➜ Fonctionnalité {i}: ").strip()
            if feature:
                features.append(feature)
                break
            print("⚠️  La fonctionnalité ne peut pas être vide. Réessayez.\n")

    return features


def ask_question_4():
    """Question 4: Authentification"""
    print("\n" + "━" * 70)
    print("📝 Question 4/4")
    print("━" * 70)
    print("\n🔐 As-tu besoin d'un système d'authentification utilisateur ?")
    print("💡 L'authentification permet de gérer des comptes utilisateurs\n")

    while True:
        choice = input("➜ Choix (oui/non): ").strip().lower()
        if choice in ['oui', 'o', 'yes', 'y']:
            return True
        elif choice in ['non', 'n', 'no']:
            return False
        print("⚠️  Répondez par 'oui' ou 'non'. Réessayez.\n")


def display_summary(data):
    """Affiche un résumé des choix"""
    print("\n" + "="*70)
    print("📋 RÉSUMÉ DE VOTRE MICRO-SAAS")
    print("="*70)
    print(f"\n🎯 Nom: {data['name']}")
    print(f"\n📖 Description:\n   {data['description']}")
    print(f"\n⚡ Fonctionnalités:")
    for i, feature in enumerate(data['features'], 1):
        print(f"   {i}. {feature}")
    print(f"\n🔐 Authentification: {'✅ Oui' if data['auth'] else '❌ Non'}")
    print("\n" + "="*70 + "\n")


def confirm_generation():
    """Demande confirmation avant de générer"""
    while True:
        choice = input("✨ Générer ce Micro-SaaS ? (oui/non): ").strip().lower()
        if choice in ['oui', 'o', 'yes', 'y']:
            return True
        elif choice in ['non', 'n', 'no']:
            return False
        print("⚠️  Répondez par 'oui' ou 'non'.\n")


def main():
    """Fonction principale"""
    try:
        print_header()

        # Question 1
        print_progress(0, 4)
        name = ask_question_1()

        # Question 2
        print_progress(1, 4)
        description = ask_question_2()

        # Question 3
        print_progress(2, 4)
        features = ask_question_3()

        # Question 4
        print_progress(3, 4)
        auth = ask_question_4()

        # Complétion
        print_progress(4, 4)

        # Préparer les données
        saas_data = {
            "name": name,
            "description": description,
            "features": features,
            "auth": auth
        }

        # Afficher le résumé
        display_summary(saas_data)

        # Demander confirmation
        if not confirm_generation():
            print("\n❌ Génération annulée.\n")
            return

        # Générer le SaaS
        print("\n🔥 Génération en cours...\n")
        print("="*70 + "\n")

        generator = MicroSaaSGenerator(saas_data)
        generator.generate_all()

        # Message de succès
        print("\n" + "="*70)
        print("🎉 FÉLICITATIONS ! Votre Micro-SaaS est prêt !")
        print("="*70)
        print(f"\n📦 Fichiers générés dans: generated-saas-{name.lower().replace(' ', '-')}/")
        print("\n📚 Prochaines étapes:")
        print(f"   1. cd generated-saas-{name.lower().replace(' ', '-')}")
        print("   2. npm install")
        print("   3. Configurez vos variables d'environnement (.env)")
        print("   4. npm run dev")
        print("\n💡 Consultez le README.md pour plus de détails\n")
        print("="*70 + "\n")

    except KeyboardInterrupt:
        print("\n\n⚠️  Génération interrompue par l'utilisateur.\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erreur: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
