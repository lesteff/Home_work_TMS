class SuperStr(str):

    def is_repeatance(self, s):
        if not s or not self:
            return False
        if len(self) % len(s) != 0:
            return False
        repeat_count = len(self) // len(s)
        return self == s * repeat_count

    def is_palindrom(self):
        lower_str = self.lower()
        return lower_str == lower_str[::-1]

s1 = SuperStr("abcabcabc")
print(s1.is_repeatance("abc"))
print(s1.is_repeatance("ab"))

s2 = SuperStr("aaaa")
print(s2.is_repeatance("a"))

s3 = SuperStr("Racecar")
print(s3.is_palindrom())

s4 = SuperStr("hello")
print(s4.is_palindrom())

s5 = SuperStr("")
print(s5.is_palindrom())
print(s5.is_repeatance("a"))