# VehicleAssignmentDjango

`python manage.py loaddata vehicle` - this is to load the fixture


`python manage.py dumpdata vehicleAPI` #To get the data dump, by default it will output on console in json format

`python manage.py loaddata vehicle` #to loaddata, it will refer to the fixture folder

`python manage.py makemigrations vehicleAPI` #To generate migrations from model

`python manage.py createsuperuser` #to create superuser

`python manage.py migrate`  #to execute all migrations

`python manage.py sqlmigrate <appname> <migration number eg. 0001 or 0004>`

`python manage.py migrate vehicleAPI 0001` #to migrate particular query


`python manage.py sqlmigrate vehicleAPI 0002` #this is to check the corresponding sql query for given migration



# Pre-requisite: 
1. Latest version of python should be installed (v 3.8.10)
2. Git for cloning or alternatively download zip from https://github.com/srijanrajput/VehicleAssignmentDjango

# Steps to install project
1. Clone this project `git clone https://github.com/srijanrajput/VehicleAssignmentDjango.git`
2. Go to terminal and enter `cd <location of project folder>\demoAPI`
3. Run server using `python manage.py runserver`

### open http://127.0.0.1:8000/ on browser. This will show the admin panel
### Username: `admin`     Password: `admin`

Here we have 2 tables

Vehicle: Vehicle is the master table
Vehicle distance logs: This is the child table that stores the daily data for each vehicle


## Assumptions
* The data for vehicle is entered daily
* In the 'Vehicle distance logs' we are putting the cumilative data for distance. 
  e.g. Distance on 1st Jan 30KM, Distance travelled on second is 20KM so for 2nd we will enter 30KM + 20 KM = 50 Km
  This distance is always cumilative. 
  
  Since there is limit for odometer that on some websites is 999,999 after which it will go to 000000 and max int value is 2,147,483,647 therefore it can save the large cumilative distances

  Benefit of saving the distance in cumilative will save time in fetching all the data between given ranges and then making calculation. So if we want to calculate distance between 2nd day till now we can simple substract the distance from day 1
 

## APIs

For getting the distance for a particular vehicle for given date:

1. API for fetching distance for particular vehicle from given date 
`http://localhost:8000/api/vehicles/<Unit>/<yyyymmdd>`
where Unit is the vehicle Unit Id and date in the mentioned format

2. For update vehicle data using `PATCH` http request here `mileage` is the mileage of the vehicle and `cumilativeDistance` being the cumilative distance on the given day. This is unique and hence there can be one entry for any day. For testing these values can be set from admin
`http://localhost:8000/api/vehicles/<Unit>`
![image](https://user-images.githubusercontent.com/9460937/120722493-cc370700-c49d-11eb-8aaf-7b7fb4f6b29a.png)

