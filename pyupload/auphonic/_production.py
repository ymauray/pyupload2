class Production:
    """Auphonic production"""

    def __init__(self, id = None, multitrack = False):
        if id is not None:
            print("Using id {}".format(id))
        else:
            print("A multitrack production ? : {}".format(multitrack))

