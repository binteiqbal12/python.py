# ============================================================
#   CLASS 3 — HOMEWORK QUESTIONS
#   Functions, Loops & OOP
#   Total Questions: 10
# ============================================================
#   Instructions:
#     - Write your answer below each question.
#     - Do NOT delete the question comments.
#     - Run your code after each question to test it.
#     - Questions 1-3  → Functions
#     - Questions 4-6  → Loops
#     - Questions 7-10 → OOP
# ============================================================


# ─────────────────────────────────────────────
# QUESTION 1 — Functions (Basic)
# ─────────────────────────────────────────────
# A mobile phone shop gives discounts based on the price:
#
#   Price >= 100,000  → 15% discount
#   Price >= 50,000   → 10% discount
#   Price >= 20,000   →  5% discount
#   Price <  20,000   →  No discount
#
# Write a function called phone_discount(price) that:
#   1. Figures out the correct discount percentage.
#   2. Calculates the discount amount.
#   3. Calculates the final price after discount.
#   4. RETURNS the final price.
#
# Then call it 3 times with different prices and print results.
#
# Example:
#   phone_discount(120000) → Final price: Rs.102000.0 (15% off)
#   phone_discount(60000)  → Final price: Rs.54000.0  (10% off)
#   phone_discount(15000)  → Final price: Rs.15000.0  (no discount)

# # Write your code below:



def phone_discount(price):
    if price >= 100000:
        discount_percent = 15
    elif price >= 50000:
        discount_percent = 10
    elif price >= 20000:
        discount_percent = 5
    else:
        discount_percent = 0

    discount_amount= price*discount_percent/100
    final_price = price - discount_amount

    print(f"Original Price : Rs. {price}")
    print(f"Discount       : {discount_percent}%  Rs. {discount_amount}")
    print(f"Final Price    : Rs. {final_price}")
    print("-" * 40)
    
    return final_price

phone_discount(150000)
phone_discount(60000)  
phone_discount(15000) 

# ─────────────────────────────────────────────
# QUESTION 2 — Functions (Default Parameters + Return)
# ─────────────────────────────────────────────
# Write a function called pizza_order(size, toppings=1, extra_cheese=False)
# that calculates the total price of a pizza order.
#
# Pricing rules:
#   Size:
#     "small"  → Rs. 400
#     "medium" → Rs. 650
#     "large"  → Rs. 900
#   Each topping costs Rs. 80  (toppings default = 1)
#   Extra cheese adds Rs. 120  (extra_cheese default = False)
#
# The function should:
#   - Calculate and RETURN the total price.
#   - Print a short summary inside the function showing what was ordered.
#
# Call the function at least 3 times with different combinations.
#
# Example:
#   pizza_order("large", toppings=3, extra_cheese=True)
#   → Large pizza | 3 toppings | Extra cheese: Yes | Total: Rs.1260

# Write your code below:
def pizza_order(size, toppings=1, extra_cheese=False):
    size_prices = {
        "small": 400,
        "medium": 650,
        "large": 900
    }
    
    base_price = size_prices[size]
    total_price = base_price + (toppings * 80)

    if extra_cheese:
        total_price += 120

    print(f"{size.capitalize()} pizza | {toppings} toppings | Extra cheese: {'Yes' if extra_cheese else 'No'} | Total: Rs.{total_price}")

    return total_price

pizza_order("large", toppings=3, extra_cheese=True)
pizza_order("medium", toppings=2)   
pizza_order("small", extra_cheese=True)

# ─────────────────────────────────────────────
# QUESTION 3 — Functions (Multiple Return Values + Scope)
# ─────────────────────────────────────────────
# Write a function called analyse_text(sentence) that:
#   1. Counts the total number of words.
#   2. Counts the total number of characters (excluding spaces).
#   3. Finds the longest word.
#   4. Returns ALL THREE values at once.
#
# Then ask the user to enter a sentence and call the function.
# Print the results clearly.
#
# Example:
#   Input   : "Python is an amazing programming language"
#   Output  :
#     Words       : 6
#     Characters  : 36
#     Longest word: programming

# Write your code below:

def analyse_test(sentence):
    words = sentence.split()
    num_words = len(words)
    num_characters = len(sentence.replace(" ", ""))
    longest_word = max(words, key=len)

    return num_words, num_characters, longest_word
sentence = input("Enter a sentence: ")
words, characters, longest = analyse_test(sentence)
print(f"sentence: {sentence}")
print(f"Words       : {words}")
print(f"Characters  : {characters}")    
print(f"Longest word: {longest}")


