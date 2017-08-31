# SaveIt v.1
import sys
import pickle



# Note w/ title, meta data and txt data
class note:
    # title
    def __init__(self, title):
        self.title = title
        self.meta = []
        self.metaIdx = 0
        self.txt = []
        self.txtIdx = 0
        self.nextNote = None
    def getTitle(self):
        return self.title
    def newTitle(self, title):
        self.title = title
    def findTitle(self, title):
        return title in self.title

    def findInAny(self, find):
        if (find in self.title) or (find in self.meta) or (find in self.txt):
            return True
        else:
            return False
        

    # meta data
    def addMeta(self, meta):
        self.meta.append(meta)
        self.metaIdx += 1
    def getMeta(self):
        return self.meta
    def getNumbMeta(self):
        return self.metaIdx
    def eraseMeta(self):
        self.meta = []
        self.metaIdx = 0
    def findMeta(self, meta):
        return meta in self.meta

    # text
    def addTxtLine(self, txt):
        self.txt.append(txt)
        self.txtIdx += 1
    def getTxt(self):
        return self.txt
    def getNumbTxt(self):
        return self.txtIdx
    def eraseTxt(self):
        self.txt = []
        self.txtIdx = 0
    def findTxt(self, txt):
        return txt in self.txt

    # linked list of notes
    def addNextNote(self, note):
        self.nextNote = note
    def getNextNote(self):
        return self.nextNote



    

    

class noteContainer:
    def __init__(self):
        self.rootNote = None
        self.numbNotes = 0
        currentNote = self.rootNote
        while not(currentNote == None):
            currentNote = currentNote.getNextNote()
            self.numbNotes += 1

    def addNote(self, note):
        if self.rootNote == None:
            self.rootNote = note
        else:
            nextNote = self.rootNote.getNextNote()
            currentNote = self.rootNote()
            while not(nextNote == None):
                currentNote = self.nextNote
                nextNote = self.nextNote.getNextNote()
            currentNote.addNextNote(note)
        self.numbNotes += 1

    def getRootNote(self):
        return self.rootNote
    def getNumbNotes(self):
        return self.numbNotes
    def eraseNotes(self):
        self.numbNotes = 0
        self.rootNote = none


class fileHandler:
    def __init__(self):
        print "Open SaveIt data"

    def loadFile(self, fileName="saveit.dat"):
        try:
            self.dataFile = open(fileName, 'rb')
            self.container = pickle.load(self.dataFile)
            self.dataFile.close()
            return self.container
        except:
            self.container = noteContainer()
            return self.container

    def saveFile(self, fileName="saveit.dat"):
        self.dataFile = open(fileName, 'wb')
        pickle.dump(self.container, self.dataFile, pickle.HIGHEST_PROTOCOL)
        self.dataFile.close()
        return True


            
        

def saveItMenu():
    print "--------------------------------------------"
    print "-a / -add        Add note"
    print "-l / -list       List notes"
    print "-e / -edit       Edit note"
    print "-d / -delete     Delete note"
    print "--------------------------------------------"
    



def main(argv):
    saveItMenu()
    fhandler = fileHandler()
    container = fhandler.loadFile("saveit.dat")
    root = container.getRootNote()

    fhandler.saveFile("saveit.dat")


if __name__ == "__main__":
    main(sys.argv)
    
