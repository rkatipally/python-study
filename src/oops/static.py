class WordTester:
    @staticmethod
    def is_palindrome(str, is_case_sensitive):
        str = ''.join(s for s in str if s.isalnum())
        if(is_case_sensitive):
            str = str.lower()
        for i in  range(len(str)//2):
            if(str[i] == str[-i-1]):
                continue
            else:
                return False
        return True

    @staticmethod
    def distinctWords(sentense):
        return set(sentense.split())


print(WordTester.distinctWords("My name is Raj, and people call me Raj"))
print(WordTester.is_palindrome("ABCCBA", False))
print(WordTester.is_palindrome("abcd", True))
