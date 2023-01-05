import streamlit as st
from dataclasses import dataclass
from PIL import Image
    
@dataclass
class Overwiew:
    
    def __post_init__(self):
        st.header("Overview of Models")
        
        with st.expander("Model 01"):
            st.subheader("Häkkinen (1993)")

            st.markdown(r"In [1] and [2], an experimental model by Häkkinen (1993) is explained, which describes the carbonation coefficient $$k$$ as follows:")
            st.markdown(r"$$k=c_{env}*c_{air}*a*f_{cm,28}^b$$")
            st.markdown(r""" 
                        * $$C_{env}$$ ➔ Environmental Coefficient
                            * $$C_{env}=1,0$$ wenn Bauteil vor Regen geschützt ist
                            * $$C_{env}=0,5$$ wenn Bauteil Regen ausgesetzt ist
                        - $$C_{air}$$ ➔ Air Content Coefficient
                            - $$C_{air}=1,0$$ für Beton mit Luftporenbildner
                            - $$C_{air}=0,7$$ für Beton ohne Luftporenbildner
                        - $$f_{cm}$$ ➔ mittlere Zylinderdruckfestigkeit des Betons im Alter von 28 Tagen [MPa]
                        - $$a$$ und $$b$$ ➔ Parameter, abhängig von der Zementart (Siehe Tab. 1)
        """)
        with st.expander("Model 02"):
            st.subheader("fib (2006)")
            col1, col2 = st.columns([1,3])
            col1.markdown(r"\small c_{env}:")
            col2.markdown(r"\small \sf environmental \, coefficient")
            col1.markdown(r"\small c_{air}:")
            col2.markdown(r"\small \sf air \, content \, coefficient")
            col1.markdown(r"\small a,b:")
            col2.markdown(r"\small \sf parameters \, relating \, to \, cement \, type")
            col1.markdown(r"\small f_{cm,28}:")
            col2.markdown(r"\small \sf mean \, compressive \, strength \, of \, concrete \, at \, age \, of \, 28 \, days")
        
        with st.expander("Model 03"):
            st.subheader("CECS (2007)")

            st.markdown(r"The from Sun et al. \cite{Sun.2020} explained model from CECS (2007) describes the course of the carbonation depth $$x_c(t)$$ as follows:")
            st.markdown(r"$$x_c(t)=3K_{CO_2}K_{kl}K_{kt}K_{ks}K_{F}T^{0.25}RH^{1.5}(1-RH)({58\over f_{cuk}}-0.76)\sqrt{t}$$")
            col1, col2 =st.columns([1,3])
            st.markdown(r"""
$$K_{CO_2}$$:  
- CO₂ density factor:  
    - $$K_{CO_2}=\sqrt{\frac{c_{Co_2}}{0,03}}$$ \
$$c_{CO_2}$$:  
CO₂ density [\%] \
$$K_{kl}$$: 
    location factor:
        $$K_{kl}=1,4$$ für die Ecke des Bauteils 
            $$K_{kl}=1,0$$ für andere Bereiche des Bauteils \
$$K_{kt}$$:  curing factor:  $$K_{kt}=1,2$$ \
$$K_{ks}$$:  stress factor:  $$K_{ks} =1,0$$ für Druckbedingungen \
$$K_{ks}=1,1$$ für Zugbedingungen \
$$K_{F}$$:  fly ash factor:  $$K_F=1,0+13,34*F^{3,3}$$ \
$$F$$:  fly ash content [weight ratio] \
$$T$$:  annualtemperature [°C] \
$$RH$$:  annual relative humidity [-] \
$$f_{cuk}$$:  charasteristic strength [MPa]

                        """)
            st.markdown("""
|            |                                           |
|------------|-------------------------------------------|
| $K_{CO_2}$ | CO₂ density factor, $$K_{CO_2}=\sqrt{{c_{Co_2}}\over{0,03}}$$            |
|            |  |
|            |                                           |
|            |                                           |
|            |                                           |
|            |                                           |
|            |                                           |
|            |                                           |
|            |                                           |
|            |                                           |
|            |                                           |
|            |                                           |
|            |                                           |
|            |                                           |
|            |                                           |
|            |                                           |
|            |                                           |
|            |                                           |
|            |                                           |
|            |                                           |

                        """)
            col1, col2 =st.columns([1,3])
            col1.markdown(r"$$K_{CO_2}$$:"); col2.markdown(r"CO₂ density factor")
            col2.markdown(r"$$K_{CO_2}=\sqrt{{c_{Co_2}}\over{0,03}}$$")
            col1, col2 =st.columns([1,3])
            col1.markdown(r"$$c_{CO_2}$$:"); col2.markdown(r"CO₂ density [\%]")
            
            col1.markdown(r"$$K_{kl}$$:"); col2.markdown(r"")
            col1.markdown(r""); col2.markdown(r"")
            col1.markdown(r""); col2.markdown(r"")
            col1.markdown(r"$$K_{kt}$$:"); col2.markdown(r"")
            col1.markdown(r"$$K_{ks}$$:"); col2.markdown(r"")
            col1.markdown(r"$$K_{F}$$:"); col2.markdown(r"")
            col1.markdown(r"$$F$$:"); col2.markdown(r"")
            col1.markdown(r"$$T$$:"); col2.markdown(r"")
            col1.markdown(r"$$RH$$:"); col2.markdown(r"")
            col1.markdown(r"$$f_{cuk}$$:"); col2.markdown(r"")
            st.markdown(r"""
                        $$K_{t}=\frac{3}{2}$$: \
                        Essen \
                        Haloo
                        """)

        with st.expander("Model 04"):
            st.subheader("Guiglia, Taliano (2013)")
            st.markdown(r"The model of Guiglia and Taliano is based on the fib-Model Code 2010 (See Model 02) and on an extensive experimental campaign. In this campaign, 1350 compressive tests were performed as well as measurements of the carbonation depth on concrete samples up to 5 years old from important infrastructure structures, such as bridges and tunnels. The compressive strengths of the sampled concrete components ranged from 20 to 50 N/mm². The carbonation coefficient $$k$$ is described by Guiglia and Taliano as follows:")
            col1, col2 = st.columns([1,2])
            col1.markdown("for abutments and piers:")
            col2.markdown("$$k=163*\sqrt{k_e*f_{cm}^{-2.1}}$$")
            col1.markdown("for tunnels:")
            col2.markdown("$$k=206*\sqrt{k_e*f_{cm}^{-2.1}}$$") 
            col1.markdown("k_e:")
            col2.markdown("environmental function (see Model 02)")
            col1.markdown("$$f_{cm}$$:")
            col2.markdown("mean value of the concrete compressive cylinder strength at 28 days")
        
        with st.expander("Model 05"):
            st.subheader("Silva et al. (2014)")

        with st.expander("Model 06"):
            st.subheader("Yang et al. (2014)")

        with st.expander("Model 07"):
            st.subheader("Hills et al. (2015)")
            
        with st.expander("Model 08"):
            st.subheader("Greve-Dierfeld, Gehlen (2016)")
            
        with st.expander("Model 09"):
            st.subheader("Ta et al. (2016)")
            
        with st.expander("Model 10"):
            st.subheader("Ekolu (2018)")
            
        with st.expander("Model 11"):
            st.subheader("Possan et al. (2021)")
            
        with st.expander("References"):
            st.write("leer")
        
       
        

       
        
        st.subheader("Model 03: CECS (2007)")
        col1, col2 = st.columns([1,3])
        col1.markdown(r"\small K_{CO_2}:")
        col2.markdown(r"\small \sf CO_2 \, density \, factor, \, K_{CO_2}=\sqrt{{c_{CO_2}\over{0.03}}}")
        col1.markdown(r"\small K_{kl}:")
        col2.markdown(r"\small \sf location \, factor, \, K_{kl}=1.4 \, for \, corner \, of \, the \, component \, and \, 1.0 \, for \, other \, area")
        col1.markdown(r"\small K_{kt}:")
        col2.markdown(r"\small \sf curing \, factor, \, K_{kt}=1.2")
        col1.markdown(r"\small K_{ks}:")
        col2.markdown(r"\small \sf stress \, factor, \, K_{ks}=1.0 \, for \, compression \, condition \, and \, 1.1 \, for \, tension \, condition")
        col1.markdown(r"\small K_{F}:")
        col2.markdown(r"\small \sf fly \, ash \, factor, \, K_{F}=1.0+13.34F^{3.3}, \, F \, is \, the \, fly \, ash \, content\, (weight ratio)")
        col1.markdown(r"\small T:")
        col2.markdown(r"\small \sf temperature")
        col1.markdown(r"\small RH:")
        col2.markdown(r"\small \sf realtive \, humidity")
        col1.markdown(r"\small f_{cuk}:")
        col2.markdown(r"\small \sf concrete \, charasterisitc \, compression \, strength")
        
        
        
        st.subheader("Model 05: Silva (2014)")
        col1, col2 = st.columns([1,2])
        col1.markdown(r"\sf for \, relative \, humidity \, <=70\%:")
        col2.markdown(r"$$k_d=0.556c-3.602X-0.148f_c+18.734$$")
        col1.markdown(r"\sf for \, relative \, humidity \, >70\%:")
        col2.markdown(r"$$k_w=3.355c-0.019C-0.042f_c+10.83$$")
        col1.markdown(r"\small c:")
        col2.markdown(r"\small \sf clinker \, content \, [{{kg} \over {m^3}}]")

        
        st.subheader("Model 06: Yang (2014)")
        col1, col2 = st.columns([3,1])
        
        st.subheader("Model 07: Hills (2015)")
        col1, col2 = st.columns([3,1])
        
        st.subheader("Model 08: Greve-Dierfeld (2015)")
        
        
        st.subheader("Model 09: Ta (2016)")
        st.markdown(r"""The model of Ta et al. [9] is based on already existing models for the calculation 
                    of the carbonation depth and takes into account many influencing factors, which are 
                    combined from these models. The model was further validated by existing data on natural 
                    carbonation with different water-cement ratios, curing times and cement types from. Fig. 2 
                    shows the formulas of the model for calculating the carbonation depth with an explanation 
                    of the variables below.
                    """)
        image1 = Image.open("Ta_Gleichungen.png")
        st.image(image1, use_column_width=True, caption=("Formulas for calculating the carbonation depth - from [9]"))
        
        col1, col2 = st.columns([3,1])
        st.write("Input values:")
        col1.markdown(r""" 
                    $$x_{CO_2}$$: ➔ carbonation front depth [m] \\
                    $$D_{CO_2}$$: ➔ CO₂ diffusion coefficient [m²/s] \\
                    $$D_{CO_2}^{28}$$: ➔ CO₂ diffusion coefficient in fresh concrete [?] \\
                    $$[CO_2]_{ext}$$: ➔ CO₂ concentration in the air [kg/m³] \\
                    $$a$$: amount of CO₂ absorbed [kg/m³] \\
                    $$C$$: cement content [kg/m³] \\
                    $$W$$:  water content of concrete [kg/m³] \\
                    $$FA$$:  fly ash content of concrete [kg/m³] \\
                    $$S$$:  sand content [kg/m³] \\
                    $$G$$:  gravel content [kg/m³] \\
                    $$S_{max}$$:  maximum nominal aggregate size [mm] \\
                    $$\phi_{clinker}$$:  cement clinker content [-] \\
                    $$M_{CO_2}$$:  Molar weight of CO₂ [g/mol] \\
                    $$M_{CaO}$$:  Molar weight of CaO [g/mol] \\
                    $$RH$$:  relative external humidity [\%] \\
                    $$T$$:  temperature [-] \\
                    $$f_c$$:  28-day compressive strenght [MPa] \\
                    $$f_{cem}$$:  standard strenght class of cement [MPa] \\
                    $$\rho_c$$:  densitiy of cement [kg/m³] \\
                    $$\rho_w$$:  densitiy of water [kg/m³] \\
                    $$\rho_{fa}$$:  densitiy of fly ash [kg/m³] \\
                    $$\phi_{air}$$:  air content in concrete [-] \\
                    $$CaO$$:  amount of calcium oxide per weight of cement [-] \\
                    $$SO_3$$:  amount of sulfur oxide per weight of cement [-] \\
                    $$SiO_2$$:  amount of silicon oxide per weight of cement [-] \\
                    $$Al_2O_3$$:  amount of aluminium oxide per weight of cement [-] \\
                    $$Fe_2O_3$$:  amount of iron oxide per weight of cement [-] \\
                    $$t_c$$:  curing time [days]
                    """)
        
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
        
        image2 = Image.open("DIN EN 197-1.jpg")
        st.image(image2, use_column_width=True)
        
        st.subheader("References")