# ─────────────────────────────────────────────
# QUESTION 4 — Loops (for + range + accumulator)
# ─────────────────────────────────────────────
# A factory produces items every day of the week.
# Daily production numbers (Monday to Sunday):
#
#   production = [120, 95, 140, 110, 130, 80, 60]
#
# Write a program using a for loop that:
#   1. Prints each day's production with the day name.
#      (index 0 = Monday, index 1 = Tuesday, ... index 6 = Sunday)
#   2. Tracks and prints the RUNNING TOTAL after each day.
#   3. After the loop, prints:
#        - Total weekly production
#        - Highest single-day production
#        - Lowest single-day production
#        - Average daily production (rounded to 1 decimal)
#        - Number of days that met the target (target = 100 units)
#
# Example output (first 2 lines):
#   Monday    : 120 units | Running Total: 120
#   Tuesday   :  95 units | Running Total: 215

# Write your code below:
production = [120, 95, 140, 110, 130, 80, 60]


day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i in range(len(production)):
        running_total = sum(production[:i + 1])
        print(f"{day_name[i]:<10}: {production[i]:<10} units | Running Total: {running_total}")
    
total_weekly=(sum(production))
highest_single_day_production=(max(production))
lowest_single_day_production=(min(production))
average_production= round(sum(production)/len(production),1)
target=100
single_day_production= len([i for i in production if i>= target])

print(f"Total weekly production: {total_weekly} units")
print(f"Highest single-day production: {highest_single_day_production} units")
print(f"Lowest single-day production: {lowest_single_day_production} units")
print(f"Average daily production: {average_production} units")
print(f"Number of days that met the target ({target} units): {single_day_production} days")





# ─────────────────────────────────────────────
# QUESTION 5 — Loops (while + break + continue)
# ─────────────────────────────────────────────
# Build a simple QUIZ GAME using a while loop.
#
# Rules:
#   - Store at least 4 questions in a list. Each question is a
#     tuple: (question_text, correct_answer)
#   - Ask each question one by one.
#   - If the answer is correct → print "Correct! ✔" and add 1 point.
#   - If the answer is wrong   → print "Wrong! The answer was X."
#   - If the user types "skip" → use continue to skip that question.
#   - If the user types "quit" → use break to end the game early.
#   - At the end, print the final score out of total questions asked.
#
# Sample questions you can use (or make your own):
#   ("What is the capital of Pakistan?", "islamabad")
#   ("How many days are in a week?", "7")
#   ("What language are we learning?", "python")
#   ("What is 15 + 27?", "42")

# Write your code below:
questions=[("What is the capital of Pakistan?", "islamabad"),
("How many days are in a week?", "7"),
("What language are we learning?", "python"),
("What is 15 + 27?", "42")
]
score=0
total_questions=len(questions)
current_index=0
print("="*40)
print(f" WELCOME TO QUIZ GAME....")
print("="*40)
print(f"type 'skip' to skip a question or 'quit' to quit early")

while current_index<total_questions:
    question_text, correct_answer=questions[current_index]
    user_answer = input(f"Question {current_index+1}: {question_text} ")
    if user_answer.lower()=="quit":
        print("You chose to quit the game early.")
        break   
    elif user_answer.lower()=="skip":
        print("You chose to skip this question.")
        current_index += 1
        continue
    
    elif user_answer.lower()==correct_answer.lower():
            print("Correct! ✔")
            score += 1
            current_index += 1
    else:
            print(f"Wrong! The answer was {correct_answer}.")
            current_index += 1
        
print(f"Final Score: {score} out of {current_index} questions asked.")   


# ─────────────────────────────────────────────
# QUESTION 6 — Loops (Nested loops — real-world)
# ─────────────────────────────────────────────
# A school has 3 classes: A, B, C.
# Each class has 4 students with the following marks:
#
#   class_data = {
#       "Class A": [85, 72, 91, 68],
#       "Class B": [55, 78, 63, 90],
#       "Class C": [40, 88, 74, 59],
#   }
#
# Write a program using NESTED LOOPS that:
#   1. Loops through each class.
#   2. Inside, loops through each student's marks.
#   3. Prints each student's mark and whether they Passed (>=50) or Failed.
#   4. After each class, prints the class average.
#   5. After all classes, prints which class had the HIGHEST average.
#
# Example (for Class A):
#   Class A:
#     Student 1: 85 → Pass
#     Student 2: 72 → Pass
#     Student 3: 91 → Pass
#     Student 4: 68 → Pass
#   Class A Average: 79.0

