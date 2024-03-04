import openai
import os

class OpenAIIntegration:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'llm_model.txt')

        with open(file_path, 'r') as file:
            self.prompt = file.read()

    def __get_ai_response_with_prompt(self, user_question: str):
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=self.prompt + "por favor, considere isso como a entrada do usuário: "+user_question,
            max_tokens=100  
        )
        return response.choices[0].text.strip()

    def get_ai_response(self, user_question: str) -> str:
        return self.__get_ai_response_with_prompt(user_question)

    def calculate_macronutrients(self, meal_description: str, nutrition_database) -> str:
        food_items_question = "Quais são os itens alimentares nesta refeição? " + meal_description
        food_items_response = self.get_ai_response(food_items_question)
        
        food_items = nutrition_database.get_food_items(food_items_response)
        
        macronutrients_question = "Quais são os macronutrientes nestes alimentos? " + ', '.join(food_items)
        macronutrients_response = self.get_ai_response(macronutrients_question)
        
        macronutrients = nutrition_database.get_nutrition_info(macronutrients_response)
        
        return macronutrients
