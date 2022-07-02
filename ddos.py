import requests,threading

url = '' # target-url

data = { } # request-data

headers = { } # request-headers

def do_Requests():
    while True:
        resp = requests.post(url,data=data,headers=headers)
        print(resp.status_code)

threads = []

for i in range(20):
    t=threading.Thread(target=do_Requests)
    t.daemon = True
    threads.append(t)

for i in range(20):
    threads[i].start()

for i in range(20):
    threads[i].join()

