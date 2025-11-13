import requests
import json

universities = {
    "Eastern Arizona College": {"majors": 0, "cost": 1800, "location": "Arizona", "distance": 325, "website": "http://www.eac.edu"},
    "Universidad Tecmilenio": {"majors": 27, "cost": 10200, "location": "Chihuahua", "distance": 270, "website": "https://tecmilenio.mx/"},
    "Tecnologico de Monterrey": {"majors": 45, "cost": 135000, "location": "Chihuahua", "distance": 265, "website": "https://www.tec.mx/"},
    "Universidad de La Salle": {"majors": 19, "cost": 50000, "location": "Chihuahua", "distance": 270, "website": "http://bajio.delasalle.edu.mx/"},
    "Universidad Autónoma de Ciudad Juárez": {"majors": 8, "cost": 4000, "location": "Nuevo Casas Grandes", "distance": 30, "website": "http://www.uacj.mx/"}
}

while True:
    uni = input("Enter in the name of a university: ")
    if uni not in universities:
        print("Invalid Input")
    else:
        for element in universities[uni]:
            print(f"{element.title()}: {universities[uni][element]}")
            # response = requests.get("http://universities.hipolabs.com/search?name="+uni)
            # print(response)
    break