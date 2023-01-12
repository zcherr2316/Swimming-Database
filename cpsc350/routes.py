
from cpsc350 import dbtour
from flask import render_template, url_for, request, redirect
import mariadb, redis
from pymongo import MongoClient, ASCENDING, DESCENDING

@dbtour.route("/")
def landing():
	if "event" in request.args and request.args['event'] != "All":
		conn = mariadb.connect(user='zack', password='coolpassword', host="localhost", port=3306, database='swimming')	
		cur = conn.cursor()
		event = request.args["event"]
		event = event.split(',')
		cur.execute("select * from swimmers natural join races where Distance=? and Stroke=? limit 10",(event[0],event[1]))
		races = cur.fetchall()
		cur.execute("select distinct Distance, Stroke from races")
		events = cur.fetchall()
		conn.close()
		r = redis.StrictRedis(password="password123", charset="utf-8",decode_responses=True)
		conferenceList = r.smembers("conferences")
		conference = r.smembers("Metropolitan")
		year = "2022"
		records = list(r.hgetall(year).items())
		yearList = r.smembers("years")
		mc = MongoClient("mongodb://localhost:27017")
		db = mc['swimming']
		collection = 'swimming'
		schoolList = db[collection].find({"name":{'$exists':True}},{'name':True,"_id":False})
		return render_template("landing.html", races=races, events=events, conferenceName="Metropolitan", conference=conference, conferenceList=conferenceList, year=year, records=records, yearList=yearList, schoolList=schoolList)
	elif "conference" in request.args and "school" not in request.args:
		conn = mariadb.connect(user='zack', password='coolpassword', host="localhost", port=3306, database='swimming')
		cur = conn.cursor()
		cur.execute("select * from swimmers natural join races limit 10")
		races = cur.fetchall()
		cur.execute("select distinct Distance, Stroke from races")
		events = cur.fetchall()
		conn.close()
		r = redis.StrictRedis(password="password123", charset="utf-8",decode_responses=True)
		conferenceList = r.smembers("conferences")
		conference = r.smembers(request.args["conference"])
		year = "2022"
		records = list(r.hgetall(year).items())
		yearList = r.smembers("years")
		mc = MongoClient("mongodb://localhost:27017")
		db = mc['swimming']
		collection = 'swimming'
		schoolList = db[collection].find({"name":{'$exists':True}},{'name':True,"_id":False})
		return render_template("landing.html", races=races, events=events,conferenceName=request.args["conference"], conference=conference, conferenceList=conferenceList, year=year, records=records, yearList=yearList, schoolList=schoolList)
	elif "year" in request.args:
		conn = mariadb.connect(user='zack', password='coolpassword', host="localhost", port=3306, database='swimming')
		cur = conn.cursor()
		cur.execute("select * from swimmers natural join races limit 10")
		races = cur.fetchall()
		cur.execute("select distinct Distance, Stroke from races")
		events = cur.fetchall()
		conn.close()
		r = redis.StrictRedis(password="password123", charset="utf-8",decode_responses=True)
		conferenceList = r.smembers("conferences")
		conference = r.smembers("Metropolitan")
		year = request.args["year"]
		records = list(r.hgetall(year).items())
		yearList = r.smembers("years")
		mc = MongoClient("mongodb://localhost:27017")
		db = mc['swimming']
		collection = 'swimming'
		schoolList = db[collection].find({"name":{'$exists':True}},{'name':True,"_id":False})
		return render_template("landing.html", races=races, events=events,conferenceName="Metropolitan", conference=conference, conferenceList=conferenceList, year=year, records=records, yearList=yearList, schoolList=schoolList)
	elif "add" in request.args:
		conn = mariadb.connect(user='zack', password='coolpassword', host="localhost", port=3306, database='swimming')
		cur = conn.cursor()
		cur.execute("select * from swimmers natural join races limit 10")
		races = cur.fetchall()
		cur.execute("select distinct Distance, Stroke from races")
		events = cur.fetchall()
		conn.close()
		r = redis.StrictRedis(password="password123", charset="utf-8",decode_responses=True)
		r.sadd(request.args["conference"],request.args["school"])
		conferenceList = r.smembers("conferences")
		conference = r.smembers(request.args["conference"])
		year = "2022"
		records = list(r.hgetall(year).items())
		yearList = r.smembers("years")
		mc = MongoClient("mongodb://localhost:27017")
		db = mc['swimming']
		collection = 'swimming'
		schoolList = db[collection].find({"name":{'$exists':True}},{'name':True,"_id":False})
		return render_template("landing.html", races=races, events=events,conferenceName=request.args["conference"], conference=conference, conferenceList=conferenceList, year=year, records=records, yearList=yearList, schoolList=schoolList)
	elif 'keyfilter' in request.args:
		conn = mariadb.connect(user='zack', password='coolpassword', host="localhost", port=3306, database='swimming')
		cur = conn.cursor()
		cur.execute("select * from swimmers natural join races limit 10")
		races = cur.fetchall()
		cur.execute("select distinct Distance, Stroke from races")
		events = cur.fetchall()
		conn.close()
		r = redis.StrictRedis(password="password123", charset="utf-8",decode_responses=True)
		conferenceList = r.smembers("conferences")
		conference = r.smembers("Metropolitan")
		year = "2022"
		records = list(r.hgetall(year).items())
		yearList = r.smembers("years")
		mc = MongoClient("mongodb://localhost:27017")
		db = mc['swimming']
		collection = 'swimming'
		schoolList = db[collection].find({request.args['key']:request.args['value']},{'name':True,"_id":False})
		return render_template("landing.html", races=races, events=events,conferenceName="Metropolitan", conference=conference, conferenceList=conferenceList, year=year, records=records, yearList=yearList, schoolList = schoolList)
	else:
		conn = mariadb.connect(user='zack', password='coolpassword', host="localhost", port=3306, database='swimming')
		cur = conn.cursor()
		cur.execute("select * from swimmers natural join races limit 10")
		races = cur.fetchall()
		cur.execute("select distinct Distance, Stroke from races")
		events = cur.fetchall()
		conn.close()
		r = redis.StrictRedis(password="password123", charset="utf-8",decode_responses=True)
		conferenceList = r.smembers("conferences")
		conference = r.smembers("Metropolitan")
		year = "2022"
		records = list(r.hgetall(year).items())
		yearList = r.smembers("years")
		mc = MongoClient("mongodb://localhost:27017")
		db = mc['swimming']
		collection = 'swimming'
		schoolList = db[collection].find({"name":{'$exists':True}},{'name':True,"_id":False})
		return render_template("landing.html", races=races, events=events,conferenceName="Metropolitan", conference=conference, conferenceList=conferenceList, year=year, records=records, yearList=yearList, schoolList = schoolList)

