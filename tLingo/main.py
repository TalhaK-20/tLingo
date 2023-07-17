import pyttsx3
from langdetect import detect
from googletrans import Translator


def translate(text, source):
    a = Translator(service_urls=['translate.google.com'])
    b = a.translate(text, dest='en', src=source)
    return b.text


def identify(text):
    a = detect(text)

    if a == 'ur':
        a = "Urdu"

    result = translate(text, a)
    return result


def main():
    print("Welcome to AI Translator")
    print("Developed by Talha khalid\n")

    query = str(input("Enter the text that you want to translate = "))
    final_result = identify(query)

    print(f"Detected Language: {detect(query)}")
    print("Translated Text: ", final_result)

    while 1:
        option = str(input("\nDo you want text-to-speech ? "
                           "Press 'y' for yes and any key for not = "))

        if option.lower() != 'y':
            break

        ai = pyttsx3.init()
        ai.say(final_result)
        ai.runAndWait()


def repeat():
    while 1:
        main()
        option = str(input("\nDo you want to use the translator again ? If yes, just press 'y'"
                           " and if not press any key = "))
        print("\n")

        if option.lower() != 'y':
            break

    print("Thank you so much. Have a lovely day :)")


repeat()
