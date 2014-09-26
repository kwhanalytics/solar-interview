"""
Randomly generate site data for the interview question.

NOTE: As the interviewee, you shouldn't need to run or modify this code.
The code was used to generate the sites in the database.
"""

# local modules
import os
import random
import math
import datetime
random.seed('Snow White')

# third party modules
import sqlite3

# constants
MAXAGE = 4*365
DATABASENAME = './performance.db'

def pert(value):
    """ pertubate a value """
    return value * (random.random()*.4 + 0.8)

def age(maxage):
    """ Function to randomly choose site age"""
    return random.random() * maxage

def monthlybase(month):
    """ Return a base irradiance value for a month of the year """
    base = 800.0
    fluctuation = 200.0 * math.cos((month - 6) / 12.0 * math.pi)
    return base + fluctuation


def run():
    """ Run the generator! """
    if os.path.exists(DATABASENAME):
        os.remove(DATABASENAME)
    con = sqlite3.connect(DATABASENAME)
    createdatabase(con)
    populate(con)



def populate(con):
    """ populate the database with data """
    sitesdictionary = {'Doc': 1.10,
                       'Dopey': 0.97,
                       'Bashful': 1.00,
                       'Grumpy': 0.70,
                       'Sneezy': 0.91,
                       'Sleepy': 1.20,
                       'Mickey Mouse': 1.05,
                       'Happy': 1.11}
    for systemname, performance in sitesdictionary.items():
        data = dailydata(performance)
        uploadsite(con, systemname, data)

def dailydata(performance):
    """ Generate daily data for a site, randomly choosing it's age """

    siteagedays = age(MAXAGE)
    startdate = datetime.datetime(2014, 1, 1)
    currentdate = startdate
    data = []
    while (startdate - currentdate).days < siteagedays:
        month = currentdate.month
        base = monthlybase(month)
        actualkwh = pert(base * performance)
        expectedkwh = pert(base)
        data.append([currentdate, actualkwh, expectedkwh])
        currentdate -= datetime.timedelta(days=1)
    return data

def createdatabase(con):
    """ create database tables """

    cur = con.cursor()

    createsystemstable = """
    create table systems (
        systemid integer primary key,
        name varchar(100)
    );
    """
    cur.execute(createsystemstable)

    createdatatable = """
    create table data (
        systemid integer,
        datatime datetime,
        actualkwh float,
        expectedkwh float,
        primary key (systemid, datatime)
    );
    """
    cur.execute(createdatatable)

    con.commit()
    cur.close()

def uploadsite(con, systemname, data):
    """ upload the data into the database """

    cur = con.cursor()

    # systemname
    cur.execute('insert into systems (name) values (?)', [systemname,])

    # systemid
    cur.execute('select systemid from systems where name = ?', [systemname,])
    rows = cur.fetchall()
    systemid = rows[0][0]

    # data
    insertdata = '''
    insert into data 
    (systemid, datatime, actualkwh, expectedkwh)
    values
    ({systemid}, ?, ?, ?) '''.format(systemid=systemid)
    cur.executemany(insertdata, data)

    con.commit()
    cur.close()




if __name__ == "__main__":
    run()
