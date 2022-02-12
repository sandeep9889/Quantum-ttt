from optparse import Values
from qiskit import QuantumCircuit, Aer
import numpy as np
import streamlit as st
from sympy import false
from game import get_random_value, validate


def quantum_superposition():
    circuit = QuantumCircuit(1,1)


    circuit.h(0)


    circuit.measure(0,0)

    simulator = Aer.get_backend('aer_simulator')

    result = simulator.run(circuit).result().get_counts()

    return result


def get_random_value():


    res = quantum_superposition()
    print(res)
    values= list(res.values())
    keys = list(res.keys())
    print(values)
    print(keys)

    random_value =  '|' + str(keys[np.argmax(values)]) + '>'
    print(random_value)


def validate(arr):
    """
    The method checks if the game is finished!
    parameters:
    arr(numpy array): The array that serves as the board
    returns :
    return 0 if any of the winning condition is satisfied by any of the player
    else return 1
     """   

     # defination a boolean variable 
    flag = True
    zero_ket = '|0>'
    one_ket = '|1>'


    #chech  for the principle diagonal condition wrt user
    if arr[0,0] == one_ket and arr[1,1] ==one_ket and arr[2,2] == one_ket:
        st.success("user has wone!")
        flag = False
    


    #chech  for the principle diagonal condition wrt ucomp
    elif arr[0,0] == zero_ket and arr[1,1] ==zero_ket and arr[2,2] == zero_ket:
        st.success("computer has wone!")
        flag = False



    #chech  for the 2nd diagonal condition wrt user
    elif arr[0,2] == one_ket and arr[1,1] ==one_ket and arr[2,0] == one_ket:
        st.success("user has wone!")
        flag = False



    #chech  for the 2nd diagonal condition wrt computer
    elif arr[0,0] == zero_ket and arr[1,1] ==zero_ket and arr[2,2] == zero_ket:
        st.success("computer has wone!")
        flag = False        
    



    if not flag:
        return 0


    #we execute the below for loops iff any of the above conditions are not
    # satisfied

    if flag:

        #checks if any of the row conqured by user
        for index in [0,1,2]:
            if(list(arr[index]) == [one_ket,one_ket,one_ket]):
                st.success("user has won")
                return 0



        #checks if any of the row conqured by comp
        for index in [0,1,2]:
            if(list(arr[index]) == [zero_ket,zero_ket,zero_ket]):
                st.success("computer has won")
                return 0

        #checks if any of the column conqured byuser
        for index in [0,1,2]:
            if(list(arr[: ,index]) == [one_ket,one_ket,one_ket]):
                st.success("user has won")
                return 0                          
        

         #checks if any of the column conqured byuser
        for index in [0,1,2]:
            if(list(arr[: ,index]) == [one_ket,one_ket,one_ket]):
                st.success("computer has won")
                return 0 

        #check if its a draw
        if '|ψ>' not in arr:
            st.write("Its a draw!")
            return 0;

        # if none of the condition
    return 0;    