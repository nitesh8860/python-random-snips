import re
# sentence='''
# abdes./asdad21
# sdasd
# asd
# as
# das
# 12.234.121.33
# 3411^@%^@)(#_fgh'''

# pattern=re.compile(r'\d+\.\d+\.\d+\.\d+')
# matches=pattern.finditer(sentence)
# for match in matches:
#     print(match)
############################################################################
# emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]

# regex = re.compile(r'([\w.]+)+(.*)@(.*)')
# result = []
# for email in emails:
#     match = re.search(regex, email)
#     if match:
#         local = match.group(1).replace('.','')
#         domain = match.group(3)
#         resultemail = local+'@'+domain
#         result.append(resultemail)
# print(result)
##############################################################################
# str = "<b>foo</b> and <i>so on</i>"
# match = re.search(r'[^>]*', str)

# print(match.group())

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
print (re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1###\2', str))
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher