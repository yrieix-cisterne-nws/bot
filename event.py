import datetime as dt

eventendoftimer = dt.datetime(2025, 9, 16, 20, 0)
actualtime = dt.datetime.now()

isitactive = eventendoftimer - actualtime


