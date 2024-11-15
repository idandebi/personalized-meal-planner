document.getElementById('calorie-form').addEventListener('submit', function (event) {
    event.preventDefault();

    let weight = parseFloat(document.getElementById('weight').value);
    let height = parseFloat(document.getElementById('height').value);
    const age = parseFloat(document.getElementById('age').value);
    const activity = parseFloat(document.getElementById('activity').value);
    const goal = document.querySelector('input[name="goal"]:checked').value;

    const weightUnit = document.getElementById('weight-unit').value;
    const heightUnit = document.getElementById('height-unit').value;

    // Convert weight if necessary
    if (weightUnit === 'lbs') {
        weight = weight / 2.205; // convert lbs to kg
    }

    // Convert height if necessary
    if (heightUnit === 'feet') {
        height = height * 30.48; // convert feet to cm
    }

    if (!isNaN(weight) && !isNaN(height) && !isNaN(age) && !isNaN(activity)) {
        const bmr = 10 * weight + 6.25 * height - 5 * age + 5;
        const calorieIntake = bmr * activity;
        let recommendedCalories;
        let proteinIntake;

        // Calculate recommended protein and calories based on goal
        if (goal === 'cutting') {
            recommendedCalories = calorieIntake - 500;
            proteinIntake = weight * 2.5; // Protein for cutting
        } else if (goal === 'bulking') {
            recommendedCalories = calorieIntake + 500;
            proteinIntake = weight * 2; // Protein for bulking
        } else if (goal === 'maintenance') {
            recommendedCalories = calorieIntake;
            proteinIntake = weight * 1.8; // Protein for maintenance
        }

        // Display recommended calories and protein
        document.getElementById('result').innerText =
            `Recommended calorie intake for ${goal}:\n ${recommendedCalories.toFixed(2)} kcal\n` +
            `\nRecommended protein intake for ${goal}:\n ${proteinIntake.toFixed(2)} grams`;

        // Store values for later use
        document.getElementById('recommendedCalories').value = recommendedCalories;
        document.getElementById('proteinIntake').value = proteinIntake;

        // Show the "Show Menu" and "Build Custom Menu" buttons
        document.getElementById('show-menu-button').style.display = 'block';
        document.getElementById('show-meal-selection-button').style.display = 'block'; // Show the custom menu button
    } else {
        document.getElementById('result').innerText = 'Please fill out all fields correctly.';
    }
});

function clearDisplay() {
    document.getElementById('menu-result').innerHTML = ''; // מנקה את התצוגה של תפריט התוצאות
    document.getElementById('meal-selection-form').style.display = 'none'; // מסתיר את טופס בחירת הארוחות
}

// When the user clicks the "Show Menu" button
document.getElementById('show-menu-button').addEventListener('click', function () {
    clearDisplay();
    const recommendedCalories = parseFloat(document.getElementById('recommendedCalories').value);
    const proteinIntake = parseFloat(document.getElementById('proteinIntake').value);
    const goal = document.querySelector('input[name="goal"]:checked').value; // Get the selected goal

    // Debugging: Print the calories, protein, and goal to be sent
    console.log("Sending Calories:", recommendedCalories);
    console.log("Sending Protein:", proteinIntake);
    console.log("Sending Goal:", goal); // Debugging

    // Send the data to the Flask server
    fetch('http://localhost:5000/generate-menu', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            calories: recommendedCalories,
            protein: proteinIntake,
            goal: goal // Add the goal to the body
        }),
    })
        .then(response => {
            console.log("Response status:", response.status);
            return response.json(); // Parse the JSON response
        })
        .then(data => {
            console.log("Server response data:", data);

            // Check if the response contains an error message
            if (data.error) {
                document.getElementById('menu-result').innerText = data.error;
            } else {
                // Format the menu result into a readable format
                const menu = data.meals;

                let result = "<br>"; // השתמש ב-br עבור רווחי שורות

                result += `<strong>Breakfast:</strong><br><br>${menu.breakfast.base_quantities.protein} ${menu.breakfast.base_quantities.pro_unit} ${menu.breakfast.protein}, <br>${menu.breakfast.base_quantities.carbs} ${menu.breakfast.base_quantities.carbs_unit} ${menu.breakfast.carbs}, <br>${menu.breakfast.base_quantities.other} ${menu.breakfast.base_quantities.other_unit} ${menu.breakfast.other}<br><br>`;
                result += `<strong>Lunch:</strong><br><br>${menu.lunch.base_quantities.protein} ${menu.lunch.base_quantities.pro_unit} ${menu.lunch.protein}, <br>${menu.lunch.base_quantities.carbs} ${menu.lunch.base_quantities.carbs_unit} ${menu.lunch.carbs}, <br>${menu.lunch.base_quantities.other} ${menu.lunch.base_quantities.other_unit} ${menu.lunch.other}<br><br>`;
                result += `<strong>Dinner:</strong><br><br>${menu.dinner.base_quantities.protein} ${menu.dinner.base_quantities.pro_unit} ${menu.dinner.protein}, <br>${menu.dinner.base_quantities.carbs} ${menu.dinner.base_quantities.carbs_unit} ${menu.dinner.carbs}, <br>${menu.dinner.base_quantities.other} ${menu.dinner.base_quantities.other_unit} ${menu.dinner.other}<br><br>`;
                result += `<strong>Snack:</strong><br><br>${menu.snack.base_quantities.protein} ${menu.snack.base_quantities.pro_unit} ${menu.snack.protein}, <br>${menu.snack.base_quantities.carbs} ${menu.snack.base_quantities.carbs_unit} ${menu.snack.carbs}<br><br><br><br>`;

                result += `${data.sum_calories} kcal<br>${data.sum_protein} g protein`; // הוספת הפלט לסוף

                document.getElementById('menu-result').innerHTML = result;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('menu-result').innerText = 'An error occurred while generating the menu.';
        });
});

