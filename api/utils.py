def filterDataRefPeriod(years, data):
    
    print("refperiod")
    print(years)
    
    mydata= []
    for x in years:
        data_retuned = getYearsData(year=x, data=data)
        
        if data_retuned != None:
            
            mydata.append(data_retuned)
        
    return mydata
        



def getYearsData(year, data):
    finaldata={}
    
    for y in data:
       
        
        refperiod = y["refperiod"]
        if refperiod[0:4] == str(year):
            print(y)
            finaldata =y
      
    
            return finaldata
        