from medspacy.ner import TargetRule

pregnancy_rules = [
    # Basic terms related to pregnancy
    TargetRule(literal="pregnancy", category="PREGNANCY", attributes={"code": "77386006"}),
    TargetRule(literal="pregnant", category="PREGNANCY", attributes={"code": "77386006"}),
    TargetRule(literal="gestation", category="PREGNANCY", attributes={"code": "77386006"}),
    TargetRule(literal="antenatal", category="PREGNANCY", attributes={"code": "263675000"}),
    TargetRule(literal="prenatal", category="PREGNANCY", attributes={"code": "118189007"}),
    
    # Phrases indicating pregnancy-related information
    TargetRule(literal="during pregnancy", pattern=[{"LOWER": "during"}, {"LOWER": "pregnancy"}], category="PREGNANCY", attributes={"code": "77386006"}),
    TargetRule(literal="if you are pregnant", pattern=[{"LOWER": "if"}, {"LOWER": "you"}, {"LOWER": "are"}, {"LOWER": "pregnant"}], category="PREGNANCY", attributes={"code": "77386006"}),
    TargetRule(literal="when pregnant", pattern=[{"LOWER": "when"}, {"LOWER": "pregnant"}], category="PREGNANCY", attributes={"code": "77386006"}),
    TargetRule(literal="while pregnant", pattern=[{"LOWER": "while"}, {"LOWER": "pregnant"}], category="PREGNANCY", attributes={"code": "77386006"}),
    TargetRule(literal="planning to became pregnant", pattern=[{"LOWER": "planning"}, {"LOWER": "to"}, {"LOWER": "become"}, {"LOWER": "pregnant"}], category="PREGNANCY", attributes={"code": "77386006"}),
    
    # Medications and warnings specific to pregnancy
    TargetRule(literal="contraindicated in pregnancy", pattern=[{"LOWER": "contraindicated"}, {"LOWER": "in"}, {"LOWER": "pregnancy"}], category="PREGNANCY_WARNING", attributes={"code": "77386006"}),
    TargetRule(literal="not recommended during pregnancy", pattern=[{"LOWER": "not"}, {"LOWER": "recommended"}, {"LOWER": "during"}, {"LOWER": "pregnancy"}], category="PREGNANCY_WARNING", attributes={"code": "77386006"}),
    TargetRule(literal="use with caution during pregnancy", pattern=[{"LOWER": "use"}, {"LOWER": "with"}, {"LOWER": "caution"}, {"LOWER": "during"}, {"LOWER": "pregnancy"}], category="PREGNANCY_WARNING", attributes={"code": "77386006"}),
    
    # Effects on the fetus or baby
    TargetRule(literal="risk of birth defects", pattern=[{"LOWER": "risk"}, {"LOWER": "of"}, {"LOWER": "birth"}, {"LOWER": "defects"}], category="PREGNANCY_RISK", attributes={"code": "LP192135-4", "system": "LOINC"}),
    TargetRule(literal="may harm the unborn baby", pattern=[{"LOWER": "may"}, {"LOWER": "harm"}, {"LOWER": "the"}, {"LOWER": "unborn"}, {"LOWER": "baby"}], category="PREGNANCY_RISK", attributes={"code": "LP192135-4", "system": "LOINC"}),
    TargetRule(literal="can cause birth defects", pattern=[{"LOWER": "can"}, {"LOWER": "cause"}, {"LOWER": "birth"}, {"LOWER": "defects"}], category="PREGNANCY_RISK", attributes={"code": "LP192135-4", "system": "LOINC"}),
    
    # Safe use during pregnancy
    TargetRule(literal="safe for use during pregnancy", pattern=[{"LOWER": "safe"}, {"LOWER": "for"}, {"LOWER": "use"}, {"LOWER": "during"}, {"LOWER": "pregnancy"}], category="PREGNANCY_SAFETY", attributes={"code": "77386006"}),
    TargetRule(literal="no known risk during pregnancy", pattern=[{"LOWER": "no"}, {"LOWER": "known"}, {"LOWER": "risk"}, {"LOWER": "during"}, {"LOWER": "pregnancy"}], category="PREGNANCY_SAFETY",  attributes={"code": "77386006"}),
]