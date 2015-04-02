# this script converts ngdoc docs to olp

# -*- coding: utf-8 -*-
import re

def convertNgdoc2Md(oldfile, newfile):
    '''\
    Filter away all the ngdoc specific syntax
    '''

    reLinkSub = re.compile(r'{@link \S+ (.+)}')
    # find links of this type:
    # {@link ng.directive:ngApp ngApp}
    # and replace them with link text
    reImgSub = re.compile(r'<img(.+)src=\"img/tutorial/(.+)\">')
    # find image references of this type:
    # <img class="diagram" src="img/tutorial/tutorial_00.png">
    # and remove "img/tutorial/" from the path
    with open(newfile, 'w') as outfile, open(oldfile, 'r') as infile:
        for i in range(5): #remove first 5 lines that include ngdoc tags
            infile.next()
        for line in infile:
            if "<ul doc-tutorial-nav" in line:
                continue
            if "<div doc-tutorial-reset" in line:
                continue
            if reLinkSub.search(line):
                m = reLinkSub.search(line)
                line = reLinkSub.sub(m.group(1), line)
            if reImgSub.search(line):
                m = reImgSub.search(line)
                line = reImgSub.sub('<img'+m.group(1)+'src=\"https://raw.githubusercontent.com/outlearn-content/angular-tutorial/master/assets/'+m.group(2)+'\">', line)
                # print line
                # print newLine
            outfile.write(line)



indices = ['00','01','02','03','04','05','06','07','08','09','10','11','12']
for index in indices:
    oldfile = 'step_'+index+'.ngdoc'
    newfile = 'step_'+index+'.md'
    convertNgdoc2Md(oldfile, newfile)
