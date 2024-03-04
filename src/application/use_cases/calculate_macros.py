from src.infrastructure.ai_integration.open_ai_integration import OpenAIIntegration as aiIntegration
from src.infrastructure.nutrion_database.fatsecret_integration import FatSecretIntegration as nutritiondatabase

class CalculateMacros:
    def __init__(self, message):
        self.message = message

    def __call__(self):
        ai_integration = aiIntegration()
        nutrition_database = nutritiondatabase()

        meal_description = self.message
        macronutrients = ai_integration.calculate_macronutrients(meal_description, nutrition_database)

        return macronutrients

