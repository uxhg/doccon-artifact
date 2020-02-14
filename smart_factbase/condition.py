
def parseConditionSentence(sentence):
    res = ''
    if 'is empty' in sentence:  # template 8
        var = sentence.split('is empty')[0].split()[-1]
        res += 'empty(' + var + ')'
    else:
        res += sentence.replace(' ', '_')
    return res
