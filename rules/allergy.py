from medspacy.ner import TargetRule

# Define the rules for the diabetes NER component
allergy_rules = [
    # Literal matching for common terms
    TargetRule(literal="Lactose", category="PRODUCT", attributes={"code": "47703008"}),
    TargetRule(
        literal="Lactose tolerance test",
        pattern=[{"LOWER": "lactose tolerance test"}],
        category="CONDITION",
        attributes={"code": "34271001"},
    ),
    ###synonym 34271001
    TargetRule(
        literal="Lactose challenge test",
        pattern=[{"LOWER": "lactose challenge test"}],
        category="CONDITION",
        attributes={"code": "34271001"},
    ),
    TargetRule(
        literal="Lactose tolerance test (procedure)",
        pattern=[{"LOWER": "lactose tolerance test (procedure)"}],
        category="CONDITION",
        attributes={"code": "34271001"},
    ),
    TargetRule(
        literal="LTT - Lactose tolerance test",
        pattern=[{"LOWER": "ltt - lactose tolerance test"}],
        category="CONDITION",
        attributes={"code": "34271001"},
    ),
    ###synonym 782415009
    TargetRule(
        literal="Intolerance to lactose",
        pattern=[{"LOWER": "intolerance to lactose"}],
        category="CONDITION",
        attributes={"code": "782415009"},
    ),
    TargetRule(
        literal="Intolerance to lactose (finding)",
        pattern=[{"LOWER": "intolerance to lactose (finding)"}],
        category="CONDITION",
        attributes={"code": "782415009"},
    ),
    ###synonym 190751001
    TargetRule(
        literal="Primary lactose intolerance",
        pattern=[{"LOWER": "primary lactose intolerance"}],
        category="CONDITION",
        attributes={"code": "190751001"},
    ),
    TargetRule(
        literal="Primary lactose intolerance (disorder)",
        pattern=[{"LOWER": "primary lactose intolerance (disorder)"}],
        category="CONDITION",
        attributes={"code": "190751001"},
    ),
    TargetRule(
        literal="Primary intolerance to lactose",
        pattern=[{"LOWER": "primary intolerance to lactose"}],
        category="CONDITION",
        attributes={"code": "190751001"},
    ),
    TargetRule(
        literal="Primary intolerance to lactose (finding)",
        pattern=[{"LOWER": "primary intolerance to lactose (finding)"}],
        category="CONDITION",
        attributes={"code": "190751001"},
    ),
]
