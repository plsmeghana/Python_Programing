import string
count_dict={}
def frequency(sentence):
    no_punct = sentence.translate(str.maketrans('', '', string.punctuation))
    slist = no_punct.lower().split(' ')
    unique_words = set(slist)
    
    count_dict={}
    
    for i in unique_words:
        count_dict[i]= slist.count(i)
    return count_dict

sentence=input()
print(frequency(sentence))
