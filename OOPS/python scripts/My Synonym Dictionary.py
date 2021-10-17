'''Mr. X is learning English and trying to improve his vocabulary.
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
    Purpose:the main function has a dictionary i.e. mydict it prints it and also prints the synonym dict
    Return: returns nothing
    """
    mydict={"Merry":"Happy","Gloomy":"Sad","Content":"Happy","Fear":"Afraid","Terror":"Afraid",
            "Depress":"Sad","Sorrow":"Sad"} #Mr X dictionary
    print("My dictionary is:\nWord\t\tMeaning")
    for i,j in mydict.items():#for loop to extract the dictionary items
        print(i+"\t\t"+j)#printing the dictionary
    synonym_dict={}#empty dictionary to store synonym
    for i in mydict.values():#taking the meanings of word from the dictionary
        synonym_dict[i]=[]#creating the empty list for the meanings to store the synonyms
        for j in mydict:#taking the words of Mr X's dictionary
            if mydict[j]==i:#checking if the word's meaning is equal to the meaning taken above in outermost loop
                synonym_dict[i].append(j)#yes then append the synonym's list by that word
    print("Synonym dictionary is:\nMeaning\t\tSynonyms")
    for i,j in synonym_dict.items():#loop for printing synonym dict
        print(i,"\t\t",j)
if __name__=="__main__":
    main()#calling main fuction