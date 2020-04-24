import json

class RestAPI:
    def __init__(self, database=None):
        self.database={
            'users':[],
        }

    def get(self, url, payload=None):
        if url != '/users':
            pass #Throw error
        else:
            if payload==None:
                return json.dumps({"users":self.database["users"]})

    #dumps = converts dict to string
    #loads = converts string to dict

    def post(self, url, payload=None):
        payload=json.loads(payload)
        
        if payload == None:
            #throw some error?
            pass
        if url == '/add':
            user = {"name": payload['user'], "owes": {}, "owed_by": {}, "balance": 0.0}
            self.database['users'].append(user)
            return  json.dumps(user)
        elif url == '/iou':  
            #find borrower/lender in db
            for user in self.database['users']:
                if user['name']==payload['lender']:
                    lender=user
                elif user['name']==payload['borrower']:
                    borrower=user
            
            #logging owes/owed_by
            lender['owed_by'][borrower['name']]=payload['amount']
            borrower['owes'][lender['name']]=payload['amount']
            
            #moving balances
            lender['balance']-=payload['amount']
            borrower['balance']+=payload['amount']

            #response info
            response={
                'users':sorted([borrower,lender], key= lambda i: i['name'])
            }
            print(response)
            return json.dumps(response)
        else:
            #Throw some error maybe?
            pass


restApi=RestAPI()

restApi.post('/add', json.dumps({"user": "Drew"}))
restApi.post('/add', json.dumps({"user": "Jocelyn"}))
restApi.post('/iou', json.dumps({"lender": "Drew", "borrower": "Jocelyn", "amount": 3.0}))
response=restApi.get('/users')
#print(response)