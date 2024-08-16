from medspacy.ner import TargetRule

pregnancy_rules = [
    # Basic terms related to pregnancy
    TargetRule(literal="pregnancy", category="PREGNANCY", attributes={"code": "77386006"}),
    TargetRule(literal="pregnant", category="PREGNANCY", attributes={"code": "77386006"}),
    TargetRule(literal="gestation", category="PREGNANCY", attributes={"code": "77386006"}),
    TargetRule(literal="antenatal", category="PREGNANCY", attributes={"code": "263675000"}),
    TargetRule(literal="prenatal", category="PREGNANCY", attributes={"code": "118189007"}),
    
    # Phrases indicating pregnancy-related information
    TargetRule(literal="", pattern=[{"LOWER": "during"}, {"LOWER": "pregnancy"}], category="PREGNANCY"),
    TargetRule(literal="", pattern=[{"LOWER": "if"}, {"LOWER": "you"}, {"LOWER": "are"}, {"LOWER": "pregnant"}], category="PREGNANCY"),
    TargetRule(literal="", pattern=[{"LOWER": "when"}, {"LOWER": "pregnant"}], category="PREGNANCY"),
    TargetRule(literal="", pattern=[{"LOWER": "while"}, {"LOWER": "pregnant"}], category="PREGNANCY"),
    TargetRule(literal="", pattern=[{"LOWER": "planning"}, {"LOWER": "to"}, {"LOWER": "become"}, {"LOWER": "pregnant"}], category="PREGNANCY"),
    
    # Pregnancy-related conditions
    TargetRule(literal="gestational diabetes", category="PREGNANCY_CONDITION"),
    TargetRule(literal="pre-eclampsia", category="PREGNANCY_CONDITION"),
    TargetRule(literal="eclampsia", category="PREGNANCY_CONDITION"),
    TargetRule(literal="hyperemesis gravidarum", category="PREGNANCY_CONDITION"),
    TargetRule(literal="morning sickness", category="PREGNANCY_CONDITION"),
    
    # Medications and warnings specific to pregnancy
    TargetRule(literal="contraindicated in pregnancy", pattern=[{"LOWER": "contraindicated"}, {"LOWER": "in"}, {"LOWER": "pregnancy"}], category="PREGNANCY_WARNING", attributes={"code": "77386006"}),
    TargetRule(literal="", pattern=[{"LOWER": "not"}, {"LOWER": "recommended"}, {"LOWER": "during"}, {"LOWER": "pregnancy"}], category="PREGNANCY_WARNING", attributes={"code": "77386006"}),
    TargetRule(literal="", pattern=[{"LOWER": "use"}, {"LOWER": "with"}, {"LOWER": "caution"}, {"LOWER": "during"}, {"LOWER": "pregnancy"}], category="PREGNANCY_WARNING", attributes={"code": "77386006"}),
    TargetRule(literal="", pattern=[{"LOWER": "pregnancy"}, {"LOWER": "category"}, {"LOWER": {"IN": ["a", "b", "c", "d", "x"]}}], category="PREGNANCY_WARNING"),
    
    # Effects on the fetus or baby
    TargetRule(literal="risk of birth defects", pattern=[{"LOWER": "risk"}, {"LOWER": "of"}, {"LOWER": "birth"}, {"LOWER": "defects"}], category="PREGNANCY_RISK"),
    TargetRule(literal="", pattern=[{"LOWER": "may"}, {"LOWER": "harm"}, {"LOWER": "the"}, {"LOWER": "unborn"}, {"LOWER": "baby"}], category="PREGNANCY_RISK"),
    TargetRule(literal="", pattern=[{"LOWER": "fetal"}, {"LOWER": "toxicity"}], category="PREGNANCY_RISK"),
    TargetRule(literal="", pattern=[{"LOWER": "teratogenic"}, {"LOWER": "effects"}], category="PREGNANCY_RISK"),
    TargetRule(literal="", pattern=[{"LOWER": "can"}, {"LOWER": "cause"}, {"LOWER": "birth"}, {"LOWER": "defects"}], category="PREGNANCY_RISK"),
    
    # Safe use during pregnancy
    TargetRule(literal="", pattern=[{"LOWER": "safe"}, {"LOWER": "for"}, {"LOWER": "use"}, {"LOWER": "during"}, {"LOWER": "pregnancy"}], category="PREGNANCY_SAFETY"),
    TargetRule(literal="", pattern=[{"LOWER": "no"}, {"LOWER": "known"}, {"LOWER": "risk"}, {"LOWER": "during"}, {"LOWER": "pregnancy"}], category="PREGNANCY_SAFETY"),
]