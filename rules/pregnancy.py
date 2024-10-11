from medspacy.ner import TargetRule

pregnancy_rules = [
    # Basic terms related to pregnancy
    TargetRule(
        literal="pregnancy", category="PREGNANCY", attributes={"code": "77386006"}
    ),
    TargetRule(
        literal="pregnant", category="PREGNANCY", attributes={"code": "77386006"}
    ),
    TargetRule(
        literal="gestation", category="PREGNANCY", attributes={"code": "77386006"}
    ),
    TargetRule(
        literal="antenatal", category="PREGNANCY", attributes={"code": "263675000"}
    ),
    TargetRule(
        literal="prenatal", category="PREGNANCY", attributes={"code": "118189007"}
    ),
    # Phrases indicating pregnancy-related information
    TargetRule(
        literal="during pregnancy",
        pattern=[{"LOWER": "during"}, {"LOWER": "pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "77386006"},
    ),
    TargetRule(
        literal="if you are pregnant",
        pattern=[
            {"LOWER": "if"},
            {"LOWER": "you"},
            {"LOWER": "are"},
            {"LOWER": "pregnant"},
        ],
        category="PREGNANCY",
        attributes={"code": "77386006"},
    ),
    TargetRule(
        literal="when pregnant",
        pattern=[{"LOWER": "when"}, {"LOWER": "pregnant"}],
        category="PREGNANCY",
        attributes={"code": "77386006"},
    ),
    TargetRule(
        literal="while pregnant",
        pattern=[{"LOWER": "while"}, {"LOWER": "pregnant"}],
        category="PREGNANCY",
        attributes={"code": "77386006"},
    ),
    TargetRule(
        literal="planning to became pregnant",
        pattern=[
            {"LOWER": "planning"},
            {"LOWER": "to"},
            {"LOWER": "become"},
            {"LOWER": "pregnant"},
        ],
        category="PREGNANCY",
        attributes={"code": "77386006"},
    ),
    # Medications and warnings specific to pregnancy
    TargetRule(
        literal="contraindicated in pregnancy",
        pattern=[{"LOWER": "contraindicated"}, {"LOWER": "in"}, {"LOWER": "pregnancy"}],
        category="PREGNANCY_WARNING",
        attributes={"code": "77386006"},
    ),
    TargetRule(
        literal="not recommended during pregnancy",
        pattern=[
            {"LOWER": "not"},
            {"LOWER": "recommended"},
            {"LOWER": "during"},
            {"LOWER": "pregnancy"},
        ],
        category="PREGNANCY_WARNING",
        attributes={"code": "77386006"},
    ),
    TargetRule(
        literal="use with caution during pregnancy",
        pattern=[
            {"LOWER": "use"},
            {"LOWER": "with"},
            {"LOWER": "caution"},
            {"LOWER": "during"},
            {"LOWER": "pregnancy"},
        ],
        category="PREGNANCY_WARNING",
        attributes={"code": "77386006"},
    ),
    # Effects on the fetus or baby
    TargetRule(
        literal="risk of birth defects",
        pattern=[
            {"LOWER": "risk"},
            {"LOWER": "of"},
            {"LOWER": "birth"},
            {"LOWER": "defects"},
        ],
        category="PREGNANCY_RISK",
        attributes={"code": "LP192135-4", "system": "LOINC"},
    ),
    TargetRule(
        literal="may harm the unborn baby",
        pattern=[
            {"LOWER": "may"},
            {"LOWER": "harm"},
            {"LOWER": "the"},
            {"LOWER": "unborn"},
            {"LOWER": "baby"},
        ],
        category="PREGNANCY_RISK",
        attributes={"code": "LP192135-4", "system": "LOINC"},
    ),
    TargetRule(
        literal="can cause birth defects",
        pattern=[
            {"LOWER": "can"},
            {"LOWER": "cause"},
            {"LOWER": "birth"},
            {"LOWER": "defects"},
        ],
        category="PREGNANCY_RISK",
        attributes={"code": "LP192135-4", "system": "LOINC"},
    ),
    # Safe use during pregnancy
    TargetRule(
        literal="safe for use during pregnancy",
        pattern=[
            {"LOWER": "safe"},
            {"LOWER": "for"},
            {"LOWER": "use"},
            {"LOWER": "during"},
            {"LOWER": "pregnancy"},
        ],
        category="PREGNANCY_SAFETY",
        attributes={"code": "77386006"},
    ),
    TargetRule(
        literal="no known risk during pregnancy",
        pattern=[
            {"LOWER": "no"},
            {"LOWER": "known"},
            {"LOWER": "risk"},
            {"LOWER": "during"},
            {"LOWER": "pregnancy"},
        ],
        category="PREGNANCY_SAFETY",
        attributes={"code": "77386006"},
    ),
    ###breast feeding 69840006 synonyms
    TargetRule(
        literal="Normal breast feeding",
        pattern=[{"LOWER": "normal breast feeding"}],
        category="CONDITION",
        attributes={"code": "69840006"},
    ),
    TargetRule(
        literal="Effective breastfeeding",
        pattern=[{"LOWER": "effective breastfeeding"}],
        category="CONDITION",
        attributes={"code": "69840006"},
    ),
    TargetRule(
        literal="Normal breast feeding (finding)",
        pattern=[{"LOWER": "normal breast feeding (finding)"}],
        category="CONDITION",
        attributes={"code": "69840006"},
    ),
    TargetRule(
        literal="Performs breastfeeding",
        pattern=[{"LOWER": "performs breastfeeding"}],
        category="CONDITION",
        attributes={"code": "69840006"},
    ),
    TargetRule(
        literal="Normal breastfeeding",
        pattern=[{"LOWER": "normal breastfeeding"}],
        category="CONDITION",
        attributes={"code": "69840006"},
    ),
    TargetRule(
        literal="Normal breastfeeding (finding)",
        pattern=[{"LOWER": "normal breastfeeding (finding)"}],
        category="CONDITION",
        attributes={"code": "69840006"},
    ),
    ### children of 77386006
    TargetRule(
        literal="Number of pregnancies, currently pregnant",
        pattern=[{"LOWER": "number of pregnancies, currently pregnant"}],
        category="PREGNANCY",
        attributes={"code": "127363001"},
    ),
    TargetRule(
        literal="Primigravida",
        pattern=[{"LOWER": "primigravida"}],
        category="PREGNANCY",
        attributes={"code": "127364007"},
    ),
    TargetRule(
        literal="Primiparity",
        pattern=[{"LOWER": "primiparity"}],
        category="PREGNANCY",
        attributes={"code": "3882004"},
    ),
    TargetRule(
        literal="Primipara",
        pattern=[{"LOWER": "primipara"}],
        category="PREGNANCY",
        attributes={"code": "3882004"},
    ),
    TargetRule(
        literal="Extra-amniotic pregnancy",
        pattern=[{"LOWER": "extra-amniotic pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "9279009"},
    ),
    TargetRule(
        literal="Abnormal pregnancy",
        pattern=[{"LOWER": "abnormal pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "11082009"},
    ),
    TargetRule(
        literal="Abnormal pregnancy, NOS",
        pattern=[{"LOWER": "abnormal pregnancy, nos"}],
        category="PREGNANCY",
        attributes={"code": "11082009"},
    ),
    TargetRule(
        literal="Precocious pregnancy",
        pattern=[{"LOWER": "precocious pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "14418008"},
    ),
    TargetRule(
        literal="Multiple gestation",
        pattern=[{"LOWER": "multiple gestation"}],
        category="PREGNANCY",
        attributes={"code": "16356006"},
    ),
    TargetRule(
        literal="Multiple gestation, NOS",
        pattern=[{"LOWER": "multiple gestation, nos"}],
        category="PREGNANCY",
        attributes={"code": "16356006"},
    ),
    TargetRule(
        literal="Multiple pregnancy, NOS",
        pattern=[{"LOWER": "multiple pregnancy, nos"}],
        category="PREGNANCY",
        attributes={"code": "16356006"},
    ),
    TargetRule(
        literal="Multiple pregnancy",
        pattern=[{"LOWER": "multiple pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "16356006"},
    ),
    TargetRule(
        literal="Prenatal examination and care of mother",
        pattern=[{"LOWER": "prenatal examination and care of mother"}],
        category="PREGNANCY",
        attributes={"code": "18114009"},
    ),
    TargetRule(
        literal="Antepartum care of mother",
        pattern=[{"LOWER": "antepartum care of mother"}],
        category="PREGNANCY",
        attributes={"code": "18114009"},
    ),
    TargetRule(
        literal="Multiparity",
        pattern=[{"LOWER": "multiparity"}],
        category="PREGNANCY",
        attributes={"code": "28079008"},
    ),
    TargetRule(
        literal="Antepartum state of mother",
        pattern=[{"LOWER": "antepartum state of mother"}],
        category="PREGNANCY",
        attributes={"code": "34784006"},
    ),
    TargetRule(
        literal="Antepartum state of mother, NOS",
        pattern=[{"LOWER": "antepartum state of mother, nos"}],
        category="PREGNANCY",
        attributes={"code": "34784006"},
    ),
    TargetRule(
        literal="Third trimester pregnancy",
        pattern=[{"LOWER": "third trimester pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "41587001"},
    ),
    TargetRule(
        literal="Last trimester of pregnancy",
        pattern=[{"LOWER": "last trimester of pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "41587001"},
    ),
    TargetRule(
        literal="Pre-admission observation, undelivered mother",
        pattern=[{"LOWER": "pre-admission observation, undelivered mother"}],
        category="PREGNANCY",
        attributes={"code": "42102002"},
    ),
    TargetRule(
        literal="Extrachorial pregnancy",
        pattern=[{"LOWER": "extrachorial pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "45307008"},
    ),
    TargetRule(
        literal="High risk pregnancy",
        pattern=[{"LOWER": "high risk pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "47200007"},
    ),
    TargetRule(
        literal="First trimester pregnancy",
        pattern=[{"LOWER": "first trimester pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "57630001"},
    ),
    TargetRule(
        literal="Unwanted pregnancy",
        pattern=[{"LOWER": "unwanted pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "58532003"},
    ),
    TargetRule(
        literal="Second trimester pregnancy",
        pattern=[{"LOWER": "second trimester pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "59466002"},
    ),
    TargetRule(
        literal="Intrauterine pregnancy",
        pattern=[{"LOWER": "intrauterine pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "65727000"},
    ),
    TargetRule(
        literal="Normal pregnancy",
        pattern=[{"LOWER": "normal pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "72892002"},
    ),
    TargetRule(
        literal="Unintended pregnancy",
        pattern=[{"LOWER": "unintended pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "83074005"},
    ),
    TargetRule(
        literal="Term pregnancy",
        pattern=[{"LOWER": "term pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "87527008"},
    ),
    TargetRule(
        literal="Megaloblastic anemia due to pregnancy",
        pattern=[{"LOWER": "megaloblastic anemia due to pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "91217009"},
    ),
    TargetRule(
        literal="Unconfirmed pregnancy",
        pattern=[{"LOWER": "unconfirmed pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "102874004"},
    ),
    TargetRule(
        literal="Surrogate pregnancy",
        pattern=[{"LOWER": "surrogate pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "102875003"},
    ),
    TargetRule(
        literal="Multiple previous pregnancies",
        pattern=[{"LOWER": "multiple previous pregnancies"}],
        category="PREGNANCY",
        attributes={"code": "102876002"},
    ),
    TargetRule(
        literal="Multiple previous pregnancies, NOS",
        pattern=[{"LOWER": "multiple previous pregnancies, nos"}],
        category="PREGNANCY",
        attributes={"code": "102876002"},
    ),
    TargetRule(
        literal="Multigravida",
        pattern=[{"LOWER": "multigravida"}],
        category="PREGNANCY",
        attributes={"code": "102876002"},
    ),
    TargetRule(
        literal="Nulliparity",
        pattern=[{"LOWER": "nulliparity"}],
        category="PREGNANCY",
        attributes={"code": "102877006"},
    ),
    TargetRule(
        literal="Nullipara",
        pattern=[{"LOWER": "nullipara"}],
        category="PREGNANCY",
        attributes={"code": "102877006"},
    ),
    TargetRule(
        literal="First pregnancy",
        pattern=[{"LOWER": "first pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "127364007"},
    ),
    TargetRule(
        literal="Routine antenatal care",
        pattern=[{"LOWER": "routine antenatal care"}],
        category="PREGNANCY",
        attributes={"code": "134435003"},
    ),
    TargetRule(
        literal="Possible pregnancy",
        pattern=[{"LOWER": "possible pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "146799005"},
    ),
    TargetRule(
        literal="Wife pregnant",
        pattern=[{"LOWER": "wife pregnant"}],
        category="PREGNANCY",
        attributes={"code": "160884000"},
    ),
    TargetRule(
        literal="H/O: stillbirth",
        pattern=[{"LOWER": "h/o: stillbirth"}],
        category="PREGNANCY",
        attributes={"code": "161743003"},
    ),
    TargetRule(
        literal="H/O: miscarriage",
        pattern=[{"LOWER": "h/o: miscarriage"}],
        category="PREGNANCY",
        attributes={"code": "161744009"},
    ),
    TargetRule(
        literal="No history of miscarriage",
        pattern=[{"LOWER": "no history of miscarriage"}],
        category="PREGNANCY",
        attributes={"code": "161745005"},
    ),
    TargetRule(
        literal="H/O: 1 miscarriage",
        pattern=[{"LOWER": "h/o: 1 miscarriage"}],
        category="PREGNANCY",
        attributes={"code": "161747002"},
    ),
    TargetRule(
        literal="H/O: 2 miscarriages",
        pattern=[{"LOWER": "h/o: 2 miscarriages"}],
        category="PREGNANCY",
        attributes={"code": "161748007"},
    ),
    TargetRule(
        literal="H/O: 3 miscarriages",
        pattern=[{"LOWER": "h/o: 3 miscarriages"}],
        category="PREGNANCY",
        attributes={"code": "161749004"},
    ),
    TargetRule(
        literal="H/O: 4 miscarriages",
        pattern=[{"LOWER": "h/o: 4 miscarriages"}],
        category="PREGNANCY",
        attributes={"code": "161750004"},
    ),
    TargetRule(
        literal="H/O: 5 miscarriages",
        pattern=[{"LOWER": "h/o: 5 miscarriages"}],
        category="PREGNANCY",
        attributes={"code": "161751000"},
    ),
    TargetRule(
        literal="H/O: 6 miscarriages",
        pattern=[{"LOWER": "h/o: 6 miscarriages"}],
        category="PREGNANCY",
        attributes={"code": "161752007"},
    ),
    TargetRule(
        literal="H/O: miscarriage NOS",
        pattern=[{"LOWER": "h/o: miscarriage nos"}],
        category="PREGNANCY",
        attributes={"code": "161753002"},
    ),
    TargetRule(
        literal="No history of abortion",
        pattern=[{"LOWER": "no history of abortion"}],
        category="PREGNANCY",
        attributes={"code": "161755009"},
    ),
    TargetRule(
        literal="H/O: 1 abortion",
        pattern=[{"LOWER": "h/o: 1 abortion"}],
        category="PREGNANCY",
        attributes={"code": "161756005"},
    ),
    TargetRule(
        literal="H/O: 2 abortions",
        pattern=[{"LOWER": "h/o: 2 abortions"}],
        category="PREGNANCY",
        attributes={"code": "161757001"},
    ),
    TargetRule(
        literal="H/O: 3 abortions",
        pattern=[{"LOWER": "h/o: 3 abortions"}],
        category="PREGNANCY",
        attributes={"code": "161758006"},
    ),
    TargetRule(
        literal="H/O: 4 abortions",
        pattern=[{"LOWER": "h/o: 4 abortions"}],
        category="PREGNANCY",
        attributes={"code": "161759003"},
    ),
    TargetRule(
        literal="H/O: 5 abortions",
        pattern=[{"LOWER": "h/o: 5 abortions"}],
        category="PREGNANCY",
        attributes={"code": "161760008"},
    ),
    TargetRule(
        literal="H/O: 6 abortions",
        pattern=[{"LOWER": "h/o: 6 abortions"}],
        category="PREGNANCY",
        attributes={"code": "161761007"},
    ),
    TargetRule(
        literal="H/O: abortion NOS",
        pattern=[{"LOWER": "h/o: abortion nos"}],
        category="PREGNANCY",
        attributes={"code": "161762000"},
    ),
    TargetRule(
        literal="H/O: ectopic pregnancy",
        pattern=[{"LOWER": "h/o: ectopic pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "161763005"},
    ),
    TargetRule(
        literal="H/O: premature delivery",
        pattern=[{"LOWER": "h/o: premature delivery"}],
        category="PREGNANCY",
        attributes={"code": "161765003"},
    ),
    TargetRule(
        literal="Past pregnancy outcome NOS",
        pattern=[{"LOWER": "past pregnancy outcome nos"}],
        category="PREGNANCY",
        attributes={"code": "161766002"},
    ),
    TargetRule(
        literal="H/O: obstetric problem",
        pattern=[{"LOWER": "h/o: obstetric problem"}],
        category="PREGNANCY",
        attributes={"code": "161803004"},
    ),
    TargetRule(
        literal="H/O: antepartum hemorrhage",
        pattern=[{"LOWER": "h/o: antepartum hemorrhage"}],
        category="PREGNANCY",
        attributes={"code": "161804005"},
    ),
    TargetRule(
        literal="H/O: antepartum haemorrhage",
        pattern=[{"LOWER": "h/o: antepartum haemorrhage"}],
        category="PREGNANCY",
        attributes={"code": "161804005"},
    ),
    TargetRule(
        literal="H/O: caesarean section",
        pattern=[{"LOWER": "h/o: caesarean section"}],
        category="PREGNANCY",
        attributes={"code": "161805006"},
    ),
    TargetRule(
        literal="H/O: cesarean section",
        pattern=[{"LOWER": "h/o: cesarean section"}],
        category="PREGNANCY",
        attributes={"code": "161805006"},
    ),
    TargetRule(
        literal="H/O: eclampsia",
        pattern=[{"LOWER": "h/o: eclampsia"}],
        category="PREGNANCY",
        attributes={"code": "161806007"},
    ),
    TargetRule(
        literal="H/O: severe pre-eclampsia",
        pattern=[{"LOWER": "h/o: severe pre-eclampsia"}],
        category="PREGNANCY",
        attributes={"code": "161807003"},
    ),
    TargetRule(
        literal="H/O:manual removal of placenta",
        pattern=[{"LOWER": "h/o:manual removal of placenta"}],
        category="PREGNANCY",
        attributes={"code": "161808008"},
    ),
    TargetRule(
        literal="H/O: postpartum hemorrhage",
        pattern=[{"LOWER": "h/o: postpartum hemorrhage"}],
        category="PREGNANCY",
        attributes={"code": "161809000"},
    ),
    TargetRule(
        literal="H/O: postpartum haemorrhage",
        pattern=[{"LOWER": "h/o: postpartum haemorrhage"}],
        category="PREGNANCY",
        attributes={"code": "161809000"},
    ),
    TargetRule(
        literal="H/O: long labour",
        pattern=[{"LOWER": "h/o: long labour"}],
        category="PREGNANCY",
        attributes={"code": "161810005"},
    ),
    TargetRule(
        literal="H/O: prolonged labour",
        pattern=[{"LOWER": "h/o: prolonged labour"}],
        category="PREGNANCY",
        attributes={"code": "161810005"},
    ),
    TargetRule(
        literal="H/O: long labor",
        pattern=[{"LOWER": "h/o: long labor"}],
        category="PREGNANCY",
        attributes={"code": "161810005"},
    ),
    TargetRule(
        literal="H/O: prolonged labor",
        pattern=[{"LOWER": "h/o: prolonged labor"}],
        category="PREGNANCY",
        attributes={"code": "161810005"},
    ),
    TargetRule(
        literal="H/O: perinatal fetal loss",
        pattern=[{"LOWER": "h/o: perinatal fetal loss"}],
        category="PREGNANCY",
        attributes={"code": "161811009"},
    ),
    TargetRule(
        literal="H/O: perinatal death",
        pattern=[{"LOWER": "h/o: perinatal death"}],
        category="PREGNANCY",
        attributes={"code": "161811009"},
    ),
    TargetRule(
        literal="H/O: previous forceps delivery",
        pattern=[{"LOWER": "h/o: previous forceps delivery"}],
        category="PREGNANCY",
        attributes={"code": "161813007"},
    ),
    TargetRule(
        literal="H/O: obstetric problem NOS",
        pattern=[{"LOWER": "h/o: obstetric problem nos"}],
        category="PREGNANCY",
        attributes={"code": "161814001"},
    ),
    TargetRule(
        literal="Obstetric examination",
        pattern=[{"LOWER": "obstetric examination"}],
        category="PREGNANCY",
        attributes={"code": "163497009"},
    ),
    TargetRule(
        literal="Nulliparous",
        pattern=[{"LOWER": "nulliparous"}],
        category="PREGNANCY",
        attributes={"code": "102877006"},
    ),
    TargetRule(
        literal="Pregnant - urine test confirms",
        pattern=[{"LOWER": "pregnant - urine test confirms"}],
        category="PREGNANCY",
        attributes={"code": "169560008"},
    ),
    TargetRule(
        literal="Pregnant - blood test confirms",
        pattern=[{"LOWER": "pregnant - blood test confirms"}],
        category="PREGNANCY",
        attributes={"code": "169561007"},
    ),
    TargetRule(
        literal="Pregnant - V.E. confirms",
        pattern=[{"LOWER": "pregnant - v.e. confirms"}],
        category="PREGNANCY",
        attributes={"code": "169562000"},
    ),
    TargetRule(
        literal="Pregnant - on history",
        pattern=[{"LOWER": "pregnant - on history"}],
        category="PREGNANCY",
        attributes={"code": "169563005"},
    ),
    TargetRule(
        literal="Pregnant - on abdom. palpation",
        pattern=[{"LOWER": "pregnant - on abdom. palpation"}],
        category="PREGNANCY",
        attributes={"code": "169564004"},
    ),
    TargetRule(
        literal="Patient pregnant NOS",
        pattern=[{"LOWER": "patient pregnant nos"}],
        category="PREGNANCY",
        attributes={"code": "169571009"},
    ),
    TargetRule(
        literal="Antenatal booking examination",
        pattern=[{"LOWER": "antenatal booking examination"}],
        category="PREGNANCY",
        attributes={"code": "169711001"},
    ),
    TargetRule(
        literal="Antenatal 12 weeks examination",
        pattern=[{"LOWER": "antenatal 12 weeks examination"}],
        category="PREGNANCY",
        attributes={"code": "169712008"},
    ),
    TargetRule(
        literal="Antenatal 16 week examination",
        pattern=[{"LOWER": "antenatal 16 week examination"}],
        category="PREGNANCY",
        attributes={"code": "169713003"},
    ),
    TargetRule(
        literal="A/N 16 week examination",
        pattern=[{"LOWER": "a/n 16 week examination"}],
        category="PREGNANCY",
        attributes={"code": "169713003"},
    ),
    TargetRule(
        literal="Antenatal 20 week examination",
        pattern=[{"LOWER": "antenatal 20 week examination"}],
        category="PREGNANCY",
        attributes={"code": "169714009"},
    ),
    TargetRule(
        literal="Antenatal 24 week examination",
        pattern=[{"LOWER": "antenatal 24 week examination"}],
        category="PREGNANCY",
        attributes={"code": "169715005"},
    ),
    TargetRule(
        literal="Antenatal 28 week examination",
        pattern=[{"LOWER": "antenatal 28 week examination"}],
        category="PREGNANCY",
        attributes={"code": "169716006"},
    ),
    TargetRule(
        literal="Antenatal 30 week examination",
        pattern=[{"LOWER": "antenatal 30 week examination"}],
        category="PREGNANCY",
        attributes={"code": "169717002"},
    ),
    TargetRule(
        literal="Antenatal 32 week examination",
        pattern=[{"LOWER": "antenatal 32 week examination"}],
        category="PREGNANCY",
        attributes={"code": "169718007"},
    ),
    TargetRule(
        literal="Antenatal 34 week examination",
        pattern=[{"LOWER": "antenatal 34 week examination"}],
        category="PREGNANCY",
        attributes={"code": "169719004"},
    ),
    TargetRule(
        literal="Antenatal 35 week examination",
        pattern=[{"LOWER": "antenatal 35 week examination"}],
        category="PREGNANCY",
        attributes={"code": "169720005"},
    ),
    TargetRule(
        literal="Antenatal 36 week examination",
        pattern=[{"LOWER": "antenatal 36 week examination"}],
        category="PREGNANCY",
        attributes={"code": "169721009"},
    ),
    TargetRule(
        literal="Antenatal 37 week examination",
        pattern=[{"LOWER": "antenatal 37 week examination"}],
        category="PREGNANCY",
        attributes={"code": "169722002"},
    ),
    TargetRule(
        literal="Antenatal 38 week examination",
        pattern=[{"LOWER": "antenatal 38 week examination"}],
        category="PREGNANCY",
        attributes={"code": "169723007"},
    ),
    TargetRule(
        literal="Antenatal 39 week examination",
        pattern=[{"LOWER": "antenatal 39 week examination"}],
        category="PREGNANCY",
        attributes={"code": "169724001"},
    ),
    TargetRule(
        literal="Antenatal 40 week examination",
        pattern=[{"LOWER": "antenatal 40 week examination"}],
        category="PREGNANCY",
        attributes={"code": "169725000"},
    ),
    TargetRule(
        literal="Antenatal 41 week examination",
        pattern=[{"LOWER": "antenatal 41 week examination"}],
        category="PREGNANCY",
        attributes={"code": "169726004"},
    ),
    TargetRule(
        literal="Antenatal 42 week examination",
        pattern=[{"LOWER": "antenatal 42 week examination"}],
        category="PREGNANCY",
        attributes={"code": "169727008"},
    ),
    TargetRule(
        literal="Mother currently breast-feeding",
        pattern=[{"LOWER": "mother currently breast-feeding"}],
        category="PREGNANCY",
        attributes={"code": "169750002"},
    ),
    TargetRule(
        literal="Postnatal visit",
        pattern=[{"LOWER": "postnatal visit"}],
        category="PREGNANCY",
        attributes={"code": "169762003"},
    ),
    TargetRule(
        literal="Postnatal - first day visit",
        pattern=[{"LOWER": "postnatal - first day visit"}],
        category="PREGNANCY",
        attributes={"code": "169763008"},
    ),
    TargetRule(
        literal="Postnatal - second day visit",
        pattern=[{"LOWER": "postnatal - second day visit"}],
        category="PREGNANCY",
        attributes={"code": "169764002"},
    ),
    TargetRule(
        literal="Postnatal - third day visit",
        pattern=[{"LOWER": "postnatal - third day visit"}],
        category="PREGNANCY",
        attributes={"code": "169765001"},
    ),
    TargetRule(
        literal="Postnatal - fourth day visit",
        pattern=[{"LOWER": "postnatal - fourth day visit"}],
        category="PREGNANCY",
        attributes={"code": "169766000"},
    ),
    TargetRule(
        literal="Postnatal - fifth day visit",
        pattern=[{"LOWER": "postnatal - fifth day visit"}],
        category="PREGNANCY",
        attributes={"code": "169767009"},
    ),
    TargetRule(
        literal="Postnatal - sixth day visit",
        pattern=[{"LOWER": "postnatal - sixth day visit"}],
        category="PREGNANCY",
        attributes={"code": "169768004"},
    ),
    TargetRule(
        literal="Postnatal - seventh day visit",
        pattern=[{"LOWER": "postnatal - seventh day visit"}],
        category="PREGNANCY",
        attributes={"code": "169769007"},
    ),
    TargetRule(
        literal="Postnatal - eighth day visit",
        pattern=[{"LOWER": "postnatal - eighth day visit"}],
        category="PREGNANCY",
        attributes={"code": "169770008"},
    ),
    TargetRule(
        literal="Postnatal - ninth day visit",
        pattern=[{"LOWER": "postnatal - ninth day visit"}],
        category="PREGNANCY",
        attributes={"code": "169771007"},
    ),
    TargetRule(
        literal="Postnatal - tenth day visit",
        pattern=[{"LOWER": "postnatal - tenth day visit"}],
        category="PREGNANCY",
        attributes={"code": "169772000"},
    ),
    TargetRule(
        literal="Infections of urethra in pregnancy",
        pattern=[{"LOWER": "infections of urethra in pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "199206009"},
    ),
    TargetRule(
        literal="Albuminuria in pregnancy without hypertension",
        pattern=[{"LOWER": "albuminuria in pregnancy without hypertension"}],
        category="PREGNANCY",
        attributes={"code": "237232007"},
    ),
    TargetRule(
        literal="Low risk pregnancy",
        pattern=[{"LOWER": "low risk pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "237239003"},
    ),
    TargetRule(
        literal="H/O: abortion",
        pattern=[{"LOWER": "h/o: abortion"}],
        category="PREGNANCY",
        attributes={"code": "267014009"},
    ),
    TargetRule(
        literal="H/O: full term delivery",
        pattern=[{"LOWER": "h/o: full term delivery"}],
        category="PREGNANCY",
        attributes={"code": "267015005"},
    ),
    TargetRule(
        literal="H/O: myomectomy/hysterotomy",
        pattern=[{"LOWER": "h/o: myomectomy/hysterotomy"}],
        category="PREGNANCY",
        attributes={"code": "267021009"},
    ),
    TargetRule(
        literal="H/O: pregnancy",
        pattern=[{"LOWER": "h/o: pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "271903000"},
    ),
    TargetRule(
        literal="H/O fetal loss",
        pattern=[{"LOWER": "h/o fetal loss"}],
        category="PREGNANCY",
        attributes={"code": "271904006"},
    ),
    TargetRule(
        literal="History of past delivery",
        pattern=[{"LOWER": "history of past delivery"}],
        category="PREGNANCY",
        attributes={"code": "272058002"},
    ),
    TargetRule(
        literal="H/O: termination",
        pattern=[{"LOWER": "h/o: termination"}],
        category="PREGNANCY",
        attributes={"code": "275567001"},
    ),
    TargetRule(
        literal="H/O: normal delivery",
        pattern=[{"LOWER": "h/o: normal delivery"}],
        category="PREGNANCY",
        attributes={"code": "275568006"},
    ),
    TargetRule(
        literal="H/O: delivery no details",
        pattern=[{"LOWER": "h/o: delivery no details"}],
        category="PREGNANCY",
        attributes={"code": "275569003"},
    ),
    TargetRule(
        literal="H/O: hysterotomy",
        pattern=[{"LOWER": "h/o: hysterotomy"}],
        category="PREGNANCY",
        attributes={"code": "275573000"},
    ),
    TargetRule(
        literal="H/O: myomectomy",
        pattern=[{"LOWER": "h/o: myomectomy"}],
        category="PREGNANCY",
        attributes={"code": "275574006"},
    ),
    TargetRule(
        literal="Pregnancy-related examination",
        pattern=[{"LOWER": "pregnancy-related examination"}],
        category="PREGNANCY",
        attributes={"code": "312891008"},
    ),
    TargetRule(
        literal="Antenatal examination",
        pattern=[{"LOWER": "antenatal examination"}],
        category="PREGNANCY",
        attributes={"code": "18114009"},
    ),
    TargetRule(
        literal="Multiparous",
        pattern=[{"LOWER": "multiparous"}],
        category="PREGNANCY",
        attributes={"code": "28079008"},
    ),
    TargetRule(
        literal="Primiparous",
        pattern=[{"LOWER": "primiparous"}],
        category="PREGNANCY",
        attributes={"code": "3882004"},
    ),
    TargetRule(
        literal="Unplanned pregnancy",
        pattern=[{"LOWER": "unplanned pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "83074005"},
    ),
    TargetRule(
        literal="Megaloblastic anaemia due to pregnancy",
        pattern=[{"LOWER": "megaloblastic anaemia due to pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "91217009"},
    ),
    TargetRule(
        literal="Routine antenatal care (procedure)",
        pattern=[{"LOWER": "routine antenatal care (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "134435003"},
    ),
    TargetRule(
        literal="Wife pregnant (context-dependent category)",
        pattern=[{"LOWER": "wife pregnant (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "160884000"},
    ),
    TargetRule(
        literal="History of - stillbirth (context-dependent category)",
        pattern=[{"LOWER": "history of - stillbirth (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161743003"},
    ),
    TargetRule(
        literal="History of - miscarriage (context-dependent category)",
        pattern=[{"LOWER": "history of - miscarriage (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161744009"},
    ),
    TargetRule(
        literal="No history of miscarriage (context-dependent category)",
        pattern=[{"LOWER": "no history of miscarriage (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161745005"},
    ),
    TargetRule(
        literal="History of - 1 miscarriage (context-dependent category)",
        pattern=[{"LOWER": "history of - 1 miscarriage (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161747002"},
    ),
    TargetRule(
        literal="History of - 2 miscarriages (context-dependent category)",
        pattern=[{"LOWER": "history of - 2 miscarriages (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161748007"},
    ),
    TargetRule(
        literal="History of - 3 miscarriages (context-dependent category)",
        pattern=[{"LOWER": "history of - 3 miscarriages (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161749004"},
    ),
    TargetRule(
        literal="History of - 4 miscarriages (context-dependent category)",
        pattern=[{"LOWER": "history of - 4 miscarriages (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161750004"},
    ),
    TargetRule(
        literal="History of - 5 miscarriages (context-dependent category)",
        pattern=[{"LOWER": "history of - 5 miscarriages (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161751000"},
    ),
    TargetRule(
        literal="History of - 6 miscarriages (context-dependent category)",
        pattern=[{"LOWER": "history of - 6 miscarriages (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161752007"},
    ),
    TargetRule(
        literal="History of - miscarriage NOS (context-dependent category)",
        pattern=[
            {"LOWER": "history of - miscarriage nos (context-dependent category)"}
        ],
        category="PREGNANCY",
        attributes={"code": "161753002"},
    ),
    TargetRule(
        literal="No history of abortion (context-dependent category)",
        pattern=[{"LOWER": "no history of abortion (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161755009"},
    ),
    TargetRule(
        literal="History of - 1 abortion (context-dependent category)",
        pattern=[{"LOWER": "history of - 1 abortion (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161756005"},
    ),
    TargetRule(
        literal="History of - 2 abortions (context-dependent category)",
        pattern=[{"LOWER": "history of - 2 abortions (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161757001"},
    ),
    TargetRule(
        literal="History of - 3 abortions (context-dependent category)",
        pattern=[{"LOWER": "history of - 3 abortions (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161758006"},
    ),
    TargetRule(
        literal="History of - 4 abortions (context-dependent category)",
        pattern=[{"LOWER": "history of - 4 abortions (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161759003"},
    ),
    TargetRule(
        literal="History of - 5 abortions (context-dependent category)",
        pattern=[{"LOWER": "history of - 5 abortions (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161760008"},
    ),
    TargetRule(
        literal="History of - 6 abortions (context-dependent category)",
        pattern=[{"LOWER": "history of - 6 abortions (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161761007"},
    ),
    TargetRule(
        literal="History of - abortion NOS (context-dependent category)",
        pattern=[{"LOWER": "history of - abortion nos (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161762000"},
    ),
    TargetRule(
        literal="History of - ectopic pregnancy (context-dependent category)",
        pattern=[
            {"LOWER": "history of - ectopic pregnancy (context-dependent category)"}
        ],
        category="PREGNANCY",
        attributes={"code": "161763005"},
    ),
    TargetRule(
        literal="History of - premature delivery (context-dependent category)",
        pattern=[
            {"LOWER": "history of - premature delivery (context-dependent category)"}
        ],
        category="PREGNANCY",
        attributes={"code": "161765003"},
    ),
    TargetRule(
        literal="Past pregnancy outcome NOS (context-dependent category)",
        pattern=[{"LOWER": "past pregnancy outcome nos (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161766002"},
    ),
    TargetRule(
        literal="History of - obstetric problem (context-dependent category)",
        pattern=[
            {"LOWER": "history of - obstetric problem (context-dependent category)"}
        ],
        category="PREGNANCY",
        attributes={"code": "161803004"},
    ),
    TargetRule(
        literal="History of - antepartum hemorrhage (context-dependent category)",
        pattern=[
            {"LOWER": "history of - antepartum hemorrhage (context-dependent category)"}
        ],
        category="PREGNANCY",
        attributes={"code": "161804005"},
    ),
    TargetRule(
        literal="History of - cesarean section (context-dependent category)",
        pattern=[
            {"LOWER": "history of - cesarean section (context-dependent category)"}
        ],
        category="PREGNANCY",
        attributes={"code": "161805006"},
    ),
    TargetRule(
        literal="History of - eclampsia (context-dependent category)",
        pattern=[{"LOWER": "history of - eclampsia (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "161806007"},
    ),
    TargetRule(
        literal="History of - severe pre-eclampsia (context-dependent category)",
        pattern=[
            {"LOWER": "history of - severe pre-eclampsia (context-dependent category)"}
        ],
        category="PREGNANCY",
        attributes={"code": "161807003"},
    ),
    TargetRule(
        literal="History of - manual removal of placenta (context-dependent category)",
        pattern=[
            {
                "LOWER": "history of - manual removal of placenta (context-dependent category)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "161808008"},
    ),
    TargetRule(
        literal="History of - postpartum hemorrhage (context-dependent category)",
        pattern=[
            {"LOWER": "history of - postpartum hemorrhage (context-dependent category)"}
        ],
        category="PREGNANCY",
        attributes={"code": "161809000"},
    ),
    TargetRule(
        literal="History of - prolonged labor (context-dependent category)",
        pattern=[
            {"LOWER": "history of - prolonged labor (context-dependent category)"}
        ],
        category="PREGNANCY",
        attributes={"code": "161810005"},
    ),
    TargetRule(
        literal="History of - perinatal fetal loss (context-dependent category)",
        pattern=[
            {"LOWER": "history of - perinatal fetal loss (context-dependent category)"}
        ],
        category="PREGNANCY",
        attributes={"code": "161811009"},
    ),
    TargetRule(
        literal="History of - previous forceps delivery (context-dependent category)",
        pattern=[
            {
                "LOWER": "history of - previous forceps delivery (context-dependent category)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "161813007"},
    ),
    TargetRule(
        literal="History of - obstetric problem NOS (context-dependent category)",
        pattern=[
            {"LOWER": "history of - obstetric problem nos (context-dependent category)"}
        ],
        category="PREGNANCY",
        attributes={"code": "161814001"},
    ),
    TargetRule(
        literal="Obstetric examination (procedure)",
        pattern=[{"LOWER": "obstetric examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "163497009"},
    ),
    TargetRule(
        literal="Possible pregnancy (finding)",
        pattern=[{"LOWER": "possible pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "102874004"},
    ),
    TargetRule(
        literal="Surrogate pregnancy (finding)",
        pattern=[{"LOWER": "surrogate pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "102875003"},
    ),
    TargetRule(
        literal="Multigravida (finding)",
        pattern=[{"LOWER": "multigravida (finding)"}],
        category="PREGNANCY",
        attributes={"code": "102876002"},
    ),
    TargetRule(
        literal="Nulliparous (finding)",
        pattern=[{"LOWER": "nulliparous (finding)"}],
        category="PREGNANCY",
        attributes={"code": "102877006"},
    ),
    TargetRule(
        literal="Pregnant - urine test confirms (finding)",
        pattern=[{"LOWER": "pregnant - urine test confirms (finding)"}],
        category="PREGNANCY",
        attributes={"code": "169560008"},
    ),
    TargetRule(
        literal="Pregnant - blood test confirms (finding)",
        pattern=[{"LOWER": "pregnant - blood test confirms (finding)"}],
        category="PREGNANCY",
        attributes={"code": "169561007"},
    ),
    TargetRule(
        literal="Pregnant - vaginal examination confirms (finding)",
        pattern=[{"LOWER": "pregnant - vaginal examination confirms (finding)"}],
        category="PREGNANCY",
        attributes={"code": "169562000"},
    ),
    TargetRule(
        literal="Pregnant - on history (finding)",
        pattern=[{"LOWER": "pregnant - on history (finding)"}],
        category="PREGNANCY",
        attributes={"code": "169563005"},
    ),
    TargetRule(
        literal="Pregnant - on abdominal palpation (finding)",
        pattern=[{"LOWER": "pregnant - on abdominal palpation (finding)"}],
        category="PREGNANCY",
        attributes={"code": "169564004"},
    ),
    TargetRule(
        literal="Patient pregnant NOS (finding)",
        pattern=[{"LOWER": "patient pregnant nos (finding)"}],
        category="PREGNANCY",
        attributes={"code": "169571009"},
    ),
    TargetRule(
        literal="Antenatal booking examination (procedure)",
        pattern=[{"LOWER": "antenatal booking examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169711001"},
    ),
    TargetRule(
        literal="Antenatal 12 weeks examination (procedure)",
        pattern=[{"LOWER": "antenatal 12 weeks examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169712008"},
    ),
    TargetRule(
        literal="Antenatal 16 week examination (procedure)",
        pattern=[{"LOWER": "antenatal 16 week examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169713003"},
    ),
    TargetRule(
        literal="Antenatal 20 week examination (procedure)",
        pattern=[{"LOWER": "antenatal 20 week examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169714009"},
    ),
    TargetRule(
        literal="Antenatal 24 week examination (procedure)",
        pattern=[{"LOWER": "antenatal 24 week examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169715005"},
    ),
    TargetRule(
        literal="Antenatal 28 week examination (procedure)",
        pattern=[{"LOWER": "antenatal 28 week examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169716006"},
    ),
    TargetRule(
        literal="Antenatal 30 week examination (procedure)",
        pattern=[{"LOWER": "antenatal 30 week examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169717002"},
    ),
    TargetRule(
        literal="Antenatal 32 week examination (procedure)",
        pattern=[{"LOWER": "antenatal 32 week examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169718007"},
    ),
    TargetRule(
        literal="Antenatal 34 week examination (procedure)",
        pattern=[{"LOWER": "antenatal 34 week examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169719004"},
    ),
    TargetRule(
        literal="Antenatal 35 week examination (procedure)",
        pattern=[{"LOWER": "antenatal 35 week examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169720005"},
    ),
    TargetRule(
        literal="Antenatal 36 week examination (procedure)",
        pattern=[{"LOWER": "antenatal 36 week examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169721009"},
    ),
    TargetRule(
        literal="Antenatal 37 week examination (procedure)",
        pattern=[{"LOWER": "antenatal 37 week examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169722002"},
    ),
    TargetRule(
        literal="Antenatal 38 week examination (procedure)",
        pattern=[{"LOWER": "antenatal 38 week examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169723007"},
    ),
    TargetRule(
        literal="Antenatal 39 week examination (procedure)",
        pattern=[{"LOWER": "antenatal 39 week examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169724001"},
    ),
    TargetRule(
        literal="Antenatal 40 week examination (procedure)",
        pattern=[{"LOWER": "antenatal 40 week examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169725000"},
    ),
    TargetRule(
        literal="Antenatal 41 week examination (procedure)",
        pattern=[{"LOWER": "antenatal 41 week examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169726004"},
    ),
    TargetRule(
        literal="Antenatal 42 week examination (procedure)",
        pattern=[{"LOWER": "antenatal 42 week examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169727008"},
    ),
    TargetRule(
        literal="Mother currently breast-feeding (finding)",
        pattern=[{"LOWER": "mother currently breast-feeding (finding)"}],
        category="PREGNANCY",
        attributes={"code": "169750002"},
    ),
    TargetRule(
        literal="Postnatal visit (procedure)",
        pattern=[{"LOWER": "postnatal visit (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169762003"},
    ),
    TargetRule(
        literal="Postnatal - first day visit (procedure)",
        pattern=[{"LOWER": "postnatal - first day visit (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169763008"},
    ),
    TargetRule(
        literal="Postnatal - second day visit (procedure)",
        pattern=[{"LOWER": "postnatal - second day visit (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169764002"},
    ),
    TargetRule(
        literal="Postnatal - third day visit (procedure)",
        pattern=[{"LOWER": "postnatal - third day visit (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169765001"},
    ),
    TargetRule(
        literal="Postnatal - fourth day visit (procedure)",
        pattern=[{"LOWER": "postnatal - fourth day visit (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169766000"},
    ),
    TargetRule(
        literal="Postnatal - fifth day visit (procedure)",
        pattern=[{"LOWER": "postnatal - fifth day visit (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169767009"},
    ),
    TargetRule(
        literal="Postnatal - sixth day visit (procedure)",
        pattern=[{"LOWER": "postnatal - sixth day visit (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169768004"},
    ),
    TargetRule(
        literal="Postnatal - seventh day visit (procedure)",
        pattern=[{"LOWER": "postnatal - seventh day visit (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169769007"},
    ),
    TargetRule(
        literal="Postnatal - eighth day visit (procedure)",
        pattern=[{"LOWER": "postnatal - eighth day visit (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169770008"},
    ),
    TargetRule(
        literal="Postnatal - ninth day visit (procedure)",
        pattern=[{"LOWER": "postnatal - ninth day visit (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169771007"},
    ),
    TargetRule(
        literal="Postnatal - tenth day visit (procedure)",
        pattern=[{"LOWER": "postnatal - tenth day visit (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "169772000"},
    ),
    TargetRule(
        literal="Infections of urethra in pregnancy (disorder)",
        pattern=[{"LOWER": "infections of urethra in pregnancy (disorder)"}],
        category="PREGNANCY",
        attributes={"code": "199206009"},
    ),
    TargetRule(
        literal="Abnormal pregnancy (finding)",
        pattern=[{"LOWER": "abnormal pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "11082009"},
    ),
    TargetRule(
        literal="Albuminuria in pregnancy without hypertension (finding)",
        pattern=[{"LOWER": "albuminuria in pregnancy without hypertension (finding)"}],
        category="PREGNANCY",
        attributes={"code": "237232007"},
    ),
    TargetRule(
        literal="Low risk pregnancy (finding)",
        pattern=[{"LOWER": "low risk pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "237239003"},
    ),
    TargetRule(
        literal="History of - abortion (context-dependent category)",
        pattern=[{"LOWER": "history of - abortion (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "267014009"},
    ),
    TargetRule(
        literal="History of - full term delivery (context-dependent category)",
        pattern=[
            {"LOWER": "history of - full term delivery (context-dependent category)"}
        ],
        category="PREGNANCY",
        attributes={"code": "267015005"},
    ),
    TargetRule(
        literal="History of - myomectomy/hysterotomy (context-dependent category)",
        pattern=[
            {
                "LOWER": "history of - myomectomy/hysterotomy (context-dependent category)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "267021009"},
    ),
    TargetRule(
        literal="History of - pregnancy (context-dependent category)",
        pattern=[{"LOWER": "history of - pregnancy (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "271903000"},
    ),
    TargetRule(
        literal="History of - fetal loss (context-dependent category)",
        pattern=[{"LOWER": "history of - fetal loss (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "271904006"},
    ),
    TargetRule(
        literal="History of past delivery (context-dependent category)",
        pattern=[{"LOWER": "history of past delivery (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "272058002"},
    ),
    TargetRule(
        literal="History of - termination (context-dependent category)",
        pattern=[{"LOWER": "history of - termination (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "275567001"},
    ),
    TargetRule(
        literal="History of - normal delivery (context-dependent category)",
        pattern=[
            {"LOWER": "history of - normal delivery (context-dependent category)"}
        ],
        category="PREGNANCY",
        attributes={"code": "275568006"},
    ),
    TargetRule(
        literal="History of - delivery no details (context-dependent category)",
        pattern=[
            {"LOWER": "history of - delivery no details (context-dependent category)"}
        ],
        category="PREGNANCY",
        attributes={"code": "275569003"},
    ),
    TargetRule(
        literal="History of - hysterotomy (context-dependent category)",
        pattern=[{"LOWER": "history of - hysterotomy (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "275573000"},
    ),
    TargetRule(
        literal="History of - myomectomy (context-dependent category)",
        pattern=[{"LOWER": "history of - myomectomy (context-dependent category)"}],
        category="PREGNANCY",
        attributes={"code": "275574006"},
    ),
    TargetRule(
        literal="Pregnancy-related examination (procedure)",
        pattern=[{"LOWER": "pregnancy-related examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "312891008"},
    ),
    TargetRule(
        literal="Number of pregnancies, currently pregnant (finding)",
        pattern=[{"LOWER": "number of pregnancies, currently pregnant (finding)"}],
        category="PREGNANCY",
        attributes={"code": "127363001"},
    ),
    TargetRule(
        literal="Primigravida (finding)",
        pattern=[{"LOWER": "primigravida (finding)"}],
        category="PREGNANCY",
        attributes={"code": "127364007"},
    ),
    TargetRule(
        literal="Precocious pregnancy (finding)",
        pattern=[{"LOWER": "precocious pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "14418008"},
    ),
    TargetRule(
        literal="Multiple pregnancy (disorder)",
        pattern=[{"LOWER": "multiple pregnancy (disorder)"}],
        category="PREGNANCY",
        attributes={"code": "16356006"},
    ),
    TargetRule(
        literal="Prenatal examination and care of mother (procedure)",
        pattern=[{"LOWER": "prenatal examination and care of mother (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "18114009"},
    ),
    TargetRule(
        literal="Multiparous (finding)",
        pattern=[{"LOWER": "multiparous (finding)"}],
        category="PREGNANCY",
        attributes={"code": "28079008"},
    ),
    TargetRule(
        literal="Antepartum state of mother (finding)",
        pattern=[{"LOWER": "antepartum state of mother (finding)"}],
        category="PREGNANCY",
        attributes={"code": "34784006"},
    ),
    TargetRule(
        literal="Primiparous (finding)",
        pattern=[{"LOWER": "primiparous (finding)"}],
        category="PREGNANCY",
        attributes={"code": "3882004"},
    ),
    TargetRule(
        literal="Third trimester pregnancy (finding)",
        pattern=[{"LOWER": "third trimester pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "41587001"},
    ),
    TargetRule(
        literal="Pre-admission observation, undelivered mother (procedure)",
        pattern=[
            {"LOWER": "pre-admission observation, undelivered mother (procedure)"}
        ],
        category="PREGNANCY",
        attributes={"code": "42102002"},
    ),
    TargetRule(
        literal="Extrachorial pregnancy (finding)",
        pattern=[{"LOWER": "extrachorial pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "45307008"},
    ),
    TargetRule(
        literal="High risk pregnancy (finding)",
        pattern=[{"LOWER": "high risk pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "47200007"},
    ),
    TargetRule(
        literal="First trimester pregnancy (finding)",
        pattern=[{"LOWER": "first trimester pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "57630001"},
    ),
    TargetRule(
        literal="Unwanted pregnancy (finding)",
        pattern=[{"LOWER": "unwanted pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "58532003"},
    ),
    TargetRule(
        literal="Second trimester pregnancy (finding)",
        pattern=[{"LOWER": "second trimester pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "59466002"},
    ),
    TargetRule(
        literal="Intrauterine pregnancy (finding)",
        pattern=[{"LOWER": "intrauterine pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "65727000"},
    ),
    TargetRule(
        literal="Normal pregnancy (finding)",
        pattern=[{"LOWER": "normal pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "72892002"},
    ),
    TargetRule(
        literal="Unplanned pregnancy (finding)",
        pattern=[{"LOWER": "unplanned pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "83074005"},
    ),
    TargetRule(
        literal="Term pregnancy (finding)",
        pattern=[{"LOWER": "term pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "87527008"},
    ),
    TargetRule(
        literal="Megaloblastic anemia due to pregnancy (disorder)",
        pattern=[{"LOWER": "megaloblastic anemia due to pregnancy (disorder)"}],
        category="PREGNANCY",
        attributes={"code": "91217009"},
    ),
    TargetRule(
        literal="Extra-amniotic pregnancy (finding)",
        pattern=[{"LOWER": "extra-amniotic pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "9279009"},
    ),
    TargetRule(
        literal="Patient ? pregnant",
        pattern=[{"LOWER": "patient ? pregnant"}],
        category="PREGNANCY",
        attributes={"code": "102874004"},
    ),
    TargetRule(
        literal="Think I am pregnant",
        pattern=[{"LOWER": "think i am pregnant"}],
        category="PREGNANCY",
        attributes={"code": "102874004"},
    ),
    TargetRule(
        literal="Think I am going to have a baby",
        pattern=[{"LOWER": "think i am going to have a baby"}],
        category="PREGNANCY",
        attributes={"code": "102874004"},
    ),
    TargetRule(
        literal="Multip",
        pattern=[{"LOWER": "multip"}],
        category="PREGNANCY",
        attributes={"code": "102876002"},
    ),
    TargetRule(
        literal="Primip",
        pattern=[{"LOWER": "primip"}],
        category="PREGNANCY",
        attributes={"code": "127364007"},
    ),
    TargetRule(
        literal="HRP - High risk pregnancy",
        pattern=[{"LOWER": "hrp - high risk pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "47200007"},
    ),
    TargetRule(
        literal="Accidental pregnancy",
        pattern=[{"LOWER": "accidental pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "83074005"},
    ),
    TargetRule(
        literal="Postnatal maternal examination (procedure)",
        pattern=[{"LOWER": "postnatal maternal examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "384634009"},
    ),
    TargetRule(
        literal="Full postnatal examination (procedure)",
        pattern=[{"LOWER": "full postnatal examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "384635005"},
    ),
    TargetRule(
        literal="Maternal postnatal 6 week examination (procedure)",
        pattern=[{"LOWER": "maternal postnatal 6 week examination (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "384636006"},
    ),
    TargetRule(
        literal="Childbirth preparation (regime/therapy)",
        pattern=[{"LOWER": "childbirth preparation (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "386235000"},
    ),
    TargetRule(
        literal="Postnatal visit (regime/therapy)",
        pattern=[{"LOWER": "postnatal visit (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "169762003"},
    ),
    TargetRule(
        literal="Postnatal - first day visit (regime/therapy)",
        pattern=[{"LOWER": "postnatal - first day visit (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "169763008"},
    ),
    TargetRule(
        literal="Postnatal - second day visit (regime/therapy)",
        pattern=[{"LOWER": "postnatal - second day visit (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "169764002"},
    ),
    TargetRule(
        literal="Postnatal - third day visit (regime/therapy)",
        pattern=[{"LOWER": "postnatal - third day visit (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "169765001"},
    ),
    TargetRule(
        literal="Postnatal - fourth day visit (regime/therapy)",
        pattern=[{"LOWER": "postnatal - fourth day visit (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "169766000"},
    ),
    TargetRule(
        literal="Postnatal - fifth day visit (regime/therapy)",
        pattern=[{"LOWER": "postnatal - fifth day visit (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "169767009"},
    ),
    TargetRule(
        literal="Postnatal - sixth day visit (regime/therapy)",
        pattern=[{"LOWER": "postnatal - sixth day visit (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "169768004"},
    ),
    TargetRule(
        literal="Postnatal - seventh day visit (regime/therapy)",
        pattern=[{"LOWER": "postnatal - seventh day visit (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "169769007"},
    ),
    TargetRule(
        literal="Postnatal - eighth day visit (regime/therapy)",
        pattern=[{"LOWER": "postnatal - eighth day visit (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "169770008"},
    ),
    TargetRule(
        literal="Postnatal - ninth day visit (regime/therapy)",
        pattern=[{"LOWER": "postnatal - ninth day visit (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "169771007"},
    ),
    TargetRule(
        literal="Postnatal - tenth day visit (regime/therapy)",
        pattern=[{"LOWER": "postnatal - tenth day visit (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "169772000"},
    ),
    TargetRule(
        literal="Routine antenatal care (regime/therapy)",
        pattern=[{"LOWER": "routine antenatal care (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "134435003"},
    ),
    TargetRule(
        literal="Postnatal maternal examination",
        pattern=[{"LOWER": "postnatal maternal examination"}],
        category="PREGNANCY",
        attributes={"code": "384634009"},
    ),
    TargetRule(
        literal="Full postnatal examination",
        pattern=[{"LOWER": "full postnatal examination"}],
        category="PREGNANCY",
        attributes={"code": "384635005"},
    ),
    TargetRule(
        literal="Maternal postnatal 6 week examination",
        pattern=[{"LOWER": "maternal postnatal 6 week examination"}],
        category="PREGNANCY",
        attributes={"code": "384636006"},
    ),
    TargetRule(
        literal="Childbirth preparation",
        pattern=[{"LOWER": "childbirth preparation"}],
        category="PREGNANCY",
        attributes={"code": "386235000"},
    ),
    TargetRule(
        literal="Pregnancy follow-up examination",
        pattern=[{"LOWER": "pregnancy follow-up examination"}],
        category="PREGNANCY",
        attributes={"code": "384634009"},
    ),
    TargetRule(
        literal="Postnatal appointment",
        pattern=[{"LOWER": "postnatal appointment"}],
        category="PREGNANCY",
        attributes={"code": "384634009"},
    ),
    TargetRule(
        literal="H/O: medical termination of pregnancy (context-dependent category)",
        pattern=[
            {
                "LOWER": "h/o: medical termination of pregnancy (context-dependent category)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "412758008"},
    ),
    TargetRule(
        literal="H/O: medical termination of pregnancy",
        pattern=[{"LOWER": "h/o: medical termination of pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "412758008"},
    ),
    TargetRule(
        literal="History of - fetal loss",
        pattern=[{"LOWER": "history of - fetal loss"}],
        category="PREGNANCY",
        attributes={"code": "267014009"},
    ),
    TargetRule(
        literal="History of - medical termination of pregnancy (context-dependent category)",
        pattern=[
            {
                "LOWER": "history of - medical termination of pregnancy (context-dependent category)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "412758008"},
    ),
    TargetRule(
        literal="Wife pregnant (situation)",
        pattern=[{"LOWER": "wife pregnant (situation)"}],
        category="PREGNANCY",
        attributes={"code": "160884000"},
    ),
    TargetRule(
        literal="History of - perinatal fetal loss (situation)",
        pattern=[{"LOWER": "history of - perinatal fetal loss (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161811009"},
    ),
    TargetRule(
        literal="History of - previous forceps delivery (situation)",
        pattern=[{"LOWER": "history of - previous forceps delivery (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161813007"},
    ),
    TargetRule(
        literal="History of - obstetric problem NOS (situation)",
        pattern=[{"LOWER": "history of - obstetric problem nos (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161814001"},
    ),
    TargetRule(
        literal="History of - obstetric problem (situation)",
        pattern=[{"LOWER": "history of - obstetric problem (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161803004"},
    ),
    TargetRule(
        literal="History of - antepartum hemorrhage (situation)",
        pattern=[{"LOWER": "history of - antepartum hemorrhage (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161804005"},
    ),
    TargetRule(
        literal="History of - cesarean section (situation)",
        pattern=[{"LOWER": "history of - cesarean section (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161805006"},
    ),
    TargetRule(
        literal="History of - eclampsia (situation)",
        pattern=[{"LOWER": "history of - eclampsia (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161806007"},
    ),
    TargetRule(
        literal="History of - severe pre-eclampsia (situation)",
        pattern=[{"LOWER": "history of - severe pre-eclampsia (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161807003"},
    ),
    TargetRule(
        literal="History of - manual removal of placenta (situation)",
        pattern=[{"LOWER": "history of - manual removal of placenta (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161808008"},
    ),
    TargetRule(
        literal="History of - postpartum hemorrhage (situation)",
        pattern=[{"LOWER": "history of - postpartum hemorrhage (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161809000"},
    ),
    TargetRule(
        literal="History of - prolonged labor (situation)",
        pattern=[{"LOWER": "history of - prolonged labor (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161810005"},
    ),
    TargetRule(
        literal="History of - stillbirth (situation)",
        pattern=[{"LOWER": "history of - stillbirth (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161743003"},
    ),
    TargetRule(
        literal="History of - miscarriage (situation)",
        pattern=[{"LOWER": "history of - miscarriage (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161744009"},
    ),
    TargetRule(
        literal="No history of miscarriage (situation)",
        pattern=[{"LOWER": "no history of miscarriage (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161745005"},
    ),
    TargetRule(
        literal="History of - 1 miscarriage (situation)",
        pattern=[{"LOWER": "history of - 1 miscarriage (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161747002"},
    ),
    TargetRule(
        literal="History of - 2 miscarriages (situation)",
        pattern=[{"LOWER": "history of - 2 miscarriages (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161748007"},
    ),
    TargetRule(
        literal="History of - 3 miscarriages (situation)",
        pattern=[{"LOWER": "history of - 3 miscarriages (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161749004"},
    ),
    TargetRule(
        literal="History of - 4 miscarriages (situation)",
        pattern=[{"LOWER": "history of - 4 miscarriages (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161750004"},
    ),
    TargetRule(
        literal="History of - 5 miscarriages (situation)",
        pattern=[{"LOWER": "history of - 5 miscarriages (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161751000"},
    ),
    TargetRule(
        literal="History of - 6 miscarriages (situation)",
        pattern=[{"LOWER": "history of - 6 miscarriages (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161752007"},
    ),
    TargetRule(
        literal="History of - miscarriage NOS (situation)",
        pattern=[{"LOWER": "history of - miscarriage nos (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161753002"},
    ),
    TargetRule(
        literal="No history of abortion (situation)",
        pattern=[{"LOWER": "no history of abortion (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161755009"},
    ),
    TargetRule(
        literal="History of - 1 abortion (situation)",
        pattern=[{"LOWER": "history of - 1 abortion (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161756005"},
    ),
    TargetRule(
        literal="History of - 2 abortions (situation)",
        pattern=[{"LOWER": "history of - 2 abortions (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161757001"},
    ),
    TargetRule(
        literal="History of - 3 abortions (situation)",
        pattern=[{"LOWER": "history of - 3 abortions (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161758006"},
    ),
    TargetRule(
        literal="History of - 4 abortions (situation)",
        pattern=[{"LOWER": "history of - 4 abortions (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161759003"},
    ),
    TargetRule(
        literal="History of - 5 abortions (situation)",
        pattern=[{"LOWER": "history of - 5 abortions (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161760008"},
    ),
    TargetRule(
        literal="History of - 6 abortions (situation)",
        pattern=[{"LOWER": "history of - 6 abortions (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161761007"},
    ),
    TargetRule(
        literal="History of - abortion NOS (situation)",
        pattern=[{"LOWER": "history of - abortion nos (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161762000"},
    ),
    TargetRule(
        literal="History of - ectopic pregnancy (situation)",
        pattern=[{"LOWER": "history of - ectopic pregnancy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161763005"},
    ),
    TargetRule(
        literal="History of - premature delivery (situation)",
        pattern=[{"LOWER": "history of - premature delivery (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161765003"},
    ),
    TargetRule(
        literal="Past pregnancy outcome NOS (situation)",
        pattern=[{"LOWER": "past pregnancy outcome nos (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161766002"},
    ),
    TargetRule(
        literal="History of - abortion (situation)",
        pattern=[{"LOWER": "history of - abortion (situation)"}],
        category="PREGNANCY",
        attributes={"code": "267014009"},
    ),
    TargetRule(
        literal="History of - full term delivery (situation)",
        pattern=[{"LOWER": "history of - full term delivery (situation)"}],
        category="PREGNANCY",
        attributes={"code": "267015005"},
    ),
    TargetRule(
        literal="History of - myomectomy/hysterotomy (situation)",
        pattern=[{"LOWER": "history of - myomectomy/hysterotomy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "267021009"},
    ),
    TargetRule(
        literal="History of past delivery (situation)",
        pattern=[{"LOWER": "history of past delivery (situation)"}],
        category="PREGNANCY",
        attributes={"code": "272058002"},
    ),
    TargetRule(
        literal="History of - hysterotomy (situation)",
        pattern=[{"LOWER": "history of - hysterotomy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "275573000"},
    ),
    TargetRule(
        literal="History of - myomectomy (situation)",
        pattern=[{"LOWER": "history of - myomectomy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "275574006"},
    ),
    TargetRule(
        literal="History of - pregnancy (situation)",
        pattern=[{"LOWER": "history of - pregnancy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "271903000"},
    ),
    TargetRule(
        literal="History of - normal delivery (situation)",
        pattern=[{"LOWER": "history of - normal delivery (situation)"}],
        category="PREGNANCY",
        attributes={"code": "275568006"},
    ),
    TargetRule(
        literal="History of - delivery no details (situation)",
        pattern=[{"LOWER": "history of - delivery no details (situation)"}],
        category="PREGNANCY",
        attributes={"code": "275569003"},
    ),
    TargetRule(
        literal="History of - medical termination of pregnancy (situation)",
        pattern=[
            {"LOWER": "history of - medical termination of pregnancy (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "412758008"},
    ),
    TargetRule(
        literal="Prenatal visit (regime/therapy)",
        pattern=[{"LOWER": "prenatal visit (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "424619006"},
    ),
    TargetRule(
        literal="Prenatal initial visit (regime/therapy)",
        pattern=[{"LOWER": "prenatal initial visit (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "424441002"},
    ),
    TargetRule(
        literal="Prenatal continuous visit (regime/therapy)",
        pattern=[{"LOWER": "prenatal continuous visit (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "422808006"},
    ),
    TargetRule(
        literal="Prenatal visit",
        pattern=[{"LOWER": "prenatal visit"}],
        category="PREGNANCY",
        attributes={"code": "424619006"},
    ),
    TargetRule(
        literal="Prenatal initial visit",
        pattern=[{"LOWER": "prenatal initial visit"}],
        category="PREGNANCY",
        attributes={"code": "424441002"},
    ),
    TargetRule(
        literal="Prenatal supplemental visit",
        pattern=[{"LOWER": "prenatal supplemental visit"}],
        category="PREGNANCY",
        attributes={"code": "422808006"},
    ),
    TargetRule(
        literal="Patient thinks they are pregnant",
        pattern=[{"LOWER": "patient thinks they are pregnant"}],
        category="PREGNANCY",
        attributes={"code": "102874004"},
    ),
    TargetRule(
        literal="Initial prenatal visit",
        pattern=[{"LOWER": "initial prenatal visit"}],
        category="PREGNANCY",
        attributes={"code": "424441002"},
    ),
    TargetRule(
        literal="Antepartum initial visit",
        pattern=[{"LOWER": "antepartum initial visit"}],
        category="PREGNANCY",
        attributes={"code": "424441002"},
    ),
    TargetRule(
        literal="Supplemental prenatal visit",
        pattern=[{"LOWER": "supplemental prenatal visit"}],
        category="PREGNANCY",
        attributes={"code": "422808006"},
    ),
    TargetRule(
        literal="Antepartum supplemental visit",
        pattern=[{"LOWER": "antepartum supplemental visit"}],
        category="PREGNANCY",
        attributes={"code": "422808006"},
    ),
    TargetRule(
        literal="Prenatal continuous visit",
        pattern=[{"LOWER": "prenatal continuous visit"}],
        category="PREGNANCY",
        attributes={"code": "422808006"},
    ),
    TargetRule(
        literal="History of - perinatal fetal loss",
        pattern=[{"LOWER": "history of - perinatal fetal loss"}],
        category="PREGNANCY",
        attributes={"code": "161811009"},
    ),
    TargetRule(
        literal="History of - previous forceps delivery",
        pattern=[{"LOWER": "history of - previous forceps delivery"}],
        category="PREGNANCY",
        attributes={"code": "161813007"},
    ),
    TargetRule(
        literal="History of - obstetric problem NOS",
        pattern=[{"LOWER": "history of - obstetric problem nos"}],
        category="PREGNANCY",
        attributes={"code": "161814001"},
    ),
    TargetRule(
        literal="History of - obstetric problem",
        pattern=[{"LOWER": "history of - obstetric problem"}],
        category="PREGNANCY",
        attributes={"code": "161803004"},
    ),
    TargetRule(
        literal="History of - antepartum hemorrhage",
        pattern=[{"LOWER": "history of - antepartum hemorrhage"}],
        category="PREGNANCY",
        attributes={"code": "161804005"},
    ),
    TargetRule(
        literal="History of - cesarean section",
        pattern=[{"LOWER": "history of - cesarean section"}],
        category="PREGNANCY",
        attributes={"code": "161805006"},
    ),
    TargetRule(
        literal="History of - eclampsia",
        pattern=[{"LOWER": "history of - eclampsia"}],
        category="PREGNANCY",
        attributes={"code": "161806007"},
    ),
    TargetRule(
        literal="History of - severe pre-eclampsia",
        pattern=[{"LOWER": "history of - severe pre-eclampsia"}],
        category="PREGNANCY",
        attributes={"code": "161807003"},
    ),
    TargetRule(
        literal="History of - manual removal of placenta",
        pattern=[{"LOWER": "history of - manual removal of placenta"}],
        category="PREGNANCY",
        attributes={"code": "161808008"},
    ),
    TargetRule(
        literal="History of - postpartum hemorrhage",
        pattern=[{"LOWER": "history of - postpartum hemorrhage"}],
        category="PREGNANCY",
        attributes={"code": "161809000"},
    ),
    TargetRule(
        literal="History of - prolonged labor",
        pattern=[{"LOWER": "history of - prolonged labor"}],
        category="PREGNANCY",
        attributes={"code": "161810005"},
    ),
    TargetRule(
        literal="History of - 5 miscarriages",
        pattern=[{"LOWER": "history of - 5 miscarriages"}],
        category="PREGNANCY",
        attributes={"code": "161751000"},
    ),
    TargetRule(
        literal="History of - 6 miscarriages",
        pattern=[{"LOWER": "history of - 6 miscarriages"}],
        category="PREGNANCY",
        attributes={"code": "161752007"},
    ),
    TargetRule(
        literal="History of - miscarriage NOS",
        pattern=[{"LOWER": "history of - miscarriage nos"}],
        category="PREGNANCY",
        attributes={"code": "161753002"},
    ),
    TargetRule(
        literal="History of - 1 abortion",
        pattern=[{"LOWER": "history of - 1 abortion"}],
        category="PREGNANCY",
        attributes={"code": "161756005"},
    ),
    TargetRule(
        literal="History of - 2 abortions",
        pattern=[{"LOWER": "history of - 2 abortions"}],
        category="PREGNANCY",
        attributes={"code": "161757001"},
    ),
    TargetRule(
        literal="History of - 3 abortions",
        pattern=[{"LOWER": "history of - 3 abortions"}],
        category="PREGNANCY",
        attributes={"code": "161758006"},
    ),
    TargetRule(
        literal="History of - 4 abortions",
        pattern=[{"LOWER": "history of - 4 abortions"}],
        category="PREGNANCY",
        attributes={"code": "161759003"},
    ),
    TargetRule(
        literal="History of - 5 abortions",
        pattern=[{"LOWER": "history of - 5 abortions"}],
        category="PREGNANCY",
        attributes={"code": "161760008"},
    ),
    TargetRule(
        literal="History of - 6 abortions",
        pattern=[{"LOWER": "history of - 6 abortions"}],
        category="PREGNANCY",
        attributes={"code": "161761007"},
    ),
    TargetRule(
        literal="History of - abortion NOS",
        pattern=[{"LOWER": "history of - abortion nos"}],
        category="PREGNANCY",
        attributes={"code": "161762000"},
    ),
    TargetRule(
        literal="History of - ectopic pregnancy",
        pattern=[{"LOWER": "history of - ectopic pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "161763005"},
    ),
    TargetRule(
        literal="History of - premature delivery",
        pattern=[{"LOWER": "history of - premature delivery"}],
        category="PREGNANCY",
        attributes={"code": "161765003"},
    ),
    TargetRule(
        literal="History of - stillbirth",
        pattern=[{"LOWER": "history of - stillbirth"}],
        category="PREGNANCY",
        attributes={"code": "161743003"},
    ),
    TargetRule(
        literal="History of - miscarriage",
        pattern=[{"LOWER": "history of - miscarriage"}],
        category="PREGNANCY",
        attributes={"code": "161744009"},
    ),
    TargetRule(
        literal="History of - 1 miscarriage",
        pattern=[{"LOWER": "history of - 1 miscarriage"}],
        category="PREGNANCY",
        attributes={"code": "161747002"},
    ),
    TargetRule(
        literal="History of - 2 miscarriages",
        pattern=[{"LOWER": "history of - 2 miscarriages"}],
        category="PREGNANCY",
        attributes={"code": "161748007"},
    ),
    TargetRule(
        literal="History of - 3 miscarriages",
        pattern=[{"LOWER": "history of - 3 miscarriages"}],
        category="PREGNANCY",
        attributes={"code": "161749004"},
    ),
    TargetRule(
        literal="History of - 4 miscarriages",
        pattern=[{"LOWER": "history of - 4 miscarriages"}],
        category="PREGNANCY",
        attributes={"code": "161750004"},
    ),
    TargetRule(
        literal="Pregnant - on abdominal palpation",
        pattern=[{"LOWER": "pregnant - on abdominal palpation"}],
        category="PREGNANCY",
        attributes={"code": "169564004"},
    ),
    TargetRule(
        literal="History of - abortion",
        pattern=[{"LOWER": "history of - abortion"}],
        category="PREGNANCY",
        attributes={"code": "267014009"},
    ),
    TargetRule(
        literal="History of - full term delivery",
        pattern=[{"LOWER": "history of - full term delivery"}],
        category="PREGNANCY",
        attributes={"code": "267015005"},
    ),
    TargetRule(
        literal="History of - pregnancy",
        pattern=[{"LOWER": "history of - pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "271903000"},
    ),
    TargetRule(
        literal="History of - normal delivery",
        pattern=[{"LOWER": "history of - normal delivery"}],
        category="PREGNANCY",
        attributes={"code": "275568006"},
    ),
    TargetRule(
        literal="History of - delivery no details",
        pattern=[{"LOWER": "history of - delivery no details"}],
        category="PREGNANCY",
        attributes={"code": "275569003"},
    ),
    TargetRule(
        literal="History of - myomectomy/hysterotomy",
        pattern=[{"LOWER": "history of - myomectomy/hysterotomy"}],
        category="PREGNANCY",
        attributes={"code": "267021009"},
    ),
    TargetRule(
        literal="History of - hysterotomy",
        pattern=[{"LOWER": "history of - hysterotomy"}],
        category="PREGNANCY",
        attributes={"code": "275573000"},
    ),
    TargetRule(
        literal="History of - myomectomy",
        pattern=[{"LOWER": "history of - myomectomy"}],
        category="PREGNANCY",
        attributes={"code": "275574006"},
    ),
    TargetRule(
        literal="History of - medical termination of pregnancy",
        pattern=[{"LOWER": "history of - medical termination of pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "412758008"},
    ),
    TargetRule(
        literal="History of choriocarcinoma of placenta (situation)",
        pattern=[{"LOWER": "history of choriocarcinoma of placenta (situation)"}],
        category="PREGNANCY",
        attributes={"code": "428978004"},
    ),
    TargetRule(
        literal="History of choriocarcinoma of placenta",
        pattern=[{"LOWER": "history of choriocarcinoma of placenta"}],
        category="PREGNANCY",
        attributes={"code": "428978004"},
    ),
    TargetRule(
        literal="Gastrointestinal tract finding associated with pregnancy (finding)",
        pattern=[
            {
                "LOWER": "gastrointestinal tract finding associated with pregnancy (finding)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "430257003"},
    ),
    TargetRule(
        literal="Possible pregnancy (situation)",
        pattern=[{"LOWER": "possible pregnancy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "146799005"},
    ),
    TargetRule(
        literal="Gastrointestinal tract finding associated with pregnancy",
        pattern=[{"LOWER": "gastrointestinal tract finding associated with pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "430257003"},
    ),
    TargetRule(
        literal="Pregnant - vaginal examination confirms",
        pattern=[{"LOWER": "pregnant - vaginal examination confirms"}],
        category="PREGNANCY",
        attributes={"code": "169562000"},
    ),
    TargetRule(
        literal="Intends to continue pregnancy (finding)",
        pattern=[{"LOWER": "intends to continue pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "439311009"},
    ),
    TargetRule(
        literal="Intends to continue pregnancy",
        pattern=[{"LOWER": "intends to continue pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "439311009"},
    ),
    TargetRule(
        literal="History of premature labor",
        pattern=[{"LOWER": "history of premature labor"}],
        category="PREGNANCY",
        attributes={"code": "441493008"},
    ),
    TargetRule(
        literal="History of premature labour",
        pattern=[{"LOWER": "history of premature labour"}],
        category="PREGNANCY",
        attributes={"code": "441493008"},
    ),
    TargetRule(
        literal="History of premature labor (situation)",
        pattern=[{"LOWER": "history of premature labor (situation)"}],
        category="PREGNANCY",
        attributes={"code": "441493008"},
    ),
    TargetRule(
        literal="History of - foetal loss",
        pattern=[{"LOWER": "history of - foetal loss"}],
        category="PREGNANCY",
        attributes={"code": "267014009"},
    ),
    TargetRule(
        literal="Granuloma gravidarum (disorder)",
        pattern=[{"LOWER": "granuloma gravidarum (disorder)"}],
        category="PREGNANCY",
        attributes={"code": "447222001"},
    ),
    TargetRule(
        literal="Granuloma gravidarum",
        pattern=[{"LOWER": "granuloma gravidarum"}],
        category="PREGNANCY",
        attributes={"code": "447222001"},
    ),
    TargetRule(
        literal="History of gestational diabetes mellitus (situation)",
        pattern=[{"LOWER": "history of gestational diabetes mellitus (situation)"}],
        category="PREGNANCY",
        attributes={"code": "472971004"},
    ),
    TargetRule(
        literal="History of gestational diabetes mellitus",
        pattern=[{"LOWER": "history of gestational diabetes mellitus"}],
        category="PREGNANCY",
        attributes={"code": "472971004"},
    ),
    TargetRule(
        literal="No history of induced termination of pregnancy",
        pattern=[{"LOWER": "no history of induced termination of pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "161755009"},
    ),
    TargetRule(
        literal="History of obstetric problem (situation)",
        pattern=[{"LOWER": "history of obstetric problem (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161803004"},
    ),
    TargetRule(
        literal="History of delivery with no details",
        pattern=[{"LOWER": "history of delivery with no details"}],
        category="PREGNANCY",
        attributes={"code": "275569003"},
    ),
    TargetRule(
        literal="History of one miscarriage",
        pattern=[{"LOWER": "history of one miscarriage"}],
        category="PREGNANCY",
        attributes={"code": "161747002"},
    ),
    TargetRule(
        literal="History of three miscarriages",
        pattern=[{"LOWER": "history of three miscarriages"}],
        category="PREGNANCY",
        attributes={"code": "161749004"},
    ),
    TargetRule(
        literal="History of five miscarriages",
        pattern=[{"LOWER": "history of five miscarriages"}],
        category="PREGNANCY",
        attributes={"code": "161751000"},
    ),
    TargetRule(
        literal="History of cesarean section",
        pattern=[{"LOWER": "history of cesarean section"}],
        category="PREGNANCY",
        attributes={"code": "161805006"},
    ),
    TargetRule(
        literal="History of severe pre-eclampsia",
        pattern=[{"LOWER": "history of severe pre-eclampsia"}],
        category="PREGNANCY",
        attributes={"code": "161807003"},
    ),
    TargetRule(
        literal="History of four abortions (situation)",
        pattern=[{"LOWER": "history of four abortions (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161759003"},
    ),
    TargetRule(
        literal="History of prolonged labor",
        pattern=[{"LOWER": "history of prolonged labor"}],
        category="PREGNANCY",
        attributes={"code": "161810005"},
    ),
    TargetRule(
        literal="History of five abortions (situation)",
        pattern=[{"LOWER": "history of five abortions (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161760008"},
    ),
    TargetRule(
        literal="History of myomectomy (situation)",
        pattern=[{"LOWER": "history of myomectomy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "275574006"},
    ),
    TargetRule(
        literal="History of miscarriage (situation)",
        pattern=[{"LOWER": "history of miscarriage (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161744009"},
    ),
    TargetRule(
        literal="History of five miscarriages (situation)",
        pattern=[{"LOWER": "history of five miscarriages (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161751000"},
    ),
    TargetRule(
        literal="History of eclampsia",
        pattern=[{"LOWER": "history of eclampsia"}],
        category="PREGNANCY",
        attributes={"code": "161806007"},
    ),
    TargetRule(
        literal="History of full term delivery",
        pattern=[{"LOWER": "history of full term delivery"}],
        category="PREGNANCY",
        attributes={"code": "267015005"},
    ),
    TargetRule(
        literal="History of previous forceps delivery",
        pattern=[{"LOWER": "history of previous forceps delivery"}],
        category="PREGNANCY",
        attributes={"code": "161813007"},
    ),
    TargetRule(
        literal="History of myomectomy or hysterotomy (situation)",
        pattern=[{"LOWER": "history of myomectomy or hysterotomy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "267021009"},
    ),
    TargetRule(
        literal="History of cesarean section (situation)",
        pattern=[{"LOWER": "history of cesarean section (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161805006"},
    ),
    TargetRule(
        literal="History of manual removal of placenta",
        pattern=[{"LOWER": "history of manual removal of placenta"}],
        category="PREGNANCY",
        attributes={"code": "161808008"},
    ),
    TargetRule(
        literal="History of full term delivery (situation)",
        pattern=[{"LOWER": "history of full term delivery (situation)"}],
        category="PREGNANCY",
        attributes={"code": "267015005"},
    ),
    TargetRule(
        literal="History of perinatal fetal loss (situation)",
        pattern=[{"LOWER": "history of perinatal fetal loss (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161811009"},
    ),
    TargetRule(
        literal="History of four miscarriages",
        pattern=[{"LOWER": "history of four miscarriages"}],
        category="PREGNANCY",
        attributes={"code": "161750004"},
    ),
    TargetRule(
        literal="History of premature delivery",
        pattern=[{"LOWER": "history of premature delivery"}],
        category="PREGNANCY",
        attributes={"code": "161765003"},
    ),
    TargetRule(
        literal="History of fetal loss",
        pattern=[{"LOWER": "history of fetal loss"}],
        category="PREGNANCY",
        attributes={"code": "267014009"},
    ),
    TargetRule(
        literal="History of perinatal fetal loss",
        pattern=[{"LOWER": "history of perinatal fetal loss"}],
        category="PREGNANCY",
        attributes={"code": "161811009"},
    ),
    TargetRule(
        literal="History of six abortions",
        pattern=[{"LOWER": "history of six abortions"}],
        category="PREGNANCY",
        attributes={"code": "161761007"},
    ),
    TargetRule(
        literal="History of pregnancy (situation)",
        pattern=[{"LOWER": "history of pregnancy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "271903000"},
    ),
    TargetRule(
        literal="History of postpartum haemorrhage",
        pattern=[{"LOWER": "history of postpartum haemorrhage"}],
        category="PREGNANCY",
        attributes={"code": "161809000"},
    ),
    TargetRule(
        literal="History of prolonged labor (situation)",
        pattern=[{"LOWER": "history of prolonged labor (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161810005"},
    ),
    TargetRule(
        literal="History of one abortion (situation)",
        pattern=[{"LOWER": "history of one abortion (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161756005"},
    ),
    TargetRule(
        literal="History of one miscarriage (situation)",
        pattern=[{"LOWER": "history of one miscarriage (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161747002"},
    ),
    TargetRule(
        literal="History of hysterotomy",
        pattern=[{"LOWER": "history of hysterotomy"}],
        category="PREGNANCY",
        attributes={"code": "275573000"},
    ),
    TargetRule(
        literal="History of four abortions",
        pattern=[{"LOWER": "history of four abortions"}],
        category="PREGNANCY",
        attributes={"code": "161759003"},
    ),
    TargetRule(
        literal="History of ectopic pregnancy",
        pattern=[{"LOWER": "history of ectopic pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "161763005"},
    ),
    TargetRule(
        literal="History of abortion (situation)",
        pattern=[{"LOWER": "history of abortion (situation)"}],
        category="PREGNANCY",
        attributes={"code": "267014009"},
    ),
    TargetRule(
        literal="History of two abortions",
        pattern=[{"LOWER": "history of two abortions"}],
        category="PREGNANCY",
        attributes={"code": "161757001"},
    ),
    TargetRule(
        literal="History of previous forceps delivery (situation)",
        pattern=[{"LOWER": "history of previous forceps delivery (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161813007"},
    ),
    TargetRule(
        literal="History of normal delivery (situation)",
        pattern=[{"LOWER": "history of normal delivery (situation)"}],
        category="PREGNANCY",
        attributes={"code": "275568006"},
    ),
    TargetRule(
        literal="History of premature delivery (situation)",
        pattern=[{"LOWER": "history of premature delivery (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161765003"},
    ),
    TargetRule(
        literal="History of antepartum hemorrhage",
        pattern=[{"LOWER": "history of antepartum hemorrhage"}],
        category="PREGNANCY",
        attributes={"code": "161804005"},
    ),
    TargetRule(
        literal="History of six abortions (situation)",
        pattern=[{"LOWER": "history of six abortions (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161761007"},
    ),
    TargetRule(
        literal="History of obstetric problem",
        pattern=[{"LOWER": "history of obstetric problem"}],
        category="PREGNANCY",
        attributes={"code": "161803004"},
    ),
    TargetRule(
        literal="History of stillbirth (situation)",
        pattern=[{"LOWER": "history of stillbirth (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161743003"},
    ),
    TargetRule(
        literal="History of severe pre-eclampsia (situation)",
        pattern=[{"LOWER": "history of severe pre-eclampsia (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161807003"},
    ),
    TargetRule(
        literal="History of postpartum hemorrhage",
        pattern=[{"LOWER": "history of postpartum hemorrhage"}],
        category="PREGNANCY",
        attributes={"code": "161809000"},
    ),
    TargetRule(
        literal="History of eclampsia (situation)",
        pattern=[{"LOWER": "history of eclampsia (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161806007"},
    ),
    TargetRule(
        literal="History of four miscarriages (situation)",
        pattern=[{"LOWER": "history of four miscarriages (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161750004"},
    ),
    TargetRule(
        literal="History of two miscarriages (situation)",
        pattern=[{"LOWER": "history of two miscarriages (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161748007"},
    ),
    TargetRule(
        literal="History of delivery with no details (situation)",
        pattern=[{"LOWER": "history of delivery with no details (situation)"}],
        category="PREGNANCY",
        attributes={"code": "275569003"},
    ),
    TargetRule(
        literal="History of medical termination of pregnancy (situation)",
        pattern=[{"LOWER": "history of medical termination of pregnancy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "412758008"},
    ),
    TargetRule(
        literal="History of three miscarriages (situation)",
        pattern=[{"LOWER": "history of three miscarriages (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161749004"},
    ),
    TargetRule(
        literal="History of antepartum hemorrhage (situation)",
        pattern=[{"LOWER": "history of antepartum hemorrhage (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161804005"},
    ),
    TargetRule(
        literal="History of three abortions (situation)",
        pattern=[{"LOWER": "history of three abortions (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161758006"},
    ),
    TargetRule(
        literal="History of manual removal of placenta (situation)",
        pattern=[{"LOWER": "history of manual removal of placenta (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161808008"},
    ),
    TargetRule(
        literal="History of medical termination of pregnancy",
        pattern=[{"LOWER": "history of medical termination of pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "412758008"},
    ),
    TargetRule(
        literal="History of ectopic pregnancy (situation)",
        pattern=[{"LOWER": "history of ectopic pregnancy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161763005"},
    ),
    TargetRule(
        literal="History of miscarriage",
        pattern=[{"LOWER": "history of miscarriage"}],
        category="PREGNANCY",
        attributes={"code": "161744009"},
    ),
    TargetRule(
        literal="History of two abortions (situation)",
        pattern=[{"LOWER": "history of two abortions (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161757001"},
    ),
    TargetRule(
        literal="History of abortion",
        pattern=[{"LOWER": "history of abortion"}],
        category="PREGNANCY",
        attributes={"code": "267014009"},
    ),
    TargetRule(
        literal="History of myomectomy",
        pattern=[{"LOWER": "history of myomectomy"}],
        category="PREGNANCY",
        attributes={"code": "275574006"},
    ),
    TargetRule(
        literal="History of pregnancy",
        pattern=[{"LOWER": "history of pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "271903000"},
    ),
    TargetRule(
        literal="History of stillbirth",
        pattern=[{"LOWER": "history of stillbirth"}],
        category="PREGNANCY",
        attributes={"code": "161743003"},
    ),
    TargetRule(
        literal="History of foetal loss",
        pattern=[{"LOWER": "history of foetal loss"}],
        category="PREGNANCY",
        attributes={"code": "267014009"},
    ),
    TargetRule(
        literal="History of five abortions",
        pattern=[{"LOWER": "history of five abortions"}],
        category="PREGNANCY",
        attributes={"code": "161760008"},
    ),
    TargetRule(
        literal="History of one abortion",
        pattern=[{"LOWER": "history of one abortion"}],
        category="PREGNANCY",
        attributes={"code": "161756005"},
    ),
    TargetRule(
        literal="History of normal delivery",
        pattern=[{"LOWER": "history of normal delivery"}],
        category="PREGNANCY",
        attributes={"code": "275568006"},
    ),
    TargetRule(
        literal="History of postpartum hemorrhage (situation)",
        pattern=[{"LOWER": "history of postpartum hemorrhage (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161809000"},
    ),
    TargetRule(
        literal="History of six miscarriages (situation)",
        pattern=[{"LOWER": "history of six miscarriages (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161752007"},
    ),
    TargetRule(
        literal="History of hysterotomy (situation)",
        pattern=[{"LOWER": "history of hysterotomy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "275573000"},
    ),
    TargetRule(
        literal="History of myomectomy or hysterotomy",
        pattern=[{"LOWER": "history of myomectomy or hysterotomy"}],
        category="PREGNANCY",
        attributes={"code": "267021009"},
    ),
    TargetRule(
        literal="History of six miscarriages",
        pattern=[{"LOWER": "history of six miscarriages"}],
        category="PREGNANCY",
        attributes={"code": "161752007"},
    ),
    TargetRule(
        literal="History of three abortions",
        pattern=[{"LOWER": "history of three abortions"}],
        category="PREGNANCY",
        attributes={"code": "161758006"},
    ),
    TargetRule(
        literal="History of two miscarriages",
        pattern=[{"LOWER": "history of two miscarriages"}],
        category="PREGNANCY",
        attributes={"code": "161748007"},
    ),
    TargetRule(
        literal="History of prolonged labour",
        pattern=[{"LOWER": "history of prolonged labour"}],
        category="PREGNANCY",
        attributes={"code": "161810005"},
    ),
    TargetRule(
        literal="History of induced termination of pregnancy under unsafe conditions (situation)",
        pattern=[
            {
                "LOWER": "history of induced termination of pregnancy under unsafe conditions (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "697994009"},
    ),
    TargetRule(
        literal="History of induced termination of pregnancy under unsafe conditions",
        pattern=[
            {
                "LOWER": "history of induced termination of pregnancy under unsafe conditions"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "697994009"},
    ),
    TargetRule(
        literal="History of preterm delivery",
        pattern=[{"LOWER": "history of preterm delivery"}],
        category="PREGNANCY",
        attributes={"code": "161765003"},
    ),
    TargetRule(
        literal="H/O: perinatal foetal loss",
        pattern=[{"LOWER": "h/o: perinatal foetal loss"}],
        category="PREGNANCY",
        attributes={"code": "161811009"},
    ),
    TargetRule(
        literal="History of - perinatal foetal loss",
        pattern=[{"LOWER": "history of - perinatal foetal loss"}],
        category="PREGNANCY",
        attributes={"code": "161811009"},
    ),
    TargetRule(
        literal="Partner pregnant (situation)",
        pattern=[{"LOWER": "partner pregnant (situation)"}],
        category="PREGNANCY",
        attributes={"code": "704502000"},
    ),
    TargetRule(
        literal="Partner pregnant",
        pattern=[{"LOWER": "partner pregnant"}],
        category="PREGNANCY",
        attributes={"code": "704502000"},
    ),
    TargetRule(
        literal="History of gestational hypertension",
        pattern=[{"LOWER": "history of gestational hypertension"}],
        category="PREGNANCY",
        attributes={"code": "709881001"},
    ),
    TargetRule(
        literal="History of gestational hypertension (situation)",
        pattern=[{"LOWER": "history of gestational hypertension (situation)"}],
        category="PREGNANCY",
        attributes={"code": "709881001"},
    ),
    TargetRule(
        literal="History of preeclampsia",
        pattern=[{"LOWER": "history of preeclampsia"}],
        category="PREGNANCY",
        attributes={"code": "105651000119100"},
    ),
    TargetRule(
        literal="History of preeclampsia (situation)",
        pattern=[{"LOWER": "history of preeclampsia (situation)"}],
        category="PREGNANCY",
        attributes={"code": "105651000119100"},
    ),
    TargetRule(
        literal="History of delivery of macrosomal infant (situation)",
        pattern=[{"LOWER": "history of delivery of macrosomal infant (situation)"}],
        category="PREGNANCY",
        attributes={"code": "32271000119102"},
    ),
    TargetRule(
        literal="History of delivery of macrosomal infant",
        pattern=[{"LOWER": "history of delivery of macrosomal infant"}],
        category="PREGNANCY",
        attributes={"code": "32271000119102"},
    ),
    TargetRule(
        literal="History of pregnancy with abortive outcome",
        pattern=[{"LOWER": "history of pregnancy with abortive outcome"}],
        category="PREGNANCY",
        attributes={"code": "713651007"},
    ),
    TargetRule(
        literal="History of induced termination of pregnancy (situation)",
        pattern=[{"LOWER": "history of induced termination of pregnancy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "713649008"},
    ),
    TargetRule(
        literal="History of pregnancy with abortive outcome (situation)",
        pattern=[{"LOWER": "history of pregnancy with abortive outcome (situation)"}],
        category="PREGNANCY",
        attributes={"code": "713651007"},
    ),
    TargetRule(
        literal="History of induced termination of pregnancy",
        pattern=[{"LOWER": "history of induced termination of pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "713649008"},
    ),
    TargetRule(
        literal="Pyogenic granuloma of gingiva co-occurrent and due to pregnancy (disorder)",
        pattern=[
            {
                "LOWER": "pyogenic granuloma of gingiva co-occurrent and due to pregnancy (disorder)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "713249002"},
    ),
    TargetRule(
        literal="Pyogenic granuloma of gingiva co-occurrent and due to pregnancy",
        pattern=[
            {"LOWER": "pyogenic granuloma of gingiva co-occurrent and due to pregnancy"}
        ],
        category="PREGNANCY",
        attributes={"code": "713249002"},
    ),
    TargetRule(
        literal="History of pre-eclampsia (situation)",
        pattern=[{"LOWER": "history of pre-eclampsia (situation)"}],
        category="PREGNANCY",
        attributes={"code": "105651000119100"},
    ),
    TargetRule(
        literal="History of pre-eclampsia",
        pattern=[{"LOWER": "history of pre-eclampsia"}],
        category="PREGNANCY",
        attributes={"code": "105651000119100"},
    ),
    TargetRule(
        literal="History of defibulation of vulva to facilitate delivery (situation)",
        pattern=[
            {
                "LOWER": "history of defibulation of vulva to facilitate delivery (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "719594003"},
    ),
    TargetRule(
        literal="History of defibulation of vulva to facilitate delivery",
        pattern=[{"LOWER": "history of defibulation of vulva to facilitate delivery"}],
        category="PREGNANCY",
        attributes={"code": "719594003"},
    ),
    TargetRule(
        literal="History of placenta previa (situation)",
        pattern=[{"LOWER": "history of placenta previa (situation)"}],
        category="PREGNANCY",
        attributes={"code": "725924008"},
    ),
    TargetRule(
        literal="History of placenta previa",
        pattern=[{"LOWER": "history of placenta previa"}],
        category="PREGNANCY",
        attributes={"code": "725924008"},
    ),
    TargetRule(
        literal="History of placenta praevia",
        pattern=[{"LOWER": "history of placenta praevia"}],
        category="PREGNANCY",
        attributes={"code": "725924008"},
    ),
    TargetRule(
        literal="History of third degree perineal laceration (situation)",
        pattern=[{"LOWER": "history of third degree perineal laceration (situation)"}],
        category="PREGNANCY",
        attributes={"code": "725941005"},
    ),
    TargetRule(
        literal="History of third degree perineal laceration",
        pattern=[{"LOWER": "history of third degree perineal laceration"}],
        category="PREGNANCY",
        attributes={"code": "725941005"},
    ),
    TargetRule(
        literal="History of fourth degree perineal laceration (situation)",
        pattern=[{"LOWER": "history of fourth degree perineal laceration (situation)"}],
        category="PREGNANCY",
        attributes={"code": "725942003"},
    ),
    TargetRule(
        literal="History of fourth degree perineal laceration",
        pattern=[{"LOWER": "history of fourth degree perineal laceration"}],
        category="PREGNANCY",
        attributes={"code": "725942003"},
    ),
    TargetRule(
        literal="History of second degree perineal laceration (situation)",
        pattern=[{"LOWER": "history of second degree perineal laceration (situation)"}],
        category="PREGNANCY",
        attributes={"code": "725943008"},
    ),
    TargetRule(
        literal="History of second degree perineal laceration",
        pattern=[{"LOWER": "history of second degree perineal laceration"}],
        category="PREGNANCY",
        attributes={"code": "725943008"},
    ),
    TargetRule(
        literal="History of episiotomy (situation)",
        pattern=[{"LOWER": "history of episiotomy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "725944002"},
    ),
    TargetRule(
        literal="History of episiotomy",
        pattern=[{"LOWER": "history of episiotomy"}],
        category="PREGNANCY",
        attributes={"code": "725944002"},
    ),
    TargetRule(
        literal="History of retained placenta (situation)",
        pattern=[{"LOWER": "history of retained placenta (situation)"}],
        category="PREGNANCY",
        attributes={"code": "725948004"},
    ),
    TargetRule(
        literal="History of retained placenta",
        pattern=[{"LOWER": "history of retained placenta"}],
        category="PREGNANCY",
        attributes={"code": "725948004"},
    ),
    TargetRule(
        literal="History of elective cesarean section (situation)",
        pattern=[{"LOWER": "history of elective cesarean section (situation)"}],
        category="PREGNANCY",
        attributes={"code": "725949007"},
    ),
    TargetRule(
        literal="History of elective cesarean section",
        pattern=[{"LOWER": "history of elective cesarean section"}],
        category="PREGNANCY",
        attributes={"code": "725949007"},
    ),
    TargetRule(
        literal="History of elective caesarean section",
        pattern=[{"LOWER": "history of elective caesarean section"}],
        category="PREGNANCY",
        attributes={"code": "725949007"},
    ),
    TargetRule(
        literal="History of placenta accreta (situation)",
        pattern=[{"LOWER": "history of placenta accreta (situation)"}],
        category="PREGNANCY",
        attributes={"code": "725950007"},
    ),
    TargetRule(
        literal="History of placenta accreta",
        pattern=[{"LOWER": "history of placenta accreta"}],
        category="PREGNANCY",
        attributes={"code": "725950007"},
    ),
    TargetRule(
        literal="History of emergency cesarean section (situation)",
        pattern=[{"LOWER": "history of emergency cesarean section (situation)"}],
        category="PREGNANCY",
        attributes={"code": "725951006"},
    ),
    TargetRule(
        literal="History of emergency cesarean section",
        pattern=[{"LOWER": "history of emergency cesarean section"}],
        category="PREGNANCY",
        attributes={"code": "725951006"},
    ),
    TargetRule(
        literal="History of emergency caesarean section",
        pattern=[{"LOWER": "history of emergency caesarean section"}],
        category="PREGNANCY",
        attributes={"code": "725951006"},
    ),
    TargetRule(
        literal="History of induced onset of labor (situation)",
        pattern=[{"LOWER": "history of induced onset of labor (situation)"}],
        category="PREGNANCY",
        attributes={"code": "725954003"},
    ),
    TargetRule(
        literal="History of induced onset of labor",
        pattern=[{"LOWER": "history of induced onset of labor"}],
        category="PREGNANCY",
        attributes={"code": "725954003"},
    ),
    TargetRule(
        literal="History of induced onset of labour",
        pattern=[{"LOWER": "history of induced onset of labour"}],
        category="PREGNANCY",
        attributes={"code": "725954003"},
    ),
    TargetRule(
        literal="History of live birth (situation)",
        pattern=[{"LOWER": "history of live birth (situation)"}],
        category="PREGNANCY",
        attributes={"code": "726001007"},
    ),
    TargetRule(
        literal="History of live birth",
        pattern=[{"LOWER": "history of live birth"}],
        category="PREGNANCY",
        attributes={"code": "726001007"},
    ),
    TargetRule(
        literal="History of hemolysis-elevated liver enzymes-low platelet count syndrome (situation)",
        pattern=[
            {
                "LOWER": "history of hemolysis-elevated liver enzymes-low platelet count syndrome (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "726513006"},
    ),
    TargetRule(
        literal="History of hemolysis-elevated liver enzymes-low platelet count syndrome",
        pattern=[
            {
                "LOWER": "history of hemolysis-elevated liver enzymes-low platelet count syndrome"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "726513006"},
    ),
    TargetRule(
        literal="History of haemolysis-elevated liver enzymes-low platelet count syndrome",
        pattern=[
            {
                "LOWER": "history of haemolysis-elevated liver enzymes-low platelet count syndrome"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "726513006"},
    ),
    TargetRule(
        literal="H/O: HELLP (hemolysis, elevated liver enzymes, low platelet count) syndrome",
        pattern=[
            {
                "LOWER": "h/o: hellp (hemolysis, elevated liver enzymes, low platelet count) syndrome"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "726513006"},
    ),
    TargetRule(
        literal="H/O: HELLP (haemolysis, elevated liver enzymes, low platelet count) syndrome",
        pattern=[
            {
                "LOWER": "h/o: hellp (haemolysis, elevated liver enzymes, low platelet count) syndrome"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "726513006"},
    ),
    TargetRule(
        literal="History of postpartum psychosis (situation)",
        pattern=[{"LOWER": "history of postpartum psychosis (situation)"}],
        category="PREGNANCY",
        attributes={"code": "726623007"},
    ),
    TargetRule(
        literal="H/O: postpartum psychosis",
        pattern=[{"LOWER": "h/o: postpartum psychosis"}],
        category="PREGNANCY",
        attributes={"code": "726623007"},
    ),
    TargetRule(
        literal="History of postpartum psychosis",
        pattern=[{"LOWER": "history of postpartum psychosis"}],
        category="PREGNANCY",
        attributes={"code": "726623007"},
    ),
    TargetRule(
        literal="History of spontaneous onset of labor (situation)",
        pattern=[{"LOWER": "history of spontaneous onset of labor (situation)"}],
        category="PREGNANCY",
        attributes={"code": "726597008"},
    ),
    TargetRule(
        literal="H/O: spontaneous onset of labor",
        pattern=[{"LOWER": "h/o: spontaneous onset of labor"}],
        category="PREGNANCY",
        attributes={"code": "726597008"},
    ),
    TargetRule(
        literal="H/O: spontaneous onset of labour",
        pattern=[{"LOWER": "h/o: spontaneous onset of labour"}],
        category="PREGNANCY",
        attributes={"code": "726597008"},
    ),
    TargetRule(
        literal="History of spontaneous onset of labor",
        pattern=[{"LOWER": "history of spontaneous onset of labor"}],
        category="PREGNANCY",
        attributes={"code": "726597008"},
    ),
    TargetRule(
        literal="History of spontaneous onset of labour",
        pattern=[{"LOWER": "history of spontaneous onset of labour"}],
        category="PREGNANCY",
        attributes={"code": "726597008"},
    ),
    TargetRule(
        literal="History of first degree perineal laceration (situation)",
        pattern=[{"LOWER": "history of first degree perineal laceration (situation)"}],
        category="PREGNANCY",
        attributes={"code": "726625000"},
    ),
    TargetRule(
        literal="H/O: first degree perineal laceration",
        pattern=[{"LOWER": "h/o: first degree perineal laceration"}],
        category="PREGNANCY",
        attributes={"code": "726625000"},
    ),
    TargetRule(
        literal="History of first degree perineal laceration",
        pattern=[{"LOWER": "history of first degree perineal laceration"}],
        category="PREGNANCY",
        attributes={"code": "726625000"},
    ),
    TargetRule(
        literal="History of intrauterine fetal death (situation)",
        pattern=[{"LOWER": "history of intrauterine fetal death (situation)"}],
        category="PREGNANCY",
        attributes={"code": "16216731000119106"},
    ),
    TargetRule(
        literal="History of intrauterine fetal death",
        pattern=[{"LOWER": "history of intrauterine fetal death"}],
        category="PREGNANCY",
        attributes={"code": "16216731000119106"},
    ),
    TargetRule(
        literal="History of intrauterine foetal death",
        pattern=[{"LOWER": "history of intrauterine foetal death"}],
        category="PREGNANCY",
        attributes={"code": "16216731000119106"},
    ),
    TargetRule(
        literal="History of molar pregnancy (situation)",
        pattern=[{"LOWER": "history of molar pregnancy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "16216821000119102"},
    ),
    TargetRule(
        literal="History of molar pregnancy",
        pattern=[{"LOWER": "history of molar pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "16216821000119102"},
    ),
    TargetRule(
        literal="History of cholestasis in pregnancy (situation)",
        pattern=[{"LOWER": "history of cholestasis in pregnancy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "16216781000119107"},
    ),
    TargetRule(
        literal="History of cholestasis in pregnancy",
        pattern=[{"LOWER": "history of cholestasis in pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "16216781000119107"},
    ),
    TargetRule(
        literal="H/O: cholestasis of pregnancy",
        pattern=[{"LOWER": "h/o: cholestasis of pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "16216781000119107"},
    ),
    TargetRule(
        literal="Past history of small for gestational age baby (situation)",
        pattern=[
            {"LOWER": "past history of small for gestational age baby (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "726565008"},
    ),
    TargetRule(
        literal="Past history of small for gestational age baby",
        pattern=[{"LOWER": "past history of small for gestational age baby"}],
        category="PREGNANCY",
        attributes={"code": "726565008"},
    ),
    TargetRule(
        literal="H/O: previous small for gestational age baby",
        pattern=[{"LOWER": "h/o: previous small for gestational age baby"}],
        category="PREGNANCY",
        attributes={"code": "726565008"},
    ),
    TargetRule(
        literal="History of previous small for gestational age baby",
        pattern=[{"LOWER": "history of previous small for gestational age baby"}],
        category="PREGNANCY",
        attributes={"code": "726565008"},
    ),
    TargetRule(
        literal="History of previous small-for-dates baby",
        pattern=[{"LOWER": "history of previous small-for-dates baby"}],
        category="PREGNANCY",
        attributes={"code": "726565008"},
    ),
    TargetRule(
        literal="Past history of baby with fetal growth restriction (situation)",
        pattern=[
            {"LOWER": "past history of baby with fetal growth restriction (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "733899004"},
    ),
    TargetRule(
        literal="H/O: previous baby with fetal growth restriction",
        pattern=[{"LOWER": "h/o: previous baby with fetal growth restriction"}],
        category="PREGNANCY",
        attributes={"code": "733899004"},
    ),
    TargetRule(
        literal="History of previous baby with fetal growth restriction",
        pattern=[{"LOWER": "history of previous baby with fetal growth restriction"}],
        category="PREGNANCY",
        attributes={"code": "733899004"},
    ),
    TargetRule(
        literal="History of previous baby with foetal growth restriction",
        pattern=[{"LOWER": "history of previous baby with foetal growth restriction"}],
        category="PREGNANCY",
        attributes={"code": "733899004"},
    ),
    TargetRule(
        literal="Past history of baby with fetal growth restriction",
        pattern=[{"LOWER": "past history of baby with fetal growth restriction"}],
        category="PREGNANCY",
        attributes={"code": "733899004"},
    ),
    TargetRule(
        literal="Past history of baby with foetal growth restriction",
        pattern=[{"LOWER": "past history of baby with foetal growth restriction"}],
        category="PREGNANCY",
        attributes={"code": "733899004"},
    ),
    TargetRule(
        literal="History of previous delivery by vacuum extraction (situation)",
        pattern=[
            {"LOWER": "history of previous delivery by vacuum extraction (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "726624001"},
    ),
    TargetRule(
        literal="H/O: previous delivery by vacuum extraction",
        pattern=[{"LOWER": "h/o: previous delivery by vacuum extraction"}],
        category="PREGNANCY",
        attributes={"code": "726624001"},
    ),
    TargetRule(
        literal="History of previous delivery by vacuum extraction",
        pattern=[{"LOWER": "history of previous delivery by vacuum extraction"}],
        category="PREGNANCY",
        attributes={"code": "726624001"},
    ),
    TargetRule(
        literal="History of pregnancy loss in non-pregnant woman (situation)",
        pattern=[
            {"LOWER": "history of pregnancy loss in non-pregnant woman (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "15011000119104"},
    ),
    TargetRule(
        literal="History of pregnancy loss in non-pregnant woman",
        pattern=[{"LOWER": "history of pregnancy loss in non-pregnant woman"}],
        category="PREGNANCY",
        attributes={"code": "15011000119104"},
    ),
    TargetRule(
        literal="History of preterm premature rupture of membranes (situation)",
        pattern=[
            {"LOWER": "history of preterm premature rupture of membranes (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "108951000119100"},
    ),
    TargetRule(
        literal="History of preterm premature rupture of membranes",
        pattern=[{"LOWER": "history of preterm premature rupture of membranes"}],
        category="PREGNANCY",
        attributes={"code": "108951000119100"},
    ),
    TargetRule(
        literal="History of gestational trophoblastic disease (situation)",
        pattern=[{"LOWER": "history of gestational trophoblastic disease (situation)"}],
        category="PREGNANCY",
        attributes={"code": "736725001"},
    ),
    TargetRule(
        literal="History of gestational trophoblastic disease",
        pattern=[{"LOWER": "history of gestational trophoblastic disease"}],
        category="PREGNANCY",
        attributes={"code": "736725001"},
    ),
    TargetRule(
        literal="History of antepartum haemorrhage",
        pattern=[{"LOWER": "history of antepartum haemorrhage"}],
        category="PREGNANCY",
        attributes={"code": "161804005"},
    ),
    TargetRule(
        literal="History of caesarean section",
        pattern=[{"LOWER": "history of caesarean section"}],
        category="PREGNANCY",
        attributes={"code": "161805006"},
    ),
    TargetRule(
        literal="Gravida 1",
        pattern=[{"LOWER": "gravida 1"}],
        category="PREGNANCY",
        attributes={"code": "127364007"},
    ),
    TargetRule(
        literal="History of placental abruption",
        pattern=[{"LOWER": "history of placental abruption"}],
        category="PREGNANCY",
        attributes={"code": "789776003"},
    ),
    TargetRule(
        literal="History of placental abruption (situation)",
        pattern=[{"LOWER": "history of placental abruption (situation)"}],
        category="PREGNANCY",
        attributes={"code": "789776003"},
    ),
    TargetRule(
        literal="History of shoulder dystocia",
        pattern=[{"LOWER": "history of shoulder dystocia"}],
        category="PREGNANCY",
        attributes={"code": "816150000"},
    ),
    TargetRule(
        literal="History of shoulder dystocia (situation)",
        pattern=[{"LOWER": "history of shoulder dystocia (situation)"}],
        category="PREGNANCY",
        attributes={"code": "816150000"},
    ),
    TargetRule(
        literal="Measured gestational weight gain",
        pattern=[{"LOWER": "measured gestational weight gain"}],
        category="PREGNANCY",
        attributes={"code": "816161008"},
    ),
    TargetRule(
        literal="Measured gestational weight gain (observable entity)",
        pattern=[{"LOWER": "measured gestational weight gain (observable entity)"}],
        category="PREGNANCY",
        attributes={"code": "816161008"},
    ),
    TargetRule(
        literal="Measured gestational weight loss",
        pattern=[{"LOWER": "measured gestational weight loss"}],
        category="PREGNANCY",
        attributes={"code": "816172003"},
    ),
    TargetRule(
        literal="Measured gestational weight loss (observable entity)",
        pattern=[{"LOWER": "measured gestational weight loss (observable entity)"}],
        category="PREGNANCY",
        attributes={"code": "816172003"},
    ),
    TargetRule(
        literal="History of postpartum gestational hypertension",
        pattern=[{"LOWER": "history of postpartum gestational hypertension"}],
        category="PREGNANCY",
        attributes={"code": "16916061000119102"},
    ),
    TargetRule(
        literal="History of postpartum gestational hypertension (situation)",
        pattern=[
            {"LOWER": "history of postpartum gestational hypertension (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "16916061000119102"},
    ),
    TargetRule(
        literal="History of hydatidiform mole",
        pattern=[{"LOWER": "history of hydatidiform mole"}],
        category="PREGNANCY",
        attributes={"code": "16216821000119102"},
    ),
    TargetRule(
        literal="History of complication occurring during labour and delivery",
        pattern=[
            {"LOWER": "history of complication occurring during labour and delivery"}
        ],
        category="PREGNANCY",
        attributes={"code": "1156096005"},
    ),
    TargetRule(
        literal="History of complication occurring during labor and delivery (situation)",
        pattern=[
            {
                "LOWER": "history of complication occurring during labor and delivery (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "1156096005"},
    ),
    TargetRule(
        literal="History of complication occurring during labor and delivery",
        pattern=[
            {"LOWER": "history of complication occurring during labor and delivery"}
        ],
        category="PREGNANCY",
        attributes={"code": "1156096005"},
    ),
    TargetRule(
        literal="History of complication of puerperium (situation)",
        pattern=[{"LOWER": "history of complication of puerperium (situation)"}],
        category="PREGNANCY",
        attributes={"code": "1156097001"},
    ),
    TargetRule(
        literal="History of complication of puerperium",
        pattern=[{"LOWER": "history of complication of puerperium"}],
        category="PREGNANCY",
        attributes={"code": "1156097001"},
    ),
    TargetRule(
        literal="History of Rhesus isoimmunization affecting pregnancy",
        pattern=[{"LOWER": "history of rhesus isoimmunization affecting pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "1156098006"},
    ),
    TargetRule(
        literal="History of Rhesus isoimmunisation affecting pregnancy",
        pattern=[{"LOWER": "history of rhesus isoimmunisation affecting pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "1156098006"},
    ),
    TargetRule(
        literal="History of Rhesus isoimmunization affecting pregnancy (situation)",
        pattern=[
            {
                "LOWER": "history of rhesus isoimmunization affecting pregnancy (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "1156098006"},
    ),
    TargetRule(
        literal="History of abnormal glucose tolerance test in pregnancy",
        pattern=[{"LOWER": "history of abnormal glucose tolerance test in pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "1156099003"},
    ),
    TargetRule(
        literal="History of pregnancy with abnormal glucose tolerance test",
        pattern=[
            {"LOWER": "history of pregnancy with abnormal glucose tolerance test"}
        ],
        category="PREGNANCY",
        attributes={"code": "1156099003"},
    ),
    TargetRule(
        literal="History of pregnancy with abnormal glucose tolerance test (situation)",
        pattern=[
            {
                "LOWER": "history of pregnancy with abnormal glucose tolerance test (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "1156099003"},
    ),
    TargetRule(
        literal="History of pregnancy with normal glucose tolerance test",
        pattern=[{"LOWER": "history of pregnancy with normal glucose tolerance test"}],
        category="PREGNANCY",
        attributes={"code": "1156101005"},
    ),
    TargetRule(
        literal="History of pregnancy with normal glucose tolerance test (situation)",
        pattern=[
            {
                "LOWER": "history of pregnancy with normal glucose tolerance test (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "1156101005"},
    ),
    TargetRule(
        literal="History of normal glucose tolerance test in pregnancy",
        pattern=[{"LOWER": "history of normal glucose tolerance test in pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "1156101005"},
    ),
    TargetRule(
        literal="Pyogenic granuloma of gingiva due to pregnancy (disorder)",
        pattern=[
            {"LOWER": "pyogenic granuloma of gingiva due to pregnancy (disorder)"}
        ],
        category="PREGNANCY",
        attributes={"code": "713249002"},
    ),
    TargetRule(
        literal="Pyogenic granuloma of gingiva due to pregnancy",
        pattern=[{"LOWER": "pyogenic granuloma of gingiva due to pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "713249002"},
    ),
    TargetRule(
        literal="History of short umbilical cord (situation)",
        pattern=[{"LOWER": "history of short umbilical cord (situation)"}],
        category="PREGNANCY",
        attributes={"code": "1208622001"},
    ),
    TargetRule(
        literal="History of short umbilical cord",
        pattern=[{"LOWER": "history of short umbilical cord"}],
        category="PREGNANCY",
        attributes={"code": "1208622001"},
    ),
    TargetRule(
        literal="Counseling for pregnancy",
        pattern=[{"LOWER": "counseling for pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "1230101008"},
    ),
    TargetRule(
        literal="Counseling for pregnancy (procedure)",
        pattern=[{"LOWER": "counseling for pregnancy (procedure)"}],
        category="PREGNANCY",
        attributes={"code": "1230101008"},
    ),
    TargetRule(
        literal="Counselling for pregnancy",
        pattern=[{"LOWER": "counselling for pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "1230101008"},
    ),
    TargetRule(
        literal="Pregnancy after cervical conization",
        pattern=[{"LOWER": "pregnancy after cervical conization"}],
        category="PREGNANCY",
        attributes={"code": "568141000005106"},
    ),
    TargetRule(
        literal="Pregnancy following cone biopsy of uterine cervix",
        pattern=[{"LOWER": "pregnancy following cone biopsy of uterine cervix"}],
        category="PREGNANCY",
        attributes={"code": "568141000005106"},
    ),
    TargetRule(
        literal="Pregnancy following cone biopsy of uterine cervix (finding)",
        pattern=[
            {"LOWER": "pregnancy following cone biopsy of uterine cervix (finding)"}
        ],
        category="PREGNANCY",
        attributes={"code": "568141000005106"},
    ),
    TargetRule(
        literal="Pregnancy after cervical conisation",
        pattern=[{"LOWER": "pregnancy after cervical conisation"}],
        category="PREGNANCY",
        attributes={"code": "568141000005106"},
    ),
    TargetRule(
        literal="Multiple pregnancy (finding)",
        pattern=[{"LOWER": "multiple pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "16356006"},
    ),
    TargetRule(
        literal="Glucose in blood 1 hour after glucose dose in pregnancy",
        pattern=[{"LOWER": "glucose in blood 1 hour after glucose dose in pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "372731000119106"},
    ),
    TargetRule(
        literal="Glucose in blood one hour after glucose dose in pregnancy",
        pattern=[
            {"LOWER": "glucose in blood one hour after glucose dose in pregnancy"}
        ],
        category="PREGNANCY",
        attributes={"code": "372731000119106"},
    ),
    TargetRule(
        literal="Glucose in blood one hour after glucose dose in pregnancy (observable entity)",
        pattern=[
            {
                "LOWER": "glucose in blood one hour after glucose dose in pregnancy (observable entity)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "372731000119106"},
    ),
    TargetRule(
        literal="Past pregnancy history of perinatal death (situation)",
        pattern=[{"LOWER": "past pregnancy history of perinatal death (situation)"}],
        category="PREGNANCY",
        attributes={"code": "1290143004"},
    ),
    TargetRule(
        literal="Past pregnancy history of perinatal death",
        pattern=[{"LOWER": "past pregnancy history of perinatal death"}],
        category="PREGNANCY",
        attributes={"code": "1290143004"},
    ),
    TargetRule(
        literal="Singleton pregnancy",
        pattern=[{"LOWER": "singleton pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "1290152008"},
    ),
    TargetRule(
        literal="Singleton pregnancy (finding)",
        pattern=[{"LOWER": "singleton pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "1290152008"},
    ),
    TargetRule(
        literal="Past pregnancy history of stillbirth (situation)",
        pattern=[{"LOWER": "past pregnancy history of stillbirth (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161743003"},
    ),
    TargetRule(
        literal="Past pregnancy history of stillbirth",
        pattern=[{"LOWER": "past pregnancy history of stillbirth"}],
        category="PREGNANCY",
        attributes={"code": "161743003"},
    ),
    TargetRule(
        literal="Past pregnancy history of ectopic pregnancy (situation)",
        pattern=[{"LOWER": "past pregnancy history of ectopic pregnancy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161763005"},
    ),
    TargetRule(
        literal="Past pregnancy history of ectopic pregnancy",
        pattern=[{"LOWER": "past pregnancy history of ectopic pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "161763005"},
    ),
    TargetRule(
        literal="Past pregnancy history of premature delivery (situation)",
        pattern=[{"LOWER": "past pregnancy history of premature delivery (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161765003"},
    ),
    TargetRule(
        literal="Past pregnancy history of premature delivery",
        pattern=[{"LOWER": "past pregnancy history of premature delivery"}],
        category="PREGNANCY",
        attributes={"code": "161765003"},
    ),
    TargetRule(
        literal="Past pregnancy history of antepartum haemorrhage",
        pattern=[{"LOWER": "past pregnancy history of antepartum haemorrhage"}],
        category="PREGNANCY",
        attributes={"code": "161804005"},
    ),
    TargetRule(
        literal="Past pregnancy history of antepartum hemorrhage (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of antepartum hemorrhage (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "161804005"},
    ),
    TargetRule(
        literal="Past pregnancy history of antepartum hemorrhage",
        pattern=[{"LOWER": "past pregnancy history of antepartum hemorrhage"}],
        category="PREGNANCY",
        attributes={"code": "161804005"},
    ),
    TargetRule(
        literal="Past pregnancy history of prolonged labor",
        pattern=[{"LOWER": "past pregnancy history of prolonged labor"}],
        category="PREGNANCY",
        attributes={"code": "161810005"},
    ),
    TargetRule(
        literal="Past pregnancy history of prolonged labour",
        pattern=[{"LOWER": "past pregnancy history of prolonged labour"}],
        category="PREGNANCY",
        attributes={"code": "161810005"},
    ),
    TargetRule(
        literal="Past pregnancy history of prolonged labor (situation)",
        pattern=[{"LOWER": "past pregnancy history of prolonged labor (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161810005"},
    ),
    TargetRule(
        literal="Past pregnancy history of full term delivery (situation)",
        pattern=[{"LOWER": "past pregnancy history of full term delivery (situation)"}],
        category="PREGNANCY",
        attributes={"code": "267015005"},
    ),
    TargetRule(
        literal="Past pregnancy history of full term delivery",
        pattern=[{"LOWER": "past pregnancy history of full term delivery"}],
        category="PREGNANCY",
        attributes={"code": "267015005"},
    ),
    TargetRule(
        literal="Past pregnancy history of premature labor (situation)",
        pattern=[{"LOWER": "past pregnancy history of premature labor (situation)"}],
        category="PREGNANCY",
        attributes={"code": "441493008"},
    ),
    TargetRule(
        literal="Past pregnancy history of premature labor",
        pattern=[{"LOWER": "past pregnancy history of premature labor"}],
        category="PREGNANCY",
        attributes={"code": "441493008"},
    ),
    TargetRule(
        literal="Past pregnancy history of premature labour",
        pattern=[{"LOWER": "past pregnancy history of premature labour"}],
        category="PREGNANCY",
        attributes={"code": "441493008"},
    ),
    TargetRule(
        literal="Past pregnancy history of live birth (situation)",
        pattern=[{"LOWER": "past pregnancy history of live birth (situation)"}],
        category="PREGNANCY",
        attributes={"code": "726001007"},
    ),
    TargetRule(
        literal="Past pregnancy history of live birth",
        pattern=[{"LOWER": "past pregnancy history of live birth"}],
        category="PREGNANCY",
        attributes={"code": "726001007"},
    ),
    TargetRule(
        literal="Past pregnancy history of small for gestational age baby (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of small for gestational age baby (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "726565008"},
    ),
    TargetRule(
        literal="Past pregnancy history of small for gestational age baby",
        pattern=[{"LOWER": "past pregnancy history of small for gestational age baby"}],
        category="PREGNANCY",
        attributes={"code": "726565008"},
    ),
    TargetRule(
        literal="Past pregnancy history of induced onset of labor",
        pattern=[{"LOWER": "past pregnancy history of induced onset of labor"}],
        category="PREGNANCY",
        attributes={"code": "725954003"},
    ),
    TargetRule(
        literal="Past pregnancy history of induced onset of labor (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of induced onset of labor (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "725954003"},
    ),
    TargetRule(
        literal="Past pregnancy history of induced onset of labour",
        pattern=[{"LOWER": "past pregnancy history of induced onset of labour"}],
        category="PREGNANCY",
        attributes={"code": "725954003"},
    ),
    TargetRule(
        literal="Past pregnancy history of cholestasis in pregnancy (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of cholestasis in pregnancy (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "16216781000119107"},
    ),
    TargetRule(
        literal="Past pregnancy history of cholestasis in pregnancy",
        pattern=[{"LOWER": "past pregnancy history of cholestasis in pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "16216781000119107"},
    ),
    TargetRule(
        literal="Past pregnancy history of molar pregnancy",
        pattern=[{"LOWER": "past pregnancy history of molar pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "16216821000119102"},
    ),
    TargetRule(
        literal="Past pregnancy history of molar pregnancy (situation)",
        pattern=[{"LOWER": "past pregnancy history of molar pregnancy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "16216821000119102"},
    ),
    TargetRule(
        literal="Past pregnancy history of pregnancy with abortive outcome (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of pregnancy with abortive outcome (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "713651007"},
    ),
    TargetRule(
        literal="Past pregnancy history of pregnancy with abortive outcome",
        pattern=[
            {"LOWER": "past pregnancy history of pregnancy with abortive outcome"}
        ],
        category="PREGNANCY",
        attributes={"code": "713651007"},
    ),
    TargetRule(
        literal="Past pregnancy history of induced termination of pregnancy (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of induced termination of pregnancy (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "713649008"},
    ),
    TargetRule(
        literal="Past pregnancy history of induced termination of pregnancy",
        pattern=[
            {"LOWER": "past pregnancy history of induced termination of pregnancy"}
        ],
        category="PREGNANCY",
        attributes={"code": "713649008"},
    ),
    TargetRule(
        literal="Past pregnancy history of pregnancy with normal glucose tolerance test (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of pregnancy with normal glucose tolerance test (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "1156101005"},
    ),
    TargetRule(
        literal="Past pregnancy history of pregnancy with normal glucose tolerance test",
        pattern=[
            {
                "LOWER": "past pregnancy history of pregnancy with normal glucose tolerance test"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "1156101005"},
    ),
    TargetRule(
        literal="Past pregnancy history of complication of pregnancy, childbirth and/or puerperium (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of complication of pregnancy, childbirth and/or puerperium (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "450891000124109"},
    ),
    TargetRule(
        literal="Past pregnancy history of complication of pregnancy, childbirth and/or puerperium",
        pattern=[
            {
                "LOWER": "past pregnancy history of complication of pregnancy, childbirth and/or puerperium"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "450891000124109"},
    ),
    TargetRule(
        literal="Past pregnancy history of medical termination of pregnancy (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of medical termination of pregnancy (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "412758008"},
    ),
    TargetRule(
        literal="Past pregnancy history of medical termination of pregnancy",
        pattern=[
            {"LOWER": "past pregnancy history of medical termination of pregnancy"}
        ],
        category="PREGNANCY",
        attributes={"code": "412758008"},
    ),
    TargetRule(
        literal="Past pregnancy history of miscarriage (situation)",
        pattern=[{"LOWER": "past pregnancy history of miscarriage (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161744009"},
    ),
    TargetRule(
        literal="Past pregnancy history of miscarriage",
        pattern=[{"LOWER": "past pregnancy history of miscarriage"}],
        category="PREGNANCY",
        attributes={"code": "161744009"},
    ),
    TargetRule(
        literal="Past pregnancy history of choriocarcinoma of placenta (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of choriocarcinoma of placenta (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "428978004"},
    ),
    TargetRule(
        literal="Past pregnancy history of choriocarcinoma of placenta",
        pattern=[{"LOWER": "past pregnancy history of choriocarcinoma of placenta"}],
        category="PREGNANCY",
        attributes={"code": "428978004"},
    ),
    TargetRule(
        literal="Past pregnancy history of complication occurring during labor and delivery (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of complication occurring during labor and delivery (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "1156096005"},
    ),
    TargetRule(
        literal="Past pregnancy history of complication occurring during labor and delivery",
        pattern=[
            {
                "LOWER": "past pregnancy history of complication occurring during labor and delivery"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "1156096005"},
    ),
    TargetRule(
        literal="Past pregnancy history of complication occurring during labour and delivery",
        pattern=[
            {
                "LOWER": "past pregnancy history of complication occurring during labour and delivery"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "1156096005"},
    ),
    TargetRule(
        literal="Past pregnancy history of complication of puerperium (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of complication of puerperium (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "1156097001"},
    ),
    TargetRule(
        literal="Past pregnancy history of complication of puerperium",
        pattern=[{"LOWER": "past pregnancy history of complication of puerperium"}],
        category="PREGNANCY",
        attributes={"code": "1156097001"},
    ),
    TargetRule(
        literal="Past pregnancy history of fourth degree perineal laceration",
        pattern=[
            {"LOWER": "past pregnancy history of fourth degree perineal laceration"}
        ],
        category="PREGNANCY",
        attributes={"code": "725942003"},
    ),
    TargetRule(
        literal="Past pregnancy history of fourth degree perineal laceration (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of fourth degree perineal laceration (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "725942003"},
    ),
    TargetRule(
        literal="Past pregnancy history of second degree perineal laceration",
        pattern=[
            {"LOWER": "past pregnancy history of second degree perineal laceration"}
        ],
        category="PREGNANCY",
        attributes={"code": "725943008"},
    ),
    TargetRule(
        literal="Past pregnancy history of second degree perineal laceration (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of second degree perineal laceration (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "725943008"},
    ),
    TargetRule(
        literal="Past pregnancy history of shoulder dystocia",
        pattern=[{"LOWER": "past pregnancy history of shoulder dystocia"}],
        category="PREGNANCY",
        attributes={"code": "816150000"},
    ),
    TargetRule(
        literal="Past pregnancy history of shoulder dystocia (situation)",
        pattern=[{"LOWER": "past pregnancy history of shoulder dystocia (situation)"}],
        category="PREGNANCY",
        attributes={"code": "816150000"},
    ),
    TargetRule(
        literal="Past pregnancy history of third degree perineal laceration",
        pattern=[
            {"LOWER": "past pregnancy history of third degree perineal laceration"}
        ],
        category="PREGNANCY",
        attributes={"code": "725941005"},
    ),
    TargetRule(
        literal="Past pregnancy history of third degree perineal laceration (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of third degree perineal laceration (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "725941005"},
    ),
    TargetRule(
        literal="Past pregnancy history of first degree perineal laceration (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of first degree perineal laceration (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "726625000"},
    ),
    TargetRule(
        literal="Past pregnancy history of first degree perineal laceration",
        pattern=[
            {"LOWER": "past pregnancy history of first degree perineal laceration"}
        ],
        category="PREGNANCY",
        attributes={"code": "726625000"},
    ),
    TargetRule(
        literal="Past pregnancy history of postpartum gestational hypertension",
        pattern=[
            {"LOWER": "past pregnancy history of postpartum gestational hypertension"}
        ],
        category="PREGNANCY",
        attributes={"code": "16916061000119102"},
    ),
    TargetRule(
        literal="Past pregnancy history of postpartum gestational hypertension (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of postpartum gestational hypertension (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "16916061000119102"},
    ),
    TargetRule(
        literal="Past pregnancy history of postpartum haemorrhage",
        pattern=[{"LOWER": "past pregnancy history of postpartum haemorrhage"}],
        category="PREGNANCY",
        attributes={"code": "161809000"},
    ),
    TargetRule(
        literal="Past pregnancy history of postpartum hemorrhage (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of postpartum hemorrhage (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "161809000"},
    ),
    TargetRule(
        literal="Past pregnancy history of postpartum hemorrhage",
        pattern=[{"LOWER": "past pregnancy history of postpartum hemorrhage"}],
        category="PREGNANCY",
        attributes={"code": "161809000"},
    ),
    TargetRule(
        literal="Past pregnancy history of postpartum psychosis (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of postpartum psychosis (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "726623007"},
    ),
    TargetRule(
        literal="Past pregnancy history of postpartum psychosis",
        pattern=[{"LOWER": "past pregnancy history of postpartum psychosis"}],
        category="PREGNANCY",
        attributes={"code": "726623007"},
    ),
    TargetRule(
        literal="Past pregnancy history of retained placenta (situation)",
        pattern=[{"LOWER": "past pregnancy history of retained placenta (situation)"}],
        category="PREGNANCY",
        attributes={"code": "725948004"},
    ),
    TargetRule(
        literal="Past pregnancy history of retained placenta",
        pattern=[{"LOWER": "past pregnancy history of retained placenta"}],
        category="PREGNANCY",
        attributes={"code": "725948004"},
    ),
    TargetRule(
        literal="Past pregnancy history of Rhesus isoimmunization affecting pregnancy (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of rhesus isoimmunization affecting pregnancy (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "1156098006"},
    ),
    TargetRule(
        literal="Past pregnancy history of Rhesus isoimmunization affecting pregnancy",
        pattern=[
            {
                "LOWER": "past pregnancy history of rhesus isoimmunization affecting pregnancy"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "1156098006"},
    ),
    TargetRule(
        literal="Past pregnancy history of Rhesus isoimmunisation affecting pregnancy",
        pattern=[
            {
                "LOWER": "past pregnancy history of rhesus isoimmunisation affecting pregnancy"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "1156098006"},
    ),
    TargetRule(
        literal="Past pregnancy history of pregnancy with abnormal glucose tolerance test",
        pattern=[
            {
                "LOWER": "past pregnancy history of pregnancy with abnormal glucose tolerance test"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "1156099003"},
    ),
    TargetRule(
        literal="Past pregnancy history of pregnancy with abnormal glucose tolerance test (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of pregnancy with abnormal glucose tolerance test (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "1156099003"},
    ),
    TargetRule(
        literal="Past pregnancy history of delivery of macrosomal infant (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of delivery of macrosomal infant (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "32271000119102"},
    ),
    TargetRule(
        literal="Past pregnancy history of delivery of macrosomal infant",
        pattern=[{"LOWER": "past pregnancy history of delivery of macrosomal infant"}],
        category="PREGNANCY",
        attributes={"code": "32271000119102"},
    ),
    TargetRule(
        literal="Past pregnancy history of intrauterine fetal death (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of intrauterine fetal death (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "16216731000119106"},
    ),
    TargetRule(
        literal="Past pregnancy history of intrauterine foetal death",
        pattern=[{"LOWER": "past pregnancy history of intrauterine foetal death"}],
        category="PREGNANCY",
        attributes={"code": "16216731000119106"},
    ),
    TargetRule(
        literal="Past pregnancy history of intrauterine fetal death",
        pattern=[{"LOWER": "past pregnancy history of intrauterine fetal death"}],
        category="PREGNANCY",
        attributes={"code": "16216731000119106"},
    ),
    TargetRule(
        literal="Past pregnancy history of spontaneous onset of labor",
        pattern=[{"LOWER": "past pregnancy history of spontaneous onset of labor"}],
        category="PREGNANCY",
        attributes={"code": "726597008"},
    ),
    TargetRule(
        literal="Past pregnancy history of spontaneous onset of labor (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of spontaneous onset of labor (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "726597008"},
    ),
    TargetRule(
        literal="Past pregnancy history of spontaneous onset of labour",
        pattern=[{"LOWER": "past pregnancy history of spontaneous onset of labour"}],
        category="PREGNANCY",
        attributes={"code": "726597008"},
    ),
    TargetRule(
        literal="Past pregnancy history of normal delivery",
        pattern=[{"LOWER": "past pregnancy history of normal delivery"}],
        category="PREGNANCY",
        attributes={"code": "275568006"},
    ),
    TargetRule(
        literal="Past pregnancy history of normal delivery (situation)",
        pattern=[{"LOWER": "past pregnancy history of normal delivery (situation)"}],
        category="PREGNANCY",
        attributes={"code": "275568006"},
    ),
    TargetRule(
        literal="Past pregnancy history of previous delivery by vacuum extraction (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of previous delivery by vacuum extraction (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "726624001"},
    ),
    TargetRule(
        literal="Past pregnancy history of previous delivery by vacuum extraction",
        pattern=[
            {
                "LOWER": "past pregnancy history of previous delivery by vacuum extraction"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "726624001"},
    ),
    TargetRule(
        literal="Past pregnancy history of defibulation of vulva to facilitate delivery",
        pattern=[
            {
                "LOWER": "past pregnancy history of defibulation of vulva to facilitate delivery"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "719594003"},
    ),
    TargetRule(
        literal="Past pregnancy history of defibulation of vulva to facilitate delivery (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of defibulation of vulva to facilitate delivery (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "719594003"},
    ),
    TargetRule(
        literal="Past pregnancy history of delivery with no details (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of delivery with no details (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "275569003"},
    ),
    TargetRule(
        literal="Past pregnancy history of delivery with no details",
        pattern=[{"LOWER": "past pregnancy history of delivery with no details"}],
        category="PREGNANCY",
        attributes={"code": "275569003"},
    ),
    TargetRule(
        literal="Past pregnancy history of induced termination of pregnancy under unsafe conditions (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of induced termination of pregnancy under unsafe conditions (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "697994009"},
    ),
    TargetRule(
        literal="Past pregnancy history of induced termination of pregnancy under unsafe conditions",
        pattern=[
            {
                "LOWER": "past pregnancy history of induced termination of pregnancy under unsafe conditions"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "697994009"},
    ),
    TargetRule(
        literal="Past pregnancy history of previous forceps delivery (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of previous forceps delivery (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "161813007"},
    ),
    TargetRule(
        literal="Past pregnancy history of previous forceps delivery",
        pattern=[{"LOWER": "past pregnancy history of previous forceps delivery"}],
        category="PREGNANCY",
        attributes={"code": "161813007"},
    ),
    TargetRule(
        literal="Past pregnancy history of cesarean section (situation)",
        pattern=[{"LOWER": "past pregnancy history of cesarean section (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161805006"},
    ),
    TargetRule(
        literal="Past pregnancy history of caesarean section",
        pattern=[{"LOWER": "past pregnancy history of caesarean section"}],
        category="PREGNANCY",
        attributes={"code": "161805006"},
    ),
    TargetRule(
        literal="Past pregnancy history of cesarean section",
        pattern=[{"LOWER": "past pregnancy history of cesarean section"}],
        category="PREGNANCY",
        attributes={"code": "161805006"},
    ),
    TargetRule(
        literal="Past pregnancy history of elective cesarean section (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of elective cesarean section (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "725949007"},
    ),
    TargetRule(
        literal="Past pregnancy history of elective caesarean section",
        pattern=[{"LOWER": "past pregnancy history of elective caesarean section"}],
        category="PREGNANCY",
        attributes={"code": "725949007"},
    ),
    TargetRule(
        literal="Past pregnancy history of elective cesarean section",
        pattern=[{"LOWER": "past pregnancy history of elective cesarean section"}],
        category="PREGNANCY",
        attributes={"code": "725949007"},
    ),
    TargetRule(
        literal="Past pregnancy history of emergency caesarean section",
        pattern=[{"LOWER": "past pregnancy history of emergency caesarean section"}],
        category="PREGNANCY",
        attributes={"code": "725951006"},
    ),
    TargetRule(
        literal="Past pregnancy history of emergency cesarean section (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of emergency cesarean section (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "725951006"},
    ),
    TargetRule(
        literal="Past pregnancy history of emergency cesarean section",
        pattern=[{"LOWER": "past pregnancy history of emergency cesarean section"}],
        category="PREGNANCY",
        attributes={"code": "725951006"},
    ),
    TargetRule(
        literal="Past pregnancy history of episiotomy (situation)",
        pattern=[{"LOWER": "past pregnancy history of episiotomy (situation)"}],
        category="PREGNANCY",
        attributes={"code": "725944002"},
    ),
    TargetRule(
        literal="Past pregnancy history of episiotomy",
        pattern=[{"LOWER": "past pregnancy history of episiotomy"}],
        category="PREGNANCY",
        attributes={"code": "725944002"},
    ),
    TargetRule(
        literal="Past pregnancy history of neonatal death",
        pattern=[{"LOWER": "past pregnancy history of neonatal death"}],
        category="PREGNANCY",
        attributes={"code": "1290167007"},
    ),
    TargetRule(
        literal="Past pregnancy history of neonatal death (situation)",
        pattern=[{"LOWER": "past pregnancy history of neonatal death (situation)"}],
        category="PREGNANCY",
        attributes={"code": "1290167007"},
    ),
    TargetRule(
        literal="Past pregnancy history of gestational diabetes mellitus",
        pattern=[{"LOWER": "past pregnancy history of gestational diabetes mellitus"}],
        category="PREGNANCY",
        attributes={"code": "472971004"},
    ),
    TargetRule(
        literal="Past pregnancy history of gestational diabetes mellitus (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of gestational diabetes mellitus (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "472971004"},
    ),
    TargetRule(
        literal="Past pregnancy history of eclampsia",
        pattern=[{"LOWER": "past pregnancy history of eclampsia"}],
        category="PREGNANCY",
        attributes={"code": "161806007"},
    ),
    TargetRule(
        literal="Past pregnancy history of eclampsia (situation)",
        pattern=[{"LOWER": "past pregnancy history of eclampsia (situation)"}],
        category="PREGNANCY",
        attributes={"code": "161806007"},
    ),
    TargetRule(
        literal="Past pregnancy history of gestational trophoblastic disease (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of gestational trophoblastic disease (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "736725001"},
    ),
    TargetRule(
        literal="Past pregnancy history of gestational trophoblastic disease",
        pattern=[
            {"LOWER": "past pregnancy history of gestational trophoblastic disease"}
        ],
        category="PREGNANCY",
        attributes={"code": "736725001"},
    ),
    TargetRule(
        literal="Past pregnancy history of gestational hypertension (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of gestational hypertension (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "709881001"},
    ),
    TargetRule(
        literal="Past pregnancy history of gestational hypertension",
        pattern=[{"LOWER": "past pregnancy history of gestational hypertension"}],
        category="PREGNANCY",
        attributes={"code": "709881001"},
    ),
    TargetRule(
        literal="Past pregnancy history of placenta accreta",
        pattern=[{"LOWER": "past pregnancy history of placenta accreta"}],
        category="PREGNANCY",
        attributes={"code": "725950007"},
    ),
    TargetRule(
        literal="Past pregnancy history of placenta accreta (situation)",
        pattern=[{"LOWER": "past pregnancy history of placenta accreta (situation)"}],
        category="PREGNANCY",
        attributes={"code": "725950007"},
    ),
    TargetRule(
        literal="Past pregnancy history of pre-eclampsia (situation)",
        pattern=[{"LOWER": "past pregnancy history of pre-eclampsia (situation)"}],
        category="PREGNANCY",
        attributes={"code": "105651000119100"},
    ),
    TargetRule(
        literal="Past pregnancy history of pre-eclampsia",
        pattern=[{"LOWER": "past pregnancy history of pre-eclampsia"}],
        category="PREGNANCY",
        attributes={"code": "105651000119100"},
    ),
    TargetRule(
        literal="Past pregnancy history of severe pre-eclampsia (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of severe pre-eclampsia (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "161807003"},
    ),
    TargetRule(
        literal="Past pregnancy history of severe pre-eclampsia",
        pattern=[{"LOWER": "past pregnancy history of severe pre-eclampsia"}],
        category="PREGNANCY",
        attributes={"code": "161807003"},
    ),
    TargetRule(
        literal="Past pregnancy history of hemolysis-elevated liver enzymes-low platelet count syndrome (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of hemolysis-elevated liver enzymes-low platelet count syndrome (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "726513006"},
    ),
    TargetRule(
        literal="Past pregnancy history of hemolysis-elevated liver enzymes-low platelet count syndrome",
        pattern=[
            {
                "LOWER": "past pregnancy history of hemolysis-elevated liver enzymes-low platelet count syndrome"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "726513006"},
    ),
    TargetRule(
        literal="Past pregnancy history of haemolysis-elevated liver enzymes-low platelet count syndrome",
        pattern=[
            {
                "LOWER": "past pregnancy history of haemolysis-elevated liver enzymes-low platelet count syndrome"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "726513006"},
    ),
    TargetRule(
        literal="Past pregnancy history of placental abruption (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of placental abruption (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "789776003"},
    ),
    TargetRule(
        literal="Past pregnancy history of placental abruption",
        pattern=[{"LOWER": "past pregnancy history of placental abruption"}],
        category="PREGNANCY",
        attributes={"code": "789776003"},
    ),
    TargetRule(
        literal="Past pregnancy history of preterm premature rupture of membranes (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of preterm premature rupture of membranes (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "108951000119100"},
    ),
    TargetRule(
        literal="Past pregnancy history of preterm premature rupture of membranes",
        pattern=[
            {
                "LOWER": "past pregnancy history of preterm premature rupture of membranes"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "108951000119100"},
    ),
    TargetRule(
        literal="Past pregnancy history of short umbilical cord (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of short umbilical cord (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "1208622001"},
    ),
    TargetRule(
        literal="Past pregnancy history of short umbilical cord",
        pattern=[{"LOWER": "past pregnancy history of short umbilical cord"}],
        category="PREGNANCY",
        attributes={"code": "1208622001"},
    ),
    TargetRule(
        literal="Past pregnancy history of placenta previa (situation)",
        pattern=[{"LOWER": "past pregnancy history of placenta previa (situation)"}],
        category="PREGNANCY",
        attributes={"code": "725924008"},
    ),
    TargetRule(
        literal="Past pregnancy history of placenta praevia",
        pattern=[{"LOWER": "past pregnancy history of placenta praevia"}],
        category="PREGNANCY",
        attributes={"code": "725924008"},
    ),
    TargetRule(
        literal="Past pregnancy history of placenta previa",
        pattern=[{"LOWER": "past pregnancy history of placenta previa"}],
        category="PREGNANCY",
        attributes={"code": "725924008"},
    ),
    TargetRule(
        literal="Past pregnancy history of pregnancy loss in non-pregnant woman (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of pregnancy loss in non-pregnant woman (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "15011000119104"},
    ),
    TargetRule(
        literal="Past pregnancy history of pregnancy loss in non-pregnant woman",
        pattern=[
            {"LOWER": "past pregnancy history of pregnancy loss in non-pregnant woman"}
        ],
        category="PREGNANCY",
        attributes={"code": "15011000119104"},
    ),
    TargetRule(
        literal="Past pregnancy history of fetal growth restriction (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of fetal growth restriction (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "733899004"},
    ),
    TargetRule(
        literal="Past pregnancy history of fetal growth restriction",
        pattern=[{"LOWER": "past pregnancy history of fetal growth restriction"}],
        category="PREGNANCY",
        attributes={"code": "733899004"},
    ),
    TargetRule(
        literal="Past pregnancy history of early neonatal death",
        pattern=[{"LOWER": "past pregnancy history of early neonatal death"}],
        category="PREGNANCY",
        attributes={"code": "1290170006"},
    ),
    TargetRule(
        literal="Past pregnancy history of early neonatal death (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of early neonatal death (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "1290170006"},
    ),
    TargetRule(
        literal="Past pregnancy history of late neonatal death",
        pattern=[{"LOWER": "past pregnancy history of late neonatal death"}],
        category="PREGNANCY",
        attributes={"code": "1290171005"},
    ),
    TargetRule(
        literal="Past pregnancy history of late neonatal death (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of late neonatal death (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "1290171005"},
    ),
    TargetRule(
        literal="Shared antenatal care (regime/therapy)",
        pattern=[{"LOWER": "shared antenatal care (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "1290175001"},
    ),
    TargetRule(
        literal="Shared antenatal care",
        pattern=[{"LOWER": "shared antenatal care"}],
        category="PREGNANCY",
        attributes={"code": "1290175001"},
    ),
    TargetRule(
        literal="Hospital antenatal care (regime/therapy)",
        pattern=[{"LOWER": "hospital antenatal care (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "1290176000"},
    ),
    TargetRule(
        literal="Hospital antenatal care",
        pattern=[{"LOWER": "hospital antenatal care"}],
        category="PREGNANCY",
        attributes={"code": "1290176000"},
    ),
    TargetRule(
        literal="Midwifery led antenatal care (regime/therapy)",
        pattern=[{"LOWER": "midwifery led antenatal care (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "1290177009"},
    ),
    TargetRule(
        literal="Midwifery led antenatal care",
        pattern=[{"LOWER": "midwifery led antenatal care"}],
        category="PREGNANCY",
        attributes={"code": "1290177009"},
    ),
    TargetRule(
        literal="General practitioner led antenatal care (regime/therapy)",
        pattern=[{"LOWER": "general practitioner led antenatal care (regime/therapy)"}],
        category="PREGNANCY",
        attributes={"code": "1290178004"},
    ),
    TargetRule(
        literal="General practitioner led antenatal care",
        pattern=[{"LOWER": "general practitioner led antenatal care"}],
        category="PREGNANCY",
        attributes={"code": "1290178004"},
    ),
    TargetRule(
        literal="Past pregnancy history of recurrent miscarriage (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of recurrent miscarriage (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "1290209002"},
    ),
    TargetRule(
        literal="Past pregnancy history of recurrent miscarriage",
        pattern=[{"LOWER": "past pregnancy history of recurrent miscarriage"}],
        category="PREGNANCY",
        attributes={"code": "1290209002"},
    ),
    TargetRule(
        literal="Past pregnancy history of multiple miscarriages",
        pattern=[{"LOWER": "past pregnancy history of multiple miscarriages"}],
        category="PREGNANCY",
        attributes={"code": "1290210007"},
    ),
    TargetRule(
        literal="Past pregnancy history of multiple miscarriages (situation)",
        pattern=[
            {"LOWER": "past pregnancy history of multiple miscarriages (situation)"}
        ],
        category="PREGNANCY",
        attributes={"code": "1290210007"},
    ),
    TargetRule(
        literal="Past pregnancy history of delivery procedure",
        pattern=[{"LOWER": "past pregnancy history of delivery procedure"}],
        category="PREGNANCY",
        attributes={"code": "272058002"},
    ),
    TargetRule(
        literal="Past pregnancy history of delivery procedure (situation)",
        pattern=[{"LOWER": "past pregnancy history of delivery procedure (situation)"}],
        category="PREGNANCY",
        attributes={"code": "272058002"},
    ),
    TargetRule(
        literal="Past pregnancy history of multiple induced termination of pregnancy",
        pattern=[
            {
                "LOWER": "past pregnancy history of multiple induced termination of pregnancy"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "1300163008"},
    ),
    TargetRule(
        literal="Past pregnancy history of multiple induced termination of pregnancy (situation)",
        pattern=[
            {
                "LOWER": "past pregnancy history of multiple induced termination of pregnancy (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "1300163008"},
    ),
    TargetRule(
        literal="History of multiple induced termination of pregnancy",
        pattern=[{"LOWER": "history of multiple induced termination of pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "1300163008"},
    ),
    TargetRule(
        literal="Pregnancy resulting from natural conception (finding)",
        pattern=[{"LOWER": "pregnancy resulting from natural conception (finding)"}],
        category="PREGNANCY",
        attributes={"code": "1300203003"},
    ),
    TargetRule(
        literal="Pregnancy resulting from natural conception",
        pattern=[{"LOWER": "pregnancy resulting from natural conception"}],
        category="PREGNANCY",
        attributes={"code": "1300203003"},
    ),
    TargetRule(
        literal="Medium risk pregnancy",
        pattern=[{"LOWER": "medium risk pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "1303255001"},
    ),
    TargetRule(
        literal="Medium risk pregnancy (finding)",
        pattern=[{"LOWER": "medium risk pregnancy (finding)"}],
        category="PREGNANCY",
        attributes={"code": "1303255001"},
    ),
    TargetRule(
        literal="HRP - high risk pregnancy",
        pattern=[{"LOWER": "hrp - high risk pregnancy"}],
        category="PREGNANCY",
        attributes={"code": "47200007"},
    ),
    TargetRule(
        literal="History of complication of pregnancy, childbirth and/or puerperium (situation)",
        pattern=[
            {
                "LOWER": "history of complication of pregnancy, childbirth and/or puerperium (situation)"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "450891000124109"},
    ),
    TargetRule(
        literal="History of complication of pregnancy, childbirth and/or puerperium",
        pattern=[
            {
                "LOWER": "history of complication of pregnancy, childbirth and/or puerperium"
            }
        ],
        category="PREGNANCY",
        attributes={"code": "450891000124109"},
    ),
    TargetRule(
        literal="Pregnancy resulting from assisted conception",
        pattern=[{"LOWER": "pregnancy resulting from assisted conception"}],
        category="PREGNANCY",
        attributes={"code": "813541000000100"},
    ),
    TargetRule(
        literal="Pregnancy resulting from assisted conception (finding)",
        pattern=[{"LOWER": "pregnancy resulting from assisted conception (finding)"}],
        category="PREGNANCY",
        attributes={"code": "813541000000100"},
    ),
]
