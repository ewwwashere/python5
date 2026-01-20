from datetime import datetime

date_formats = {
    'The Moscow Times': '%A, %B %d, %Y',
    'The Guardian': '%A, %d.%m.%y', 
    'Daily News': '%A, %d %B %Y'
}

dates = {
    'The Moscow Times': 'Wednesday, October 2, 2002',
    'The Guardian': 'Friday, 11.10.13',
    'Daily News': 'Thursday, 18 August 1977'
}

for newspaper, date_str in dates.items():
    date_obj = datetime.strptime(date_str, date_formats[newspaper])
    print(date_obj)
