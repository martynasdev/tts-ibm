# Api and url for connection
_api_key = ''
_url = ''


# Audio dictionary to define the file name, format and accept conversion format
_audio_dict = {
    'name': 'converted_text',
    'format': '.mp3',
    'accept_format': 'audio/mp3'
}



def getapi():
    return _api_key

def geturl():
    return _url

def getAudioDict(i):
    if i == 'name':
        return _audio_dict['name']
    elif i == 'format':
        return _audio_dict['format']
    elif i == 'accept_format':
        return _audio_dict['accept_format']
    else:
        return print('Invalid Audio Dictionary argument')
