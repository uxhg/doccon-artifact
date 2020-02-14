import collections
import json
from typing import Set, List

from datalog.pred import HasFnFact, HasParamFact
from macros import CODE_FACTS_OUTPUT_DIR


def extractHASFUNCTIONFacts(lib, version, sentence) -> (List[str], Set[HasFnFact]):
    all_contracts, all_functions, _ = getAllContractsAndFunctionsAndParams(lib, version)
    sentence_facts: List[str] = []
    sentence_facts_dl: Set[HasFnFact] = set()
    for word in sentence.strip().split():
        word = word.replace('`', '')
        word = word.strip().strip('.').strip(',').strip('{').strip('}')
        if '.' in word:
            #print(word)
            contract_name = word.split('.')[0].strip('"').strip('\'')
            func_name = word.split('.')[1].strip('.').strip(',').strip(';').strip('"').strip('\'')
            #if contract_name not in all_contracts or func_name not in all_functions:
            if func_name not in all_functions:
                print(f"{func_name} is not in functions set")
                continue
            fact = 'CONTRACT,' + contract_name + ',HASFUNCTION,' + func_name
            if fact not in sentence_facts:
                sentence_facts.append(fact)
            # add HasFn/2 fact
            sentence_facts_dl.add(HasFnFact(contract_name, func_name))
    return sentence_facts, sentence_facts_dl


def extractHASPARAMFacts(lib, version, sentence, ct, fn) -> (List[str], Set[HasParamFact]):
    _, all_functions, all_params = getAllContractsAndFunctionsAndParams(lib, version)
    dl_facts = set()
    sentence_facts = list()
    words = [word.strip('.').strip(',') for word in sentence.strip().split()]
    keywords = []
    for i in range(len(words)):
        if words[i][0] == words[i][-1] == '`':
            if i > 0 and words[i-1] == "member": # member var of class, not param
                continue
            keywords.append(words[i].strip('`'))
    for kw in keywords:
        #print(kw)
        if kw not in all_params:
            continue
        fact = 'FUNCTION,PLACEHOLDER,HASPARAM,' + kw
        dl_facts.add(HasParamFact(ct, fn, kw))
        if fact not in sentence_facts:
            sentence_facts.append(fact)
    return sentence_facts, dl_facts

def getAllContractsAndFunctionsAndParams(lib, version):
    all_contracts, all_functions, all_params = [], [], []
    function_params_info_json = CODE_FACTS_OUTPUT_DIR + '/' + lib + '/' + version + '/contracts.json'
    with open(function_params_info_json, 'r') as fr:
        function_params_info = json.load(fr, object_pairs_hook=collections.OrderedDict)
    for fqn in function_params_info:
        contract_name = fqn.split('.')[0]
        function_name = fqn.split('.')[-1]
        if contract_name not in all_contracts:
            all_contracts.append(contract_name)
        if function_name not in all_functions:
            all_functions.append(function_name)
        for param in function_params_info[fqn]:
            if param not in all_params:
                all_params.append(param)
    return all_contracts, all_functions, all_params
