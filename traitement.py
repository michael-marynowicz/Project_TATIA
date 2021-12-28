import nltk
import gensim
from textblob import TextBlob
nltk.downloader.download('vader_lexicon')
nltk.download('word2vec_sample')
from nltk.data import find
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from scipy import sparse
import numpy as np
from sklearn.linear_model import LogisticRegression

sia = SentimentIntensityAnalyzer()

def algo_with_svm():
    #RECUPERATION DU CSV
    data = pd.read_csv('reviews.csv')
    nom = data["Product Name"].head(10000)
    reviews = data['Reviews'].head(10000)
    rating = data['Rating'].head(10000)
    cat = categorie(rating) # transformation des notes en categorie
    
    #Vectorizer les phrases
    vectorizer = CountVectorizer()
    reviews = vectorizer.fit_transform(reviews)
    
    #Split la liste entre la zone de training et de test 
    X_train , X_test , y_train, y_test = train_test_split(reviews, cat, test_size=0.30)

    #Declaration du modele
<<<<<<< HEAD
    clf_svc1 = svm.SVC(probability=True)
    clf_svc2 = svm.SVC(probability=True)
    clf_svc3 = svm.SVC(probability=True)
=======
    clf_svc1 = LogisticRegression()
    clf_svc2 = LogisticRegression()
    clf_svc3 = LogisticRegression()
>>>>>>> f0ee39bd0fb10491cdbc540336a63b1f9086cbfa


    X_train_very_good_and_neutre = []
    X_test_very_good_and_neutre = []

    X_train_neutre_and_very_bad = []
    X_test_neutre_and_very_bad = []

    X_train_very_bad_and_very_good = []
    X_test_very_bad_and_very_good = []

    y_train_very_good_and_neutre= []
    y_test_very_good_and_neutre= []

    y_train_neutre_and_very_bad= []
    y_test_neutre_and_very_bad= []

    y_train_very_bad_and_very_good = []
    y_test_very_bad_and_very_good = []

    #trie des y_test pour les 3 SVM specialisées 
    for i in range(len(y_test)):
        if (y_test[i]=="very good" or y_test[i]=="neutre"):
            X_test_very_good_and_neutre.append(X_test[i].toarray()[0])
            
            y_test_very_good_and_neutre.append(y_test[i])

        if (y_test[i]=="very bad" or y_test[i]=="neutre"):
          
            X_test_neutre_and_very_bad.append(X_test[i].toarray()[0])
            
            y_test_neutre_and_very_bad.append(y_test[i])

        if(y_test[i]=="very bad" or y_test[i]=="very good"):           
            
            X_test_very_bad_and_very_good.append(X_test[i].toarray()[0])
            
            y_test_very_bad_and_very_good.append(y_test[i])

    #trie des y_train pour les 3 SVM specialisées 
    for i in range(len(y_train)):

        if (y_train[i]=="very good" or y_train[i]=="neutre"):
        
            X_train_very_good_and_neutre.append(X_train[i].toarray()[0])
            
            y_train_very_good_and_neutre.append(y_train[i])

        if (y_train[i]=="very bad" or y_train[i]=="neutre"):
            
            X_train_neutre_and_very_bad.append(X_train[i].toarray()[0])
            
            y_train_neutre_and_very_bad.append(y_train[i])
       
        if(y_train[i]=="very bad" or y_train[i]=="very good"):
            
            X_train_very_bad_and_very_good.append(X_train[i].toarray()[0])
            
            y_train_very_bad_and_very_good.append(y_train[i])
    
    #Conversion en csc_matrix pour l'entrainement et l'application des SVM
    X_train_very_good_and_neutre = sparse.csc_matrix(X_train_very_good_and_neutre)
    X_train_neutre_and_very_bad = sparse.csc_matrix(X_train_neutre_and_very_bad)
    X_train_very_bad_and_very_good = sparse.csc_matrix(X_train_very_bad_and_very_good)

    X_test_very_good_and_neutre = sparse.csc_matrix(X_test_very_good_and_neutre)
    X_test_neutre_and_very_bad = sparse.csc_matrix(X_test_neutre_and_very_bad)
    X_test_very_bad_and_very_good = sparse.csc_matrix(X_test_very_bad_and_very_good)
    
    clf_svc1.fit(X_train_very_good_and_neutre, y_train_very_good_and_neutre)
    clf_svc2.fit(X_train_neutre_and_very_bad, y_train_neutre_and_very_bad) 
    clf_svc3.fit(X_train_very_bad_and_very_good, y_train_very_bad_and_very_good)
    
    #Le modèle prédit sur la zone de test 
    result1 = clf_svc1.predict(X_test_very_good_and_neutre) 
    result2 = clf_svc2.predict(X_test_neutre_and_very_bad) 
    result3 = clf_svc3.predict(X_test_very_bad_and_very_good) 
   
    #statistiques
    print("very good and neutre = \n",classification_report(y_test_very_good_and_neutre, result1),"\n")
    print("neutre and very bad = \n",classification_report(y_test_neutre_and_very_bad, result2),"\n")
    print("very good and very bad = \n",classification_report(y_test_very_bad_and_very_good, result3),"\n")
    
    #Affichage des matrice de confusion
