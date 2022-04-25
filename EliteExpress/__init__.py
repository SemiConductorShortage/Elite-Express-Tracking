import requests
import random

class getInfo:
    def __init__(self, number):

        link = f"https://www.elite-co.com/default.aspx?awbno={number}"
        
        Info = requests.get(link)
        Info = Info.text
        self.recordFound = True

        Info = Info.split('<div class="modal-body">')[1]
        Info = Info.split('<style type="text/css">')[0]
        Info = Info.split('\n')
        self.places = {

            }

        self.details = {}
        self.detailsNoTimestamp = []
        for line in range(len(Info)):
        #BEGIN DETECTION
        
            if "<p class=\"order-track-text-stat" in Info[line]:  # Get Status Lines / Tracking Details
                detail = Info[line].strip()
                detail = detail.split('>')[1].replace('</p','')
                timestamp = Info[line+2].strip().split('>')[1].replace('</span','')
                self.details[detail] = timestamp
                self.detailsNoTimestamp.append(detail)
                place = detail.split("-")[0]
                self.places[place] = "v"
                
            if 'Delivered To' in Info[line]:
                self.FirstName = Info[line].split(':')[2].split('<')[0]
                self.shipmentEnd = Info[line+2].strip().split('>')[1].replace('</span','')
            if '<p id="status">' in Info[line]:
                
                self.status = Info[line].split('<p id="status">')[1].split('</p>')[0]
                if self.status.strip() == "":
                    self.recordFound = False
                    #print("Record Is Nonexistent")
                self.Delivered = 'Delivered' in Info[line]

            if '<p id="date">' in Info[line]:
                self.shipmentDate = Info[line].split('">')[1].split("</p>")[0]
            if '<p id="weight">' in Info[line]:
                self.weight = Info[line].split('">')[1].split("</p>")[0]
            if '<p id="origin">' in Info[line]:
                self.origin = Info[line].split('">')[1].split("</p>")[0]
            if '<p id="destn">' in Info[line]:
                self.destination = Info[line].split('">')[1].split("</p>")[0]
            if '<p id="peice">' in Info[line]:  #The web developers had a minor spelling issue here manne I cant do anything about it
                self.count = Info[line].split('">')[1].split("</p>")[0]
            if 'shipment information received' in Info[line]:
                self.shipmentStart = Info[line+2].strip().split('>')[1].replace('</span','')
            if 'pickup booked' in Info[line]:
                self.shipmentStart = Info[line+2].strip().split('>')[1].replace('</span','')
        if self.recordFound:
            if 'pickup booked' not in self.detailsNoTimestamp:
                if 'shipment information received' not in self.detailsNoTimestamp:
                    earliestStatus = self.detailsNoTimestamp[-1]
                    self.shipmentStart = self.details[str(earliestStatus)]


#minimum= 1182547000     #  try numbers like 1182547001 if you want to try a sample of how this would turn out
#for i in range(minimum, minimum+300):
#    try:
#        time.sleep(random.randrange(5,7))
#        getInfo(i)
#    except:
#        time.sleep(6)
#        getInfo(i)


def styleData(number):
    print(f"---AIRWAY BILL NUMBER {number}---")
    h = getInfo(number)
    details = '\n'.join(
        list(h.details)
        )

    listDetails = details.split('\n')
    details = []



    for i in listDetails:  #Styling

        sortedList = sorted(listDetails)
        maxStrLen=len(str(sortedList[-1:]))
        data = i
        i = i[0:3].upper()+i[3:].title()
        if 'shipment in transit' in i.lower():
            i = i[0:-3]+(i[-3:].upper())

        spacing = maxStrLen-len(i)
        spacing = " "*spacing
        details.append(i+f"{spacing}| "+h.details[data])

    details = '\n'.join(details)
    print(details)
    print(f"Status : {h.status}")
    print(f"Weight : {h.weight}")
    print(f"Locations : {', '.join(list(h.places.keys()))}")
    print(f"Is Delivered : {h.Delivered}")
    print(f"Shipment Date : {h.shipmentDate}")
    print(f"Count of Packages: {h.count}")

    if h.Delivered:
        print(f"Delivered To: {h.FirstName}")

