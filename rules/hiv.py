from medspacy.ner import TargetRule

hiv_rules = [
    # Literal matching for common terms
    TargetRule(literal="HIV", category="CONDITION", attributes={"code": "86406008"}),
    TargetRule(literal="human immunodeficiency virus", category="CONDITION", attributes={"code": "86406008"}),
    TargetRule(literal="HIV positive", category="CONDITION", attributes={"code": "86406008"}),
    TargetRule(literal="HIV infection", category="CONDITION", attributes={"code": "86406008"}),
    TargetRule(literal="AIDS", category="CONDITION", attributes={"code": "118940003"}),
    TargetRule(literal="acquired immunodeficiency syndrome", category="CONDITION", attributes={"code": "118940003"}),
    
    # spaCy patterns for capturing variations and related terms
    TargetRule(literal="hiv infected", pattern=[{"LOWER": "hiv"}, {"LOWER": {"IN": ["1", "2", "infected", "positive"]}}], category="CONDITION", attributes={"code": "165816005"}),
    
    # Medications and treatments
    TargetRule(literal="tenofovir", category="TREATMENT", attributes={"code": "117466", "system": "RxNorm"}),
    TargetRule(literal="emtricitabine", category="TREATMENT", attributes={"code": "276237", "system": "RxNorm"}),
    TargetRule(literal="dolutegravir", category="TREATMENT", attributes={"code": "1433868", "system": "RxNorm"}),
    
    # Risk factors and related behaviors
    TargetRule(literal="intravenous drug use", pattern=[{"LOWER": "intravenous"}, {"LOWER": "drug"}, {"LOWER": "use"}], category="RISK", attributes={"code": "386340006"}),
    TargetRule(literal="IV drug use", pattern=[{"LOWER": "iv"}, {"LOWER": "drug"}, {"LOWER": "use"}], category="RISK", attributes={"code": "386340006"}),
    TargetRule(literal="unprotected sex", pattern=[{"LOWER": "unprotected"}, {"LOWER": "sex"}], category="RISK", attributes={"code": "2314005"}),
]