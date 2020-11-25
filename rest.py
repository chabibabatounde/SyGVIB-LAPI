#!/usr/bin/python
# -*- coding: utf8 -*-
import requests


class REQUETESERVE():
    urlServeur  = "https://sygvib.000webhostapp.com/request.php"

    def __init__(self):
        print('RESTFULL Instacié : @ : '+self.urlServeur)

    def sendImmatriculation(self, plate_number):
        print("Envoi de la requete...")
        self.send(plate_number)

    def send(self,plate_number):
        try:
            resp = requests.post(self.urlServeur,data={'numero':plate_number})
            print("Requete envoyée")
            #print (resp.text)
        except Exception as ex :
            print("Une erreur est suvenue lors de l'envoi de la requete")
            print(ex)

       



class RESTAPI():
    
    def __init__(self,tokenUrl,login,psswd):
        data={"login": login, "password": psswd }
        token=self.post(tokenUrl,data)
        
    def getToken():
        return token
        
    def get(self,url):
        resp = requests.get(url)
        print (resp)
        if resp.type =='erreur':
            # une erreur s'est produite
            #raise ApiError('GET /tasks/ {}'.format(resp.status_code))
            print ('une erreur s\'est produite:')
            print (resp)
        else:
            print(resp.valeur)

    def post(self,url,data):
        resp = requests.post(url,data)
        print (resp)
        if resp.type !='erreur':
            #raise ApiError('POST /tasks/ {}'.format(resp.status_code))
            print('Requete envoyée:')
            print(rep.valeur)
        else:
            print('Une erreur s\'est produite: ')

        return resp
            



