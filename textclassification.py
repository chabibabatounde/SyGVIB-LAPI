class TextClassification:
    
    def get_text(self, machine_learning_result):
    
        plate_string = ''
        for eachPredict in machine_learning_result:
            plate_string += eachPredict[0]
            
        return plate_string
    
    def text_reconstruction(self, plate_string, position_list):
      
        posListCopy = position_list[:]
        position_list.sort()
        rightplate_string = ''
        for each in position_list:
            rightplate_string += plate_string[posListCopy.index(each)]
            
        return rightplate_string