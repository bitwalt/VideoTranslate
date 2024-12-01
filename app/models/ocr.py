import easyocr

class EasyOcrModel:
    
    def __init__(self, cfg):
        self.lang = cfg['lang']
        self.reader = easyocr.Reader(['en'])
                
    def read_text(self, img):
        return self.reader.readtext(img)
                
                
    def display_text(bounds):
        text = []
        for x in bounds:
            t = x[1]
            text.append(t)
        text = ' '.join(text)
        return text 
