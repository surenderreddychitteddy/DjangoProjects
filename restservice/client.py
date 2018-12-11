import requests





hostname="http://127.0.0.1"
port=8000
base_url = "%s:%s/"%(hostname,port)

study_hall_url = base_url+"expens/"
res=requests.post(study_hall_url,josn={
	"School":"1"
	"name":"kpavan"
	})
print res.Text
print res.status_code
