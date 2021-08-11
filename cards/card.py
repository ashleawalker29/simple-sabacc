class Card(object):

    STAVES = ['Circles', 'Triangles', 'Squares', 'Sylop']

    def __init__(self, value, stave):
        if (
            (type(value) is not int) or
            (value > 10 or value < 0) or
            (stave not in self.STAVES) or
            (value is None or stave is None)):

            self.value = 0
            self.stave = 'Sylop'
        else:
            self.value = value
            self.stave = stave
