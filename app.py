from flask import Flask, request, jsonify
import menu1  # כאן אתה מייבא את הקוד שלך שמייצר את התפריט
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate-menu', methods=['POST'])
def generate_menu():
    try:
        data = request.get_json()
        print(f"Received data: {data}")  # הדפסת הנתונים שהתקבלו מה-POST
        calories = data.get('calories')
        protein = data.get('protein')
        goal = data.get('goal')

        menu = menu1.generate_menu(calories, protein, goal)

        return jsonify(menu)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred while generating the menu"}), 500

@app.route('/get-meal-options', methods=['POST'])
def get_meal_options():
    data = request.get_json()  # קבל את הנתונים מהבקשה
    goal = data.get('goal')  # קבל את ה-GOAL

    menu_options = sort_goal(goal)

    meal_options = {
        "breakfast": [menu_options['breakfast_options'][0]['name'],menu_options['breakfast_options'][1]['name']],
        "lunch": [menu_options['lunch_options'][0]['name'],menu_options['lunch_options'][1]['name']],
        "dinner": [menu_options['dinner_options'][0]['name'], menu_options['dinner_options'][1]['name']],
        "snack": [menu_options['snack_options'][0]['name']]
    }
    return jsonify(meal_options)

def sort_goal(goal):
    if(goal == 'cutting'):
        menu = menu1.meals.menu_c['meals']
    elif (goal == 'bulking'):
        menu = menu1.meals.menu_b['meals']
    elif (goal == 'maintenance'):
        menu = menu1.meals.menu_m['meals']
    return menu

@app.route('/custom-menu', methods=['POST'])
def custom_menu():
    data = request.get_json()
    # עיבוד התפריט המותאם אישית כאן
    print(f"Custom menu request data: {data}")

    customated_menu = menu1.generate_menu(data.get('calories'),data.get('protein'),data.get('goal'),data.get('mealSelections'))
    print(customated_menu)
    return jsonify(customated_menu)

if __name__ == '__main__':
    app.run(debug=True)
