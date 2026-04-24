from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

#classmate class
class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}."

# Store classmates in a list
classmates_list = [
    Classmate("Ashley Mondragon", "Topaz", "Math"),
    Classmate("Queeny Haraj Ramos", "Emerald", "Science"),
    Classmate("Sam G. Bernice Luna", "Sapphire", "English"),
    Classmate("Danielle Dimasuhid", "Amethyst", "Math"),
    Classmate("Ebtisam A. Al Hazmi", "Ruby", "History")
]

def display_list(event):
    #Loop to display all introductions
    output_div = document.querySelector("#output")
    output_div.innerHTML = "" 
    
    for person in classmates_list:
        new_p = document.createElement("p")
        new_p.className = "border-b border-gray-100 pb-1 mb-1"
        new_p.innerText = person.introduce()
        output_div.appendChild(new_p)

def add_classmate_event(event):
    # User input logic with Error Handling
    name_el = document.querySelector("#name")
    sec_el = document.querySelector("#section")
    sub_el = document.querySelector("#subject")
    output_div = document.querySelector("#output")

    # Checks if all the items are filled in
    if name_el.value.strip() and sec_el.value.strip() and sub_el.value.strip():
        new_person = Classmate(name_el.value, sec_el.value, sub_el.value)
        classmates_list.append(new_person)
        
        # Show success message
        output_div.innerHTML = f'<p class="text-blue-600 font-bold">Added: {new_person.name} successfully!</p>'
        
        # Clear inputs
        name_el.value = ""
        sec_el.value = ""
        sub_el.value = ""
    else:
        # Show error message if boxes are empty
        output_div.innerHTML = '<p class="text-red-500 font-bold">Error, please fill in the required boxes</p>'

#first message 
document.querySelector("#output").innerHTML = "Ready! System loaded."
