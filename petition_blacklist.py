from blacklist import blacklist, titlecase
import csv, sys

infile = csv.reader(open(sys.argv[1], 'rU'))
headers = infile.next()

clean_data = []
blacklist_data = []

for row in infile:
	if blacklist(row[0]) or blacklist(row[1]) or blacklist(row[2], 50) or blacklist(row[3]):
		blacklist_data.append(titlecase(row))
	else:
		clean_data.append(titlecase(row))

clean_outfile = csv.writer(open(sys.argv[1] + '_good.csv', 'w'))
clean_outfile.writerow(headers)
clean_outfile.writerows(clean_data)

blacklist_outfile = csv.writer(open(sys.argv[1] + '_bad.csv', 'w'))
blacklist_outfile.writerow(headers)
blacklist_outfile.writerows(blacklist_data)

