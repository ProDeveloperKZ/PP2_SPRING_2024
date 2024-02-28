#ex1 
import re

def match_ab_string(s):
    pattern = r"a{1}b*"
    return bool(re.match(pattern,s))
    
txt = ["ab", "abb", "abbb", "abc", "ba", ""]
for i in txt:
    if match_ab_string(i):
        print(i)
    
    
#ex 2
import re

def match_a3b_string(s):
    pattern = r"ab{2,3}"
    return bool(re.match(pattern,s))
    
txt = ["ab", "abb", "abbb", "abc", "ba", ""]
for i in txt:
    if match_a3b_string(i):
        print(i)
    
#ex 3
import re

def sequences(s):
    pattern = r"[a-z]"
    return bool(re.match(pattern, s))
    
txt = ["Asen", "arsen", "KBTU", "bombcladdd_dd"]
for i in txt:
    if sequences(i):
        print(i)
     
#ex 4
import re

def sequences(s):
    pattern = r"[A-Z][a-z]"
    return bool(re.match(pattern, s))
    
txt = ["Arnur", "arnur", "kBTU", "Bombcladdddd", "BBBombacladd"]
for i in txt:
    if sequences(i):
        print(i)
    
#ex 5
import re
def my_regex(s):
    pattern = r"^a.*b$"
    return bool(re.match(pattern,s))

txt = ["abbb", "KBTU", "Bombclatt", "arnurb", "ab"]
for i in txt:
    if my_regex(i):
        print(i)
    
#ex 6
import re 
def replace_regex(s):
    pattern = r"[,\s.]"
    return re.sub(pattern,":", s)

txt = "Пах-пах-пах, кандай гажап иис"
new_txt = replace_regex(txt)
print(new_txt)


#ex 7
def snake_to_camel(s):
    words = s.split('_')
    camel = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel

snake_s = "arnur_bombaclatttt_kbtu_pp2"
camel_s = snake_to_camel(snake_s)
print("First word: ", snake_s)
print("Second word: ", camel_s )


#ex 8
import re
def Split_uppers(s):
    return re.findall(r"[A-Z][a-z]*|[a-z]", s)

my_word = "ItsAnExample"
print(my_word)
print(Split_uppers(my_word))


#ex 9 
import re

def insert_spaces(s):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", s)

txt = "ThisIsAStringWithUppercaseLetters"
print(txt)
print(insert_spaces(txt))


#ex 10
