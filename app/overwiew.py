import streamlit as st
    
class overwiew:
    
    def __init__(self):
        st.header("Overview of Models")
        
        st.write("All models are based on the square-root-of-time-rule:")
        st.latex("X(t)=k*\sqrt{t}")
        col1, col2 = st.columns([1,3])
        col1.latex("\small k:")
        col2.latex("\small \sf describes \, the \, carbonation \, rate \, ({{mm} \over {years^{0.5}}})")
        col1.latex("\small t:")
        col2.latex("\small \sf time \, (years)")
        
        st.subheader("Model 01: Häkkinen (1993)")
        st.latex("k=c_{env}*c_{air}*a*f_{cm,28}^b")
        col1, col2 = st.columns([1,3])
        col1.latex("\small c_{env}:")
        col2.latex("\small \sf environmental \, coefficient")
        col1.latex("\small c_{air}:")
        col2.latex("\small \sf air \, content \, coefficient")
        col1.latex("\small a,b:")
        col2.latex("\small \sf parameters \, relating \, to \, cement \, type")
        col1.latex("\small f_{cm,28}:")
        col2.latex("\small \sf mean \, compressive \, strength \, of \, concrete \, at \, age \, of \, 28 \, days")
        
        st.subheader("Model 02: fib (2006)")
        col1, col2 = st.columns([3,1])
        
        st.subheader("Model 03: CECS (2007)")
        st.latex("k=3K_{CO_2}*K_{kl}*K_{kt}*K_{ks}*K_{F}T^{0.25}*RH^{1.5}*(1-RH)*({58\over f_{cuk}}-0.76)")
        col1, col2 = st.columns([1,3])
        col1.latex("\small K_{CO_2}:")
        col2.latex("\small \sf CO_2 \, density \, factor, \, K_{CO_2}=\sqrt{{c_{CO_2}\over{0.03}}}")
        col1.latex("\small K_{kl}:")
        col2.latex("\small \sf location \, factor, \, K_{kl}=1.4 \, for \, corner \, of \, the \, component \, and \, 1.0 \, for \, other \, area")
        col1.latex("\small K_{kt}:")
        col2.latex("\small \sf curing \, factor, \, K_{kt}=1.2")
        col1.latex("\small K_{ks}:")
        col2.latex("\small \sf stress \, factor, \, K_{ks}=1.0 \, for \, compression \, condition \, and \, 1.1 \, for \, tension \, condition")
        col1.latex("\small K_{F}:")
        col2.latex("\small \sf fly \, ash \, factor, \, K_{F}=1.0+13.34F^{3.3}, \, F \, is \, the \, fly \, ash \, content\, (weight ratio)")
        col1.latex("\small T:")
        col2.latex("\small \sf temperature")
        col1.latex("\small RH:")
        col2.latex("\small \sf realtive \, humidity")
        col1.latex("\small f_{cuk}:")
        col2.latex("\small \sf concrete \, charasterisitc \, compression \, strength")
        
        st.subheader("Model 04: Guiglia (2013)")
        col1, col2 = st.columns([1,2])
        col1.latex("\sf for \, abutments \, and \, piers:")
        col2.latex("k=163*\sqrt{k_e*f_{cm}^{-2.1}}")
        col1.latex("\sf for \, tunnels:")
        col2.latex("k=206*\sqrt{k_e*f_{cm}^{-2.1}}") 
        col1.latex("\small k_e:")
        col2.latex("\small \sf environmental \, function")
        col1.latex("\small f_{cm}:")
        col2.latex("\small\sf mean\,value\,of\,the\,concrete\,compressive\,cylinder\,strength\,at\,28\,days")
        
        st.subheader("Model 05: Silva (2014)")
        col1, col2 = st.columns([3,1])
        col1.latex("\sf for \, relative \, humidity \, <=70\%:")
        col2.latex("k_d=0.556c-3.602X-0.148f_c+18.734")
        col1.latex("\sf for \, relative \, humidity \, >70\%:")
        col2.latex("k_w=3.355c-0.019C-0.042f_c+10.83")
        col1.latex("\small c:")
        col2.latex("\small \sf clinker \, content \, [{{kg} \over {m^3}}]")

        
        st.subheader("Model 06: Yang (2014)")
        col1, col2 = st.columns([3,1])
        
        st.subheader("Model 07: Hills (2015)")
        col1, col2 = st.columns([3,1])
        
        st.subheader("Model 08: Greve-Dierfeld (2015)")
        col1, col2 = st.columns([3,1])
        
        st.subheader("Model 09: Ta (2016)")
        col1, col2 = st.columns([3,1])
        
        st.subheader("Model 10: Ekolu (2018)")
        col1, col2 = st.columns([3,1])
        
        st.subheader("Model 11: Possan (2021)")
        col1, col2 = st.columns([3,1])
        
