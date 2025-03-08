#import streamlit as st

#def calculate(num1, num2, operation):
  #  if operation == "Addition":
   #     result = num1 + num2
    #elif operation == "Subtraction":
     #   result = num1 - num2
    #elif operation == "Multiply":
     #   result = num1 * num2
    #elif operation == "Division":
     #   try:
      #      result = num1 / num2
       # except ZeroDivisionError:
        #    result = "Cannot be divide by zero"
    #return result

#def main():
    # st.title("Simple Calculator")
     #num1 = st.number_input("Enter your first number", step=1)
    #num2 = st.number_input("Enter your second number", step=2)
    #operation = st.radio("Select operation",['Addition', 'Subtraction', 'Multiply', 'Division'])

    #result = calculate(num1, num2, operation)

    #st.write(f"Result of the {operation} of {num1} and {num2} {result}")

#if __name__ == "__main__":
 #   main()


# BMI Calculator

def calculate_bmi(weight, height):
    # BMI Formula: BMI = weight (kg) / height (m)^2
    bmi = weight / (height ** 2)
    return bmi


def categorize_bmi(bmi):
    # BMI categories based on World Health Organization (WHO)
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("Welcome to the BMI Calculator!")

    # Get user input for weight and height
    weight = float(input("Please enter your weight in kilograms (kg): "))
    height = float(input("Please enter your height in meters (m): "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Get BMI category
    category = categorize_bmi(bmi)

    # Output results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Based on your BMI, you are classified as: {category}")


if __name__ == "__main__":
    main()