@dbtour.route ("/add_data")
def add_data():
	if "submitted" in request.args:
		conn = mariadb.connect(user='zack', password='coolpassword', host="localhost", port=3306, database='swimming')	
		cur = conn.cursor()
		fname = request.args["Firstname"]
		lname = request.args["Lastname"]
		age = int (request.args["Age"])
		classlevel = request.args["Class"]
		school = request.args["School"]
		distance = int (request.args["Distance"])
		stroke = request.args["Stroke"]
		minutes = int (request.args["Minutes"])
		seconds = int (request.args["Seconds"])
		decimals = int (request.args["Decimals"])
		place = request.args["Place"]
		date = request.args["Date"]
		if age != '' and classlevel != '' and school != '':
			cur.execute("insert into swimmers (Firstname, Lastname, Age, Class, School) values (?,?,?,?,?)", (fname,lname,age,classlevel,school))
			conn.commit()
		if distance != '' and stroke != '' and minutes != '' and seconds != '' and decimals != '' and place != '' and date != '':
			cur.execute("insert into races (Distance, Stroke, Minutes, Seconds, Decimals, PLace, Date, Firstname, Lastname) values (?,?,?,?,?,?,?,?,?)",(distance,stroke,minutes,seconds,decimals,place,date,fname,lname))
			conn.commit()
		conn.close()
		return redirect(url_for('landing'))
	else:
		return render_template("add_data.html")

@dbtour.route ("/school_data")
def school_data():
	if 'update' in request.args:
		mc = MongoClient("mongodb://localhost:27017")
		db = mc['swimming']
		collection = 'swimming'
		school = request.args['name']
		for key in request.args:
			if key != 'update':
				db[collection].update_one({"name" : school},{"$set" : {key:request.args[key]}})
		return redirect(url_for('landing'))
	elif 'add' in request.args:
		mc = MongoClient("mongodb://localhost:27017")
		db = mc['swimming']
		collection = 'swimming'
		school = request.args['name']
		db[collection].update_one({'name':school},{"$set":{request.args['key']:request.args['value']}})
		return redirect(url_for('landing'))
	else:
		mc = MongoClient("mongodb://localhost:27017")
		db = mc['swimming']
		collection = 'swimming'
		schoolData = db[collection].find({"name": request.args['school']},{"_id":False})
		school = request.args['school']
		return render_template("school_data.html", schoolData=schoolData, school=school)
