from text_to_num import alpha2digit

sentence = 'Habían trescientos hombres y quinientas mujeres pero cero animales'
print("Sentence to convert >>> ",sentence)

converted_sentence = alpha2digit(sentence,'es')
print("Converted Sentence >>> ",converted_sentence)