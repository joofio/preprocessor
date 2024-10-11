from medspacy.ner import TargetRule

hiv_rules = [
    # Literal matching for common terms
    TargetRule(literal="HIV", category="CONDITION", attributes={"code": "86406008"}),
    TargetRule(
        literal="human immunodeficiency virus",
        category="CONDITION",
        attributes={"code": "86406008"},
    ),
    TargetRule(
        literal="HIV positive", category="CONDITION", attributes={"code": "86406008"}
    ),
    TargetRule(
        literal="HIV infection", category="CONDITION", attributes={"code": "86406008"}
    ),
    TargetRule(literal="AIDS", category="CONDITION", attributes={"code": "118940003"}),
    TargetRule(
        literal="acquired immunodeficiency syndrome",
        category="CONDITION",
        attributes={"code": "118940003"},
    ),
    # spaCy patterns for capturing variations and related terms
    TargetRule(
        literal="hiv infected",
        pattern=[
            {"LOWER": "hiv"},
            {"LOWER": {"IN": ["1", "2", "infected", "positive"]}},
        ],
        category="CONDITION",
        attributes={"code": "165816005"},
    ),
    # Medications and treatments
    TargetRule(
        literal="tenofovir",
        category="TREATMENT",
        attributes={"code": "117466", "system": "RxNorm"},
    ),
    TargetRule(
        literal="emtricitabine",
        category="TREATMENT",
        attributes={"code": "276237", "system": "RxNorm"},
    ),
    TargetRule(
        literal="dolutegravir",
        category="TREATMENT",
        attributes={"code": "1433868", "system": "RxNorm"},
    ),
    # Risk factors and related behaviors
    TargetRule(
        literal="intravenous drug use",
        pattern=[{"LOWER": "intravenous"}, {"LOWER": "drug"}, {"LOWER": "use"}],
        category="RISK",
        attributes={"code": "386340006"},
    ),
    TargetRule(
        literal="IV drug use",
        pattern=[{"LOWER": "iv"}, {"LOWER": "drug"}, {"LOWER": "use"}],
        category="RISK",
        attributes={"code": "386340006"},
    ),
    TargetRule(
        literal="unprotected sex",
        pattern=[{"LOWER": "unprotected"}, {"LOWER": "sex"}],
        category="RISK",
        attributes={"code": "2314005"},
    ),
    ### synonyms of 19030005
    TargetRule(
        literal="Human immunodeficiency virus",
        pattern=[{"LOWER": "human immunodeficiency virus"}],
        category="CONDITION",
        attributes={"code": "19030005"},
    ),
    TargetRule(
        literal="Human immunodeficiency virus, NOS",
        pattern=[{"LOWER": "human immunodeficiency virus, nos"}],
        category="CONDITION",
        attributes={"code": "19030005"},
    ),
    TargetRule(
        literal="HIV",
        pattern=[{"LOWER": "hiv"}],
        category="CONDITION",
        attributes={"code": "19030005"},
    ),
    TargetRule(
        literal="AIDS virus",
        pattern=[{"LOWER": "aids virus"}],
        category="CONDITION",
        attributes={"code": "19030005"},
    ),
    TargetRule(
        literal="Human immunodeficiency virus (organism)",
        pattern=[{"LOWER": "human immunodeficiency virus (organism)"}],
        category="CONDITION",
        attributes={"code": "19030005"},
    ),
    TargetRule(
        literal="HIV - Human immunodeficiency virus",
        pattern=[{"LOWER": "hiv - human immunodeficiency virus"}],
        category="CONDITION",
        attributes={"code": "19030005"},
    ),
    ### synonyms of 165816005
    TargetRule(
        literal="HTLV-3 antibody positive",
        pattern=[{"LOWER": "htlv-3 antibody positive"}],
        category="CONDITION",
        attributes={"code": "165816005"},
    ),
    TargetRule(
        literal="HIV positive",
        pattern=[{"LOWER": "hiv positive"}],
        category="CONDITION",
        attributes={"code": "165816005"},
    ),
    TargetRule(
        literal="HIV positive (finding)",
        pattern=[{"LOWER": "hiv positive (finding)"}],
        category="CONDITION",
        attributes={"code": "165816005"},
    ),
    TargetRule(
        literal="Human immunodeficiency virus (HIV) positive (finding)",
        pattern=[{"LOWER": "human immunodeficiency virus (hiv) positive (finding)"}],
        category="CONDITION",
        attributes={"code": "165816005"},
    ),
    TargetRule(
        literal="Human immunodeficiency virus (HIV) positive",
        pattern=[{"LOWER": "human immunodeficiency virus (hiv) positive"}],
        category="CONDITION",
        attributes={"code": "165816005"},
    ),
    TargetRule(
        literal="Human immunodeficiency virus positive (finding)",
        pattern=[{"LOWER": "human immunodeficiency virus positive (finding)"}],
        category="CONDITION",
        attributes={"code": "165816005"},
    ),
    TargetRule(
        literal="Human immunodeficiency virus positive",
        pattern=[{"LOWER": "human immunodeficiency virus positive"}],
        category="CONDITION",
        attributes={"code": "165816005"},
    ),
    TargetRule(
        literal="Human immunodeficiency virus detected (finding)",
        pattern=[{"LOWER": "human immunodeficiency virus detected (finding)"}],
        category="CONDITION",
        attributes={"code": "165816005"},
    ),
    TargetRule(
        literal="Human immunodeficiency virus detected",
        pattern=[{"LOWER": "human immunodeficiency virus detected"}],
        category="CONDITION",
        attributes={"code": "165816005"},
    ),
    TargetRule(
        literal="HIV detected",
        pattern=[{"LOWER": "hiv detected"}],
        category="CONDITION",
        attributes={"code": "165816005"},
    ),
    ###synonyms of 86406008
    TargetRule(
        literal="Human immunodeficiency virus infection",
        pattern=[{"LOWER": "human immunodeficiency virus infection"}],
        category="CONDITION",
        attributes={"code": "86406008"},
    ),
    TargetRule(
        literal="Human immunodeficiency virus infection, NOS",
        pattern=[{"LOWER": "human immunodeficiency virus infection, nos"}],
        category="CONDITION",
        attributes={"code": "86406008"},
    ),
    TargetRule(
        literal="HIV infection",
        pattern=[{"LOWER": "hiv infection"}],
        category="CONDITION",
        attributes={"code": "86406008"},
    ),
    TargetRule(
        literal="Human immunodeficiency virus infection (disorder)",
        pattern=[{"LOWER": "human immunodeficiency virus infection (disorder)"}],
        category="CONDITION",
        attributes={"code": "86406008"},
    ),
    TargetRule(
        literal="HIV - Human immunodeficiency virus infection",
        pattern=[{"LOWER": "hiv - human immunodeficiency virus infection"}],
        category="CONDITION",
        attributes={"code": "86406008"},
    ),
]
