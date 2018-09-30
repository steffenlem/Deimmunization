class EpitopePrediction:
    epitope_prediction = []

    def __init__(self, epitope_prediction):
        self.epitope_prediction = epitope_prediction

    # probabilities of MHC allels are needed (europe)
    def get_immunogenicity(self):
        return -1

    ## TODO evaluate wether this class is necessary...
