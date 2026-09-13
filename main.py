ph_book={
 "0568323222"  :"Amal",
 "0522222232":"Mohammed",
 "0532335983":"Khadijah",
 "0545341144":"Abdullah",
 "0545534556":"Rawan",
 "0560664566":"Faisal",
 "0567917077":"Layla"
}

num= input("enter a phone number :")

if len(num)==10 and num in ph_book :
    print(ph_book.get(num))
elif not num.isdigit() or len(num)!=10: 
    print ("this invalid number!!")
else :
    print("Sorry, the number is not found")

      