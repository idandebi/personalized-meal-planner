
class menu:
    def __init__(self,goal , options = [0,0,0,0]):
        self.breakfast = meals(0,goal,options)
        self.lunch = meals(1,goal,options)
        self.dinner = meals(2,goal,options)
        self.snack = meals(3,goal,options)

        self.calculate_sums()

    def calculate_sums(self):
        self.sum_cal = self.breakfast.sum_calories + self.lunch.sum_calories+ self.dinner.sum_calories + self.snack.sum_calories
        self.sum_pro = self.breakfast.sum_pro + self.lunch.sum_pro + self.dinner.sum_pro + self.snack.sum_pro

class meals:
    menu_m = {
        'meals': {
            'breakfast_options': [
                {
                    'name': 'eggs, white bread and salad',
                    'ingredients': {
                        'protein': [
                            {'name': 'eggs', 'calories': 140, 'protein': 12, 'base_quantity': 2, 'unit': ''}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'white bread', 'calories': 200, 'protein': 4, 'base_quantity': 2, 'unit': 'slices'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'cucumber, tomato and red pepper salad', 'calories': 60, 'protein': 0, 'base_quantity': 1, 'unit': ''}
                        ]
                    },
                    'total_calories': 400,
                    'total_protein': 16
                },
                {
                    'name': 'cottege 5%, white bread and salad',
                    'ingredients': {
                        'protein': [
                            {'name': 'Cottege 5%', 'calories': 125, 'protein': 15, 'base_quantity': 150,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'white bread', 'calories': 200, 'protein': 4, 'base_quantity': 2, 'unit': 'slices'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'cucumber, tomato and red pepper salad', 'calories': 60, 'protein': 0, 'base_quantity': 1, 'unit': ''}
                        ]
                    },
                    'total_calories': 410,
                    'total_protein': 19
                }
            ],
            'lunch_options': [
                {
                    'name': 'grilled chicken breast,cooked brown rice and salad',
                    'ingredients': {
                        'protein': [
                            {'name': 'grilled chicken breast', 'calories': 160, 'protein': 30, 'base_quantity': 100, 'unit': 'g'}
                            # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'cooked brown rice', 'calories': 220, 'protein': 5, 'base_quantity': 200,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'half avocado,cucumber and tomato salad', 'calories': 200, 'protein': 0, 'base_quantity': 1,'unit': ''}
                        ]
                    },
                    'total_calories': 580,
                    'total_protein': 35
                },
                {
                    'name': 'baked salmon, cooked quinoa and roasted brocoli',
                    'ingredients': {
                        'protein': [
                            {'name': 'baked salmon', 'calories': 200, 'protein': 20, 'base_quantity': 100,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'cooked quinoa', 'calories': 220, 'protein': 8, 'base_quantity': 100,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'roasted brocoli', 'calories': 55, 'protein': 4, 'base_quantity': 100,'unit': 'g'}
                        ]
                    },
                    'total_calories': 475,
                    'total_protein': 32
                }
            ],
            'dinner_options': [
                {
                    'name': 'baked salmon,baked potato and roasted carrots',
                    'ingredients': {
                        'protein': [
                            {'name': 'baked salmon', 'calories': 210, 'protein': 20, 'base_quantity': 100,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'baked potato', 'calories': 225, 'protein': 3, 'base_quantity': 250,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'roasted carrots', 'calories': 50, 'protein': 0, 'base_quantity': 100,'unit': ''}
                        ]
                    },
                    'total_calories': 485,
                    'total_protein': 23
                },
                {
                    'name': 'rib eye, baked sweet potato and salad',
                    'ingredients': {
                        'protein': [
                            {'name': 'rib eye', 'calories': 375, 'protein': 33, 'base_quantity': 150,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'baked sweet potato', 'calories': 180, 'protein': 4, 'base_quantity': 200,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'cucumber, tomato and red pepper salad', 'calories': 60, 'protein': 0, 'base_quantity': 1, 'unit': ''}
                        ]
                    },
                    'total_calories': 615,
                    'total_protein': 37
                }
            ],
            'snack_options': [
                {
                    'name': 'greek yogurt(0%) and banana',
                    'ingredients': {
                        'protein': [
                            {'name': 'greek yogurt(0%)', 'calories': 150, 'protein': 20, 'base_quantity': 150,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'banana', 'calories': 100, 'protein': 0, 'base_quantity': 2,'unit': ''}  # 1 מנת בסיס
                        ]
                    },
                    'total_calories': 350,
                    'total_protein': 20
                },
                {
                    'name': 'Snack Option 2',
                    'ingredients': {
                        'protein': [
                            {'name': 'hummus', 'calories': 150, 'protein': 5, 'base_quantity': 100}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'carrot sticks', 'calories': 50, 'protein': 1, 'base_quantity': 100}  # 1 מנת בסיס
                        ]
                    },
                    'total_calories': 200,
                    'total_protein': 6
                }
            ]
        }
    }
    menu_b = {
        'meals': {
            'breakfast_options': [
                {
                    'name': 'cottege (9%), white bread and salad',
                    'ingredients': {
                        'protein': [
                            {'name': 'cottege (9%)', 'calories': 300, 'protein': 25, 'base_quantity': 250, 'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'white bread', 'calories': 300, 'protein': 6, 'base_quantity': 3, 'unit': 'slices'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'cucumber, tomato and red pepper salad', 'calories': 60, 'protein': 0, 'base_quantity': 1, 'unit': ''}
                        ]
                    },
                    'total_calories': 700,
                    'total_protein': 31
                },
                {
                    'name': 'eggs, white bread and salad',
                    'ingredients': {
                        'protein': [
                            {'name': 'eggs', 'calories': 280, 'protein': 24, 'base_quantity': 4, 'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'white bread', 'calories': 300, 'protein': 6, 'base_quantity': 3, 'unit': 'slices'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'cucumber, tomato and red pepper salad', 'calories': 60, 'protein': 0, 'base_quantity': 1, 'unit': ''}
                        ]
                    },
                    'total_calories': 640,
                    'total_protein': 30
                }
            ],
            'lunch_options': [
                {
                    'name': 'grilled ribeye steak, cooked brown rice and salad',
                    'ingredients': {
                        'protein': [
                            {'name': 'grilled ribeye steak', 'calories': 200, 'protein': 20, 'base_quantity': 100,'unit': 'g'}
                            # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'cooked brown rice', 'calories': 400, 'protein': 7.5, 'base_quantity': 300,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'half avocado,cucumber and tomato salad', 'calories': 200, 'protein': 0, 'base_quantity': 1,'unit': ''}
                        ]
                    },
                    'total_calories': 800,
                    'total_protein': 27.5
                },
                {
                    'name': 'grilled chicken breast, pasta and salad',
                    'ingredients': {
                        'protein': [
                            {'name': 'grilled chicken breast', 'calories': 180, 'protein': 25, 'base_quantity': 100,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'pasta', 'calories': 400, 'protein': 15, 'base_quantity': 300,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'half avocado,cucumber and tomato salad', 'calories': 200, 'protein': 0, 'base_quantity': 1,'unit': ''}
                        ]
                    },
                    'total_calories': 780,
                    'total_protein': 40
                }
            ],
            'dinner_options': [
                {
                    'name': 'baked salmon, cooked pasta and roasted vegetables',
                    'ingredients': {
                        'protein': [
                            {'name': 'baked salmon', 'calories': 200, 'protein': 20, 'base_quantity': 100,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'cooked pasta', 'calories': 450, 'protein': 15, 'base_quantity': 300,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'roasted vegetables', 'calories': 100, 'protein': 0, 'base_quantity': 100,'unit': ''}
                        ]
                    },
                    'total_calories': 750,
                    'total_protein': 35
                },
                {
                    'name': 'grilled kebab, baked potato and roasted carrots',
                    'ingredients': {
                        'protein': [
                            {'name': 'grilled kebab', 'calories': 250, 'protein': 20, 'base_quantity': 100,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'baked potato', 'calories': 250, 'protein': 5, 'base_quantity': 250,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'roasted carrots', 'calories': 50, 'protein': 0, 'base_quantity': 100,'unit': ''}
                        ]
                    },
                    'total_calories': 550,
                    'total_protein': 25
                }
            ],
            'snack_options': [
                {
                    'name': 'greek yogurt(0%) and banana',
                    'ingredients': {
                        'protein': [
                            {'name': 'greek yogurt(0%)', 'calories': 150, 'protein': 20, 'base_quantity': 150,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'banana', 'calories': 100, 'protein': 0, 'base_quantity': 1,'unit': ''}  # 1 מנת בסיס
                        ]
                    },
                    'total_calories': 250,
                    'total_protein': 20
                },
                {
                    'name': 'Snack Option 2',
                    'ingredients': {
                        'protein': [
                            {'name': 'hummus', 'calories': 150, 'protein': 5, 'base_quantity': 100}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'carrot sticks', 'calories': 50, 'protein': 1, 'base_quantity': 100}  # 1 מנת בסיס
                        ]
                    },
                    'total_calories': 200,
                    'total_protein': 6
                }
            ]
        }
    }
    menu_c = {
        'meals': {
            'breakfast_options': [
                {
                    'name': 'cottege 5%, white bread and salad',
                    'ingredients': {
                        'protein': [
                            {'name': 'cottege 5%', 'calories': 250, 'protein': 25, 'base_quantity': 250,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'white bread', 'calories': 160, 'protein': 7, 'base_quantity': 2,'unit': 'slices'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'cucumber, tomato and red pepper salad', 'calories': 60, 'protein': 0, 'base_quantity': 1,'unit': ''}
                        ]
                    },
                    'total_calories': 470,
                    'total_protein': 32
                },
                {
                    'name': 'baked tuna, white bread and salad',
                    'ingredients': {
                        'protein': [
                            {'name': 'baked tuna', 'calories': 110, 'protein': 25, 'base_quantity': 100,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'white bread', 'calories': 160, 'protein': 7, 'base_quantity': 2,'unit': 'slices'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'cucumber, tomato and red pepper salad', 'calories': 60, 'protein': 0, 'base_quantity': 1,'unit': ''}
                        ]
                    },
                    'total_calories': 550,
                    'total_protein': 26
                }
            ],
            'lunch_options': [
                {
                    'name': 'grilled chicken breast,cooked brown rice and roasted brocoli',
                    'ingredients': {
                        'protein': [
                            {'name': 'grilled chicken breast', 'calories': 160, 'protein': 30, 'base_quantity': 100,'unit': 'g'}
                            # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'cooked brown rice', 'calories': 220, 'protein': 5, 'base_quantity': 200,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'roasted brocoli', 'calories': 55, 'protein': 4, 'base_quantity': 100,'unit': 'g'}
                        ]
                    },
                    'total_calories': 435,
                    'total_protein': 39
                },
                {
                    'name': 'lean turkey meat, quinoa and salad',
                    'ingredients': {
                        'protein': [
                            {'name': 'lean turkey meat', 'calories': 200, 'protein': 44, 'base_quantity': 150,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'cooked quinoa', 'calories': 220, 'protein': 8, 'base_quantity': 100,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'cucumber, tomato and red pepper salad', 'calories': 60, 'protein': 0, 'base_quantity': 1,'unit': ''}
                        ]
                    },
                    'total_calories': 610,
                    'total_protein': 50
                }
            ],
            'dinner_options': [
                {
                    'name': 'grilled tuna, cooked quinoa and salad',
                    'ingredients': {
                        'protein': [
                            {'name': 'grilled tuna', 'calories': 150, 'protein': 37.5, 'base_quantity': 150, 'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'cooked quinoa', 'calories': 180, 'protein': 6, 'base_quantity': 150,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'cucumber tomato and quarter avocado salad', 'calories': 120, 'protein': 1, 'base_quantity': 1,'unit': ''}
                        ]
                    },
                    'total_calories': 450,
                    'total_protein': 44.5
                },
                {
                    'name': 'smoked salmon, white bread and salad',
                    'ingredients': {
                        'protein': [
                            {'name': 'smoked salmon', 'calories': 240, 'protein': 40, 'base_quantity': 200, 'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'white bread', 'calories': 100, 'protein': 2, 'base_quantity': 1, 'unit': 'slices'}  # 1 מנת בסיס
                        ],
                        'other': [
                            {'name': 'cucumber, tomato and red pepper salad', 'calories': 60, 'protein': 0, 'base_quantity': 1, 'unit': ''}
                        ]
                    },
                    'total_calories': 400,
                    'total_protein': 42
                }
            ],
            'snack_options': [
                {
                    'name': 'greek yogurt(0%) and banana',
                    'ingredients': {
                        'protein': [
                            {'name': 'greek yogurt(0%)', 'calories': 150, 'protein': 20, 'base_quantity': 150,'unit': 'g'}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'banana', 'calories': 100, 'protein': 0, 'base_quantity': 1,'unit': ''}  # 1 מנת בסיס
                        ]
                    },
                    'total_calories': 250,
                    'total_protein': 20
                },
                {
                    'name': 'Snack Option 2',
                    'ingredients': {
                        'protein': [
                            {'name': 'hummus', 'calories': 150, 'protein': 5, 'base_quantity': 100}  # 1 מנת בסיס
                        ],
                        'carbs': [
                            {'name': 'carrot sticks', 'calories': 50, 'protein': 1, 'base_quantity': 100}  # 1 מנת בסיס
                        ]
                    },
                    'total_calories': 200,
                    'total_protein': 6
                }
            ]
        }
    }
    menu = {}


    def __init__(self,sort,goal, options):
        if goal == 'cutting':
            self.menu = self.menu_c
        elif goal == 'bulking':
            self.menu = self.menu_b
        elif goal == 'maintenance':
            self.menu = self.menu_m
        else:
            print(goal)
            raise ValueError("Invalid goal. Please choose 'cutting', 'bulking', or 'maintenance'.")

        if sort == 0:
            self.meal = self.menu['meals']['breakfast_options'][options[sort]]
            self.sum_calories = self.menu['meals']['breakfast_options'][options[sort]]['total_calories']
            self.sum_pro = self.menu['meals']['breakfast_options'][options[sort]]['total_protein']
        if sort == 1:
            self.meal = self.menu['meals']['lunch_options'][options[sort]]
            self.sum_calories = self.menu['meals']['lunch_options'][options[sort]]['total_calories']
            self.sum_pro = self.menu['meals']['lunch_options'][options[sort]]['total_protein']
        if sort == 2:
            self.meal = self.menu['meals']['dinner_options'][options[sort]]
            self.sum_calories = self.menu['meals']['dinner_options'][options[sort]]['total_calories']
            self.sum_pro = self.menu['meals']['dinner_options'][options[sort]]['total_protein']
        if sort == 3:
            self.meal = self.menu['meals']['snack_options'][options[sort]]
            self.sum_calories = self.menu['meals']['snack_options'][options[sort]]['total_calories']
            self.sum_pro = self.menu['meals']['snack_options'][options[sort]]['total_protein']



    def update_sums(self):
        self.calculate_cal()
        self.meal['total_calories'] = self.sum_calories
        self.meal['total_protein'] = self.sum_pro

    def calculate_cal(self):
        self.sum_calories = self.meal['ingredients']['protein'][0]['calories'] + self.meal['ingredients']['carbs'][0]['calories'] +  self.meal['ingredients']['other'][0]['calories']
        self.sum_pro = self.meal['ingredients']['protein'][0]['protein'] + self.meal['ingredients']['carbs'][0]['protein'] + self.meal['ingredients']['other'][0]['protein']


def custom_menu(new_menu, client_calories,client_protein):
    while(True):
        gap_pro = client_protein - new_menu.sum_pro
        check = new_menu.breakfast.meal['ingredients']['protein'][0]['protein']
        check1 = new_menu.lunch.meal['ingredients']['protein'][0]['protein']
        check2 = new_menu.dinner.meal['ingredients']['protein'][0]['protein']

        new_menu.breakfast.meal['ingredients']['protein'][0]['calories'] *= (((gap_pro/3)+check)/check)
        new_menu.breakfast.meal['ingredients']['protein'][0]['protein'] *= (((gap_pro/3)+check  )/check)
        new_menu.breakfast.meal['ingredients']['protein'][0]['base_quantity'] *= (((gap_pro/3)+check)/check)
        new_menu.breakfast.update_sums()

        new_menu.lunch.meal['ingredients']['protein'][0]['calories'] *= (((gap_pro / 3) + check1) / check1)
        new_menu.lunch.meal['ingredients']['protein'][0]['protein'] *= (((gap_pro / 3) + check1) / check1)
        new_menu.lunch.meal['ingredients']['protein'][0]['base_quantity'] *= (((gap_pro / 3) + check1) / check1)
        new_menu.lunch.update_sums()

        new_menu.dinner.meal['ingredients']['protein'][0]['calories'] *= (((gap_pro / 3) + check2) / check2)
        new_menu.dinner.meal['ingredients']['protein'][0]['protein'] *= (((gap_pro / 3) + check2) / check2)
        new_menu.dinner.meal['ingredients']['protein'][0]['base_quantity'] *= (((gap_pro / 3) + check2) / check2)
        new_menu.dinner.update_sums()

        new_menu.calculate_sums()
        gap_cal = client_calories - new_menu.sum_cal

        check = new_menu.breakfast.meal['ingredients']['carbs'][0]['calories']
        check1 = new_menu.lunch.meal['ingredients']['carbs'][0]['calories']
        check2 = new_menu.dinner.meal['ingredients']['carbs'][0]['calories']


        new_menu.breakfast.meal['ingredients']['carbs'][0]['calories'] *= (((gap_cal / 3) + check) / check)
        new_menu.breakfast.meal['ingredients']['carbs'][0]['protein'] *= (((gap_cal / 3) + check) / check)
        new_menu.breakfast.meal['ingredients']['carbs'][0]['base_quantity'] *= (((gap_cal / 3) + check) / check)
        new_menu.breakfast.update_sums()

        new_menu.lunch.meal['ingredients']['carbs'][0]['calories'] *= (((gap_cal / 3) + check1) / check1)
        new_menu.lunch.meal['ingredients']['carbs'][0]['protein'] *= (((gap_cal / 3) + check1) / check1)
        new_menu.lunch.meal['ingredients']['carbs'][0]['base_quantity'] *= (((gap_cal / 3) + check1) / check1)
        new_menu.lunch.update_sums()

        new_menu.dinner.meal['ingredients']['carbs'][0]['calories'] *= (((gap_cal / 3) + check2) / check2)
        new_menu.dinner.meal['ingredients']['carbs'][0]['protein'] *= (((gap_cal / 3) + check2) / check2)
        new_menu.dinner.meal['ingredients']['carbs'][0]['base_quantity'] *= (((gap_cal / 3) + check2) / check2)
        new_menu.dinner.update_sums()

        new_menu.calculate_sums()

        if((client_protein - 2 <new_menu.sum_pro< client_protein + 2) & (client_calories - 5 <new_menu.sum_cal< client_calories + 5)):
            rounding_num(new_menu)
            break

def rounding_num(menu):

    help_rounding(menu.breakfast.meal['ingredients']['protein'][0])
    help_rounding(menu.lunch.meal['ingredients']['protein'][0])
    help_rounding(menu.dinner.meal['ingredients']['protein'][0])

    help_rounding(menu.breakfast.meal['ingredients']['carbs'][0])
    help_rounding(menu.lunch.meal['ingredients']['carbs'][0])
    help_rounding(menu.dinner.meal['ingredients']['carbs'][0])

    menu.breakfast.update_sums()
    menu.lunch.update_sums()
    menu.dinner.update_sums()
    menu.calculate_sums()
def help_rounding(ingredient):
    if(ingredient['unit'] == 'g'):
        ingredient['base_quantity'] = round(ingredient['base_quantity']/5)*5

    else:
        ingredient['base_quantity'] = round(ingredient['base_quantity'] * 2) /2

def print_menu(new_menu):
    print(new_menu.sum_pro)

    print(new_menu.sum_cal)
    print()

    print(new_menu.breakfast.meal['ingredients']['protein'][0]['name'])
    print(new_menu.breakfast.meal['ingredients']['protein'][0]['base_quantity'])
    print()

    print(new_menu.breakfast.meal['ingredients']['carbs'][0]['name'])
    print(new_menu.breakfast.meal['ingredients']['carbs'][0]['base_quantity'])
    print()

    print(new_menu.breakfast.meal['ingredients']['other'][0]['name'])
    print(new_menu.breakfast.meal['ingredients']['other'][0]['base_quantity'])
    print()
    print(new_menu.lunch.meal['ingredients']['protein'][0]['name'])
    print(new_menu.lunch.meal['ingredients']['protein'][0]['base_quantity'])
    print()

    print(new_menu.lunch.meal['ingredients']['carbs'][0]['name'])
    print(new_menu.lunch.meal['ingredients']['carbs'][0]['base_quantity'])
    print()

    print(new_menu.lunch.meal['ingredients']['other'][0]['name'])
    print(new_menu.lunch.meal['ingredients']['other'][0]['base_quantity'])
    print()

    print(new_menu.dinner.meal['ingredients']['protein'][0]['name'])
    print(new_menu.dinner.meal['ingredients']['protein'][0]['base_quantity'])
    print()

    print(new_menu.dinner.meal['ingredients']['carbs'][0]['name'])
    print(new_menu.dinner.meal['ingredients']['carbs'][0]['base_quantity'])
    print()

    print(new_menu.dinner.meal['ingredients']['other'][0]['name'])
    print(new_menu.dinner.meal['ingredients']['other'][0]['base_quantity'])
    print()

    print(new_menu.snack.meal['ingredients']['protein'][0]['name'])
    print(new_menu.snack.meal['ingredients']['protein'][0]['base_quantity'])
    print()

    print(new_menu.snack.meal['ingredients']['carbs'][0]['name'])
    print(new_menu.snack.meal['ingredients']['carbs'][0]['base_quantity'])
    print()


def generate_menu(calories,protein, goal,options = [0,0,0,0]):
    new_menu = menu(goal,options)
    custom_menu(new_menu, calories, protein)

    # Return the structured menu dictionary
    menu_dict = {
        "sum_protein": round(new_menu.sum_pro),
        "sum_calories": round(new_menu.sum_cal),
        "meals": {
            "breakfast": {
                "protein": new_menu.breakfast.meal['ingredients']['protein'][0]['name'],
                "carbs": new_menu.breakfast.meal['ingredients']['carbs'][0]['name'],
                "other": new_menu.breakfast.meal['ingredients']['other'][0]['name'],
                "base_quantities": {
                    "protein": new_menu.breakfast.meal['ingredients']['protein'][0]['base_quantity'],
                    "carbs": new_menu.breakfast.meal['ingredients']['carbs'][0]['base_quantity'],
                    "other": new_menu.breakfast.meal['ingredients']['other'][0]['base_quantity'],
                    "pro_unit": new_menu.breakfast.meal['ingredients']['protein'][0]['unit'],
                    "carbs_unit": new_menu.breakfast.meal['ingredients']['carbs'][0]['unit'],
                    "other_unit": new_menu.breakfast.meal['ingredients']['other'][0]['unit']
                }
            },
            "lunch": {
                "protein": new_menu.lunch.meal['ingredients']['protein'][0]['name'],
                "carbs": new_menu.lunch.meal['ingredients']['carbs'][0]['name'],
                "other": new_menu.lunch.meal['ingredients']['other'][0]['name'],
                "base_quantities": {
                    "protein": new_menu.lunch.meal['ingredients']['protein'][0]['base_quantity'],
                    "carbs": new_menu.lunch.meal['ingredients']['carbs'][0]['base_quantity'],
                    "other": new_menu.lunch.meal['ingredients']['other'][0]['base_quantity'],
                    "pro_unit": new_menu.lunch.meal['ingredients']['protein'][0]['unit'],
                    "carbs_unit": new_menu.lunch.meal['ingredients']['carbs'][0]['unit'],
                    "other_unit": new_menu.lunch.meal['ingredients']['other'][0]['unit']
                }
            },
            "dinner": {
                "protein": new_menu.dinner.meal['ingredients']['protein'][0]['name'],
                "carbs": new_menu.dinner.meal['ingredients']['carbs'][0]['name'],
                "other": new_menu.dinner.meal['ingredients']['other'][0]['name'],
                "base_quantities": {
                    "protein": new_menu.dinner.meal['ingredients']['protein'][0]['base_quantity'],
                    "carbs": new_menu.dinner.meal['ingredients']['carbs'][0]['base_quantity'],
                    "other": new_menu.dinner.meal['ingredients']['other'][0]['base_quantity'],
                    "pro_unit": new_menu.dinner.meal['ingredients']['protein'][0]['unit'],
                    "carbs_unit": new_menu.dinner.meal['ingredients']['carbs'][0]['unit'],
                    "other_unit": new_menu.dinner.meal['ingredients']['other'][0]['unit']
                }
            },
            "snack": {
                "protein": new_menu.snack.meal['ingredients']['protein'][0]['name'],
                "carbs": new_menu.snack.meal['ingredients']['carbs'][0]['name'],
                "base_quantities": {
                    "protein": new_menu.snack.meal['ingredients']['protein'][0]['base_quantity'],
                    "carbs": new_menu.snack.meal['ingredients']['carbs'][0]['base_quantity'],
                    "pro_unit": new_menu.snack.meal['ingredients']['protein'][0]['unit'],
                    "carbs_unit": new_menu.snack.meal['ingredients']['carbs'][0]['unit']

                }
            }
        }
    }

    return menu_dict

#print(generate_menu(1800, 100))