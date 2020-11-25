from textclassification import TextClassification

class TestTextClassification():

    @classmethod
    def setup_class(self):
        self.text_class_instance = TextClassification()

    def test_get_text(self):
        print 'Traitement du texte'
        text = self.text_class_instance.get_text([['A'], ['5'], ['D'], ['B']])
        assert text == 'A5DB'

    def test_text_reconstruction(self):
        print 'Reconstruction'
        new_text = self.text_class_instance.text_reconstruction('DACB',
            [10, 1, 6, 4])
        assert new_text == 'ABCD'

