def circle(x,y,rad,text1,text2,link):
  line = '<line x1="'+str(x-rad)+'" y1="'+str(y)+'" x2="'+str(x+rad)+'" y2="'+str(y)+'" style="stroke:rgb(0,0,0);stroke-width:2" />'
  text = '<circle cx="'+str(x)+'" cy="'+str(y)+'" r="'+str(rad)+'" stroke="black" stroke-width="2" fill="white" onClick="window.location.href=\''+link+'.html\'"/> \n <text x="'+str(x-0.45*rad)+'" y="'+str(y+0.5*rad)+'" class="heavy">'+text2+'</text>\n<text x="'+str(x-0.45*rad)+'" y="'+str(y-0.5*rad)+'" class="heavy">'+text1+'</text>\n'+line
  return text

def hexa(x,y,rad,text,text2,link):
   line = '<line x1="'+str(x-rad)+'" y1="'+str(y)+'" x2="'+str(x+rad)+'" y2="'+str(y)+'" style="stroke:rgb(0,0,0);stroke-width:2" />'
   e ="""<polygon class="hex" points=\""""+str(x-rad)+""","""+str(y)+""" """+str(x-(0.5*rad))+""","""+str(y+((5/6)*rad))+""" """+str(x+(0.5*rad))+""","""+str(y+(5/6)*rad)+""" """+str(x+rad)+""","""+str(y)+""" """+str(x+(0.5*rad))+""","""+str(y-(5/6)*rad)+""" """+str(x-(0.5*rad))+""","""+str(y-(5/6)*rad)+"""\" stroke="black" stroke-width="2" fill="white" onClick="window.location.href='"""+link+""".html'"></polygon>
   <text x=\""""+str(x-0.45*rad)+"""\" y=\""""+str(y+0.5*rad)+"""\" class="heavy">"""+text2+"""</text>\n<text x=\""""+str(x-0.45*rad)+"""\" y=\""""+str(y-0.5*rad)+"""\" class="heavy">"""+text+"""</text>\n"""+line
   return e

def rec(x,y,height,width,link,label):
  r = '<rect x="'+str(x)+'" y="'+str(y)+'" width="'+str(width)+'" height="'+str(height)+'" stroke="black" stroke-width="2" fill="white" onClick="window.location.href=\''+link+'.html\'"></rect>\n'
  z = """ <text x=\""""+str(x)+"""\" y=\""""+str(y)+"""\" class="heavy">"""+label+"""</text>"""
  return r+z

def controlelec(x,y,text1,text2,link1,link2):
  a = circle(x,y,35,text1,text2,link1)
  b = hexa(x+((2.1)*35),y,35*1.1,text1,text2,link2)
  return a+b

#Requires link for navigation location , *argv for pairs of points
def poly(link,*argv):
  exportlist = []
  string = ""
  indexer = 2
  for arg in argv:
    exportlist.append(arg)
  for i in exportlist:
    if (indexer % 2) == 0:
      string = string+str(i)+","
    else:
      string = string+str(i)+" "
    indexer = indexer+1
  stringexport = '<polygon points="'+string+'" onClick="window.location.href=\''+link+'.html\'" style="fill:white;stroke:black;stroke-width:2" />'
  return stringexport

def text(x,y,text1):
  text = """ <text x=\""""+str(x)+"""\" y=\""""+str(y)+"""\" class="heavy">"""+text1+"""</text>"""
  return text

#print(controlele c(50,50,"text1","null","null","null"))