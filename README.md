# tts-ibm
Text to speech converter (IBM Watson)

******default_data.py******
Includes:
  1. Api key and url address of IBM Text-To-Speech
  2. Stores audio dictionary with parameters of audio name, format and accept format

******functions.py******
Includes functions:
  1. getAudioFile() - returns name based on default data
  2. getText() - returns docx file's information in string format
  3. swichText() - returns selected document type (initial implementation handles .txt and .docx files)
  4. enterGender() - returns gender in string(random, male or female)
  5. checkRandomness() - checks if user has chosen random language or gender and returns amount of random selections
  6. selectLanguage() - loops through a IBM watson voices.txt file and checks for all available languages. 
                        From terminal user selects the language and returns back its code in string
  
******main.py******
Includes:
  1. Authenticates with IBM Watson
  2. Pulls down all possible voices and stores them into .txt file
  3. Voice file .txt is added into a list of dictionaries
  4. New list of dictionaries is created based on user preferences
  5. Text is sent and voice file received from IBM Watson
