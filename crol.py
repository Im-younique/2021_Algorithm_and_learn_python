import requests
import os

url = 'http://210.95.181.23/6440000/CnNetAcademic/schlshpServcList?numOfRows=10&pageNo={num}'

lst = []
for i in range(1,51):
    result = requests.get(url.format(num=i)).json()
    if result['resultCode'] != '03':
        lst.append(result)
    print(i)

# title, field11, field02, field04, deptNm, field07, field08, field01
# field03, field05, field06, authorNm, field09, exp, field10


f = open("C:/Temp/학술용역.txt", 'w')

for line in lst:
    for items in line['items']:
            mylist = [items['title'], items['field11'], items['field02'], items['field04'], items['deptNm'], items['field07'],
                    items['field01'], items['field03'], items['field05'], items['field06'], items['authorNm'], items['field08'],
                    items['field09'], items['exp'], items['field10']]
            
            for i in range(len(mylist)):
                if mylist[i] == None:
                    mylist[i] = "None"
                else:
                    mylist[i] = mylist[i].replace('\r\n', "")
            
            for l in mylist:
                print(l + "|", file=f, end="")
            
            print(file=f)
            
            # t1,t2,t3,t4,t5,t6 = items['title'], items['field11'], items['field02'], items['field04'], items['deptNm'], items['field07']
            # t8,t9,t10,t11,t12,t13 = items['field01'], items['field03'], items['field05'], items['field06'], items['authorNm'], items['field08']
            # t14, t15, t16 = items['field09'], items['exp'], items['field10']
            
            # try:
            #     t1 = items['title'].replace('\r\n','')
            #     t2 = items['field11'].replace('\r\n','')
            #     t3 = items['field02'].replace('\r\n','')
            #     t4 = items['field04'].replace('\r\n','')
            #     t5 = items['deptNm'].replace('\r\n','')
            #     t6 = items['field07'].replace('\r\n','')
            #     t8 = items['field01'].replace('\r\n','')
            #     t9 = items['field03'].replace('\r\n','')
            #     t10 = items['field05'].replace('\r\n','')
            #     t11 = items['field06'].replace('\r\n','')
            #     t12 = items['authorNm'].replace('\r\n','')
            #     t13 = items['field08'].replace('\r\n','')
            #     t14 = items['field09'].replace('\r\n','')
            #     t15 = items['exp'].replace('\r\n','')
            #     t16 = items['field10'].replace('\r\n','')
            # except:
            #     t1 = items['title']
            #     t2 = items['field11']
            #     t3 = items['field02']
            #     t4 = items['field04']
            #     t5 = items['deptNm']
            #     t6 = items['field07']
            #     t8 = items['field01']
            #     t9 = items['field03']
            #     t10 = items['field05']
            #     t11 = items['field06']
            #     t12 = items['authorNm']
            #     t13 = items['field08'].replace('\r\n','')
            #     t14 = items['field09'].replace('\r\n','')
            #     t15 = items['exp'].replace('\r\n','')
            #     t16 = items['field10'].replace('\r\n','')

            # print(t1, "|", t2, "|", t3, "|", t4, "|", t5, "|", t6, "|", t8, "|", t9, "|", t10, "|", t11, "|", t12, "|", t13, "|", t14, "|", t15, "|", t16, file=f)


f.close()