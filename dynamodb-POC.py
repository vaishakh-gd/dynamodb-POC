s='' #file s are proprietary information 
#since this code runs inside ec2 machine print statments are used for debugging
l=s.split(";")
d={}
import boto3

client = boto3.client('dynamodb',
                      aws_access_key_id='',
                      aws_secret_access_key='',
region_name='us-east-1'
                      )
for i in l:
    t=i.split("#")
    t1=t[1:]
    d[t[0]]=t[1]
#print(d)
import json

f = open("7.txt")
f1 = open("8.txt")
#line  must contain requestId: and LogicalTree --
a=[]

for i in f.readlines():
    if(("requestId:" in i) and ("LogicalTree" in i)):
        a1 = i.split("LogicalTree")
        a.append(a1)



#print(a)



#print("AAAAAAAAAAWWWWWWWWWWWWWW" ,a)
count=0
t=[]
dict1={}
b1=False
b2=False
for j in a:
    parsedLogicalTreeJson = json.loads(j[1])
    arr=[]
    b1=False
    b2=False
    print()
    print("--------------------------------------------------------")
    arr.append("these are filters")
    filter=[]
    for m in parsedLogicalTreeJson["nodes"]["1"]["filter"]:
        print("FILTER  ISSSSIS ",m["key"]["name"])
        b1=True
        arr.append(m["key"]["name"])
        filter.append(m["key"]["name"])
        #print("filter mehhh is ",filter)
    #print("filter blehhh is ",filter)
    arr.append("these are group by list of dimensions")
    if(len(filter)>=1):
        filter.sort()
        #print("filter keee--------------------------------------ehhh is ", filter)
    s='^'
    if(filter!=None and len(filter)!=0):
        s=s.join(filter)
    groupby=[]
    for q in parsedLogicalTreeJson["nodes"]["1"]["groupBy"]:
        print("GROUPBY  ISSSSIS ",q["name"])
        b2=True
        arr.append(q["name"])
        groupby.append(q["name"])

    x=''
    if(len(groupby)>=1):
        groupby.sort()
        p = '^'
        x=p.join(groupby)
    #print("loserrrr filter is ",filter)
        s+="|"+groupby[0]
    dict1[s]=1
    t.append(arr)
    if(b1==True and b2==True):
        count+=1
        print("COUNT IS ",count)


print("count is ",count)
print("length of dict is ",len(dict1))

dict2={}
c2=0
for i in dict1.keys():
    if("|" in i):
        dict2[i]=dict1[i]
        c2+=1

print("dict2 is ", dict2)
print("c2 is ",c2)
print("len of dict2 is ",len(dict2))
print("Total dict is is ",dict1)










    #f1.write(str(parsed2["nodes"]["1"]["filter"]))



'''
parsed2 = json.loads(a[1])
print("hi babes")
print()
print(parsed2["nodes"]["1"]["filter"])
print()
print()
'''

for i in dict2.keys():
    l = client.get_item(TableName="vaishakhsPOC",
                        Key={'projectionDimensionList': {"S": i}})
    print
    if ('Item' in l):
        print("yeepppPPPPPPPPPPPPPPPPPPPPPP")
        v = int(l['Item']['count']['N']) + 1
        v1=str(v)
        print("-------------------------------------------------------------")
        print("l is ", l)
        print("-------------------------------------------------------------")

        client.put_item(TableName="vaishakhsPOC", Item={
            'groupBy': {"S": "Key"},
            'projectionDimensionList': {"S":i},
            'count': {"N": v1},
            'alreadyProjectionPresent': {"S": "yes"
                }
            })
        print("WWWWWWWWWWWWWWWWWWWW-------------------------------------------------------------")
        print("l is ", l)
        print("WWWWWWWWWWWWWWWWWWWW-------------------------------------------------------------")
    else:
        print("noppPPPPPPPPPPPPPPPPPPPPPPP")
        client.put_item(TableName="vaishakhsPOC", Item={
            'groupBy': {"S": "Key"},
            'projectionDimensionList': {"S": i},
            'count': {"N": "1"},
            'alreadyProjectionPresent': {"S": "yes"}
        }
                        )






