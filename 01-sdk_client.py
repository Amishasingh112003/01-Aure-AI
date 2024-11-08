"""We need to set an environment variable .This must have :
  * endpoint of the azure as : "AI_SERVICE_ENDPOINT"
  * API key as : "AI_SERVICE_KEY"
  * AI_SERVICE_ENDPOINT='https://xxxxxazu.cognitivervices.azure.com/'
  * AI_SERVICE_KEY='DcccvvvbbxxxEFnNrPjRy3o0urZ3xxxx73d8prTm4oxrXl78Bxxxxx9AKACYcccccJ3ccAACOGqFUd' 
"""

#this one is the clientsdk.py
from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def main():
    global ai_endpoint
    global ai_key
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Get user input (until they enter "quit")
        userText = ''
        while userText.lower() != 'quit':
            userText = input('\nEnter some text ("quit" to stop)\n')
            if userText.lower() != 'quit':
                language = GetLanguage(userText)
                print('Language:', language)
    except Exception as ex:
        print(ex)

def GetLanguage(text):
    # Create client using endpoint and key
    credential = AzureKeyCredential(ai_key)
    client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

    # Call the service to get the detected language
    detectedLanguage = client.detect_language(documents=[text])[0]
    return detectedLanguage.primary_language.name

if __name__ == "__main__":
    main()
