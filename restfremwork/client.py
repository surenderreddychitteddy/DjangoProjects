import  requests
hostname="http://127.0.0.1"
port=8000
base_url="%s:%s/"%(hostname,port)
product_url=base_url+"product/"
resp=requests.post(product_url,
	json={"Customer":2,"des":"aaaaafffefdhc"})
resp=requests.get(product_url)
print resp.status_code
print resp.text
