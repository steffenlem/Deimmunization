class PointMutation:
    """
    instance of the class store the information about the point mutation itself and its effect
    """

    def __init__(self, amino_acid, index, immunogenicity, ddG, oldAA):
        """
        Constructor
        :param amino_acid: amino_acid after mutation
        :param index: index of point mutation
        """
        self.amino_acid = amino_acid
        self.index = index
        self.immunogenicity = immunogenicity
        self.ddG = ddG
        self.oldAA = oldAA

    @property
    def amino_acid(self):
        return self._amino_acid

    @amino_acid.setter
    def amino_acid(self, value):
        self._amino_acid = value

    @amino_acid.deleter
    def amino_acid(self):
        del self.amino_acid

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value

    @index.deleter
    def index(self):
        del self.index

    @property
    def immunogenicity(self):
        return self._immunogenicity

    @immunogenicity.setter
    def immunogenicity(self, value):
        self._immunogenicity = value

    @immunogenicity.deleter
    def immunogenicity(self):
        del self.immunogenicity

    @property
    def ddG(self):
        return self._ddG

    @ddG.setter
    def ddG(self, value):
        self._ddG = value

    @ddG.deleter
    def ddG(self):
        del self.ddG

    @property
    def oldAA(self):
        return self._oldAA

    @oldAA.setter
    def oldAA(self, value):
        self._oldAA = value

    @oldAA.deleter
    def oldAA(self):
        del self.oldAA


    def __str__(self):
        return 'Wild type residue: ' + str(self.oldAA) + '   ' + 'Index: ' + str(self.index + 1) + '   ' + 'Mutated residue: ' + str(self.amino_acid) + '   ' + 'Immunogenicity: ' + str(
            self.immunogenicity) + '   ' + 'ddG: ' + str(self.ddG)
