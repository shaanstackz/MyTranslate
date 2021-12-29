#Name: Shaan Kohli
#Student Number: 501028410

#Display Improvements Made
print("IMPROVEMENTS MADE: Used a different language (Dutch), used a different domain rather than eating and drinking (refer to Dutch and second French translations),")
print("Increased the vocabulary to the French and Dutch dictionary, Added comments, Added the reverseDictionary function (refer to the first thing printed in output),")
print("Added a thesaurus (translates a specific input to synonyms of the words, which then translates to dutch from there),")
print("Added a compareCharacters function which compares the number of characters found in the input and output, Removed the extra period in output,")
print("Added the word count of the input and output\n")

#English to French Dictionary
EtoF = {'bread' : 'pain', 'wine' : 'vin', 'with' : 'avec', 'I' : 'Je',
        'eat' : 'mange', 'drink' : 'bois', 'John' : 'Jean', 'friends' : 'amis', 'and' : 'et', 'of' : 'du', 'red' : 'rouge', 'play' : 'jouer',
        'basketball' : 'basketball', 'by' : 'par', 'myself' : 'moi-même', 'because' : 'car', 'require' : 'exiger', 'exercise' : 'exercice'}
#French to English Dictionary
FtoE = {'pain': 'bread', 'vin': 'wine', 'avec': 'with', 'Je': 'I', 'mange': 'eat', 'bois': 'drink', 'Jean': 'John', 'amis': 'friends', 'et': 'and', 'du': 'of', 'rouge': 'red',
        'jouer' : 'play', 'basketball' : 'basketball', 'par' : 'by', 'moi-même' : 'myself', 'car' : 'because', 'exiger' : 'require', 'exercice' : 'exercise', 'ne' : 'not', 'joue' : 'play',
        'pas' : 'not', 'au' : 'at', 'basket' : 'basketball'}
#English to Dutch Dictionary
EtoD = {'night' : 'nacht', 'long' : 'lang', 'a' : 'een', 'Friday' : 'Vrijdag', 'sit' : 'zitten', 'phone' : 'telefoon',
        'watch' : 'toezitch', 'my' : 'mijn', 'to' : 'naar', 'while' : 'terwijl', 'playing' : 'spelen', 'couch' : 'bankstel',
        'and' : 'en', 'I' : 'ik', 'on' : 'Aan', 'my' : 'mijn', 'television' : 'televisie', 'like' : 'als', 'two' : 'twee',
        'red' : 'rood', 'english' : 'Engels', 'Friday evening' : 'vrijdagavond', 'sits' : 'zit', 'gladly' : 'graag', 'sofa' : 'bank',
        'look' : 'kijk', 'play' : 'speel', 'eat' : 'eten', 'every' : 'elke', 'type' : 'type', 'vegetable' : 'groente',
        'as' : 'als', 'love' : 'liefde', 'any' : 'ieder', 'device' : 'apparaat', 'peaceful' : 'vredig', 'fearless' : 'onbevreesd',
        'energize' : 'energie geven', 'involve' : 'betrekken', 'condition' : 'staat', 'thoughtful' : 'attent', 'unclear' : 'onduidelijk'}
#Reverse Dictionary function to show Dutch to English Dictionary
def reverseDictionary(dictionary):
    DtoE={}
    for key in dictionary.keys():
        DtoE[dictionary[key]] = key
    return DtoE
#Print Dutch to English Dictionary
print(reverseDictionary(EtoD))
#English Thesaurus
EtoES = {'eat' : 'consume', 'every' : 'all', 'type' : 'sort', 'vegetable' : 'herb', 'as' : 'since', 'love' : 'adore', 'any' : 'each', 'i' : 'i',
         'of' : 'of', 'device' : 'gadget', 'peaceful' : 'serene', 'fearless' : 'intrepid', 'energize' : 'invigorate', 'involve' : 'embroil',
         'condition' : 'fettle', 'thoughtful' : 'pensive', 'unclear' : 'ambiguous'}
