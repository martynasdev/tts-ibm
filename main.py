import jsonG
import re
import random
import docx
import os

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from functions import *
from default_data import *

# Dictionaries
parsed_dict = {}g

# Lists
list_of_lang_dict = []
parsed_list_of_dict = []
user_selection = []

# Variables
randomness = 0
valid_case = 0
allowed_keys = ['language', 'gender']
text_as_txt = 'txt'
text_as_docx = 'docx'


# Program start

# IBM Watson text to speech authentication
# authenticator = IAMAuthenticator(getapi())
authenticatorg = IAMAuthenticator(getapi())
text_to_speech = TextToSpeechV1(
    authenticator = authenticator
)
# text_to_speech.set_service_url(geturl())
text_to_speech.set_service_url(geturl())
#PGet the list of voices and write them into json file
voices = text_to_speech.list_voices().get_result()
with open('voices.txt', 'w') as outfile:
    json.dump(voices, outfile, indent = 2)

# Get name and format of the audio file
audio_file = getAudioFile(getAudioDict('name'), getAudioDict('format'))

# Parse json file of voices to new list of dictionaries based on gender, name, description and language
with open('voices.txt') as json_file:
    data = json.load(json_file)
    for i in data['voices']:
        parsed_dict = {
            "gender": i["gender"],
            "name": i["name"],
            "description": i["description"],
            "language": i["language"]
        }
        list_of_lang_dict.append(parsed_dict)


# Obtain user criteria for text conversion
user_selection.append(selectLanguage(list_of_lang_dict))
user_selection.append(getGender(int(enterGender())))
# Check if any 'random' language or gender was selected
randomness = checkRandomness(user_selection)


# Based on randomness parse the list of dictionaries to reach specific voice and gender
if randomness == 0:
    for i in range(len(list_of_lang_dict)):
        valid_case = 0
        for j in range(len(allowed_keys)):
            if bool(list_of_lang_dict[i][allowed_keys[j]] == user_selection[j]):
                valid_case += 1

        # Found valid case were language and gender meets user selection
        if valid_case == len(allowed_keys):
            parsed_dict = {
                "gender": list_of_lang_dict[i]['gender'],
                "name": list_of_lang_dict[i]['name'],
                "description": list_of_lang_dict[i]['description'],
                "language": list_of_lang_dict[i]['language']
            }
            parsed_list_of_dict.append(parsed_dict)
elif randomness == 1:
    for i in range(len(user_selection)):
        if user_selection[i] != 'random':
            pref_key = user_selection[i]

            for j in range(len(list_of_lang_dict)):
                if bool(list_of_lang_dict[j][allowed_keys[i]] == pref_key):

                    parsed_dict = {
                        "gender": list_of_lang_dict[j]['gender'],
                        "name": list_of_lang_dict[j]['name'],
                        "description": list_of_lang_dict[j]['description'],
                        "language": list_of_lang_dict[j]['language']
                    }

                    parsed_list_of_dict.append(parsed_dict)
else:
    print('\nThe voice and language will be selected randomly\n')


if len(parsed_list_of_dict) != 0 :
    # Some sort of preference
    selected_voice = random.choice(parsed_list_of_dict)
else:
    # No preference from the user side and select the voice randomly
    selected_voice = random.choice(list_of_lang_dict)

# Define the chosen voice data for text to speech conversion based on user preference
chosen = [selected_voice['gender'], selected_voice['name'], selected_voice['description'], selected_voice['language']]

#Document type selection
text = switch_text(text_as_txt,text_as_docx)
if text == 'txt':
    with open("text_to_convert.txt", "r") as myfile:
        text_to_translate = myfile.read().replace('\n', ' ')
elif text == 'docx':
    text_to_translate = str(getText("text_to_convert.docx"), 'UTF-8')

#Write & get back the audio file
with open(audio_file, 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            text_to_translate,
            voice = chosen[1],
            accept= getAudioDict('accept_format')
        ).get_result().content)

#Info for terminal
print('\nThe text was converted using ' + chosen[0] + ' voice.' + '\n' +
    'The language used: ' + chosen[3] + '\n' +
    'Author: ' + chosen[2] + '\n')
