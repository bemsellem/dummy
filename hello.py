#! /usr/bin/env python3
"""Script pour conduire"""
class Car(object):
    """classe définissant une voiture"""
    def __init__(self, name, color, model):
        """Trois paramètres : nom, couleur et modèle"""
        self.name = name
        self.color = color
        self.model = model

    def car_status(self):
        """méthode donnant le statut de la voiture"""
        return "ça roule"

if __name__ == "__main__":
    MY_CAR = Car("Rêvé par Isa", "jaune", "BMW")
    print(MY_CAR.car_status())
