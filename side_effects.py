from medspacy.ner import TargetRule

side_effect_rules = [
    # 1. Nausea
    TargetRule(
        literal="nausea",
        category="SIDE_EFFECT",
        pattern=[{"LOWER": {"IN": ["nausea", "feeling sick", "upset stomach"]}}],
        attributes={"code": "422587007"}
    ),
    
    # 2. Drowsiness
    TargetRule(
        literal="drowsiness",
        category="SIDE_EFFECT",
        pattern=[{"LOWER": {"IN": ["drowsiness", "sleepiness", "somnolence"]}}],
        attributes={"code": "79519003"}
    ),
    
    # 3. Dizziness
    TargetRule(
        literal="dizziness",
        category="SIDE_EFFECT",
        pattern=[{"LOWER": {"IN": ["dizziness", "lightheadedness", "vertigo"]}}],
        attributes={"code": "404640003"}
    ),
    
    # 4. Headache
    TargetRule(
        literal="headache",
        category="SIDE_EFFECT",
        pattern=[{"LOWER": {"IN": ["headache", "migraine"]}}],
        attributes={"code": "25064002"}
    ),
    
    # 5. Dry Mouth
    TargetRule(
        literal="dry mouth",
        category="SIDE_EFFECT",
        pattern=[{"LOWER": {"IN": ["dry mouth", "xerostomia"]}}],
        attributes={"code": "87715008"}
    ),
    
    # 6. Diarrhea
    TargetRule(
        literal="diarrhea",
        category="SIDE_EFFECT",
        pattern=[{"LOWER": {"IN": ["diarrhea", "loose stools", "watery stools", "diarrhoea"]}}],
        attributes={"code": "62315008"}
    ),
    
    # 7. Constipation
    TargetRule(
        literal="constipation",
        category="SIDE_EFFECT",
        pattern=[{"LOWER": {"IN": ["constipation", "hard stools"]}}],
        attributes={"code": "14760008"}
    ),
    
    # 8. Rash or Itching
    TargetRule(
        literal="rash",
        category="SIDE_EFFECT",
        pattern=[{"LOWER": {"IN": ["rash", "itching", "pruritus", "hives", "urticaria"]}}],
        attributes={"code": "418290006"}
    ),
    
    # 9. Blurred Vision
    TargetRule(
        literal="blurred vision",
        category="SIDE_EFFECT",
        pattern=[{"LOWER": {"IN": ["blurred vision", "vision blurriness"]}}],
        attributes={"code": "240091000000105"}
    ),
    
    # 10. Weight Gain
    TargetRule(
        literal="weight gain",
        category="SIDE_EFFECT",
        pattern=[{"LOWER": {"IN": ["weight gain", "increased weight"]}}],
        attributes={"code": "8943002"}
    ),
    
    # 11. Insomnia
    TargetRule(
        literal="insomnia",
        category="SIDE_EFFECT",
        pattern=[{"LOWER": {"IN": ["insomnia", "trouble sleeping", "sleep disturbances"]}}],
        attributes={"code": "193462001"}
    ),
    
    # 12. Swelling
    TargetRule(
        literal="swelling",
        category="SIDE_EFFECT",
        pattern=[{"LOWER": {"IN": ["swelling", "edema", "fluid retention"]}}],
        attributes={"code": "65124004"}
    ),
    
    # 13. Fatigue
    TargetRule(
        literal="fatigue",
        category="SIDE_EFFECT",
        pattern=[{"LOWER": {"IN": ["fatigue", "tiredness", "exhaustion"]}}],
        attributes={"code": "84229001"}
    ),
    
    # 14. Loss of Appetite
    TargetRule(
        literal="loss of appetite",
        category="SIDE_EFFECT",
        pattern=[{"LOWER": {"IN": ["loss of appetite", "decreased appetite", "anorexia"]}}],
        attributes={"code": "79890006"}
    ),
    
    # 15. Heartburn or Acid Reflux
    TargetRule(
        literal="heartburn",
        category="SIDE_EFFECT",
        pattern=[{"LOWER": {"IN": ["heartburn", "acid reflux", "indigestion", "dyspepsia"]}}],
        attributes={"code": "698065002"}
    ),
]