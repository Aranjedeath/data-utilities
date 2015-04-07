import requests, sys, csv

url = 'https://donate.everytown.org/rest/v1/action/'
auth = ('leo', 'maig10022')


# delete file must contain two columns: action_id, then user_id
deletes = [x.split(',')[0] for x in open(sys.argv[1])]

with open(sys.argv[1].replace('.csv', '_results.csv'), 'a') as outfile:
	outfile.write('action_id,response_code\r\n')

for delete in deletes:
	try: 
		r = requests.delete(url + delete + '/', auth=auth)
	except Exception, e:
		print e
	with open(sys.argv[1].replace('.csv', '_results.csv'), 'a') as outfile:
		outfile.write('{0},{1}\r\n'.format(delete, str(r)))

