import streamlit as st

# Layout Configuration
st.set_page_config(page_title="SHETTI TECHNICAL APP", layout="centered")

# App Title
st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>SHETTI TECHNICAL APP</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Official Production Blueprint & Quality Registry</p>", unsafe_allow_html=True)

# 1. Inputs
quality_name = st.text_input("Quality Name:", "GMPD 663N")
rov = st.number_input("Roving Hank:", 0.60, step=0.01)
base = st.number_input("Base Yarn (Denier):", 150, step=10)
cover = st.number_input("Cover Yarn (Denier):", 75, step=10)
target = st.number_input("Target Denier:", 800, step=10)

# 2. Logic (Simplified Draft Calculation)
total_draft = round(((5315 / rov) / (target - base - cover)), 2)

# 3. Display Data (1-40 parameters)
st.subheader("Production Parameters Registry")
st.write(f"**Quality:** {quality_name} | **Target Denier:** {target}")
st.write(f"**Total Draft:** {total_draft} | **Main Draft:** {round(total_draft * 1.15, 2)}")

# Parameters Grid (Simplified display)
st.table({
    "Parameter": ["Total Draft", "Main Draft", "TPI", "TPM", "Result Denier", "Shift Yield"],
    "Value": [total_draft, round(total_draft*1.15, 2), 12.95, 510, target, 649.4]
})

# 4. Download Function
if st.button("Download Technical Report (.txt)"):
    report = f"Quality: {quality_name}\nDraft: {total_draft}\nTarget: {target}"
    st.download_button("Click to Download", report, "report.txt")
    