# Write your code below:
class_data = {
    "Class A": [85, 72, 91, 68],
    "Class B": [55, 78, 63, 90],
    "Class C": [40, 88, 74, 59],
}
for class_name, marks in class_data.items():
    print(f"{class_name}:")
    total_marks = 0
    for i, mark in enumerate(marks):
        status = "Pass" if mark >= 50 else "Fail"
        print(f"  Student {i + 1}: {mark} → {status}")
        total_marks += mark
    class_average = total_marks / len(marks)
    print(f"{class_name} Average: {class_average:.1f}\n")

        
# ─────────────────────────────────────────────
# QUESTION 7 — OOP (Class + __init__ + Methods)
# ─────────────────────────────────────────────
# Create a class called MobilePhone with:
#
#   Attributes (set in __init__):
#     brand       → e.g. "Samsung"
#     model       → e.g. "Galaxy S24"
#     battery     → starts at 100 (always, regardless of input)
#     is_on       → starts as False (phone is off by default)
#
#   Methods:
#     power_on()        → if already on, print "Already on."
#                         otherwise set is_on = True and print a message.
#     power_off()       → if already off, print "Already off."
#                         otherwise set is_on = False and print a message.
#     make_call(mins)   → if phone is off, print "Turn on the phone first."
#                         otherwise reduce battery by (mins * 2).
#                         If battery drops below 0, set it to 0 and
#                         print "Battery died during the call!"
#                         Otherwise print call duration and remaining battery.
#     charge(percent)   → increase battery by percent, max 100.
#                         Print the new battery level.
#     status()          → print brand, model, battery %, and on/off state.
#
# Create TWO phones and test all methods on each.

# Write your code below:

class MobilePhone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battery = 100      
        self.is_on = "False"     

    def power_on(self):
        if self.is_on:
            print("Already on.")
        else:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")

    def power_off(self):
        if not self.is_on:
            print("Already off.")
        else:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")

    def make_call(self, mins):
        if not self.is_on:
            print("Turn on the phone first.")
        else:
            self.battery -= mins * 2
            if self.battery < 0:
                self.battery = 0
                print("Battery died during the call!")
            else:
                print(f"Call lasted {mins} mins. Battery remaining: {self.battery}%")

    def charge(self, percent):
        self.battery = min(100, self.battery + percent)
        print(f"Charging done. Battery is now {self.battery}%")

    def status(self):
        state = "ON" if self.is_on else "OFF"
        print(f"Brand: {self.brand} | Model: {self.model} | Battery: {self.battery}% | State: {state}")


phone1 = MobilePhone("Samsung", "Galaxy S24")
phone2 = MobilePhone("Apple", "iPhone 15")

phone1.status()
phone1.power_on()
phone1.make_call(10)
phone1.make_call(40)
phone1.charge(50)
phone1.status() 


# ─────────────────────────────────────────────
# QUESTION 8 — OOP (Class with a list + methods)
# ─────────────────────────────────────────────
# Create a class called ShoppingCart that models an
# online shopping cart.
#
#   Attributes (set in __init__):
#     customer_name  → name of the customer
#     items          → empty list (will store dictionaries)
#
#   Each item in the list is a dictionary:
#     { "name": "Milk", "price": 120, "qty": 2 }
#
#   Methods:
#     add_item(name, price, qty=1)
#       → Add the item to the list. If the item already exists,
#         increase its quantity instead.
#
#     remove_item(name)
#       → Remove the item by name. If not found, print a message.
#
#     get_total()
#       → Return the total cost (price × qty for all items).
#
#     view_cart()
#       → Print a formatted receipt showing all items,
#         their quantities, prices, and the grand total.
#
# Create a cart, add 4 items, remove 1, then print the receipt.

# Write your code below:

class  ShoppingCart:
    def __init__(self,customer_name):
        self.customer_name=customer_name
        self.items=[]
     
    
    def add_item(self, name, price, qty=1):
        for item in self.items:
            if item["name"].lower() == name.lower():
                item["qty"] += qty
                return
        self.items.append({"name": name, "price": price, "qty": qty})

    def remove_item(self,name):
        for item in self.items:
            if item["name"].lower()==name.lower():
                self.items.remove(item)
                return
        print(f"{name} not found in the cart.")

    def get_total(self):
        return sum(item["price"] * item["qty"] for item in self.items)

    def view_cart(self):
        print(f"  Shopping Cart — {self.customer_name}")
        print(f"{'='*40}")
        print(f"{'Item':<15} {'Qty':>5} {'Price':>8} {'Subtotal':>10}")
        print(f"{'-'*40}")
        for item in self.items:
            subtotal = item["price"] * item["qty"]
            print(f"{item['name']:<15} {item['qty']:>5} {item['price']:>8.2f} {subtotal:>10.2f}")
        print(f"{'='*40}")
        print(f"{'Grand Total:':>30} {self.get_total():>10.2f}")
        print(f"{'='*40}\n")


