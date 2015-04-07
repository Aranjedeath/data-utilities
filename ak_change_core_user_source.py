import requests, sys, csv

url = 'https://donate.everytown.org/rest/v1/user/'

auth = ('leo', 'maig10022')


# input file must contain two columns: user_id, and new_source
infile = csv.reader(open(sys.argv[1]))
headers = infile.next()
print headers

# creates a response file to track results
outfile = csv.writer(open(sys.argv[1].replace('.csv', '_results.csv'), 'w'))

for row in infile:
	user_id, new_source = row
	data = {'source':new_source}
	
	try: 
		r = requests.put(url + user_id + '/', data=data, auth=auth)
	except Exception, error:
		r = error
	
	outfile.writerow([user_id, r])
# 

# 
# # Test
# test_user_id = '2120578'
# 
# try:
# 	r = requests.put(url + test_user_id + '/', data={'source':'test_source2'}, auth=auth)
# except Exception, error:
# 	r = error
# 
# print r
# 
