import datetime
today = datetime.datetime.today()

str_s = input("대화할까요?")

if str_s == "그래":
    print("반가워요!")

elif str_s == "안녕하세요":
    print("안녕안녕~")

elif "몇 시" in str_s:
    print("지금은 {}시예요!".format(today.hour))

else:
    print(str_s)