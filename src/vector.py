class Vector:
    def __init__(self):
        self.x = None
        self.y = None

    @classmethod
    def New(cls):
        rvec = Vector()
        rvec.x = 0
        rvec.y = 0
        return rvec

    @classmethod
    def FromVector(cls, vec):
        rvec = Vector()
        rvec.x = vec.x
        rvec.y = vec.y
        return rvec
