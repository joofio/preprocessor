from medspacy.ner import TargetRule

# Add custom code attributes to the Span class



# Define the rules for the diabetes NER component
diabetes_rules = [
    # Literal matching for common terms
    TargetRule(literal="diabetes", category="CONDITION", code="73211009"),
    TargetRule(literal="diabetic", category="CONDITION", code="73211009"),
    TargetRule(literal="type 1 diabetes", category="CONDITION", code="46635009"),
    TargetRule(literal="type 2 diabetes", category="CONDITION", code="44054006"),
    TargetRule(literal="type I diabetes", category="CONDITION", code="46635009"),
    TargetRule(literal="type II diabetes", category="CONDITION", code="44054006"),
    TargetRule(literal="DM1", category="CONDITION", code="46635009"),
    TargetRule(literal="DM2", category="CONDITION", code="44054006"),
    TargetRule(literal="insulin resistance", pattern=[{"LOWER": "insulin"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "resistance"}], category="CONDITION", code="763325000"),
    TargetRule(literal="hyperglycemia", category="CONDITION"),
    TargetRule(literal="hypoglycemia", category="CONDITION"),
    TargetRule(literal="", pattern=[{"LOWER": "glucose"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "intolerance"}], category="CONDITION"),
    TargetRule(literal="", pattern=[{"LOWER": "gestational"}, {"LOWER": "diabetes"}], category="CONDITION"),
    TargetRule(literal="", pattern=[{"LOWER": "pre"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "diabetes"}], category="CONDITION"),
    TargetRule(literal="", pattern=[{"LOWER": "prediabetes"}], category="CONDITION"),

    # Contextual rules using spaCy patterns (e.g., "history of diabetes")
    TargetRule(literal="", pattern=[{"LOWER": "history"}, {"LOWER": "of"}, {"LOWER": {"IN": ["diabetes", "dm1", "dm2"]}}], category="CONDITION"),
    TargetRule(literal="", pattern=[{"LOWER": "family"}, {"LOWER": "history"}, {"LOWER": "of"}, {"LOWER": {"IN": ["diabetes", "type", "1", "2"]}}], category="CONDITION"),
    TargetRule(literal="", pattern=[{"LOWER": "poorly"}, {"LOWER": "controlled"}, {"LOWER": "diabetes"}], category="CONDITION"),

    # Medication and treatment-related rules
    TargetRule(literal="metformin", category="TREATMENT"),
    TargetRule(literal="insulin", category="TREATMENT"),
    TargetRule(literal="insulin therapy", category="TREATMENT"),
    TargetRule(literal="glucose monitoring", category="TREATMENT"),
    TargetRule(literal="", pattern=[{"LOWER": "sglt2"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "inhibitor"}], category="TREATMENT"),
    TargetRule(literal="", pattern=[{"LOWER": "glp1"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "receptor"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "agonist"}], category="TREATMENT"),

    # Complications associated with diabetes
    TargetRule(literal="diabetic neuropathy", category="COMPLICATION"),
    TargetRule(literal="diabetic retinopathy", category="COMPLICATION"),
    TargetRule(literal="diabetic nephropathy", category="COMPLICATION"),
    TargetRule(literal="", pattern=[{"LOWER": "diabetic"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "foot"}], category="COMPLICATION"),
    TargetRule(literal="", pattern=[{"LOWER": "hyperosmolar"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "hyperglycemic"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "state"}], category="COMPLICATION"),
    TargetRule(literal="", pattern=[{"LOWER": "diabetic"}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": "ketoacidosis"}], category="COMPLICATION"),
]