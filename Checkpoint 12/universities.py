import requests
import json

universities = {
    "Eastern Arizona College": {"majors": 0, "cost": 1800, "location": "Arizona", "distance": 325},
    "Universidad Tecmilenio": {"majors": 27, "cost": 10200, "location": "Chihuahua", "distance": 270},
    "Tecnologico de Monterrey": {"majors": 45, "cost": 135000, "location": "Chihuahua", "distance": 265},
    "Universidad de La Salle": {"majors": 19, "cost": 50000, "location": "Chihuahua", "distance": 270},
    "Universidad Autónoma de Ciudad Juárez": {"majors": 8, "cost": 4000, "location": "Nuevo Casas Grandes", "distance": 30}
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