cart = ShoppingCart("Aqsaa")

cart.add_item("Milk", 120, 2)
cart.add_item("Bread", 85)
cart.add_item("Eggs", 200, 3)
cart.add_item("Butter", 350)
cart.get_total()
cart.remove_item("Bread")

cart.view_cart()

# ─────────────────────────────────────────────
# QUESTION 9 — OOP (Inheritance)
# ─────────────────────────────────────────────
# Create a base class called Employee with:
#   Attributes: name, employee_id, base_salary
#   Methods:
#     get_info()     → print name, ID, and base salary
#     get_salary()   → return base_salary
#
# Then create TWO child classes that inherit from Employee:
#
#   class FullTimeEmployee(Employee):
#     Extra attribute: department
#     Overrides get_salary() → adds a monthly bonus of Rs. 5,000
#     Overrides get_info()   → also shows department + final salary
#
#   class PartTimeEmployee(Employee):
#     Extra attribute: hours_per_week
#     Overrides get_salary() → salary = base_salary × (hours_per_week / 40)
#     Overrides get_info()   → also shows hours per week + final salary
#
# Create at least 2 full-time and 2 part-time employees.
# Store all 4 in a single list.
# Loop through the list and call get_info() on each.
# At the end, print who earns the most.

# Write your code below:
 
class Employee: 
    def __init__(self,name, employee_id, base_salary):
        self.name=name
        self.employee_id=employee_id
        self.base_salary=base_salary
    
    def get_info(self):
        print(f"Name: {self.name} | ID: {self.employee_id} | Base Salary: Rs.{self.base_salary}")

    def get_salary(self):
        return self.base_salary 

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, department):
        super().__init__(name, employee_id, base_salary)
        self.department=department

    def get_salary(self):
        return self.base_salary + 5000

    def get_info(self):
        final_salary=self.get_salary()
        print(f"Name: {self.name} | ID: {self.employee_id} | Department: {self.department} | Final Salary: Rs.{final_salary}")

class PartTimeEmployee(Employee):
    def __init__(self,name, employee_id, base_salary, hours_per_week):
        super().__init__(name, employee_id, base_salary)
        self.hours_per_week=hours_per_week

    def get_salary(self):
        total_salary =self.base_salary * (self.hours_per_week / 40)
        return total_salary
    def get_info(self):
          print(f"Name: {self.name} | ID: {self.employee_id} | Hours per Week: {self.hours_per_week} | Final Salary: Rs.{self.get_salary()}")

full_time1=FullTimeEmployee("Ali", 101, 50000, "IT")
full_time2=FullTimeEmployee("Sara", 102, 60000, "HR")
part_time1=PartTimeEmployee("Ahmed", 201, 40000, 20)
part_time2=PartTimeEmployee("Fatima", 202, 35000, 15)

employess=[full_time1, full_time2, part_time1, part_time2]
for employee in employess:
    employee.get_info()

higheast_earner=max(employess, key=lambda emp: emp.get_salary())
print(f"\nHighest Earner: {higheast_earner.name} | Final Salary: Rs.{higheast_earner.get_salary()}")


# ─────────────────────────────────────────────
# QUESTION 10 — OOP (Full Mini Project)
# ─────────────────────────────────────────────
# Build a HOSPITAL APPOINTMENT SYSTEM using OOP.
#
# Create a class called Doctor with:
#   Attributes: name, specialization, fee
#   Method: get_info() → print doctor details
#
# Create a class called Appointment with:
#   Attributes:
#     patient_name
#     doctor         → a Doctor OBJECT (not just a name)
#     date
#     is_confirmed   → starts as False
#   Methods:
#     confirm()      → set is_confirmed = True, print confirmation
#     cancel()       → set is_confirmed = False, print cancellation
#     summary()      → print full details of the appointment
#
# Create a class called Hospital with:
#   Attributes:
#     hospital_name
#     appointments   → empty list
#   Methods:
#     book_appointment(patient_name, doctor, date)
#       → create an Appointment object and add to the list
#     view_all()     → print summary of every appointment
#     count_confirmed() → return how many appointments are confirmed
#
# Demo:
#   1. Create 2 or 3 Doctor objects.
#   2. Create a Hospital object.
#   3. Book 3 or 4 appointments using different doctors.
#   4. Confirm some, cancel some.
#   5. Call view_all() and count_confirmed().

# Write your code below:




# ============================================================
#   END OF CLASS 3 HOMEWORK
#   Submit your completed file to your instructor.
# ============================================================