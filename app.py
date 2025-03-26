import streamlit as st
import pandas as pd

# Title
st.title("Solar Savings Calculator")

# User Input
bill = st.number_input("Enter your Monthly Electricity Bill (₹)", min_value=0, value=3500)
annual_bill = bill * 12  # Yearly bill
increase_rate = 0.05  # 5% increase every 5 years

# Calculation
years = list(range(1, 26))
bills = [annual_bill]

for i in range(1, 25):
    if i % 5 == 0:  # Every 5 years, increase by 5%
        annual_bill *= 1.05
    bills.append(annual_bill)

# Convert to DataFrame
df = pd.DataFrame({"Year": years, "Projected Annual Bill (₹)": bills})

# Show Results
st.write("### Estimated Electricity Bill Over 25 Years:")
st.line_chart(df.set_index("Year"))
st.write(df)

# Savings with Solar
solar_savings = sum(bills) * 0.80  # Assuming 80% savings
st.write(f"#### Potential Savings with Solar: ₹{solar_savings:,.2f}")
