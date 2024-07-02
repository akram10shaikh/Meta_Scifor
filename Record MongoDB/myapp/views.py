from django.shortcuts import render
import pymongo
from bson.objectid import ObjectId

# Create your views here.

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['akram']
collection = db['newcollection']


def home(request):
	return render(request,'index.html')

def add_data(request):
	if request.method == "POST":
		name = request.POST.get('n1')
		city = request.POST.get('c1')
		phone = request.POST.get('p1')

		data = {
		"name":name,
		"city":city,
		"phone":phone,
		}
		
		collection.insert_one(data)
		message = "Data store successfully"
		return render(request,'index.html',{'message':message})


def showdata(request):
	data = collection.find()
	return render(request,'show.html',{'data':data})

def update_data(request,id):
	object_id = ObjectId(id)
	data = collection.find({"_id":object_id})
	return render(request,'update.html',{'data':data})

def edit(request):
	if request.method == 'POST':
		name = request.POST.get('n1')
		city = request.POST.get('c1')
		phone = request.POST.get('p1')


		