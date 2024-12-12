import requests
import json

def get_translation_and_transliteration(text, source_lang, target_lang):
    # Google Translate API URL for fetching translation and transliteration
    url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl={source_lang}&tl={target_lang}&dt=t&dt=rm&q={text}'
    
    # Make the request to Google Translate
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        result = response.json()
        # print("Full API response:", result)

        try:
            translation = result[0][0][0]  # Translation text
            transliteration = result[0][1][3]  # transliteration text
            # Return both translation and transliteration
            return translation, transliteration
        except IndexError:
            return "Translation not available", "Transliteration not available"
    else:
        return "Failed to fetch data", ""

# # Test
# text = "مظلة"  # Arabic for "umbrella"
# source_lang = "ar"  # Source language: Arabic
# target_lang = "en"  # Target language: English

# translation, transliteration = get_translation_and_transliteration(text, source_lang, target_lang)
# print(f"Translation of '{text}' from Arabic to English: {translation}")
# print(f"Transliteration of '{text}' from Arabic to English: {transliteration}")

def get_definition(word):
    
    api_key = 'd232c847-3fb9-4c56-901d-5c16b5469c27'  
    url = f'https://www.dictionaryapi.com/api/v3/references/learners/json/{word}?key={api_key}'
    
    # Make the request to the Merriam-Webster API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        result = response.json()
        
        # Check for a valid response
        if isinstance(result, list) and result:
            # Extract the first definition
            definitions = result[0]['shortdef'][0]
            return definitions
        else:
            return "No definitions found"
    else:
        return "Failed to fetch data"

# # # Test
# word = "umbrella"
# definitions = get_definition(word)
# print(f"Definition of '{word}': {definitions}")