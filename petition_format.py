from jinja2 import Template
import csv, re, sys
from collections import OrderedDict


infile = csv.reader(open(sys.argv[1], 'rU'))

# skip headers
infile.next()

data = OrderedDict([])

for index, row in enumerate(infile):
	first_name, last_name, address1, city, state, zipcode = row
	data[index] = {'first_name':first_name, 'last_name':last_name, 'address1':address1, 'city':city, 'state':state, 'zipcode':zipcode}

print len(data)

t = Template(open('petition_format_template.html').read())
outfile = open(sys.argv[1]+'.html', 'w')
outfile.write(t.render({'data':data}))
outfile.close()
