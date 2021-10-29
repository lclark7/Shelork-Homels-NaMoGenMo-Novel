text = open("/content/Sherlock-Holmes.txt", "r").read()

import random

def altchapter():
  ngrams = {}
  d = 4


  for i in range(len(text)-d-1):
    stem = text[i:i+d]
    twig = text[i+d]

    if (stem not in ngrams.keys()):
      ngrams[stem] = [twig]
    else:
      ngrams[stem].append(twig)

  seed = random.choice(list(ngrams.keys()))
  new_text = seed
  #print(seed)
  for i in range(10000):
    root = new_text[-d:]
    if(root in ngrams.keys() and len(ngrams[root]) > 0):
      pick = random.randrange(len(ngrams[root]))
      new_text += ngrams[root][pick]
      ngrams[root].pop(pick)

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

for c in range(12):
  
  #novel += chapter()
  
  #novel += f'''
## Chapter {c}
  #'''

  novel += altchapter()

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
