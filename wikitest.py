import wikipedia

def send_eiki(text):
    wikipedia.set_lang('uz')
    return wikipedia.summary(text, sentences=2)

