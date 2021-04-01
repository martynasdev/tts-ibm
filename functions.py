import re
import docx
import time
error = 'Error encountered'
max_no_of_text_src = 2



def getAudioFile(name,format):
    return name+format


#Use docx file as an input
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        txt = para.text.encode('ascii', 'ignore')
        fullText.append(txt)
    return b'\n'.join(fullText)

#switcher between document types
def switch_text(txt, docx):
    text_selection_term = '\n*********Document type*********\n'+\
                        '0 - txt document\n'+\
                        '1 - docx document\n'+\
                        'Enter the document type: '
    txt_case_of = {
        0: txt,
        1: docx
    }
    while True:
        try:
            doc_input = input(text_selection_term)
            # Implement Switch case in this loop
            if 0 <= int(doc_input) < max_no_of_text_src:

                break
            else:
                print('\nWrong document code type entered. Try again\n')
                time.sleep(1)
        except Exception as error:
            print(error)

    return txt_case_of.get(int(doc_input), "Invalid document type")

# Enter gender
def enterGender():
    gender_term_text = '\n*********Gender selection*********\n'+ \
    '0 - Use random gender\n'+ \
    '1 - Male\n'+ \
    '2 - Female\n'+ \
    'Enter the number of preferred gender: '

    while True:
        try:
            # print(gender_term_text)
            user_input = input(gender_term_text)

            if 0 <= int(user_input) < 3:
                break
            else:
                print('\nWrong gender code entered. Try again\n')
                time.sleep(1)
        except Exception as error:
            print(error)

    return user_input

def getGender(i):
    switch = {
        0: 'random',
        1: 'male',
        2: 'female'
    }
    return switch.get(i, "Invalid gender")



# Cgeck if any user selected language or gender to be random
def checkRandomness(list_to_check):
    random = 0
    for i in range(len(list_to_check)):
        if list_to_check[i] == 'random':
            random += 1

    return random

# Select a language based on possibile options
def selectLanguage(list_of_dictionaries):
    # regex for seraching voice description
    criteria_male = re.compile('(?<=:\s)(.+?)(?=male)')
    criteria_female = re.compile('(?<=:\s)(.+?)(?=female)')
    # Sets to track unique values
    set_of_languages = {}
    set_of_languages = set()
    # Lists for language description and code
    lang_desc = []
    lang_code = []
    # Vars
    primary_set_len = 0
    lang_term_txt = '\n*********Language selection*********\n'

    # Loop the list of dictionaries
    for i in range(len(list_of_dictionaries)):
        set_of_languages.add(list_of_dictionaries[i]['language'])

        # Check if new language is added to set and search for language description and language code
        if len(set_of_languages) > primary_set_len:
            primary_set_len = len(set_of_languages)

            f = criteria_female.search(list_of_dictionaries[i]['description'])
            if f:
                if len(lang_desc) == 0:
                    lang_desc.append('0 - random')
                    lang_code.append('random')

                lang_desc.append(str(len(lang_desc)) + ' - ' + f.group())
                lang_code.append(list_of_dictionaries[i]['language'])

            else:
                m = criteria_male.search(list_of_dictionaries[i]['description'])
                if m:
                    if len(lang_desc) == 0:
                        lang_desc.append('0 - random')
                        lang_code.append('random')

                    lang_desc.append(str(len(lang_desc)) + ' - ' + m.group())
                    lang_code.append(list_of_dictionaries[i]['language'])


    for i in range(len(lang_desc)):
        lang_term_txt += lang_desc[i] + '\n'

    # Handle correct user input for language code selection
    while True:
        try:
            user_input = int(input(lang_term_txt + 'Enter the number of preferred language: '))
            if 0 <= user_input < len(lang_desc):
                break
            else:
                print('\nWrong language code entered. Try again\n')
                time.sleep(1)
        except Exception as error:
            print(error)

    return lang_code[user_input]
