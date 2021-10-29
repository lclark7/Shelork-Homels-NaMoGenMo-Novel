# Import Sherlock Holmes text file from Gutenberg.

text = open("/content/Sherlock-Holmes.txt", "r").read()

# Set up ngrams.

import random

def chapter():

  ngrams = []

  for b in range(len(text) - 4):
    ngrams.append(text[b:b+4])

  random.shuffle(ngrams)
  seed = random.choice(ngrams)

  new_text = seed

  for i in range(100000):
    for n in ngrams:
      if (n[:3] == new_text[-3:]):
        new_text += n[-1]
        ngrams.remove(n)
        #break

  return(new_text)
  
  
  # let's install weasyprint!
!pip install weasyprint==52.5

# also we need markdown
import markdown

# import some specific parts of weasyprint
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration


import random

novel = """


# Shelorck Homels
### by Lyndsey Clark


"""

for c in range(1):
  
  #novel += chapter()
  
 # novel += f'''
## Chapter {c}
 # '''
  novel += chapter().capitalize()

#print(novel)


# convert the markdown formatted novel string into html
html = markdown.markdown(novel)


# prepare WeasyPriny
font_config = FontConfiguration()
rendered_html = HTML(string=html)

css = CSS(string='''
@import url('https://fonts.googleapis.com/css2?family=Festive&display=swap');

@import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@300&display=swap');
body {
font-family: 'Merriweather', serif;
}

hr {
  break-after: recto; 
}

h1 {
  font-size: 50pt;
  text-align:center;
  margin-top: 3in;
  font-family: 'Festive',cursive;
}
h2{
  break-before: recto;
  margin-top: 3in;
  font-family: 'Festive',cursive;
}

h3 {
  font-size: 20pt;
  text-align:center;
  break-after: recto;
}

/* set the basic page geometry and start the incrementer */
@page {
  font-family: 'Merriweather', serif;
  margin: 1in;
  size: letter;
  counter-increment: page;
  @bottom-center {
    content: "[" counter(page)"]";
    text-align:center;
    font-style: italic;
    color: #666666;
  }
}


/* blank the footer on the first page */
@page:first{
  @bottom-left {content: ""}
  @bottom-right {content: ""}
  @bottom-center {content: ""}
}


''', font_config=font_config)


# Finally, this creates a PDF called "sample.pdf" with all the above settings
rendered_html.write_pdf('/content/sample.pdf', stylesheets=[css],font_config=font_config)
