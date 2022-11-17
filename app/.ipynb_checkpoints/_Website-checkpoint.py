import streamlit as st
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from CarboModel import CarboModel
import Silva
#import Guiglia

#Formel Guiglia
def xt_rechnung(a:int,ke:float,fcm:float,t:int)->float:
    """
    

    Parameters
    ----------
    a : int
        parameter (if abutments and piers or tunnels) (-)
    ke : float
        environmental function (-)
    fcm : float
        mean value of the concrete compressive cylinder strength at 28 days fcm (N/mm²)
    t : int
        time (years)

    Returns
    -------
    float
        carbonation depth (mm)

    """
    return (a * pow(ke*pow(fcm,-2.1),0.5)*pow(t,0.5))
    
#Ablauf Berechnung, Plotten:
def rechnung(rh:int,t:int,fcm:float,building:str)->None:
    """
    

    Parameters
    ----------
    rh : int
        relative humidity (%)
    t : int
        time (years)
    fcm : float
        mean value of the concrete compressive cylinder strength at 28 days fcm (N/mm²)
    building : str
        abutments and piers or tunnels
    Returns
    -------
    None
        -

    """
    #Berechnung ke:
    ke = (((1.0-((rh*0.01)**5.0)))/(1.0-((65.0/100.0)**5.0)))**2.5
    
    #if int(ga) == 1:
     #   ke = 1.025
    #elif int(ga) == 2:
     #   ke = 0.947
    #elif int(ga) == 3:
     #   ke = 0.691
        
    #fcm = float(fcm) 
    #t = float(t) 
    #ke = float(ke)
    
    if fcm == 0:
        
        st.warning("fcm can't be 0")
        return None
        
    if building == "abutments and piers":
        
        a = 163
        
    elif building == "others":
        
        a = 206
    
    xt = xt_rechnung(a,ke,fcm,t)
    xt = round(xt,1)
    
    st.success("Carbonation depth of the concrete: " + str(xt) + " mm")
    
    #Plotten:
    t_min = 0
    t_max = t
    #t_range = np.linspace(t_min, t_max, 500)
    t_range = np.arange(t_min, t_max, 0.1)
    fig1, ax1 = plt.subplots()
    ax1.grid(True)
    ax1.set(xlabel = "Time (years)", ylabel = "X(t) (mm)", title = sb)
    ax1.plot(t_range, xt_rechnung(a, ke, fcm, t_range))
    #plt.xscale("log")
    st.pyplot(fig1)
    
    #a = pd.DataFrame(((0,0),(xt,t)), columns=["Carbonation depth X(t) (mm)","√t (years)"])
    #st.line_chart(a, y = "Carbonation depth X(t) (mm)", x = "√t (years)") 
    
    return None

#Aufbau Website:
st.title("Calculation of Carbonation Depth")
st.sidebar.subheader("Select Model:")
sb = st.sidebar.selectbox(" ",("Home","Overview","Model 1", "Model 2", "Model 3", "Model 4", "Model 5", "Model 6", "Model 7", "Model 8", "Model 9", "Model 10"),label_visibility="collapsed")
#p1 = st.sidebar.button("Home")
#p2 = st.sidebar.button("Overwiew")
#p3 = st.sidebar.button("Model 1")
#p4 = st.sidebar.button("Model 2")
#st.selectbox("Choose a Model:", ("Home","Model 1", "Model 2"))

if sb == "Home":        # Homepage
   st. header("Welcome")
    
if sb == "Overview":    # Overview of the Models, exposure classes
    st.header("Overview of Models")
    
    st.subheader("Model 1: ...")
    col1, col2 = st.columns([3,1])
    col1.write("Explanation of Model")
    col2.write("Input:")
    col2.write ("- ...")
    col2.write ("- ...")
    
    st.subheader("Model 2: ...")
    col1, col2 = st.columns([3,1])
    col1.write("Explanation of Model")
    col2.write("Input:")
    col2.write ("- ...")
    col2.write ("- ...")
    
    st.subheader("Model 3: ...")
    col1, col2 = st.columns([3,1])
    col1.write("Explanation of Model")
    col2.write("Input:")
    col2.write ("- ...")
    col2.write ("- ...")
    
    st.subheader("Model 4: ...")
    col1, col2 = st.columns([3,1])
    col1.write("Explanation of Model")
    col2.write("Input:")
    col2.write ("- ...")
    col2.write ("- ...")
    
    st.subheader("Model 5: ...")
    col1, col2 = st.columns([3,1])
    col1.write("Explanation of Model")
    col2.write("Input:")
    col2.write ("- ...")
    col2.write ("- ...")
    
    st.subheader("Model 6: ...")
    col1, col2 = st.columns([3,1])
    col1.write("Explanation of Model")
    col2.write("Input:")
    col2.write ("- ...")
    col2.write ("- ...")
    
    st.subheader("Model 7: ...")
    col1, col2 = st.columns([3,1])
    col1.write("Explanation of Model")
    col2.write("Input:")
    col2.write ("- ...")
    col2.write ("- ...")
    
    st.subheader("Model 8: ...")
    col1, col2 = st.columns([3,1])
    col1.write("Explanation of Model")
    col2.write("Input:")
    col2.write ("- ...")
    col2.write ("- ...")
    
    st.subheader("Exposure classes:")
    col1, col2 = st.columns([1,3])
    col1.write("XC1")
    col2.write("Dry or permanently wet")
    col1, col2 = st.columns([1,3])
    col1.write("XC2")
    col2.write("Wet, rarely dry")
    col1, col2 = st.columns([1,3])
    col1.write("XC3")
    col2.write("Moderate humidity")
    col1, col2 = st.columns([1,3])
    col1.write("XC4")
    col2.write("Cyclic wet and dry")

