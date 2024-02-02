import streamlit as st
import numpy

operations="for sum choose '+' , for subtract choose '-' , for multiplication choose '*', for division choose '/', for power choose '**', for square root choose '****(1/2)', for cubic root choose '***(1/3)', for division remainder choose '%'"

OP=["+","-","*","/","**","**(1/2)","**(1/3)","%"]

functions={"for normal calculations":1,
          "for bigger than or less than checker":2,
          "for odd or even checker":3,
          "for divisibility check":4,
          "for multiplication table":5,
          "for factorial":6,
          "to find distance between two points":7,
          "for slope":8,
          "for area of square":9,
          "for area of circle":10,
          "for cylinder volume":11,
          "for cylinder surface area":12,
          "temperature calculation from celsius to fahrenheit or vice versa":13}

Functions=["Normal calculations",
          "Bigger than or less than checker",
          "Even or odd checker",
          "Divisibility check",
          "Multiplication table",
          "Factorial",
          "Find distance between two points",
          "Slope",
          "Area of square",
          "Area of circle",
          "Cylinder volume",
          "Cylinder surface area",
          "Temperature calculation from celsius to fahrenheit or vice versa"]

def normal_calc():
    try:  
        st.title("Note :")
        st.markdown("If your operation is to get a power of a number place the number as the fisrt number and the power is the second number")
        st.write("Ex:3 to the power of 2 (3 is the first number and 2 is the second number)")
        st.markdown("If your operation is to get a square root of a number place the number as the first number and place the second number as Zero(0)")
        st.write("Ex: square root of 9 is 3 (9 is the first number and the root is by deafult is a square root so enter 0 as the second number)")
        num1=st.number_input("please enter the first number = ")
        num2=st.number_input("please enter the second number = ")
        st.markdown(operations)
        op=st.selectbox("please enter the operation symbol : ",OP)
        if num2==0 and op=="/":
            try:
                return (num1/num2)
            except:
                return ("Can't divide by Zero")
        elif op == '+':
            return (num1+num2)
        elif op == '-':
            return (num1-num2)
        elif op == '*':
            return (num1*num2)
        elif op == '/':
            return (num1/num2)
        elif op == '**':
            return (num1**num2)
        elif op == '**(1/2)':
            return (num1**(1/2))
        elif op == '**(1/3)':
            return (num1**(1/3))
        elif op == '%':
            return (num1%num2)
        else:
            return ("Wrong operation")
    except:
        return ("Please enter a number")

def bigger_or_less_than():
    try:
        a=st.number_input("Please enter the first number : ")
        b=st.number_input("Please enter the second number : ")
        if a>b:
            return (f"{a} is greater than {b}")
        elif a==b:
            return (f"{a} is equal {b}")
        else:
            return (f"{b} is greater than {a}")
    except:
        return ("Please enter a number")
        
def odd_or_even():
    try:
        num=st.number_input("Please enter a number : ")
        if num%2==0:
            return (f"{num} is an even number")
        else:
            return (f"{num} is an odd number")
    except:
        return ("Please enter a whole number")
        
def divisible():
    try:
        st.title("Ex: 9 is divisible by 3\n   (9 is the number and 3 is the divisible number)")
        num=st.number_input("Please enter the number : ")
        x=st.number_input("Please enter the divisible number : ")
        if num%x==0:
            return (f"{num} is divisible by {x}")
        else:
            return (f"{num} is not divisible by {x}")
    except:
        return ("Please enter a whole number")

def multiplication_table():
    try:
        num=st.number_input("Please enter a number : ")
        st.title(f'multiplication table for the number {num}')
        for y in range(1,11):
            return (f"{num}*{y}={num*y}")
            return ("------")
    except:
        return ("Please enter a whole number")
        
def factorial():
    try:
        num = st.number_input("please enter a number : ")
        fact = 1
        i = 1
        while i<=num:
            fact = fact*i
            i = i+1
        return (f"Factorial of {num} = {fact}")
    except:
        return ("Please enter a whole number")
        
def distance_between_two_points():
    try:
        coor1=st.number_input("Please enter X1 : ")
        coor2=st.number_input("Please enter Y1 : ")
        coor3=st.number_input("Please enter X2 : ")
        coor4=st.number_input("Please enter Y2 : ")
        distance=(((coor3-coor1)**2)+((coor4-coor2)**2))**0.5
        return (distance)
    except:
        return ("Please enter a whole number")

def slope():
    try:
        coor1=st.number_input("Please enter X1 : ")
        coor2=st.number_input("Please enter Y1 : ")
        coor3=st.number_input("Please enter X2 : ")
        coor4=st.number_input("Please enter Y2 : ")
        slope=((coor4-coor2)/(coor3-coor1))
        return (slope)
    except:
        return ("Please enter a whole number")
        
def area_of_square():
    try: 
        length=st.number_input("Please enter the side length : ")
        area=length**2
        return (area)
    except:
        return ("Please enter a number")
        
def area_of_circle():
    try:
        radius=st.number_input("Please enter the radius of the circle : ")
        area=3.14*(radius**2)
        return (area)
    except:
        return ("Please enter a number")
        
def cylinder_volume():
    try:
        height=st.number_input("Please enter the height of the cylinder : ")
        radius=st.number_input("Please enter the radius of the cylinder : ")
        pi=(22/7)
        volume=pi*(radius**2)*height
        return (volume)
    except:
        return ("Please enter a whole number")
        
def cylinder_surface_area():
    try:
        height=st.number_input("Please enter the height of the cylinder : ")
        radius=st.number_input("Please enter the radius of the cylinder : ")
        pi=(22/7)
        surface_area=(2*pi*radius*height)+(2*pi*(radius**2))
        return (surface_area)
    except:
        return ("Please enter a whole number")
        
def temperature_degree():
    try:
        list2=["c","f"]
        temperature=st.number_input("please enter the temperature degree : ")
        temp_in=st.selectbox("Degree type",list2)
        temp_in_celsius=(temperature-32)*(5/9)
        temp_in_fahrenheit=(temperature*(9/5))+32
        if temp_in=="c" :
            return (f"the temperature degree in fahrenheit is : {temp_in_fahrenheit}")
        else:
            return (f"the temperature degree in celsius is : {temp_in_celsius}")
    except:
        return ("Wrong degree type")

def main():
    st.title("Calculator")
    func=st.selectbox("Functions",Functions)
    if func=="Normal calculations":
        result=normal_calc()
    elif func=="Bigger than or less than checker":
        result=bigger_or_less_than()
    elif func=="Even or odd checker":
        result=odd_or_even()
    elif func=="Divisibility check":
        result=divisible()
    elif func=="Multiplication table":
        result=st.write("Coming soon")
    elif func=="Factorial":
        result=factorial()
    elif func=="Find distance between two points":
        result=distance_between_two_points()
    elif func=="Slope":
        result=slope()
    elif func=="Area of square":
        result=area_of_square()
    elif func=="Area of circle":
        result=area_of_circle()
    elif func=="Cylinder volume":
        result=cylinder_volume()
    elif func=="Cylinder surface area":
        result=cylinder_surface_area()
    elif func=="Temperature calculation from celsius to fahrenheit or vice versa":
        result=temperature_degree()
    if st.button("calculate"):
        st.write(result)
        
if __name__=="__main__":
    main()
