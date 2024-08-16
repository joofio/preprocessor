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
    TargetRule(literal="", pattern=[{"LOWER": "hiv"}, {"LOWER": "positive"}], category="CONDITION"),
    TargetRule(literal="", pattern=[{"LOWER": "hiv"}, {"LOWER": "1"}], category="CONDITION"),
    TargetRule(literal="", pattern=[{"LOWER": "hiv"}, {"LOWER": "2"}], category="CONDITION"),
    TargetRule(literal="", pattern=[{"LOWER": "hiv"}, {"LOWER": "infected"}], category="CONDITION"),
    TargetRule(literal="", pattern=[{"LOWER": "anti"}, {"LOWER": "retroviral"}, {"LOWER": "therapy"}], category="TREATMENT"),
    TargetRule(literal="", pattern=[{"LOWER": "antiretroviral"}, {"LOWER": "therapy"}], category="TREATMENT"),
    TargetRule(literal="", pattern=[{"LOWER": "highly"}, {"LOWER": "active"}, {"LOWER": "antiretroviral"}, {"LOWER": "therapy"}], category="TREATMENT"),
    TargetRule(literal="", pattern=[{"LOWER": "history"}, {"LOWER": "of"}, {"LOWER": {"IN": ["hiv", "aids"]}}], category="CONDITION"),
    TargetRule(literal="", pattern=[{"LOWER": "newly"}, {"LOWER": "diagnosed"}, {"LOWER": "hiv"}], category="CONDITION"),
    TargetRule(literal="", pattern=[{"LOWER": "long"}, {"LOWER": "-"}, {"LOWER": "term"}, {"LOWER": "hiv"}], category="CONDITION"),
    
    # Complications and related conditions
    TargetRule(literal="", pattern=[{"LOWER": "opportunistic"}, {"LOWER": "infection"}], category="COMPLICATION"),
    TargetRule(literal="", pattern=[{"LOWER": "pneumocystis"}, {"LOWER": "pneumonia"}], category="COMPLICATION"),
    TargetRule(literal="", pattern=[{"LOWER": "kaposi"}, {"LOWER": "'s"}, {"LOWER": "sarcoma"}], category="COMPLICATION"),
    TargetRule(literal="", pattern=[{"LOWER": "cytomegalovirus"}, {"LOWER": "retinitis"}], category="COMPLICATION"),
    TargetRule(literal="", pattern=[{"LOWER": "hiv"}, {"LOWER": "associated"}, {"LOWER": "neurocognitive"}, {"LOWER": "disorder"}], category="COMPLICATION"),
    TargetRule(literal="", pattern=[{"LOWER": "hiv"}, {"LOWER": "related"}, {"LOWER": "dementia"}], category="COMPLICATION"),
    
    # Medications and treatments
    TargetRule(literal="tenofovir", category="TREATMENT"),
    TargetRule(literal="emtricitabine", category="TREATMENT"),
    TargetRule(literal="dolutegravir", category="TREATMENT"),
    TargetRule(literal="", pattern=[{"LOWER": "pre"}, {"LOWER": "-"}, {"LOWER": "exposure"}, {"LOWER": "prophylaxis"}], category="TREATMENT"),
    TargetRule(literal="", pattern=[{"LOWER": "post"}, {"LOWER": "-"}, {"LOWER": "exposure"}, {"LOWER": "prophylaxis"}], category="TREATMENT"),
    
    # Risk factors and related behaviors
    TargetRule(literal="", pattern=[{"LOWER": "intravenous"}, {"LOWER": "drug"}, {"LOWER": "use"}], category="RISK"),
    TargetRule(literal="", pattern=[{"LOWER": "iv"}, {"LOWER": "drug"}, {"LOWER": "use"}], category="RISK"),
    TargetRule(literal="", pattern=[{"LOWER": "unprotected"}, {"LOWER": "sex"}], category="RISK"),
    TargetRule(literal="", pattern=[{"LOWER": "sex"}, {"LOWER": "with"}, {"LOWER": "men"}], category="RISK"),
    TargetRule(literal="", pattern=[{"LOWER": "needle"}, {"LOWER": "sharing"}], category="RISK"),
]