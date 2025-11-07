import streamlit as st

# --- Streamlit Calculator MVP ---
st.set_page_config(page_title="Streamlit Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Simple Streamlit Calculator")

# Step 1: Input numbers
st.subheader("Step 1: Enter Numbers")
num1 = st.number_input("Enter first number:", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number:", value=0.0, format="%.2f")

# Step 2: Choose operation
st.subheader("Step 2: Choose Operation")
operation = st.selectbox(
    "Select operation:",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Step 3: Calculate result
st.subheader("Step 3: Get Result")
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"✅ Result: {num1} + {num2} = {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"✅ Result: {num1} - {num2} = {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"✅ Result: {num1} × {num2} = {result}")
    elif operation == "Division":
        if num2 == 0:
            st.error("❌ Cannot divide by zero!")
        else:
            result = num1 / num2
            st.success(f"✅ Result: {num1} ÷ {num2} = {result}")

# Step 4: Optional - Reset
if st.button("Reset"):
    st.rerun()

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
