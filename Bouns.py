def Input_Weather_Data(dic):
    city_name =input("enter the name of city ")
    date= input("enter the date:")
    temperature =input("enter the temperature:")
    humidity =input("enter the humidity:")
    condition = input ("enter the weather condition : ")

    if  not city_name in dic:
        dic [city_name]={}
        dic [city_name][date]={
            "temperature" :temperature,
            "humidity":humidity,
             "condition":condition
        }
        print("success")
  
def Query (dic)  :
    city=input("enter the city mane to see the weather detailes:") 
    if city in dic :
     print ("this a detailes for",city,":")  
     for key ,value in dic[city].items():
       print (key, value)

    else:
       print("city not found!")
             

weather_data={"Riyadh": {
        "2026-09-13": {
            "temperature": 35.0,
            "humidity": 20.0,
            "condition": "Sunny"
        },
        "2026-09-14": {
            "temperature": 36.0,
            "humidity": 18.0,
            "condition": "Clear"
        }
    },
    "Jeddah": {
        "2026-09-13": {
            "temperature": 38.0,
            "humidity": 60.0,
            "condition": "Cloudy"
        }
    }
}
while True:
    print ("1- add weather data:")
    print ("2- search roe city:")
    print ("3- exit")
    choice = input ("your choice:")
    if choice=="1":
       Input_Weather_Data(weather_data)
    elif  choice=="2":
         Query (weather_data)
    elif  choice=="3":
       break
    else:
       print(" invalid choice try egine")  

print ("thank you")         