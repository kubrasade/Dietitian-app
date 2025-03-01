from decimal import Decimal

class SurveyService:
    @staticmethod
    def calculate_bmi(weight: Decimal, height: Decimal) ->dict:
        if not weight or not height or height  == 0:
            return {"bmi": None, "bmi_category": None}
        
        bmi = weight / (height ** 2)
        bmi= round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        elif 30 <= bmi < 34.9:
            category = "Obese Class 1"
        elif 35 <= bmi < 39.9:
            category = "Obese Class 2"
        else:
            category = "Obese Class 3"

        return {"bmi": bmi, "category": category}