import Orange

data = Orange.data.Table("combination.basket")
rules = Orange.associate.AssociationRulesSparseInducer(data, support=0.25, confidence=0.5)

for r in rules:
    print "%.2f %.2f %s" % (r.support, r.confidence, r)