<<<<<<< HEAD
    print("very good and neutre = \n",confusion_matrix(result1, y_test_very_good_and_neutre),"\n")
    print("neutre and very bad = \n",confusion_matrix(result2, y_test_neutre_and_very_bad),"\n")
    print("very good and very bad = \n",confusion_matrix(result3, y_test_very_bad_and_very_good),"\n")
=======
    print("very good and neutre = \n",confusion_matrix(result1, y_test_very_good_and_neutre))
    print("neutre and very bad = \n",confusion_matrix(result2, y_test_neutre_and_very_bad))
    print("very good and very bad = \n",confusion_matrix(result3, y_test_very_bad_and_very_good))
>>>>>>> f0ee39bd0fb10491cdbc540336a63b1f9086cbfa


    
#Pour inserer de nouveau commentaire     
    
    reviews2 = data['Reviews'].head(10000)
<<<<<<< HEAD
    reviews2[0] = "I am not happy it's a bad phone" # le commentaire que l'on souhaite traiter
=======
    reviews2[0] = "Stopped working after 2 months. Not happy with this phone." # le commentaire que l'on souhaite traiter
>>>>>>> f0ee39bd0fb10491cdbc540336a63b1f9086cbfa
    reviews2 = vectorizer.fit_transform(reviews2)
    
    ynew1 = clf_svc1.predict(reviews2) 
    ynew2 = clf_svc2.predict(reviews2)
    ynew3 = clf_svc3.predict(reviews2)
    print("votre commentaire est caracterisé de : ")
    #One vs One
    if (ynew1[0]=="neutre"): 
        if (ynew2[0]== "neutre"):
<<<<<<< HEAD
            print("neutre\n")
        else:
  
            if (ynew3[0]=="very bad"):
                print("very bad\n")
    else:
        if (ynew3[0]=="very good"):
                print("very good\n")
        else:
            if(ynew2[0]== "neutre"):
                print("very good\n")
            else:
                print("conflit\n")
=======
            print("neutre")
        else:
  
            if (ynew3[0]=="very bad"):
                print("very bad")
    else:
        if (ynew3[0]=="very good"):
                print("very good")
        else:
            if(ynew2[0]== "neutre"):
                print("very good ")
            else:
                print("conflit")
>>>>>>> f0ee39bd0fb10491cdbc540336a63b1f9086cbfa

# regroupement des 3 SVM specialisées pour traiter les reviews entierement avec les 3 categories confondues
    cat_commentaire1 = clf_svc1.predict(X_test)
    cat_commentaire2 =clf_svc2.predict(X_test)
    cat_commentaire3 =clf_svc3.predict(X_test)

    predictions1 = clf_svc1.predict_proba(X_test)
    predictions2 = clf_svc2.predict_proba(X_test)
    predictions3 = clf_svc3.predict_proba(X_test)


    acc=0
    y_final = []
    for i in range(len(y_test)):
        very_good = 0
        very_bad = 0
        neutre = 0
        #nous demandons au SVM ce qu'elles ont predit pour cette reviews
<<<<<<< HEAD
        if (cat_commentaire1[i]=="very good" and predictions1[i][1]>0.5):
            very_good+=1
        if (cat_commentaire3[i]=="very good" and predictions3[i][1]>0.5):
            very_good+=1
        if (cat_commentaire2[i]=="very bad" and predictions2[i][1]>0.5):
            very_bad+=1
        if (cat_commentaire3[i]=="very bad" and predictions3[i][0]>0.5):
            very_bad+=1
        if (cat_commentaire1[i]=="neutre" and predictions1[i][0]>0.5):
            neutre+=1
        if (cat_commentaire2[i]=="neutre" and predictions2[i][0]>0.5):
            neutre+=1
        
        

        # si 2 SVM sont d'accord alors nous considerons que c'est la bonne prediction
        if (very_good==2):
            if (y_test[i]=="very good"): # si c'est effectivement la bonne nous augmentons notre accumulateur de bonne prediction 
                acc+=1
            y_final.append("very good")
        elif (very_bad==2):
            if (y_test[i]=="very bad"):
                acc+=1
            y_final.append("very bad")
        elif (neutre==2):
            if (y_test[i]=="neutre"):
                acc+=1
            y_final.append("neutre")
        else:
            p1 = max(predictions1[i][0],predictions1[i][1])
            p2 = max(predictions2[i][0],predictions2[i][1])
            p3 = max(predictions3[i][0],predictions3[i][1])
        
            if (max(p1,p2,p3)==p1):
                if (max(predictions1[i][0],predictions1[i][1])==predictions1[i][0]):
                    y_final.append("neutre")
                    if (y_test[i]=="neutre"):
                        acc+=1
                else:
                    if (y_test[i]=="very good"):
                        acc+=1
                    y_final.append("very good")

            elif (max(p1,p2,p3)==p2):
                if (max(predictions2[i][0],predictions2[i][1])==predictions2[i][0]):
                    if (y_test[i]=="neutre"):
                        acc+=1
                    y_final.append("neutre")
                else:
                    if (y_test[i]=="very bad"):
                        acc+=1
                    y_final.append("very bad")
          
            else:
                if (max(predictions3[i][0],predictions3[i][1])==predictions3[i][0]):
                    if (y_test[i]=="very bad"):
                        acc+=1
                    y_final.append("very bad")
                else:
                    if (y_test[i]=="very good"):
                        acc+=1
                    y_final.append("very good")
            
            
        

