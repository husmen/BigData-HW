# Functions adapted from ProgrammingHistorian (updated to Python3)
# http://niche.uwo.ca/programming-historian/index.php/Tag_clouds

# Take one long string of words and put them in an HTML box.
# If desired, width, background color & border can be changed in the function
# This function stuffs the "body" string into the the HTML formatting string.
def make_HTML_box(body):
    '''Required -- body (string), a string of words
       Return -- a string that specifies an HTML box containing the body
    '''
    box_str = """<div style=\"
    width: 560px;
    background-color: rgb(250,250,250);
    border: 1px grey solid;
    text-align: center\" >{:s}</div>
    """
    return box_str.format(body)

def make_HTML_word(word,cnt,high,low):
    ''' make a word with a font size to be placed in the box. Font size is scaled
    between high and low (to be user set). high and low represent the high 
    and low counts in the document. cnt is the count of the word 
    Required -- word (string) to be formatted
             -- cnt (int) count of occurances of word
             -- high (int) highest word count in the document
             -- low (int) lowest word count in the document
    Return -- a string formatted for HTML that is scaled with respect to cnt'''
    ratio = (cnt-low)/float(high-low)
    font_size = high*ratio + (1-ratio)*low
    font_size = int(font_size)
    word_str = '<span style=\"font-size:{:s}px;\">{:s}</span>'
    return word_str.format(str(font_size), word)

def print_HTML_file(body,title):
    ''' create a standard html page (file) with titles, header etc.
    and add the body (an html box) to that page. File created is title+'.html'
    Required -- body (string), a string that specifies an HTML box
    Return -- nothing'''
    fd = open(title+'.html','w')
    the_str="""
    <html> <head>
    <title>"""+title+"""</title>
    </head>

    <body>
    <h1>"""+title+'</h1>'+'\n'+body+'\n'+"""<hr>
    </body> </html>
    """
    fd.write(the_str)
    fd.close()

# example usage

pairs = [('hi',25),('there',6),('mom',50),('fred',19),('bill',30)]
high_count=20
low_count=2
body=''
for word,cnt in pairs:
    body = body + " " + make_HTML_word(word,cnt,high_count,low_count)
box = make_HTML_box(body)  # creates HTML in a box
print_HTML_file(box,'testFile')  # writes HTML to file name 'testFile.html'
