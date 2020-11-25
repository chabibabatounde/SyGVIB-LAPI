

import os
from preprocess import PreProcess
from deepMachine import DeepMachineLearning
from ocr import OCROnObjects
from textclassification import TextClassification
from datetime import datetime
import plotting
# import wx
import time
from rest import RESTAPI
from rest import REQUETESERVE

imagepath = ''
listRow = 0
listResult = ''

def license_plate_extract(plate_like_objects, pre_process):
    number_of_candidates = len(plate_like_objects)

    print('Reconnaissance des zone de plaque...')
    #print(plate_like_objects)

    if number_of_candidates == 0:
        print('Aucune zone de la plaque detectee')
        
        return []

    if number_of_candidates == 1:
        print('Une zone de plaque trouvee')
        license_plate = pre_process.inverted_threshold(plate_like_objects[0])
    else:
        print('Plusieurs zones de plaque trouvees')
        print('Validation de la zone de plaque...')
        license_plate = pre_process.validate_plate(plate_like_objects)
        print('Une zone de plaque trouvee')
    return license_plate

#remettre event apres
def execute_LAPI(imagepath):
    start_time = time.time()
    root_folder = os.path.dirname(os.path.realpath(__file__))
    models_folder = os.path.join(root_folder, 'ml_models')
    pre_process = PreProcess(imagepath)
    plate_like_objects = pre_process.get_plate_like_objects()
    license_plate = license_plate_extract(plate_like_objects, pre_process)

    if len(license_plate) == 0:
        return False
    ocr_instance = OCROnObjects(license_plate)
    
    if ocr_instance.candidates == {}:
        print("Aucun caractere n'est lu")
        return False

    # plotting.plot_cca(license_plate, ocr_instance.candidates['coordinates'])

    deep_learn = DeepMachineLearning()
    text_result = deep_learn.learn(ocr_instance.candidates['fullscale'],
        os.path.join(models_folder, 'SVC_model', 'SVC_model.pkl'),
        (20, 20))

    text_phase = TextClassification()
    scattered_plate_text = text_phase.get_text(text_result)
    plate_text = text_phase.text_reconstruction(scattered_plate_text,
        ocr_instance.candidates['columnsVal'])
    
    #listResult.InsertStringItem(listRow, plate_text)
    print (plate_text)
    #plate_text = "BC7751"

    print("Numero Identifie : " + plate_text + "RB")
  
    try:
        requete = REQUETESERVE()
        requete.sendImmatriculation(plate_text)

    except Exception as ex:
        print(ex)

    
    print('Temps d\'execution:' + str(time.time() - start_time) + " Seconde")