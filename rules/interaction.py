from medspacy.ner import TargetRule

# Define the rules for the diabetes NER component
interaction_rules = [
    # Literal matching for common terms
    TargetRule(
        literal="Decreased renal function (finding)",
        category="CONDITION",
        attributes={"code": "76114004"},
    ),
    # Literal matching for common terms
    TargetRule(
        literal="Hypericum perforatum L.",
        category="PRODUCT",
        attributes={
            "code": "XK4IUX8MNB",
            "system": "https://gsrs.ncats.nih.gov/ginas/app/beta",
        },
    ),
    TargetRule(
        literal="Hypericum perforatum",
        category="PRODUCT",
        attributes={
            "code": "XK4IUX8MNB",
            "system": "https://gsrs.ncats.nih.gov/ginas/app/beta",
        },
    ),
    TargetRule(
        literal="St. John’s wort",
        category="PRODUCT",
        attributes={
            "code": "XK4IUX8MNB",
            "system": "https://gsrs.ncats.nih.gov/ginas/app/beta",
        },
    ),
]
