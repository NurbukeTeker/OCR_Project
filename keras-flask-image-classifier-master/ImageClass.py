class Imageclass():
    def __init__(self,name):
        self.name = name
        self.prediction = ""
        self.approved = False
        self.newlabel = ""

    def nameImage(self, filepath):
        self.name = filepath
    
    def labelImage(self, prediction):
        self.prediction = prediction
    
    
    def approved(self, approved):
        self.approved = approved
        self.newlabel = self.prediction


    def newLabel(self, newlabel):
         self.newlabel = newlabel
         self.approved = False
         