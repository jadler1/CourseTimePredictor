#requests: for api usage
#json: for using json returned by api
#csv: output csv file for data

import requests
import json
import csv

#params: parameters used to query API
params = {
    'key': YOUR_KEY_HERE,
    'term': '',
    'subject': ''
}

#fields: fields we will use in categorizing classes
fields = ['title','id','term','subject','instructor','catalog_num','room','seats','meeting_days','start_time','end_time','component','section']

with open('terms.json') as terms:
    term_dict = json.load(terms)

with open('subjects.json') as subjects:
    subject_dict = json.load(subjects)

for term in term_dict:
    params['term'] = term['id']
    for subject in subject_dict:
        params['subject'] = subject['symbol'].encode('ascii', 'ignore')
        response = requests.get('http://api.asg.northwestern.edu/courses/', params=params)
        # calling response.json() returns the response as a Python dictionary or list
        for res in response.json():
            response_obj=[]
            for field in fields:
                if type(res[field]) is unicode:
                    response_obj.append((res[field]).encode('ascii','ignore'))
                else:
                    response_obj.append(res[field])
            with open('course_data.csv', 'ab') as data:
                writer = csv.writer(data)
                writer.writerow(response_obj)
