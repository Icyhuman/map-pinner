import shutil

#Copy all actually used screenshots into separate folder to be moved to final page
def copyusedimgs():
    with open('pins.txt', 'r') as file:
        for line in file.readlines():
            path = line.split(',')[2][:-1]
            shutil.copy(path, 'pinnedshots')

#Generate html for pins to be copy pasted into final website
def generatehtml():
    with open('pins.txt', 'r') as source:
        with open('generatedHTMLcode.txt', 'a') as target:
            for line in source.readlines():
                left, top, src = line.split(',')
                src=src[:-1] #trim newline
                target.write('<img class="pin" style="left: '+left+'; top: '+top+'" onclick="pinclick(self, \''+src+'\')>\n')

copyusedimgs()
generatehtml()