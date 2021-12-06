import re
stringExample = """

"""
def encontrarNumeroExpediente(remate: str)-> str:

    # re.match(r'expediente([^(.,;)]+)',remate)
    print(re.findall(r'expediente([^(.,;)]+)',remate))

encontrarNumeroExpediente(stringExample)