#Dutch to English Dictionary
DtoE = {'nacht' : 'night', 'lange' : 'long', 'een' : 'a', 'Vrijdag' : 'Friday', 'zitten' : 'sit', 'telefoon' : 'phone',
        'toezitch' : 'watch', 'mijn' : 'my', 'naar' : 'to', 'terwijl' : 'while', 'spelen' : 'playing', 'bankstel' : 'couch',
        'en' : 'and', 'ik' : 'I', 'op' : 'on', 'mijn' : 'my', 'televisie' : 'television', 'als' : 'like', 'vrijdagavond' : 'Friday evening',
        'zit' : 'sits', 'graag' : 'gladly', 'bank' : 'sofa', 'kijk' : 'look', 'speel' : 'play', 'eten' : 'eat', 'elke' : 'every', 'type' : 'type',
        'groente' : 'vegetable', 'als' : 'as', 'liefde' : 'love', 'ieder' : 'any', 'apparaat' : 'device', 'vredig' : 'peaceful', 'onbevreesd': 'fearless',
        'energie geven' : 'energize', 'betrekken' : 'involve', 'staat' : 'condition', 'attent' : 'thoughtful', 'onduidelijk' : 'unclear'}
#English Thesaurus to Dutch Thesaurus
EStoDS = {'consume' : 'consumeren', 'all' : 'alle', 'sort' : 'soort', 'herb' : 'kruid', 'since' : 'sinds', 'adore' : 'aanbidden', 'each' : 'elk', 'i' : 'ik',
          'of' : 'van', 'gadget' : 'gadget', 'serene' : 'sereen', 'intrepid' : 'onverschrokken', 'invigorate' : 'versterken', 'embroil' : 'verwikkelen',
          'fettle' : 'afrossen', 'pensive' : 'nadenkend', 'ambiguous' : 'dubbelzinnig'}
#Dutch Thesaurus to English Thesaurus
DStoES = {'consumeren' : 'consume', 'alle' : 'all', 'soort' : 'sort', 'kruid' : 'herb', 'sinds' : 'since', 'aanbidden' : 'adore', 'elk' : 'each', 'ik' : 'i',
          'van' : 'of', 'gadget' : 'gadget', 'sereen' : 'serene', 'onverschrokken' : 'intrepid', 'versterken' : 'invigorate', 'verwikkelen' : 'embroil',
          'afrossen' : 'fettle', 'nadenkend' : 'pensive', 'dubbelzinnig' : 'ambiguous'}
#Dictionarys sorted
dicts = {'English to French' : EtoF, 'French to English' : FtoE, 'English to Dutch' : EtoD, 'Dutch to English' : DtoE, 'English Thesaurus' : EtoES, 'English to Dutch Thesaurus' : EStoDS,
         'Dutch to English Thesaurus' : DStoES}
#Function for translating certain words in dictionary
def translateWord(word, dictionary) :
    if word in dictionary.keys() :
        return dictionary[word]
    elif word != '' :
        return '"' + word + '"'
    return word
#Function for translating a given phrase
def translate(phrase, dicts, direction) :
    #Upper case letters
    UCletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #Lower case letters
    LCletters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCletters + LCletters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    #Process for finding the translated words
    for character in phrase :
        if character in letters :
            word = word + character
        else :
            translation = translation + translateWord(word, dictionary) + character
            word = ''
    #Finding the translation
    translation = translation + translateWord(word, dictionary) + character
    #Returning the final translation
    return translation
#Function to compare Input and Output Character Count
def compareCharacters(word, translatedword):
    count=0
    count1=0
    #Determine count of Input
    for x in range(0, len(word)):
        if(word[x]!=''):
            count+=1
    print('\nInput Character Count:', count)
    #Determine count of Output
    for x in range(0, len(translatedword)):
        if(translatedword[x]!=''):
            count1+=1
    print('\nOutput Character Count:', count1)
    #If Input greater than Output
    if (count>count1):
        count=count-count1
        print('\nInput has',count,'more characters than output')
    #If Output greater than Input
    else:
        count1=count1-count
        print('\nOutput has',count1,'more characters than input')

