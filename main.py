def program(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele  
    return str1 
  
text = "aba"
s = list(reversed(text))
fungsi = program(s)
# print(program(s)) 
if fungsi == text:
  print ("sama / palindrome")
else:
  print ("Tidak palindrome")
