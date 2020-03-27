'''
Example 1: valid credit card number
4539 1488 0343 6467
The first step of the Luhn algorithm is to double every second digit, starting from the right. We will be doubling

4_3_ 1_8_ 0_4_ 6_6_
If doubling the number results in a number greater than 9 then subtract 9 from the product. The results of our doubling:

8569 2478 0383 3437
Then sum all of the digits:

8+5+6+9+2+4+7+8+0+3+8+3+3+4+3+7 = 80
If the sum is evenly divisible by 10, then the number is valid. This number is valid!

Example 2: invalid credit card number
8273 1232 7352 0569
Double the second digits, starting from the right

7253 2262 5312 0539
Sum the digits

7+2+5+3+2+2+6+2+5+3+1+2+0+5+3+9 = 57
57 is not evenly divisible by 10, so this number is not valid.
'''
import re

class Luhn:
    def __init__(self, card_num):
        self.card_num=card_num.replace(' ', '')
        
    def valid(self):
        card_num=list(self.card_num)
        for i in range(len(card_num)):
            if card_num[i].isdigit() == False:
                return False
            card_num[i]=int(card_num[i])

        if len(card_num) < 2:
            return False

        for i in range(len(card_num)-2,-1,-2):
                if card_num[i]*2<=9:
                    card_num[i]*=2
                else:
                    card_num[i]=card_num[i]*2-9
        
        return True if sum(card_num) % 10 is 0 else False

test=Luhn("4539 1488 0343 6467")

print(test.valid())