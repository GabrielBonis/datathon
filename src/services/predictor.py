def predict_pipeline(data):
    # Exemplo dummy
    if data.skill_level > 7 and data.motivation_score > 0.8:
        return "Aprovado"
    return "Reprovado"
