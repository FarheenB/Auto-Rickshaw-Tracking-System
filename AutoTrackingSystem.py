import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
from webapp2_extras import json
import urllib2


class RFIDLatLong(ndb.Model):
    rfid_name = ndb.StringProperty(indexed=True, default=None)
    location = ndb.StringProperty(indexed=True)
    latitude = ndb.StringProperty(indexed=True, default=None)
    longitude = ndb.StringProperty(indexed=True, default=None)
    
    def add_RFID(self, rfid_name = None, location = None, latitude = None ,longitude = None):
        rfid = RFIDLatLong(id=location)
        rfid.rfid_name = rfid_name
        rfid.location = location
        rfid.latitude = latitude
        rfid.longitude = longitude
        rfid.put()

class AutoLocationTrack(ndb.Model):
    auto_number = ndb.StringProperty(indexed=True, default=None)
    path = ndb.StringProperty(indexed=True, default=None)
    current_rfid = ndb.StringProperty(indexed=True, default=None)
    last_rfid = ndb.StringProperty(indexed=True, default=None)
    latitude = ndb.StringProperty(default=None)
    longitude = ndb.StringProperty(default=None)
    distance = ndb.StringProperty(default=None)
    time_to_reach = ndb.StringProperty(default=None)
    availability = ndb.StringProperty(default="Vacant")
    updated_on = ndb.DateTimeProperty(indexed=True, required=True)

    def add_auto(self, auto_number = None, path = None, current_rfid = None ,last_rfid = None, availability=None, updated_on=None):
        rfid = AutoLocationTrack(id=auto_number)
        rfid.auto_number = auto_number
        rfid.path = path
        rfid.current_rfid = current_rfid
        rfid.last_rfid = last_rfid
        rfid.availability = availability
        import datetime
        rfid.updated_on = datetime.datetime.now()
        rfid.put()
    
    def update_auto_path(self, auto_number=None, current_rfid=None, availability = None):
        auto = AutoLocationTrack.get_by_id(auto_number)
        if current_rfid !='':
            temp = auto.current_rfid
            auto.current_rfid = current_rfid
            auto.last_rfid = temp
            auto.path = auto.path + "->" + current_rfid
        
        import datetime
        auto.updated_on = datetime.datetime.now()
        auto.availability = availability
        auto.put()


class AutoDummyData(webapp2.RequestHandler):
    

    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        # import json
        
        auto_dummy = AutoLocationTrack()
        auto_number = "Auto5"

        auto_dummy.add_auto(auto_number = auto_number, path = "IIT_1", current_rfid = "IIT_1" ,last_rfid = None)

        auto_dummy.update_auto_path(auto_number, "IIT_2")
        auto_dummy.update_auto_path(auto_number, "IIT_3")
        auto_dummy.update_auto_path(auto_number, "IIT_4")
        auto_dummy.update_auto_path(auto_number, "IIT_5")



