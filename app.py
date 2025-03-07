import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain

def main():
    st.set_page_config(page_title="Unit Converter", layout="centered", initial_sidebar_state="expanded")
    
    st.markdown("""
        <style>
            body { font-family: 'Arial', sans-serif; }
            .stButton>button { border-radius: 8px; font-size: 16px; }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🔄 Universal Unit Converter")
    
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/1698/1698535.png", width=80)
        option = st.selectbox("Select a Conversion Type", [
            "Length", "Weight", "Temperature", "Time", "Speed", "Area", "Volume", "Data Storage", "Energy", "Pressure", "Currency Converter", "BMI Calculator"
        ])
        
        dark_mode = st.toggle("🌙 Dark Mode")
    
    if dark_mode:
        st.markdown("""
            <style>
                body { background-color: #1e1e1e; color: white; }
                .stButton>button { background-color: #444; color: white; }
            </style>
        """, unsafe_allow_html=True)
    
    if option == "BMI Calculator":
        bmi_calculator()
    elif option == "Currency Converter":
        currency_converter()
    else:
        unit_converter(option)

def unit_converter(category):
    st.subheader(f"⚙️ {category} Converter")
    
    converters = {
        "Length": length_converter,
        "Weight": weight_converter,
        "Temperature": temperature_converter,
        "Time": time_converter,
        "Speed": speed_converter,
        "Area": area_converter,
        "Volume": volume_converter,
        "Data Storage": data_storage_converter,
        "Energy": energy_converter,
        "Pressure": pressure_converter,
    }
    
    if category in converters:
        converters[category]()
    else:
        st.write("Conversion feature for this category will be implemented here.")

def perform_conversion(units, factors):
    col1, col2 = st.columns(2)
    with col1:
        input_value = st.number_input("Enter value", min_value=0.0, format="%.2f")
        from_unit = st.selectbox("From", units)
    with col2:
        to_unit = st.selectbox("To", units)
    
    if st.button("Convert"):
        result = input_value * (factors[to_unit] / factors[from_unit])
        st.success(f"### {input_value} {from_unit} = {result:.4f} {to_unit}")

def length_converter():
    st.subheader("📏 Length Converter")
    length_units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"]
    conversion_factors = {
        "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000,
        "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701
    }
    perform_conversion(length_units, conversion_factors)

def weight_converter():
    st.subheader("⚖️ Weight Converter")
    weight_units = ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"]
    conversion_factors = {
        "Kilograms": 1, "Grams": 1000, "Milligrams": 1000000,
        "Pounds": 2.20462, "Ounces": 35.274
    }
    perform_conversion(weight_units, conversion_factors)

def temperature_converter():
    st.subheader("🌡️ Temperature Converter")
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    perform_conversion(temperature_units, {})

def time_converter():
    st.subheader("⏳ Time Converter")
    time_units = ["Seconds", "Minutes", "Hours", "Days"]
    conversion_factors = {
        "Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400
    }
    perform_conversion(time_units, conversion_factors)

def speed_converter():
    st.subheader("🚗 Speed Converter")
    speed_units = ["Meters per second", "Kilometers per hour", "Miles per hour", "Feet per second"]
    conversion_factors = {
        "Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694, "Feet per second": 3.28084
    }
    perform_conversion(speed_units, conversion_factors)

def area_converter():
    st.subheader("📐 Area Converter")
    area_units = ["Square meters", "Square kilometers", "Square feet", "Square inches", "Hectares", "Acres"]
    conversion_factors = {
        "Square meters": 1, "Square kilometers": 0.000001, "Square feet": 10.7639,
        "Square inches": 1550, "Hectares": 0.0001, "Acres": 0.000247105
    }
    perform_conversion(area_units, conversion_factors)

def volume_converter():
    st.subheader("🛢️ Volume Converter")
    volume_units = ["Liters", "Milliliters", "Cubic meters", "Cubic inches", "Gallons", "Cups"]
    conversion_factors = {
        "Liters": 1, "Milliliters": 1000, "Cubic meters": 0.001,
        "Cubic inches": 61.0237, "Gallons": 0.264172, "Cups": 4.16667
    }
    perform_conversion(volume_units, conversion_factors)

def data_storage_converter():
    st.subheader("💾 Data Storage Converter")
    data_units = ["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"]
    conversion_factors = {
        "Bytes": 1, "Kilobytes": 0.001, "Megabytes": 0.000001,
        "Gigabytes": 0.000000001, "Terabytes": 0.000000000001
    }
    perform_conversion(data_units, conversion_factors)

def energy_converter():
    st.subheader("⚡ Energy Converter")
    energy_units = ["Joules", "Kilojoules", "Calories", "Kilocalories", "Watt-hours"]
    conversion_factors = {
        "Joules": 1, "Kilojoules": 0.001, "Calories": 0.239006, "Kilocalories": 0.000239006, "Watt-hours": 0.000277778
    }
    perform_conversion(energy_units, conversion_factors)

def pressure_converter():
    st.subheader("🌡️ Pressure Converter")
    pressure_units = ["Pascals", "Kilopascals", "Bars", "PSI"]
    conversion_factors = {
        "Pascals": 1, "Kilopascals": 0.001, "Bars": 0.00001, "PSI": 0.000145038
    }
    perform_conversion(pressure_units, conversion_factors)

def bmi_calculator():
    st.subheader("📏 Body Mass Index (BMI) Calculator")
    
    gender = st.selectbox("Select Gender", ["Male", "Female", "Other"])
    
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.2f")
    with col2:
        height = st.number_input("Enter your height (m)", min_value=0.5, format="%.2f")
    
    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = weight / (height ** 2)
            st.success(f"### Your BMI: {bmi:.2f}")
            
            if bmi < 18.5:
                st.warning(f"⚠️ you are Underweight - Focus on a nutritious diet!")
            elif 18.5 <= bmi < 24.9:
                st.success(f"✅ your BMI is Perfect - Stay healthy!")
                rain(emoji="🎉", font_size=30, falling_speed=5, animation_length="2s")
            elif 25 <= bmi < 29.9:
                st.warning(f"⚠️ you are Overweight - Focus on a balanced diet and exercise!")
            else:
                st.error(f"❌ you are Above the Healthy Range - Consider a healthier routine!")
        else:
            st.error("Please enter valid weight and height values.")


def currency_converter():
    st.subheader("💱 Currency Converter")
    currencies = ["USD", "EUR", "GBP", "INR", "PKR", "AUD", "CAD", "JPY", "CNY"]
    
    col1, col2 = st.columns(2)
    with col1:
        amount = st.number_input("Enter amount", min_value=0.0, format="%.2f")
        from_currency = st.selectbox("From", currencies)
    with col2:
        to_currency = st.selectbox("To", currencies)
    
    conversion_rates = {
        "USD": {"EUR": 0.92, "GBP": 0.78, "INR": 82.5, "PKR": 280.0, "AUD": 1.48, "CAD": 1.34, "JPY": 148.5, "CNY": 7.1},
        "EUR": {"USD": 1.09, "GBP": 0.85, "INR": 89.7, "PKR": 304.0, "AUD": 1.61, "CAD": 1.46, "JPY": 161.2, "CNY": 7.8},
        "GBP": {"USD": 1.27, "EUR": 1.17, "INR": 105.2, "PKR": 356.0, "AUD": 1.90, "CAD": 1.72, "JPY": 188.4, "CNY": 9.1},
    }
    
    if st.button("Convert"):
        if from_currency in conversion_rates and to_currency in conversion_rates[from_currency]:
            result = amount * conversion_rates[from_currency][to_currency]
            st.success(f"### {amount} {from_currency} = {result:.2f} {to_currency}")
        else:
            st.error("Conversion rate not available")


if __name__ == "__main__":
    main()
