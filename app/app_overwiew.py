import streamlit as st
from PIL import Image
    
class app_overwiew:
    
    def __init__(self):
        st.header("Overview of Models")
        
        st.write("All models are based on the square-root-of-time-rule:")
        st.markdown("$X(t)=k*\sqrt{t}$")
        col1, col2 = st.columns([1,3])
        col1.markdown("\small k:")
        col2.markdown("\small \sf describes \, the \, carbonation \, rate \, ({{mm} \over {years^{0.5}}})")
        col1.markdown("\small t:")
        col2.markdown("\small \sf time \, (years)")
        
        st.subheader("Model 01: Häkkinen (1993)")
        st.markdown("$k=c_{env}*c_{air}*a*f_{cm,28}^b$")
        col1, col2 = st.columns([1,3])
        col1.markdown("\small c_{env}:")
        col2.markdown("\small \sf environmental \, coefficient")
        col1.markdown("\small c_{air}:")
        col2.markdown("\small \sf air \, content \, coefficient")
        col1.markdown("\small a,b:")
        col2.markdown("\small \sf parameters \, relating \, to \, cement \, type")
        col1.markdown("\small f_{cm,28}:")
        col2.markdown("\small \sf mean \, compressive \, strength \, of \, concrete \, at \, age \, of \, 28 \, days")
        
        st.subheader("Model 02: fib (2006)")
        col1, col2 = st.columns([3,1])
        
        st.subheader("Model 03: CECS (2007)")
        st.markdown("$k=3K_{CO_2}*K_{kl}*K_{kt}*K_{ks}*K_{F}T^{0.25}*RH^{1.5}*(1-RH)*({58\over f_{cuk}}-0.76)$")
        col1, col2 = st.columns([1,3])
        col1.markdown("\small K_{CO_2}:")
        col2.markdown("\small \sf CO_2 \, density \, factor, \, K_{CO_2}=\sqrt{{c_{CO_2}\over{0.03}}}")
        col1.markdown("\small K_{kl}:")
        col2.markdown("\small \sf location \, factor, \, K_{kl}=1.4 \, for \, corner \, of \, the \, component \, and \, 1.0 \, for \, other \, area")
        col1.markdown("\small K_{kt}:")
        col2.markdown("\small \sf curing \, factor, \, K_{kt}=1.2")
        col1.markdown("\small K_{ks}:")
        col2.markdown("\small \sf stress \, factor, \, K_{ks}=1.0 \, for \, compression \, condition \, and \, 1.1 \, for \, tension \, condition")
        col1.markdown("\small K_{F}:")
        col2.markdown("\small \sf fly \, ash \, factor, \, K_{F}=1.0+13.34F^{3.3}, \, F \, is \, the \, fly \, ash \, content\, (weight ratio)")
        col1.markdown("\small T:")
        col2.markdown("\small \sf temperature")
        col1.markdown("\small RH:")
        col2.markdown("\small \sf realtive \, humidity")
        col1.markdown("\small f_{cuk}:")
        col2.markdown("\small \sf concrete \, charasterisitc \, compression \, strength")
        
        st.subheader("Model 04: Guiglia (2013)")
        col1, col2 = st.columns([1,2])
        col1.markdown("\sf for \, abutments \, and \, piers:")
        col2.markdown("$k=163*\sqrt{k_e*f_{cm}^{-2.1}}$")
        col1.markdown("\sf for \, tunnels:")
        col2.markdown("$k=206*\sqrt{k_e*f_{cm}^{-2.1}}$") 
        col1.markdown("\small k_e:")
        col2.markdown("\small \sf environmental \, function")
        col1.markdown("\small f_{cm}:")
        col2.markdown("\small\sf mean\,value\,of\,the\,concrete\,compressive\,cylinder\,strength\,at\,28\,days")
        
        st.subheader("Model 05: Silva (2014)")
        col1, col2 = st.columns([1,2])
        col1.markdown("\sf for \, relative \, humidity \, <=70\%:")
        col2.markdown("$k_d=0.556c-3.602X-0.148f_c+18.734$")
        col1.markdown("\sf for \, relative \, humidity \, >70\%:")
        col2.markdown("$k_w=3.355c-0.019C-0.042f_c+10.83$")
        col1.markdown("\small c:")
        col2.markdown("\small \sf clinker \, content \, [{{kg} \over {m^3}}]")

        
        st.subheader("Model 06: Yang (2014)")
        col1, col2 = st.columns([3,1])
        
        st.subheader("Model 07: Hills (2015)")
        col1, col2 = st.columns([3,1])
        
        st.subheader("Model 08: Greve-Dierfeld (2015)")
        col1, col2 = st.columns([3,1])
        
        st.subheader("Model 09: Ta (2016)")
        st.write("Input values:")
        st.markdown("Test")
        
        st.subheader("Model 10: Ekolu (2018)")
        col1, col2 = st.columns([3,1])
        
        st.subheader("Model 11: Possan (2021)")
        col1, col2 = st.columns([3,1])
        
        st.header("Exposure classes:")
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
        
        image = Image.open("DIN EN 197-1.jpg")
        st.image(image, use_column_width=True)
