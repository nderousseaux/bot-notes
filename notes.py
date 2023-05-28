from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # Initiate the browser
import time

browser = webdriver.Chrome(ChromeDriverManager().install())

while True:

    browser.get('https://notes.iutrs.unistra.fr/resultat/')

    #Si on est pas connecté on se connecte
    if "?next=" in browser.current_url:
        browser.get('https://cas.unistra.fr/cas/login?service=https%3A%2F%2Fnotes.iutrs.unistra.fr%2Faccounts%2Flogin%2F%3Fnext%3D%252F%253Fnext%253D%252Fresultat%252F')
        name = <username>
        password = <password>
        browser.find_element_by_name("username").send_keys(name)
        browser.find_element_by_name("password").send_keys(password)
        browser.find_element_by_name('submit').click()
    browser.get('https://notes.iutrs.unistra.fr/resultat/')



    tableau_browser = browser.find_element_by_css_selector('table')
    
    #On supprime la colonne des moyennes
    colonne_moyenne = browser.find_element_by_class_name('classname')
    driver.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, element)


    with open('tableau_notes.html', 'r') as fichier_notes:
        tableau_file = fichier_notes.read()
    

    #Si la page à changée, on enregistre la nouvelle page
    if tableau_browser != tableau_file:
        
        with open('tableau_notes.html', 'w') as fichier_notes:
            fichier_notes.write(tableau_browser)
        
        print("la page à été modifiée")


    time.sleep(5)
    #Je suis un commentaire très beau