// Show the meal selection form when the button is clicked
document.getElementById('show-meal-selection-button').addEventListener('click', function () {
    clearDisplay();
    document.getElementById('meal-selection-form').style.display = 'block'; // Show the meal selection form
    loadMealOptions(); // Load meal options from the server
});

// Load meal options from the server
function loadMealOptions() {
    const goal = document.querySelector('input[name="goal"]:checked').value; // אסוף את ה-GOAL שנבחר

    // שלח את הבקשה לשרת עם ה-GOAL
    fetch('http://localhost:5000/get-meal-options', {
        method: 'POST', // השתמש במתודה POST
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ goal: goal }) // שלח את ה-GOAL ב-body
    })
        .then(response => response.json())
        .then(data => {
            console.log("Meal Options Data:", data);
            populateMealSelection(data); // Populate the meal selection form
        })
        .catch(error => console.error('Error:', error));
}

// Populate meal selection form
function populateMealSelection(data) {
    const breakfastContainer = document.getElementById('breakfast-options');
    const lunchContainer = document.getElementById('lunch-options');
    const dinnerContainer = document.getElementById('dinner-options');
    const snackContainer = document.getElementById('snack-options');

    // Clear existing options
    breakfastContainer.innerHTML = '';
    lunchContainer.innerHTML = '';
    dinnerContainer.innerHTML = '';
    snackContainer.innerHTML = '';

    // Populate breakfast options
    breakfastContainer.innerHTML += `<br>`;
    data.breakfast.forEach((option, index) => {
        const label = document.createElement('label');
        label.innerHTML = `<input type="radio" name="breakfast-options" value="${index}"> ${option}`; // השתמש באינדקס כערך
        breakfastContainer.appendChild(label);
        breakfastContainer.appendChild(document.createElement('br')); // הוספת שורה חדשה
        
    });
    breakfastContainer.innerHTML += `<br>`;


    // Populate lunch options
    lunchContainer.innerHTML += `<br>`;
    data.lunch.forEach((option, index) => {
        const label = document.createElement('label');
        label.innerHTML = `<input type="radio" name="lunch-options" value="${index}"> ${option}`; // השתמש באינדקס כערך
        lunchContainer.appendChild(label);
        lunchContainer.appendChild(document.createElement('br')); // הוספת שורה חדשה
    });
    lunchContainer.innerHTML += `<br>`;

    // Populate dinner options
    dinnerContainer.innerHTML += `<br>`;
    data.dinner.forEach((option, index) => {
        const label = document.createElement('label');
        label.innerHTML = `<input type="radio" name="dinner-options" value="${index}"> ${option}`; // השתמש באינדקס כערך
        dinnerContainer.appendChild(label);
        dinnerContainer.appendChild(document.createElement('br')); // הוספת שורה חדשה
    });
    dinnerContainer.innerHTML += `<br>`;

    // Populate snack options
    snackContainer.innerHTML += `<br>`
    data.snack.forEach((option, index) => {
        const label = document.createElement('label');
        label.innerHTML = `<input type="radio" name="snack-options" value="${index}"> ${option}`; // השתמש באינדקס כערך
        snackContainer.appendChild(label);
        snackContainer.appendChild(document.createElement('br')); // הוספת שורה חדשה
    });
    snackContainer.innerHTML += `<br>`
}

