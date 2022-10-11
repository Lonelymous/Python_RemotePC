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
            print(f"ascii: {ascii}")
            encoded = ascii << 1
            print(f"encoded: {encoded}")
            answer += chr(encoded)
        self.message = answer
        return answer

    def Decode(self):
        answer = ""
        for m in self.message:
            ascii = ord(m)
            print(f"ascii: {ascii}")
            decoded = ascii >> 1
            print(f"decoded: {decoded}")
            answer += chr(decoded)
        self.message = answer
        return answer