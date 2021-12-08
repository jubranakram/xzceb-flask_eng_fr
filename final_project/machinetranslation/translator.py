'''
Module Name: English-French Translator
Author: Jubran Akram
'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text: str) -> str:
    '''Returns the french translation of input english text'''

    if english_text is not None:
        french_text = language_translator.translate(text=english_text,
                                                    model_id='en-fr').get_result()
        return french_text

    return None


def french_to_english(french_text: str) -> str:
    '''Returns the english translation of input french text'''
    if french_text is not None:
        english_text = language_translator.translate(text=french_text,
                                                     model_id='fr-en').get_result()
        return english_text

    return None


if __name__ == '__main__':
    # English to French translation
    EN_TEXT = "Hello, How are you?"
    fr_translation = english_to_french(EN_TEXT)
    fr_trans_json = json.dumps(fr_translation)
    print(fr_translation.get('translations')[0].get('translation'))

    # French to English translation
    FR_TEXT = 'Bonjour, Comment es-tu?'
    en_translation = french_to_english(FR_TEXT).get('translations')[
        0].get('translation')
    en_trans_json = json.dumps(en_translation)
    print(en_translation)
