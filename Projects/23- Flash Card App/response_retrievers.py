import requests
import json
import requests
from bs4 import BeautifulSoup

def get_translation(text, source_lang, target_lang):
    # Google Translate API URL for fetching translation and transliteration
    url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl={source_lang}&tl={target_lang}&dt=t&dt=rm&q={text}'
    
    # Make the request to Google Translate
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        result = response.json()
        # print(result)
        # print("Full API response:", result)
        try:
            translation = result[0][0][0]  # Translation text
            # transliteration = result[0][1][3]  # transliteration text
            return translation # transliteration
        except IndexError:
            return "Translation not available" # "Transliteration not available"
    else:
        return "Failed to fetch data"

# # TEST
# # text = "مظلة"  # Arabic for "umbrella"
# text = "de"
# source_lang = "es"  # Source language: Spanish
# target_lang = "en"  # Target language: English
# translation = get_translation(text, source_lang, target_lang) # , transliteration 
# print(f"Translation of '{text}' from {source_lang} to English: {translation}")
# # print(f"Transliteration of '{text}' from {source_lang} to English: {transliteration}")

def get_transliteration(word):
    # Construct the URL for the translation page
    url = f"https://www.spanishdict.com/translate/{word}"
    
    # Make the request to the website
    response = requests.get(url)
    
    if response.status_code == 200:
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the span that contains the entire pronunciation (class 'haXtlXDT')
        pronunciation_span = soup.find('span', class_='haXtlXDT')
        
        if pronunciation_span:
            
            # Find all the div elements inside the span (these contain parts of the pronunciation)
            pronunciation_divs = pronunciation_span.find_all('div')

            # Extract and concatenate the text from the divs
            phonetic_transcription = ''.join([div.text.strip() for div in pronunciation_divs])
            
            return phonetic_transcription.strip()
        
        # If no phonetic transcription is found, return the word itself as transliteration
        else:
            return word
    else:
        print(f"Error: Unable to reach SpanishDict (Status code: {response.status_code})")
        return word

# # TEST
# word = "hola"  # Replace with the word you want to search
# phonetic_transcription = get_transliteration(word)
# if phonetic_transcription:
#     print(f"The phonetic transcription or transliteration for '{word}' is: {phonetic_transcription}")
# else:
#     print(f"Could not find the phonetic transcription for '{word}'.")

def fetch_example_sentence_with_translation(word, source_lang = "eng", target_lang = "eng"):
    # Construct the API URL
    url = f'https://tatoeba.org/en/api_v0/search?from={source_lang}&to={target_lang}&query={word}'
    
    # Send a GET request to the API
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Check if there are any results
        if data['results']:
            
            # print(data["results"])
            # Get the first result (Arabic sentence and English translation)
            sentence = data['results'][0]['text']
            translation = data['results'][0]['translations'][1][0]["text"]
            
            if translation:
                return sentence, translation
            else:
                return sentence, "No English translation available"
        else:
            return "", "No sentences found for the word."
    else:
        return "", f"Error: Unable to fetch sentences (status code {response.status_code})"

# # TEST
# # word = 'مظلة'  # "Umbrella" in Arabic
# word = "de"
# sentence, english_translation = fetch_example_sentence_with_translation(word, "spa", "eng")

# # Display the result
# if sentence:
#     print(f"Sentence: {sentence}")
#     print(f"English Translation: {english_translation}")
# else:
#     print(english_translation)

def get_spanish_sentence_and_translation(word):
    # Construct the URL for the translation page
    url = f"https://www.spanishdict.com/translate/{word}"
    
    # Make the request to the website
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the div that contains the example sentence and translation
        sentence_div = soup.find('div', class_='Vk1u6rhl')
        
        if sentence_div:
            # Extract the Spanish sentence
            spanish_sentence = sentence_div.find('span', lang='es').text.strip() if sentence_div.find('span', lang='es') else None
            
            # Extract the English translation
            english_translation = sentence_div.find('span', lang='en').text.strip() if sentence_div.find('span', lang='en') else None
            
            return spanish_sentence, english_translation
        
        return "", ""
    
    else:
        return f"Error: Unable to reach SpanishDict (Status code: {response.status_code})", None

# # Example usage
# word = "mochila"  # Replace with the word you want to search
# spanish_sentence, english_translation = get_spanish_sentence_and_translation(word)

# if spanish_sentence and english_translation:
#     print(f"Spanish sentence: {spanish_sentence}")
#     print(f"English translation: {english_translation}")
# else:
#     print(f"Could not find an example sentence for '{word}'.")

