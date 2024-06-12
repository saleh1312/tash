import os
from pyarabic.araby import strip_harakat , strip_tashkeel, strip_diacritics,strip_tatweel,sentence_tokenize
import re
import string
import grapheme
import random


def remove_punctuation(text):
  translator = str.maketrans("", "", string.punctuation)
  x = text.translate(translator)
  return x




def extract_let_tash(sent):
    exp_tat = strip_tatweel(sent)
    exp_punc = remove_punctuation(exp_tat)
    exp_sps = re.sub(r'\s+', ' ', exp_punc)
    exp_nums = re.sub(r'\d+', '', exp_sps)
    exp_dot = re.sub(r'،', '', exp_nums)
    exp_grapheme=list( grapheme.graphemes(exp_dot) )
    let = [graph[0] for graph in exp_grapheme]
    tash = [graph[1:] if graph[1:] != "" else " " for graph in exp_grapheme]
    
    return let , tash




def sample_unique(data):
    samples_lets , sampled_tash = [] , []

    for sent in random.sample(data,4):
        let , tash = extract_let_tash(sent)
        samples_lets.extend(let)
        sampled_tash.extend(tash)
        
    u_samples_lets = list(set(samples_lets))
    u_sampled_tash = list(set(sampled_tash))
    
    return u_samples_lets , u_sampled_tash