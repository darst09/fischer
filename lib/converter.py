class Converter:    
    #----------------------------------
    #перевод текста в строку шестнадцатеричный формат    
    #----------------------------------
    def textToHex(self, sText):
        utf8 = sText.encode("utf-8")
        sHex = utf8.hex()
        return sHex
    
    #----------------------------------
    #перевод строки в шестнадцатеричном формате в текст
    #----------------------------------    
    def hexToText(self, sHex):
        utf8 = bytes.fromhex(sHex)
        sText = utf8.decode('utf-8')
        return sText