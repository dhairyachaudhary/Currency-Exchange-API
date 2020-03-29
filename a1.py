# Name : Dhairya Chaudhary
# Roll No : 2019035
# Group : 8

import urllib.request
import datetime

def getLatestRates():
    """Returns: a JSON string that is a response to a latest rates query.
	The Json string will have the attributes: rates, base and date (yyyy-mm-dd)."""
    link=urllib.request.urlopen("https://api.exchangeratesapi.io/latest")
    readinfo=(link.read()).decode('utf-8')
    return readinfo

#Task 1

def changeBase(amount, currency, desiredCurrency, date):
    """Outputs: a float value f"""
    linktoopen="https://api.exchangeratesapi.io/"+date
    oldlink=urllib.request.urlopen(linktoopen)
    readinfo=(oldlink.read()).decode('utf-8')
    if currency=="EUR":
        r1=1
    else:
        r1=readinfo[readinfo.find(currency)+5:]
        try:
            r1=float(r1[:(r1.find(","))])
        except:
            r1=float(r1[:(r1.find("}"))])
    if desiredCurrency=="EUR":
        r2=1
    else:
        r2=readinfo[readinfo.find(desiredCurrency)+5:]
        try:
            r2=float(r2[:r2.find(",")])
        except:
            r2=float(r2[:r2.find("}")])
    return amount*(r2/r1)

#Task 2

def swap(i1,i2,list):
    """Helper function for interchanging two list elements"""
    temp=list[i1]
    list[i1]=list[i2]
    list[i2]=temp

def sorter(list):
    """Helper function for sorting the values in a list as required by the printAscending function"""
    for pointer1 in range(len(list)-1):
        for pointer2 in range(pointer1+1,len(list)):
            if (float(list[pointer1][6:]))>(float(list[pointer2][6:])):
                swap(pointer1,pointer2,list)

def printAscending(json):
    """Output: the sorted order of the Rates
	You don't have to return anything.
	Parameter:json: a json string to parse."""
    json=getLatestRates()
    json=json[json.find("{")+(json[json.find("{")+1:]).find("{")+2:]
    list=json.split(",")
    list.remove(list[-1])
    list.remove(list[-1])
    list[-1]=list[-1][:-1]
    sorter(list)
    for element in list:
        print("1 Euro =",element[6:],element[1:4])

#Task 3

def FridayChecker(date):
    """Helper function that checks whether or not a given date is a Friday."""
    date = datetime.datetime(int(date[0:4]), int(date[5:7]), int(date[8:]))
    if (date.weekday()==4):
        return True
    else:
        return False

def extremeFridays(startDate, endDate, currency):
    """Output: on which friday was currency the strongest and on which was it the weakest.
	You don't have to return anything.
	Parameters: stardDate and endDate: strings of the form yyyy-mm-dd
	currency: a string representing the currency those extremes you have to determine"""
    link="https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate
    histlink=urllib.request.urlopen(link)
    histinfo=(histlink.read()).decode('utf-8')
    histinfo=histinfo[histinfo.find("{")+(histinfo[histinfo.find("{")+1:]).find("{")+2:]
    histinfo=histinfo[:histinfo.find("},\"start_at\"")]
    #Datelist will contain dates that are Fridays and valuelist will contain the value of the currency (with refernce to the Euro) on that date
    datelist=[]
    valuelist=[]
    import itertools
    for x in itertools.repeat(1):
        if histinfo=="":
            break
        if FridayChecker(histinfo[1:11])==True:
            datelist.append(histinfo[1:11])
            value=histinfo[histinfo.find(currency)+5:]
            value=float(value[:value.find(",")])
            valuelist.append(value)
        histinfo=histinfo[histinfo.find("}")+2:]
    weakestdate=(datelist[valuelist.index(max(valuelist))])
    strongestdate=(datelist[valuelist.index(min(valuelist))])
    print(currency+" was strongest on "+strongestdate+". 1 Euro was equal to", min(valuelist), currency)
    print(currency+" was weakest on "+weakestdate+". 1 Euro was equal to", max(valuelist), currency)


#Task 4

def findMissingDates(startDate, endDate):
    """Output: the dates that are not present when you do a json query from startDate to endDate
		You don't have to return anything.
		Parameters: stardDate and endDate: strings of the form yyyy-mm-dd"""
    day=int(startDate[8:])
    month=int(startDate[5:7])
    year=int(startDate[:4])
    endday=int(endDate[8:])
    endmonth=int(endDate[5:7])
    endyear=int(endDate[:4])
    totaldatalink=urllib.request.urlopen("https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate)
    totaldata=(totaldatalink.read()).decode('utf-8')
    totaldata=totaldata[:totaldata.find("},\"start_at\"")]

    print("The following dates were not present:")

    a=True
    #a becomes false when the date is greater than endDate as per a controlling condition in the loop
    import itertools
    for x in itertools.repeat(1):
        if a==False:
            break
        if (day<10 and month<10):
            datetofind=str(year)+"-"+"0"+str(month)+"-"+"0"+str(day)
        elif (day>=10 and month<10):
            datetofind=str(year)+"-"+"0"+str(month)+"-"+str(day)
        elif (day<10 and month>=10):
            datetofind=str(year)+"-"+str(month)+"-"+"0"+str(day)
        else:
            datetofind=str(year)+"-"+str(month)+"-"+str(day)

        p=totaldata.find(datetofind)
        if p==-1:
            print(datetofind)

        #Increment
        if month==12 and day==31:
            day=1
            month=1
            year=year+1
        elif (((month==1 or month==3 or month==5 or month==7 or month==8 or month== 10) and day==31) or ((month==4 or month==6 or month==9 or month==11) and day==30) or (day==28 and month==2 and (year%4!=0 or year%400==0)) or (day==29 and month==2)):
            day=1
            month=month+1
        else:
            day=day+1

        #Loop controlling condition
        if (year>endyear) or (year==endyear and month>endmonth) or (year==endyear and month==endmonth and day>endday):
            a=False
