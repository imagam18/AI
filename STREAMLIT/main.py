import streamlit as st
# Class 1
st.title("Hi! Im am Stramlit web App")
st.header("Im Header")
st.subheader("This is my stream sub-heading")
st.text("Agam saxena")

# Class 2

st.markdown("**HELLO** *world* Agam")
Value ={"a":"1,2,3","b":"4,5,6"}
st.json(Value)

code ="""
class Person:
    def __int__(self,name):
        self.name = name
    
    def __str__(self):
        return f{self.name}
P1 = Person(Agam)
print(P1)
"""
st.code(code,language ="python")


#class 3

st.write("## H2")