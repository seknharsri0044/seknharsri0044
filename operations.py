import json
import string
import random
from json import JSONDecodeError
from datetime import datetime,date

def AutoGenerate_EventID():
    #generate a random Event ID
    Event_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return Event_ID

def Register(type,member_json_file,organizer_json_file,Full_Name,Email,Password):
    '''Register the member/ogranizer based on the type with the given details'''
    if type.lower()=='organizer':
        f=open(organizer_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
    else:
        f=open(member_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()


def Login(type,members_json_file,organizers_json_file,Email,Password):
    '''Login Functionality || Return True if successful else False'''
    d=0
    if type.lower()=='organizer':
        f=open(organizers_json_file,'r+')
    else:
        f=open(members_json_file,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Email"]==Email and content[i]["Password"]==Password:
            d=1
            break
    if d==0:
        f.close()
        return False
    f.close()
    return True

def Create_Event(org,events_json_file,Event_ID,Event_Name,Start_Date,Start_Time,End_Date,End_Time,Users_Registered,Capacity,Availability):
    
    '''Create an Event with the details entered by organizer'''
    create_event_file=open(events_json_file,'r+')
    event_file_1={     
            "Id":Event_ID,
            "Name":Event_Name,
            "Organizer":org,
            "Start Date":Start_Date,
            "Start Time":Start_Time,
            "End Date":End_Date,
            "End Time":End_Time,
            "Users Registered":Users_Registered,
            "Capacity":Capacity,
            "Seats Available":Availability
        }
    try:
        content=json.load(create_event_file)
        if event_file_1 not in content:
            content.append(event_file_1)
            create_event_file.seek(0)
            create_event_file.truncate()
            json.dump(content,create_event_file)
        
    except JSONDecodeError:
        list_1=[] 
        list_1.append(event_file_1)
        json.dump(list_1,create_event_file)
        create_event_file.close()


def View_Events(org,events_json_file):
    name=org
    file=open(events_json_file,'r+')
    content=json.load(file)
    if len(content) != 0:
        for i in range(len(content)):
            if content[i]["Organizer"]==org:
                dit=[{
                    "ID":content[i]['Id'],
                    "Name":content[i]['Name'],
                    "Organizer":content[i]['Organizer'],
                    "Start Date":content[i]['Start Date'],
                    "Start Time":content[i]['Start Time'],
                    "End Date":content[i]['End Date'],
                    "End Time":content[i]['End Time'],
                    "Users Registered":content[i]['Users Registered'],
                    "Capacity":content[i]['Capacity'],
                    "Seats Available":content[i]['Seats Available'],
                }]
                return dit
            else:
                pass
    else:
        return content
    file.close()

    

def View_Event_ByID(events_json_file,Event_ID):
    '''Return details of the event for the event ID entered by user'''
    event_file=open(events_json_file,'r+')
    event_file_content=json.load(event_file)
    for i in range(len(event_file_content)):
        if event_file_content[i]["Id"]==Event_ID:
              d=[{
                "ID":event_file_content[i]['Id'],
                "Name":event_file_content[i]['Name'],
                "Organizer":event_file_content[i]['Organizer'],
                "Start Date":event_file_content[i]['Start Date'],
                "Start Time":event_file_content[i]['Start Time'],
                "End Date":event_file_content[i]['End Date'],
                "End Time":event_file_content[i]['End Time'],
                "Users Registered":event_file_content[i]['Users Registered'],
                "Capacity":event_file_content[i]['Capacity'],
                "Seats Available":event_file_content[i]['Seats Available'],
            }]
    
    return d
   
    f.close()
    

def Update_Event(org,events_json_file,event_id,detail_to_be_updated,updated_detail):
    '''Update Event by ID || Take the key name to be updated from member, then update the value entered by user for that key for the selected event
    || Return True if successful else False'''
     file_1=open(events_json_file,'r+')
    content=json.load(file_1)
    organizer=org
    for i in range(len(content)):
        if content[i]["Id"]==event_id:
            if detail_to_be_updated=='Name':
                content[i]['Name']=updated_detail
            elif detail_to_be_updated=='Start Date':
                content[i]['Start Date']=updated_detail
            elif detail_to_be_updated=='Start Time':
                content[i]['Start Time']=updated_detail
            elif detail_to_be_updated=='End Date':
                content[i]['End Date']=updated_detail
            elif detail_to_be_updated=='End Time':
                content[i]['End Time']=updated_detail
            else:
                return False  
            file_1.seek(0)
            file_1.truncate()
            json.dump(content,file_1)
            file_1.close() 
    return True

    

def Delete_Event(org,events_json_file,event_ID):
    '''Delete the Event with the entered Event ID || Return True if successful else False'''
    file=open(events_json_file,'r+')
    content=json.load(file)
    id=event_ID
    for i in range(len(content)):
        if content[i]["Id"]==event_ID:
            del content[i]
            file.seek(0)
            file.truncate()
            json.dump(content, file)
            file.close()
            return True
        else:
            return False


def Register_for_Event(events_json_file,event_id,Full_Name):
    '''Register the logged in member in the event with the event ID entered by member. 
    (append Full Name inside the "Users Registered" list of the selected event)) 
    Return True if successful else return False'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''Write your code below this line'''
     file_1=open(events_json_file,'r+')
    content=json.load(file_1)
    for i in range(len(content)):
        if content[i]["Id"]==event_id:
            content[i]["Users Registered"].append(Full_Name)
            content[i]['Seats Available']-=1
    file_1.seek(0)
    file_1.truncate()
    json.dump(content, file_1)
    file_1.close()
    return True
       

def fetch_all_events(events_json_file,Full_Name,event_details,upcoming_ongoing):
    '''View Registered Events | Fetch a list of all events of the logged in memeber'''
    '''Append the details of all upcoming and ongoing events list based on the today's date/time and event's date/time'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''Write your code below this line'''
     f=open(events_json_file,'r+')
    content=json.load(f)
    for i in range(len(content)):
        if Full_Name in content[i]['Users Registered']:
            # if datetime. strptime(content[i]['Start Date'], '%Y-%m-%d')>=datetime.strptime(date_today, '%Y-%m-%d'):
            if datetime. strptime(content[i]['Start Date'], '%Y-%m-%d')<=datetime.strptime(date_today, '%Y-%m-%d'):
                upcoming_ongoing.append(content[i])
    return upcoming_ongoing
 
    

def Update_Password(members_json_file,Full_Name,new_password):
    '''Update the password of the member by taking a new passowrd || Return True if successful else return False'''
     file_1=open(members_json_file,'r+')
    content=json.load(file_1)
    for i in range(len(content)):
        if content[i]["Full Name"]==Full_Name:
            content[i]["Password"]=new_password
    file_1.seek(0)
    file_1.truncate()
    json.dump(content, file_1)
    file_1.close()
    return True


def View_all_events(events_json_file):
    '''Read all the events created | DO NOT change this function'''
    '''Already Implemented Helper Function'''
    details=[]
    f=open(events_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return details
    for i in range(len(content)):
        details.append(content[i])
    return details