=======
        if (cat_commentaire1[i]=="very good"):
            very_good+=1
        if (cat_commentaire1[i]=="neutre"):
            neutre+=1
        if (cat_commentaire2[i]=="neutre"):
            neutre+=1
        if (cat_commentaire2[i]=="very bad"):
            very_bad+=1
        if (cat_commentaire3[i]=="very bad"):
            very_bad+=1
        if (cat_commentaire3[i]=="very good"):
            very_good+=1

        # si 2 SVM sont d'accord alors nous considerons que c'est la bonne prediction
        if (very_good==2):
            if (y_test[i]=="very good"): # si c'est effectivement la bonne nous augmentons notre accumulateur de bonne prediction 
                acc+=1
            y_final.append("very good")
        elif (very_bad==2):
            if (y_test[i]=="very bad"):
                acc+=1
            y_final.append("very bad")
        elif (neutre==2):
            if (y_test[i]=="neutre"):
                acc+=1
            y_final.append("neutre")
        else:
            y_final.append("very good")

>>>>>>> f0ee39bd0fb10491cdbc540336a63b1f9086cbfa
    print(confusion_matrix(y_final, y_test))

    print("statistiique totaux = \n",classification_report(y_test, y_final))
 
    return ("la precision sur l'ensemble des reviews traitées est de : "+str((acc/len(y_test))*100)+"%")
    


def correction(sentences):
    sentences_corrige = []
    for i in range (len(sentences)):
        corrige = TextBlob(sentences[i])
        sentences_corrige.append(str(corrige.correct()))
    return sentences_corrige

def categorie(tab):
    cat = []
    for i in range(len(tab)):
        if (tab[i]==1):
            cat.append("very bad")
        elif (tab[i]>1 and tab[i]<5):
            cat.append("neutre")
        else: 
            cat.append("very good")
    return cat


print(algo_with_svm())

########################################### a garder pour citer dans le rapport ##################################################################


def essais():
    file_content = pd.read_csv('reviews.csv')
    
    tokens = nltk.word_tokenize("gooddd")
    tokensWithType = nltk.pos_tag(tokens)
    sentence =''
    for wt, type in tokensWithType:
        if (type.startswith('JJ')):
            sentence+=' '+wt
    neutre = extract_neutre(sentence)

    context_list,sentence_without_neutre = context(file_content,neutre) 

    note_neutre = evalue_with_context(context_list)
    return get_note(sentence_without_neutre,note_neutre)

def determine_polarity(text):
    blob = TextBlob(text)
    acc=0
    result=0
    for sentence in blob.sentences:
        result+=(sentence.sentiment.polarity+1)*2.5
        acc+=1
    return result/acc

def evalue_with_context(all_neutre_list):
    note=0
    acc=0
    for i in range(len(all_neutre_list)):
        note +=determine_polarity(all_neutre_list[i])
        acc+=1
    return note/acc

def context(file_content,neutres): #essais pour avoir le context
    context_of_neutre_word = []
    file_content_list = list(file_content.split(" "))
    for i in range(len(file_content_list)):
        if (file_content_list[i] in neutres and (i>0 and i<len(file_content_list)-1)):
            context = file_content_list[i-1]+' '+file_content_list[i]+' '+file_content_list[i+1]
            context_of_neutre_word.append(context)
            file_content=file_content.replace(context,"")
            
    return context_of_neutre_word,file_content

def extract_neutre(sentence):

    neutre = ''
    sentence_list = list(sentence.split(" "))
    for i in range(len(sentence_list)):
        if (sia.polarity_scores(sentence_list[i])['neu']==1):
            neutre+=sentence_list[i]+' '
    return neutre

def get_sentiment(sentence):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(sentence)

def get_synonyme(word):
    word2vec_sample =str(find('models/word2vec_sample/pruned.word2vec.txt'))
    model = gensim.models.KeyedVectors.load_word2vec_format(word2vec_sample, binary=False)
    return model.most_similar(positive=[word], topn = 1)

def get_note(content,note_neutre):
    print(determine_polarity(content))
    return (determine_polarity(content)+note_neutre)/2 # on retourne le total des etoiles 


