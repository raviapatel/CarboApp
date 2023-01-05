            # -*- coding: utf-8 -*-
            """
            Created on Sat Dec 10 15:11:58 2022
            
            @author: marco
            """
        import streamlit as st
            
                #f_c
                f_c = st.number_input("Mean Concrete Compressive Strenght: [MPa]", min_value=(1.0), max_value=(100.0), value=(30.0), step=(0.5))
                
                #C
                C = st.number_input("Clinker Content: [kg/m³]", min_value=(0.0), value=(350.0), step=(5.0))
                
                #AirEntrained
                AirEntrained = st.radio("Choose if Component is Air Entrained:", ["Air Entrained","Not Air Entrained"])
                
                #FA
                FA = st.number_input("Fly Ash Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0))
                
                #SF
                SF = st.number_input("Silicia Fume Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0))
                
                #GGBS
                GGBS = st.number_input("Blast Furnance Slag Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0))
                
                #t
            t = st.number_input("Service Time: [years]", min_value=(1), value=(50), step=(1))
                
                #RH
                RH = st.number_input("Mean Relative Air Humidity: [%]", min_value=(0.0), max_value=(100.0), value=(70.0), step=(0.5))
                
                #C_co2
                #fällt weg
                
                #t_c
                t_c = st.number_input("Curing Time: [days]", min_value=(0), value=(3), step=(1))
                
                #p_dr
                p_dr = st.number_input("Probability of Driving Rain: [%]", min_value=(0.0), max_value=(100.0), value=(30.0), step=(0.5))
                
                #ToW
                ToW = st.number_input("Average Number of Rainy Days per Year [days]", min_value=(0.0), max_value=(365.0), value=(130.0))
                
                #R_NAC
                R_NAC = st.number_input("Inverse Effective Carbonation Resistance (NAC): [(mm²/years)/(kg/m³)]", min_value=(0.0), value=(0.0), step=(0.5))
                
                #Stress
                Stress = st.radio("Choose Stress on Component:", ["Pressure", "Tension"])
                
                #T
                T = st.number_input("Mean Temperature: [°C]", value=(15.0), step=(0.5))
                
                #CO2
                CO2 = st.number_input("CO2 Density around Concrete Surface: [%]", min_value=(0.0), max_value=(100.0), value=(0.04), step=(0.005), format=("%.4f"))
                
                #ExCo
                ExCo = st.radio("Choose Exposure Condition of Component:", ["Indoor", "Outdoor", "Exposed to Rain", "Sheltered from Rain"])
                
                #Location
                Location = st.radio("Choose Location of Component:", ["Corner", "Other Area"])
                
                #Building
                Building = st.radio("Building Type:", ("Tunnel","Others"))
                
                #ExpC
                ExpC = st.radio("Choose Exposure Class:", ("XC1","XC2","XC3","XC4")) 
                
                #S
                S = st.number_input("Sand Content: [kg/m³]", min_value=(0.0), value=(1000.0), step=(5.0))
                
                #G 
                G = st.number_input("Gravel Content: [kg/m³]", min_value=(0.0), value=(800.0), step=(5.0))
                
                #Finishing
                if ExCo =="Indoor": 
                    Finishing = st.radio("Choose Finishing of Component:", ["Nothing", "Paint", "Mortar", "Tile"])
                else: 
                    Finishing = st.radio("Choose Finishing of Component:", ["Nothing", "Plaster", "Paint", "Mortar", "Mortar + Plaster", "Mortar + Paint", "Tile"])
                
                #wc
                
                
                #mixture
                mixture = st.radio("Choose Content in the Concrete:",["Ordinary Portland Cement (OPC)","OPC + Blast Furnace Slag","OPC + Fly Ash"])
                
                #Depending
                Depending = st.radio("Model depending on...", ["Time","Compressive Strength"])
                
                #Origin
                Origin = st.radio("Choose Origin of Component:",["Experimental", "Structural"])
                
                #Age
                Age = st.number_input("Age of Concrete: [years] ", min_value=(0.0),value=(5.0), step=(0.5))
                
                #wb
                wb = st.number_input("Water / Binder Ratio: [-]",min_value=(0.0), value=(0.5), max_value=(0.65),step=(0.01))
    
                #CEM
                Cem = st.radio("Choose Cement Type:", ["CEM I", "CEM II/A","CEM II/A-L", "CEM II/A-S", "CEM II/B", "CEM II/B-S", "CEM III/A", "CEM IV/A", "CEM IV/B"])
    
                #L 
                #fällt weg L = st.number_input("Limestone Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0))
                
                #PZ
                # fällt weg PZ = st.number_input("Pozzolan Content: [kg/m³]", min_value=(0.0), value=(0.0), step=(5.0))
                
                #W
                W = st.number_input("Water Content: [kg/m³]", min_value=(0.0))
                
                #CaO
                CaO = st.number_input("Amount of Calcium Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.645), step=(0.01), format=("%.4f"))
                
                #SO3
                SO3 = st.number_input("Amount of Sulfur Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.035), step=(0.01), format=("%.4f"))
                
                #SiO2
                SiO2 = st.number_input("Amount of Silicon Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.205), step=(0.01), format=("%.4f"))
                
                #Al2O3
                Al2O3 = st.number_input("Amount of Aluminium Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.045), step=(0.01), format=("%.4f"))
                
                #Fe2O3
                Fe2O3 = st.number_input("Amount of Iron Oxide per Weight of Cement: [-]", min_value=(0.0), max_value=(1.0), value=(0.030), step=(0.01), format=("%.4f"))
                
                #p_c
                p_c = st.number_input("Density of Cement: [kg/m³]", value=(3140.0), min_value=(0.0), step=(0.5))
                
                #p_FA
                p_FA = st.number_input("Density of Fly Ash: [kg/m³]", value=(2580.0), min_value=(0.0), step=(0.5))
                
                #p_w
                p_w = st.number_input("Density of Water: [kg/m³]", value=(1000.0), min_value=(0.0), step=(0.5))
                
                #phi_clinker
                
                
                #S_max
                S_max = st.number_input("Maximum Aggregate Size: [mm]", min_value=(0.0), value=(32.0), step=(0.5))
                
                #f_cem
                f_cem = st.number_input("Mean Cement Compressive Strenght: [N/mm²]",  min_value=(0.0), value=(42.5), step=(0.5))
                                        
                #FA_c
                FA_c = st.number_input("Fly Ash Content: [weight ratio]", min_value=(0.0), value=(0.0), max_value=(1.0), step=(0.01))
                
                #GGBS_c
                #fällt weg
                
                #c_nom
                c_nom = st.number_input("Concrete Cover: [mm]",  min_value=(0.0), value=(20.0), step=(0.5))
                
                #sample_total 
                sample_total = st.number_input("Total of Samples: [-]", min_value=(1), value=(1000))
        #Probabilistisch:
                #c_nom


                #RH
                
                
                #b_c
                
                
                #R_ACC
                
                
                #k_t
                
                
                #e_t
                
                
                #C_satm
                self.C_co2=np.random.normal(self.CO2, 0.1e-3, self.sample_total) # [kg/m³]
                
                #b_w
                
                