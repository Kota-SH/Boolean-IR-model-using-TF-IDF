# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 20:29:34 2019

@author: Haripriya K S
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 10:43:25 2019

@author: Haripriya K S
"""

import sys
import re
import operator
temp_postings=0
count_temp=0

def mergePostingListAND(list1, list2):
    mergeResult = list(set(list1) & set(list2))
    mergeResult.sort()
    i=j=0
    count=0
    while(i<len(list1) and j<len(list2)):
        if list1[i] < list2[j]:
            i+=1
            count+=1
        elif(list1[i]==list2[j]):
            i+=1
            j+=1
            count+=1
        else: 
            j+=1
            count+=1
    return mergeResult,count

def mergePostingListOR(list1, list2):
    mergeResult = list(set(list1) | set(list2))
    mergeResult.sort()
    i=j=0
    count=0
    while(i<len(list1) and j<len(list2)):
        if list1[i] < list2[j]:
            i+=1
            count+=1
        elif(list1[i]==list2[j]):
            i+=1
            j+=1
            count+=1
        else: 
            j+=1
            count+=1
    return mergeResult,count

def DaatAnd(query_list):
    print('DaatAnd')
    for i in range(0,len(query_list)):
        if(i!=len(query_list)-1):
            print(query_list[i],"",end="")
        else:
            print(query_list[i])
    if len(query_list) == 0:
        return None
    if len(query_list) == 1:
        result_list = posting_dictionary[query_list[0]]
        
    else:
        result_list = []
        comparision=0
        #print(query_list)
        for i in range(1, len(query_list)):
            if (len(result_list) == 0):
                result_list,count = mergePostingListAND(posting_dictionary[query_list[0]], posting_dictionary[query_list[i]])
            else:
                result_list,count = mergePostingListAND(result_list, posting_dictionary[query_list[i]])
            comparision+=count
        #print(comparision)
        #print(result_list)
        if(len(result_list)==0):
            print('Results: empty')
        else:
            print('Results: ',end="")
            for i in range(0,len(result_list)):
                if(i!=len(result_list)-1):
                    print(result_list[i],"",end="")
                else:
                    print(result_list[i])
        print('Number of documents in results:',len(result_list))
        print('Number of comparisons:',comparision)
        tfidf_AND(result_list,query_list)

def DaatOr(query_list):
    print('DaatOr')
    for i in range(0,len(query_list)):
        if(i!=len(query_list)-1):
            print(query_list[i],"",end="")
        else:
            print(query_list[i])    
    if len(query_list) == 0:
        return None
    if len(query_list) == 1:
        result_list = posting_dictionary[query_list[0]]
        
    else:
        result_list = []
        comparision=0
        #print(query_list)
        for i in range(1, len(query_list)):
            if (len(result_list) == 0):
                result_list,count = mergePostingListOR(posting_dictionary[query_list[0]], posting_dictionary[query_list[i]])
            else:
                result_list,count = mergePostingListOR(result_list, posting_dictionary[query_list[i]])
            comparision+=count
        #print(comparision)
        #print(result_list)
        if(len(result_list)==0):
            print('Results: empty')
        else:
            print('Results: ',end="")
            for i in range(0,len(result_list)):
                if(i!=len(result_list)-1):
                    print(result_list[i],"",end="")
                else:
                    print(result_list[i])
        print('Number of documents in results:',len(result_list))
        print('Number of comparisons:',comparision)
        tfidf_OR(result_list,query_list)

def tfidf_AND(docs,terms):
    print('TF-IDF')
    if(len(docs)==0):
        print('Results: empty')
    else:
        tfidf_sorted_dictionary={}
        for i in docs:
            count=0
            for j in terms:
                count+=tf_idf_pre_dictionary[i+'_'+j]
            tfidf_words=len(words_list[i])
            tfidf_sorted_dictionary.update({i:((count/tfidf_words)*(len(words_list)/len(docs)))})
        sorted_dictionary=sorted(tfidf_sorted_dictionary.items(), key=operator.itemgetter(1))
        empty=[]
        for i in sorted_dictionary:
            empty.append(i[0])
        empty.reverse()
        print('Results: ',end="")
        for k in range(0,len(empty)):
            if(k!=len(empty)-1):
                print(empty[k],"",end="")
            else:
                print(empty[k])


def tfidf_OR(docs,terms):
    print('TF-IDF')
    global count_temp
    count_temp+=1
    if(len(docs)==0):
        print('Results: empty')
    else:
        tfidf_sorted_dictionary={}
        for i in docs:
            k=0
            for j in terms:
                if j in words_list[i]: 
                    count=0
                    x=0
                    count+=tf_idf_pre_dictionary[i+'_'+j]
                    tfidf_words=len(words_list[i])
                    x=len(words_list)/len(posting_dictionary[j])
                    k+=((count/tfidf_words)*x)
            tfidf_sorted_dictionary.update({i:k})
        #print(tfidf_sorted_dictionary)
        sorted_dictionary=sorted(tfidf_sorted_dictionary.items(), key=operator.itemgetter(1))
        empty=[]
        for i in sorted_dictionary:
                empty.append(i[0])
        empty.reverse()
        print('Results: ',end="")
        for k in range(0,len(empty)):
            if(k!=len(empty)-1):
                print(empty[k],"",end="")
            else:
                if(count_queries!=count_temp):
                    print(empty[k])
                else:
                    print(empty[k],end="")
    
def Retrieve_Postings(test):
    global temp_postings
    for i in test:        
        k=[]
        k=posting_dictionary[i]
        k.sort()
        if temp_postings==0:
            print('GetPostings')
            temp_postings=1
        else:
            print('\nGetPostings')
        print(i)
        print("Postings list:",end="")
        for l in k:
            print("",l,end="")
    print("")
        
#input_file = input("Enter input file path")
#output_file = input("Enter output file path")
#input_file = open('Project2_Sample_input.txt','r')
words = {}
words_list={}
postings_list = {}
tf_idf_pre_dictionary={}
query_list = []
query_words = []
input_doc=sys.argv[1]
out=sys.argv[2]
f=open(out,'w')
sys.stdout=f
with open(input_doc, 'r') as f:
    doc_text=[]
    temp_list=[]
    for i in f:
        doc2=i.split()
        for term2 in doc2:
            count=0
            if doc2[0]!=term2:
                d=doc2[0]
                d=d+'_'+term2
                count=doc2.count(term2)
                tf_idf_pre_dictionary.update({d:count})
                temp_list.append(term2)
    #print(tf_idf_pre_dictionary)


with open(input_doc, 'r') as f:
    doc_text=[]        
    for line in f:
        line = line.strip()
        doc_id, doc_text = line.split("\t", 1)
        words[doc_id] = doc_text
        doc = doc_text.split(" ")
        words_list.update({doc_id:doc})
        
    for i in words.keys():
        words_list2 = words_list.values()
        words_list_flattened = [val for sublist in words_list2 for val in sublist]



    term = list(dict.fromkeys(words_list_flattened))
    #print(term)
    term.sort()
    posting_dictionary={}
    for term in term:
        list1=[]
        for i in words_list.keys():
            if (term in words_list[i]):
                #print(words_list[i])
                list1.append(i)
        posting_dictionary.update({term:list1})
    for key,values in posting_dictionary.items(): #SORTING VALUES OF EACH KEY IN DICTIONARY
         values.sort()
    

queries=sys.argv[3]
with open(queries, 'r') as f1:
    query_list1=[]
    for line1 in f1:
        count_queries=sum(1 for line in open(queries))
        query = line1.split()
        query_list=[]
        for i in query:
            query_list.append(i)
        query_list1.append(query_list)
        Retrieve_Postings(query_list)
        DaatAnd(query_list)
        DaatOr(query_list)
#    print(query_list1)