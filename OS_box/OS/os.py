import  os
import glob
os.chdir('Fle')
fle = glob.glob('*')
for name in fle :
    print(name)
    os.remove(name)
with open('1.txt','w',encoding='utf-8') as f:
    f.write('sdas')
os.makedirs('1122')  #创建文件夹
print(glob.glob('*'))
print(os.getcwd())