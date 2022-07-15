number = input("숫자를 입력하세요.")
last_ch = number[-1]

if last_ch in "02468":
    print("{}은(는) 짝수입니다.".format(number))
    
if last_ch in "13579":
    print("{}은(는) 홀수입니다.".format(number))