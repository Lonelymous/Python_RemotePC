class Message:
    message = ""

    def __init__(self, message):
        self.message = message

    def GetString(self):
        return self.message

    def Encode(self):
        answer = ""
        for m in self.message:
            ascii = ord(m)
            encoded = ascii << 1
            answer += chr(encoded)
        self.message = answer
        return answer

    def Decode(self):
        answer = ""
        for m in self.message:
            ascii = ord(m)
            decoded = ascii >> 1
            answer += chr(decoded)
        self.message = answer
        return answer