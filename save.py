import time

def save_to_file():
# open함수는 파일을 읽어오고 해당 파일이 없다면 생성함
# file = open("job.csv", mode='w')
# print(file)
# return
    FN= str(time.strftime("%Y%m%d"))+".csv"
    with open(FN,mode='w') as f:
        f.write("Hello World")
    return