class DummyData(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        import json
        dummy_rfid = RFIDLatLong()

        lat_long = {
            'lat':'19.1246',
            'long': '72.9160'

        }
        dummy_rfid.add_RFID(rfid_name="IIT_1", location="IIT Main Gate",latitude = lat_long['lat'] , longitude= lat_long['long'])
        
        dummy_rfid = RFIDLatLong()
        # (19.127069, 72.915648)
        lat_long = {
            'lat': '19.127069',
            'long': '72.915648'

        }
        dummy_rfid.add_RFID(rfid_name="IIT_2", location="IIT Main Road Banglows",latitude = lat_long['lat'] , longitude= lat_long['long'])
        
        dummy_rfid = RFIDLatLong()
        # (19.128453, 72.915412)
        lat_long = {
            'lat': '19.128453',
            'long': '72.915412'

        }
        dummy_rfid.add_RFID(rfid_name="IIT_3", location="IIT Hostel 10",latitude = lat_long['lat'] , longitude= lat_long['long'])
        
        # (19.131584, 72.915282)
        dummy_rfid = RFIDLatLong()
        lat_long = {
            'lat': '19.131584',
            'long': '72.915282'

        }
        dummy_rfid.add_RFID(rfid_name="IIT_4", location="IIT SOM",latitude = lat_long['lat'] , longitude= lat_long['long'])
        
        dummy_rfid = RFIDLatLong()
        
        #(19.132538, 72.914774)
        lat_long = {
            'lat': '19.132538',
            'long': '72.914774'

        }
        dummy_rfid.add_RFID(rfid_name="IIT_5", location="IIT Main building",latitude = lat_long['lat'] , longitude= lat_long['long'])
        
        # (19.133197, 72.913085)
        dummy_rfid = RFIDLatLong()
        lat_long = {
            'lat': '19.133197',
            'long': '72.913085'

        }
        dummy_rfid.add_RFID(rfid_name="IIT_6", location="IIT Hockey Ground",latitude = lat_long['lat'] , longitude= lat_long['long'])
        
        # (19.133652, 72.911936)
        dummy_rfid = RFIDLatLong()
        lat_long = {
            'lat': '19.133652',
            'long': '72.911936'

        }
        dummy_rfid.add_RFID(rfid_name="IIT_7", location="IIT New SAC Building",latitude = lat_long['lat'] , longitude= lat_long['long'])
        
        # (19.134929, 72.908258)
        dummy_rfid = RFIDLatLong()
        lat_long = {
            'lat': '19.134929',
            'long': '72.908258'

        }
        dummy_rfid.add_RFID(rfid_name="IIT_8", location="IIT Hostel 9",latitude = lat_long['lat'] , longitude= lat_long['long'])
        
        # (19.135244, 72.907109)
        dummy_rfid = RFIDLatLong()
        lat_long = {
            'lat': '19.135244',
            'long': '72.907109'

        }
        dummy_rfid.add_RFID(rfid_name="IIT_9", location="IIT Hostel 6",latitude = lat_long['lat'] , longitude= lat_long['long'])
        
        (19.135523, 72.905581)
        dummy_rfid = RFIDLatLong()
        lat_long = {
            'lat': '19.135523',
            'long': '72.905581'

        }
        dummy_rfid.add_RFID(rfid_name="IIT_10", location="IIT Hostel 12",latitude = lat_long['lat'] , longitude= lat_long['long'])
        
        self.response.write(template.render(path, ''))        

class MainPage(webapp2.RequestHandler):
    def get(self):
        rfid = []
        rfid_map = {} 
        import json
        # Data for RFID
        current_location = "IIT_4"
        all_rfid = RFIDLatLong.query().fetch()
        for rf in all_rfid:
            rfid_map[rf.rfid_name] = {'latitude':rf.latitude,'longitude':rf.longitude}
            rfid.append(rf)
        
        # Data for autos 
        all_autos = AutoLocationTrack.query().fetch()
        autos = []
        vacant = 0
        filled = 0
        
        for auto in all_autos:
            auto.latitude = rfid_map[auto.current_rfid]['latitude']
            auto.longitude = rfid_map[auto.current_rfid]['longitude']
            if auto.availability =="Vacant":
                vacant = vacant + 1
            else:
                filled = filled + 1
            
            autos.append(auto)
        
        autos_nearby = []  
        import datetime
        
        for auto in all_autos:
            current_location_person = int(current_location.split("_")[1])
            current_rfid = int(auto.current_rfid.split("_")[1])
            if current_rfid>=current_location_person:
                dis = int(current_rfid) - int(current_location_person) 
            else:
                dis = int(current_location_person) - int(current_rfid)  
            if dis <=10:
                current_time = datetime.datetime.now()
                c = current_time - auto.updated_on
                auto.time_to_reach = str(c.seconds / 60 )
                auto.distance = str(dis*100)
                autos_nearby.append(auto)
            autos_nearby.sort(key=lambda x: str(x.distance), reverse=False)
        context = {
    		'data_rfid': rfid,
            'data_auto':autos,
            'current_location':current_location,
            'vacant_auto':vacant,
            'filled_auto':filled,
            'near_by_auto':autos_nearby,
            'current_time':datetime.datetime.now()
            
    	}

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.write(template.render(path,  context))

class AdminDashBoard(webapp2.RequestHandler):
    def get(self):
        rfid = []
        rfid_map = {} 
        import json
        # Data for RFID
        all_rfid = RFIDLatLong.query().fetch()
        for rf in all_rfid:
            rfid_map[rf.rfid_name] = {'latitude':rf.latitude,'longitude':rf.longitude}
            rfid.append(rf)
        
        # Data for autos 
        all_autos = AutoLocationTrack.query().fetch()
        autos = []
        vacant = 0
        filled = 0
        for auto in all_autos:
            auto.latitude = rfid_map[auto.current_rfid]['latitude']
            auto.longitude = rfid_map[auto.current_rfid]['longitude']
            autos.append(auto)
            if auto.availability =="Vacant":
                vacant = vacant + 1
            else:
                filled = filled + 1
        context = {
    		'data_rfid': rfid,
            'data_auto':autos,
            'total_count':len(all_autos),
            'vacant_auto':vacant,
            'filled_auto':filled

    	}

        path = os.path.join(os.path.dirname(__file__), 'admin_panel.html')
        self.response.write(template.render(path,  context))
    
    def post(self):
        req = self.request
        all_autos = AutoLocationTrack.query().fetch()
        for auto in all_autos:
            auto_number = auto.auto_number
            new_rfid = req.get(auto_number+"_rfid")
            is_vacant = req.get(auto_number+"_availability")
            auto_dummy = AutoLocationTrack()
            auto_dummy.update_auto_path(auto_number, new_rfid, is_vacant)
        self.redirect('/admin_home')

class AddRFID(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('rfid_name')
        rfid_location = self.request.get('rfid_location')
        rfid_lat = self.request.get('latitude')
        rfid_long = self.request.get('longitude')
        rf = RFIDLatLong()
        rf.add_RFID(rfid_name = name, location = rfid_location, latitude = rfid_lat ,longitude = rfid_long)
        self.redirect('/admin_home')

class AddAuto(webapp2.RequestHandler):
    def post(self):
        auto_number = self.request.get('auto_number')
        auto_current = 'IIT_1'
        auto_availability = self.request.get('availability_auto')
       
        auto_dummy = AutoLocationTrack()
        auto_dummy.add_auto(auto_number = auto_number, path = auto_current, current_rfid = auto_current ,last_rfid = None,availability = auto_availability)
        self.redirect('/admin_home')

class DeleteAuto(webapp2.RequestHandler):
    def post(self):
        auto_number = self.request.get('auto_number')
        auto_dummy = AutoLocationTrack()
        auto_dummy = auto_dummy.get_by_id(auto_number)
        ndb.Key(AutoLocationTrack, auto_number).delete()
        self.redirect('/admin_home')

  
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/dummy', DummyData),
    ('/auto_dummy', AutoDummyData),
    ('/admin_home', AdminDashBoard),
    ('/add_rfid', AddRFID),
    ('/add_auto_new', AddAuto),
    ('/delete_auto', DeleteAuto)
    


], debug=True)