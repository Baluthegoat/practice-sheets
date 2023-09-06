def romanToInt(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(s)):
        print("I: " + str(i))
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            print("IF: " + str(rom_val[s[i]]))
            print("IF - 1: " + str(rom_val[s[i - 1]]))
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            print("ELSE: " + str(rom_val[s[i]]))
            int_val += rom_val[s[i]]
    print("ANSWER: " + str(int_val))
    return int_val
# def romanToInt(s: str) -> int:
#         rom_val = {
#         'I':1,
#         'V':5,
#         'X':10,
#         'L':50,
#         'C':100,
#         'D':500,
#         'M':1000,
#         }
#         # print(s)
#         sum = 0
#         if len(s) == 1:
#             return s
#         elif len(s) == 2 and (rom_val[s[1]] > rom_val[s[0]]):
#               print(rom_val[s[1]]- rom_val[s[0]])
#               return rom_val[s[1]]- rom_val[s[0]]
#         elif len(s) == 2 and (rom_val[s[1]] < rom_val[s[0]]):
#               print(rom_val[s[1]] + rom_val[s[0]])
#               return rom_val[s[1]] + rom_val[s[0]]
#         else:
            
#             for i in range(len(s)):
                
#                 # print(i + pointer + 2)
#                 print('P: ' + str(pointer))
#                 if (i + pointer + 2) > len(s):
#                      break
#                 elif (rom_val[s[i + pointer + 2]] > rom_val[s[i + pointer]]):
                    
#                     sum = sum + rom_val[s[i + pointer + 2]] - rom_val[s[i + pointer]] 
                    
#                     pointer = pointer + 1
#                 elif (rom_val[s[i + pointer + 2]] < rom_val[s[i + pointer]]):
#                     sum = sum + rom_val[s[i + pointer]]  
            
#             # print(sum)
#             return sum
                    
              

romanToInt('LVIII')