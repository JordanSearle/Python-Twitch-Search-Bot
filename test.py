import sys
sys.path.append('c:/users/jorda/appdata/local/programs/python/python38-32/lib/site-packages')

import requests
import string
from googlesearch import search
from bs4 import BeautifulSoup

# to search
#print(chatbot_query('how old is samuel l jackson'))

def chatbot_query(query, index=0):
    fallback = 'Sorry, I cannot think of a reply for that.'
    result = ''    
    try:
        search_result_list = list(search(query, num=10, stop=10, pause=1,safe='on'))
        
        page = requests.get(search_result_list[index])

        print(search_result_list[index])
       
        
        soup = BeautifulSoup(page.content, features="html.parser")
        article_text = ''
        article = soup.findAll('p')
        for element in article:            
            article_text += '\n' + ''.join(element.findAll(text = True))
        article_text = article_text.replace('\n', '')
        first_sentence = article_text.split('.')
        first_sentence = first_sentence[0].split('?')[0]
        chars_without_whitespace = first_sentence.translate(
             { ord(c): None for c in string.whitespace }
        )

        if len(chars_without_whitespace) > 0:
            result = first_sentence
        else:
            result = fallback   
        return result
    except:        
        if len(result) == 0: result = fallback
        return result
#print(chatbot_query('how old is samual j jackson'))
