"""
build a dictionary to translate a text
"""

text = "i like apples and bananas , because my head sometimes gets big."
list_text =text.split( )
mydictionary = {'apples':input('some fruit'),'head':input('an ajective'),'bananas':input('some other fruit or thing')}

for i in range(len(list_text)):
    for key in mydictionary.keys():
        if list_text[i] == key:
            list_text.remove(list_text[i])
            list_text.insert(i,mydictionary[key])

# new_text = ''
# for word in list_text:
#     new_text = new_text + ' ' + word
# print(new_text)


print(' '.join(list_text))
print(mydictionary.get('apples'))
print(mydictionary['apples'])

def translate(text1,dict1):
    list_text = text1.split()
    new_list =[]
    for word in list_text:
        translation = dict1.get(word)
        new_list.append(translation if translation else word)
    return ' '.join(new_list)

print(translate(text,mydictionary))