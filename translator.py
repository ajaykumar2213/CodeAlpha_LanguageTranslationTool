from deep_translator import GoogleTranslator

print("=== Language Translation Tool ===")

text = input("Enter text: ")

translated = GoogleTranslator(
    source='auto',
    target='ta'
).translate(text)

print("Translated Text:")
print(translated)
