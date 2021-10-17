'''
Mr. X is learning English and trying to improve his vocabulary.
So, he started created his own diary "myDict" with one word and its meaning. He was happy to learn new words.
But one day, someone asked him synonym of a word, he was able to tell the meaning but not able to tell synonyms.So, he
decided to create one more diary "synonym_dict" where he started collecting all words with the same meaning and
write all words on a single page.
IN THIS PROGRAM MR. X HAS CREATED HIS DICTIONARY mydict AND THEN THE PROGRAMMER HELPS HIM TO CREATE A synonym_dict
My dictionary is:
Word            Meaning
Merry           Happy
Gloomy          Sad
Content         Happy
Fear            Afraid
Terror          Afraid
Depress         Sad
Sorrow          Sad
Synonym dictionary is:
Meaning         Synonyms
Happy            ['Merry','Content']
Sad              ['Gloomy','Depress','Sorrow']
Afraid           ['Fear','Terror']
'''
def main():
    """
    Purpose:the main function has a dictionary i.e. mydict it prints it and calls the recursive function syn_dict
    Return: returns nothing
    """
    mydict={"Merry":"Happy","Gloomy":"Sad","Content":"Happy","Fear":"Afraid",
            "Terror":"Afraid","Depress":"Sad","Sorrow":"Sad"}#Mr X dictionary
    print("My dictionary is:\nWord\t\tMeaning")
    for i,j in mydict.items():#for loop to extract the dictionary items
        print(i+"\t\t"+j)#printing the dictionary
    synonym_dict=syn_dict(mydict)#calling the recursive function syn_dict
    print("Synonym dictionary is:\nMeaning\t\tSynonyms")
    for i,j in synonym_dict.items():#for loop to extract the dictionary items
        print(i,"\t\t",j)#printing the dictionary
def syn_dict(mydict):
    """
    purpose:its a recursive function that returns the synonym dictionary for Mr. X
    param: mydict
    return: synonym dictionary
    """
    if mydict=={}:#base condition checks if the mydict is null
        return {} #returns an empty dictionary
    else: #if dictionary is non empty
        item=mydict.popitem() #extracting the last item of the dictinory
        synonym_dict=syn_dict(mydict) #function recursivly calls itself and stores the return in synonym_dict
        if item[1] not in synonym_dict:#if the meaning is not in synonym dict
            synonym_dict[item[1]]=[item[0]] #create a list of the word that are synonyms
        else:
            synonym_dict[item[1]].append(item[0]) #if the list is already created for synonym then append it by the word
        return synonym_dict #return the synonym dictionary

if __name__=="__main__":
    main() #calling main function