#Translate sentence from English to French
sentence = 'I drink good red wine, and eat bread.'
#Use the translate function
translated = translate(sentence, dicts, 'English to French')
#Display input and output
print('--------------------------------------')
print('Input:', sentence)
#Remove extra period by splicing
print('Output:', translated[:-1])
#Determine word count of input and output
print('\nWord count of input:',len(sentence.split()))
print('\nWord count of output:',len(translated.split()))
#Use compareCharacters function
compareCharacters(sentence,translated)
print('--------------------------------------')
#Translate sentence from French to English
sentence = 'Je bois du vin rouge.'
#Use the translate function
translated = translate(sentence, dicts, 'French to English')
#Display input and output
print('\nInput:', sentence)
#Remove extra period by splicing
print('Output:', translated[:-1])
#Determine word count of input and output
print('\nWord count of input:',len(sentence.split()))
print('\nWord count of output:',len(translated.split()))
#Use compareCharacters function
compareCharacters(sentence,translated)
print('--------------------------------------')

#Translate sentence from English to French (different domain)
sentence = 'I play basketball by myself because I require exercise.'
#Use the translate function
translated = translate(sentence, dicts, 'English to French')
#Display input and output
print('--------------------------------------')
print('Input:', sentence)
#Remove extra period by splicing
print('Output:', translated[:-1])
#Determine word count of input and output
print('\nWord count of input:',len(sentence.split()))
print('\nWord count of output:',len(translated.split()))
#Use compareCharacters function
compareCharacters(sentence,translated)
print('--------------------------------------')
#Translate sentence from French to English
sentence = 'Je ne joue pas au basket.'
#Use the translate function
translated = translate(sentence, dicts, 'French to English')
#Display input and output
print('\nInput:', sentence)
#Remove extra period by splicing
print('Output:', translated[:-1])
#Determine word count of input and output
print('\nWord count of input:',len(sentence.split()))
print('\nWord count of output:',len(translated.split()))
#Use compareCharacters function
compareCharacters(sentence,translated)
print('--------------------------------------')

#Translate sentence from English to Dutch
sentence = 'on a long Friday night, I like to sit on my couch and watch television while playing on my phone.'
#Use the translate function
translated = translate(sentence, dicts, 'English to Dutch')
#Display input and output
print('--------------------------------------')
print('Input:', sentence)
#Remove extra period by splicing
print('Output:', translated[:-1])
#Determine word count of input and output
print('\nWord count of input:',len(sentence.split()))
print('\nWord count of output:',len(translated.split()))
#Use compareCharacters function
compareCharacters(sentence,translated)
print('--------------------------------------')
#Translate sentence from Dutch to English
sentence = 'op een lange vrijdagavond zit ik graag op mijn bank en kijk ik televisie terwijl ik op mijn telefoon speel.'
#Use the translate function
translated = translate(sentence, dicts, 'Dutch to English')
#Display input and output
print('\nInput:', sentence)
#Remove extra period by splicing
print('Output:', translated[:-1])
#Determine word count of input and output
print('\nWord count of input:',len(sentence.split()))
print('\nWord count of output:',len(translated.split()))
#Use compareCharacters function
compareCharacters(sentence,translated)

#Change the english sentence according to words on the English Thesaurus
sentence = 'i eat every type of vegetable as i love any vegetable.'
#Use the translate function
translated = translate(sentence, dicts, 'English Thesaurus')
print('--------------------------------------')
#Display input
print('Input:', sentence)
#Translate the sentence receieved through the Thesaurus to Dutch
sentence = 'i consume all sort of herb since i adore each herb.'
#Use the translate function
translated = translate(sentence, dicts, 'English to Dutch Thesaurus')
#Output and remove the extra period by splicing
print('Output:', translated[:-1])
#Determine word count of input and output
print('\nWord count of input:',len(sentence.split()))
print('\nWord count of output:',len(translated.split()))
#Use the compareCharacters function
compareCharacters(sentence,translated)
print('--------------------------------------')
#Translate the Dutch sentence back to English for the user to know what the program translated it from
sentence='ik consumeren alle soort van kruid sinds ik aanbidden elk kruid.'
#Use the translate function
translated = translate(sentence, dicts, 'Dutch to English Thesaurus')
#Display input and output
print('--------------------------------------')
print('Input:', sentence)
#Remove the extra period by splicing
print('Output:', translated[:-1])
#Determine word count of input and output
print('\nWord count of input:',len(sentence.split()))
print('\nWord count of output:',len(translated.split()))
#Use the compareCharacters function
compareCharacters(sentence,translated)
print('--------------------------------------')