// Add event listener for meal selection form submission
document.getElementById('meal-selection-form').addEventListener('submit', function (event) {
    event.preventDefault();

    

    // Gather selected meal options (only one per meal type)
    const breakfastOption = document.querySelector('input[name="breakfast-options"]:checked')?.value || null; // Use null if no selection
    const lunchOption = document.querySelector('input[name="lunch-options"]:checked')?.value || null;
    const dinnerOption = document.querySelector('input[name="dinner-options"]:checked')?.value || null;
    const snackOption = document.querySelector('input[name="snack-options"]:checked')?.value || null;

    // Convert options to indices
    const breakfastIndex = breakfastOption ? parseInt(breakfastOption) : -1; // Assuming you want to send -1 if nothing is selected
    const lunchIndex = lunchOption ? parseInt(lunchOption) : -1;
    const dinnerIndex = dinnerOption ? parseInt(dinnerOption) : -1;
    const snackIndex = snackOption ? parseInt(snackOption) : -1;

    // Create an array of selected options
    const selectedOptions = [breakfastIndex, lunchIndex, dinnerIndex, snackIndex];

    // Get the recommended calorie and protein values
    const recommendedCalories = parseFloat(document.getElementById('recommendedCalories').value);
    const recommendedProtein = parseFloat(document.getElementById('proteinIntake').value);

    // Get the selected goal
    const goal = document.querySelector('input[name="goal"]:checked').value; // אסוף את ה-GOAL שנבחר

    // Send selected meal options to server
    fetch('http://localhost:5000/custom-menu', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            mealSelections: selectedOptions, // Send the array of selections
            calories: recommendedCalories, // Send the recommended calorie value
            protein: recommendedProtein, // Send the recommended protein value
            goal: goal // Send the goal
        }),
    })
        .then(response => response.json())
        .then(data => {
            // Process the custom menu response
            console.log("Custom Menu Data:", data);
            // Display custom menu data
            const menuResult = document.getElementById('menu-result');
            menuResult.innerHTML = ''; // Clear previous results

            const menu = data.meals;

            menuResult.innerHTML += `<strong>Breakfast:</strong><br><br>${menu.breakfast.base_quantities.protein} ${menu.breakfast.base_quantities.pro_unit} ${menu.breakfast.protein}, <br>${menu.breakfast.base_quantities.carbs} ${menu.breakfast.base_quantities.carbs_unit} ${menu.breakfast.carbs}, <br>${menu.breakfast.base_quantities.other} ${menu.breakfast.base_quantities.other_unit} ${menu.breakfast.other}<br><br>`;
            menuResult.innerHTML += `<strong>Lunch:</strong><br><br>${menu.lunch.base_quantities.protein} ${menu.lunch.base_quantities.pro_unit} ${menu.lunch.protein}, <br>${menu.lunch.base_quantities.carbs} ${menu.lunch.base_quantities.carbs_unit} ${menu.lunch.carbs}, <br>${menu.lunch.base_quantities.other} ${menu.lunch.base_quantities.other_unit} ${menu.lunch.other}<br><br>`;
            menuResult.innerHTML += `<strong>Dinner:</strong><br><br>${menu.dinner.base_quantities.protein} ${menu.dinner.base_quantities.pro_unit} ${menu.dinner.protein}, <br>${menu.dinner.base_quantities.carbs} ${menu.dinner.base_quantities.carbs_unit} ${menu.dinner.carbs}, <br>${menu.dinner.base_quantities.other} ${menu.dinner.base_quantities.other_unit} ${menu.dinner.other}<br><br>`;
            menuResult.innerHTML += `<strong>Snack:</strong><br><br>${menu.snack.base_quantities.protein} ${menu.snack.base_quantities.pro_unit} ${menu.snack.protein}, <br>${menu.snack.base_quantities.carbs} ${menu.snack.base_quantities.carbs_unit} ${menu.snack.carbs}<br><br><br><br>`;

            menuResult.innerHTML += `${data.sum_calories} kcal<br>${data.sum_protein} g protein`;
            document.getElementById('meal-selection-form').style.display = 'none';

        })
        .catch(error => console.error('Error:', error));
});
