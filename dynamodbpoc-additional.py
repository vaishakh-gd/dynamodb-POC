import boto3

client = boto3.client('dynamodb',
                      aws_access_key_id='',
                      aws_secret_access_key='',
region_name='us-east-1'
                      )

'''
client.create_table(TableName="vaishakhsPOC",
                    KeySchema=[
    {
        "AttributeName": "projectionDimensionList" ,
        'KeyType' : "HASH"
    }
],AttributeDefinitions=[
        {
            "AttributeName": "projectionDimensionList" ,
            'AttributeType': "S"
        } ],
                    ProvisionedThroughput={
                        'ReadCapacityUnits': 123,
                        'WriteCapacityUnits': 123
                    },
                    )
'''

client.put_item(TableName="vaishakhsPOC",Item={
'groupBy':{"S":"Key"},
'projectionDimensionList':{"S":'Brand^DSP^DataSource^Something2|DSP'},
    'count':{"N":"1996"}
})


l=client.get_item(TableName="vaishakhsPOC",Key={'projectionDimensionList':{"S":'Brand^DSP^DataSource^Something23|DSP'}})

print(l)
# it returns of type dictionary
if('Item' in l):
    print("yeepppPPPPPPPPPPPPPPPPPPPPPP")
else:
    print("noppPPPPPPPPPPPPPPPPPPPPPPP")

print(type(l['Item']))

print(l['Item']['count']['N'])

v=int(l['Item']['count']['N'])+100

print(v)

#print(client.list_tables())