elif sb == "Model 1":   # Model 01 - fib (2006)
    st.subheader("Model 1")

elif sb == "Model 2":   # Model 02 - Guiglia (2013)
    st.subheader("Model 2")
    building = st.selectbox("Building type:", ("abutments and piers","others"))
    rh = st.slider("Relative humidity (%):", 1,100,50, help=("E.g. the relative humidity in Germany is approximately between 68 and 88 percent"))
    t = st.slider("Minimum lifetime (years):", 1,100,50)
    fcm = st.number_input("Mean value of the concrete compressive cylinder strength at 28 days fcm (N/mm²):",0.0,None,25.0,step=(0.5))
    
    if st.button("Calculate"):
        rechnung(rh,t,fcm,building)

elif sb == "Model 3":   # Model 03 - fibGuiglia (2013)
    st.subheader("Model 3")
    
elif sb == "Model 4":   # Model 04 - Silva (2014)
    name = st.subheader("Model 4")
    rh = st.slider("Relative humidity (%):", 1,100,50, help=("E.g. the relative humidity in Germany is approximately between 68 and 88 percent"))    
    ExpC = st.selectbox("Exposure class:", ("XC1","XC2","XC3","XC4")) 
    t = st.slider("Minimum lifetime (years): ", 1,100,50)
    fc = st.number_input("Mean value of the concrete compressive cylinder strength at 28 days fcm (N/mm²):",0.0,None,25.0,step=(0.5))
    st.write("Optional:")
    if st.checkbox("CO2"):    
        CO2 = st.number_input("CO2: (%)",0.0,None,0.04,step=(0.01))
    else: 
        CO2 = 0.04
    if st.checkbox("C"):
         C = st.number_input("C: (kg/m³)",0.0,None,220.0,step=(0.5))
    else:
         C = 220
    if st.checkbox("phi_clinker"): 
        phi_clinker = st.number_input("phi_Clinker: (%)",0.0,None,98.0,step=(0.5)) * 0.01
    else:
        phi_clinker = 0.98
   
    if st.button("Calculate "): 
        Modell02 = Silva.Silva(name, C, fc, phi_clinker, ExpC, rh, CO2) #(name, C, f_c, phi_clinker, ExpC, RH, CO2))(name, 0.5, 25, 0.5, 0.5, rh, 0.05)
        st.success(str(round(Modell02.x_c(t),1)) + " mm")
        t_range = np.arange(0, t, 0.1)
        fig1, ax1 = plt.subplots()
        ax1.grid(True)
        ax1.set(xlabel = "Time (years)", ylabel = "Carbonation depth (mm)", title = sb)
        ax1.plot(t_range, Modell02.x_c(t_range))
        #plt.xscale("log")
        st.pyplot(fig1)    #oder: st.write(fig1)
        
elif sb == "Model 5":   # Model 05 - Hills (2015)
    st.subheader("Model 5")
    
elif sb == "Model 6":   # Model 06 - fibGreveDierfeld (2016)
    st.subheader("Model 6")
    
elif sb == "Model 7":   # Model 07 - Ta (2016)
    st.subheader("Model 7")
    
elif sb == "Model 8":   # Model 08 - Ekolu (2018)
    st.subheader("Model 8")
    
elif sb == "Model 9":   # Model 09 - Possan (2021)
    st.subheader("Model 9")
    
#elif sb == "Model 10": # Modell 10 - 
    st.subheader("Model 10")





#tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Start", "Modell 1", "Modell 2", "Modell 3", "Modell 4", "Modell 5"])

#with tab1:
#    " "
#
#with tab2:
#    st.subheader("Modell 1: ")
#    building = st.selectbox("Building type:", ("abutments and piers","tunnels"))
#    rh = st.slider("Relative humidity (%):", 1,100,50, help=("E.g. the relative humidity in Germany is approximately between 68 and 88 percent"))
#    t = st.slider("Minimum lifetime (years):", 1,100,50)
#    fcm = st.number_input("Mean value of the concrete compressive cylinder strength at 28 days fcm (N/mm²):",0.0,None,25.0,step=(0.5))
#
#    if st.button("Calculate"):
#        rechnung(rh,t,fcm,building)
#
#with tab3:
#    st.subheader(" Modell 2: ")
#    rh = st.slider("Relative humidity (%):j ", 1,100,50, help=("E.g. the relative humidity in Germany is approximately between 68 and 88 percent"))    
#    xc = st.selectbox("Exposure class:j ", ("XC1","XC2","XC3","XC4")) 
#    t = st.slider("Minimum lifetime (years): ", 1,100,50)
#    
#    if st.button("Calculate "): 
#        st.success("yes")
#        
#with tab4:
#    st.subheader("Modell 3: ")
#    
#with tab5:
#    st.subheader("Modell 4: ")
#    
#with tab6:
#    st.subheader("Modell 5: ")
    
#with tab2:
    
#    df = pd.DataFrame((("64","84"),("67","104"),("75","64")),index=("1","2","3"),columns=("relative humidity (%)","number of rainy days (-)"))
#    st.table(df)

