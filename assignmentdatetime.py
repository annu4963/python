# import datetime
# d=datetime.date.today()
# # time delta helps to postpond & prepond the date
# tdelta= datetime.timedelta(days=7)
# print(d+tdelta)
# bday=datetime.date(2023,1,26)
# tillday=bday-d
# print(tillday)
# print(d.year)
# print(d.month)
# print(d.day)

# import datetime
# t=datetime.time(9,20,30,2000)
# print(t)

# import datetime
# dt=datetime.datetime(2019,9,2,9,20,30,20000)
# print(dt.time())
# print(dt.date())

# import datetime
# dt=datetime.datetime.today()
# dn=datetime.datetime.now()
# dutc=datetime.datetime.utcnow()
# print(dt)
# print(dn)
# print(dutc)

import datetime
jobs=[
    {
        'title':'python Devloper',
        'company':'Eprabidhi Nepal',
        'location':'putalisadak',
        'date_posted':'2020-05-04',
        'description':'Python developer with 5 years of experience',
        'salary':100000
    },
    {
        'title':'Java Devloper',
        'company':'Facebook',
        'location':'Menlo Park,CA',
        'date_posted':'2022-12-05',
        'description':'Java developer with 5 years of experience',
        'salary':200000
    }
]

today_date=datetime.date.today()
expired_job=[]
for job in jobs:
    job_date=datetime.datetime.strptime(
        job['date_posted'],'%Y-%m-%d').date()
    if job_date<today_date:
        expired_job.append(job)

print(expired_job)

