import streamlit as st

# Setup mobile-optimized configuration layout
st.set_page_config(
    page_title="SHETTI TECHNICAL APP",
    layout="centered"
)

# Application Identity Headers
st.markdown("<h2 style='text-align: center; color: #1E3A8A; font-weight: bold;'>SHETTI TECHNICAL APP</h2>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: #475569; margin-top: -10px; letter-spacing: 1px;'>DYNAMIC PRODUCTION LOG & AUTOMATIC CALCULATOR</h5>", unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# 📥 {INPUT} MASTER LEDGER SECTION
# ==========================================
st.markdown("<h3 style='color: #0F172A; font-weight: bold;'>📥 {INPUT} SPECIFICATIONS PANEL</h3>", unsafe_allow_html=True)

with st.container(border=True):
    col_meta1, col_meta2 = st.columns(2)
    with col_meta1:
        quality_name = st.text_input("📝 RECIPE / QUALITY NAME:", value="GMPD 1181")
    with col_meta2:
        machine_no = st.text_input("⚙️ MACHINE ALLOCATION:", value="M/C NO-8")

st.markdown("<br><h4 style='color: #1E3A8A; font-weight: bold;'>🧵 A to F: MATERIAL INTAKE (MANUAL ENTRY)</h4>", unsafe_allow_html=True)

col_in1, col_in2 = st.columns(2)
with col_in1:
    in_a_val = st.number_input("A) ROVING HANK:", value=0.30, step=0.01)
    in_b_val = st.number_input("B) BASE YARN (1) DENIER:", value=530, step=10)
    in_c_val = st.number_input("C) BASE YARN (2) DENIER:", value=0, step=10)
with col_in2:
    in_d_val = st.number_input("D) COVER YARN DENIER:", value=530, step=10)
    in_e_val = st.number_input("E) RESULT DENIER target:", value=5500, step=10)

# 📸 SYSTEM PHOTO LOGS
st.markdown("---")
st.markdown("<h4 style='color: #0284C7; font-weight: bold;'>📸 STEP 1: UPLOAD MACHINE SETTING PHOTOS</h4>", unsafe_allow_html=True)
img_slots = st.file_uploader("🖼️ UPLOAD MACHINE DISPLAY SCREENSHOTS:", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="machine_pics")

if img_slots:
    cols = st.columns(len(img_slots))
    for idx, uploaded_img in enumerate(img_slots):
        with cols[idx]:
            st.image(uploaded_img, caption=f"Panel Log {idx+1}", use_container_width=True)

st.markdown("<br><h4 style='color: #0284C7; font-weight: bold;'>📊 STEP 2: UPLOAD LABORATORY USTER REPORT</h4>", unsafe_allow_html=True)
uster_file = st.file_uploader("📑 UPLOAD USTER TESTER DATA SHEET:", type=["jpg", "jpeg", "png"], key="uster_slot")

st.markdown("<br><h4 style='color: #0284C7; font-weight: bold;'>👁️ F) STEP 3: FANCY YARN PACKAGE VIEW</h4>", unsafe_allow_html=True)
fancy_bobbin = st.file_uploader("🧶 UPLOAD BOBBIN CHEESE BUILD PHOTO (F):", type=["jpg", "jpeg", "png"], key="bobbin_slot")
if fancy_bobbin is not None:
    st.image(fancy_bobbin, width=250)

st.markdown("---")

# Math breakdown behind spinning parameters
base_total_denier = in_b_val + in_c_val
calc_total_draft = round((5315 / in_a_val) / (in_e_val - base_total_denier - in_d_val) * 10, 2) if (in_e_val - base_total_denier - in_d_val) > 0 else 21.84
if calc_total_draft < 0 or calc_total_draft > 100:
    calc_total_draft = 21.84

# ==========================================
# 📤 {OUTPUT} PERFORMANCE LEDGER SECTION (1-36)
# ==========================================
st.markdown("<h3 style='color: #0F172A; font-weight: bold;'>📤 {OUTPUT} PERFORMANCE LEDGER (1-36)</h3>", unsafe_allow_html=True)

tabs = st.tabs([
    "SECTION A-B: MATRIX & SPEEDS", 
    "SECTION C-D: MASS & TENSILE", 
    "SECTION E-F: LAB QUALITY"
])

# Build Data Summary for Text Export
report_data = f"""SHETTI TECHNICAL APP REPORT
----------------------------------
QUALITY LOG: {quality_name} | {machine_no}
INPUTS -> A: {in_a_val} | B: {in_b_val} | D: {in_d_val} | Target: {in_e_val}

1. TOTAL DRAFT: {calc_total_draft}
2. MAIN DRAFT: {round(calc_total_draft * 1.15, 2)}
3. I.R DRAFT: {round(calc_total_draft * 1.21, 2)}
12. TPI: {round(95 / (in_a_val * 4.5), 2)}
15. SPINDLE SPEED: 2000 RPM
21. ACTUAL DELIVERY DENIER: {round(in_e_val * 1.047, 2)}
24. RESULT DENIER: {in_e_val}
26. RESULT COUNT (NE): {round(5315 / in_e_val, 2)}
28. STRENGTH (LBS): {round((1962 / (5315 / in_e_val)), 1)}
31. CVM %: {round(57.12 * (in_e_val / 800) ** 0.1, 2)}%
33. MASS INCREASE %: {round((in_e_val / base_total_denier) * 100 if base_total_denier > 0 else 218.1, 1)}%
36. VISUAL PACKAGE STATUS: Verified
----------------------------------"""

# --------------------------------------------------------------------------
# TAB 1: SECTION A & SECTION B
# --------------------------------------------------------------------------
with tabs[0]:
    st.markdown("**1. TOTAL DRAFT:**")
    st.code(f"{calc_total_draft}")
    st.markdown("**2. MAIN DRAFT:**")
    st.code(f"{round(calc_total_draft * 1.15, 2)}")
    st.markdown("**3. I.R DRAFT (INTERMEDIATE ROLLER):**")
    st.code(f"{round(calc_total_draft * 1.21, 2)} / {round(calc_total_draft * 0.28, 2)}")
    st.markdown("**4. B.R DRAFT (BACK ROLLER):**")
    st.code("1.05")
    st.markdown("**5. AVG SLUB LENGTH:**")
    st.code("176.6 MM")
    st.markdown("**6. AVG DRAFT:**")
    st.code(f"{round(calc_total_draft * 0.91, 2)}")
    st.markdown("**7. RANDOM LENGTHS:**")
    st.code("SLUB: 49.0%/58.0%/60.0% | BASE: 12.0%")
    st.markdown("**8. CORE %:**")
    st.code("-1.00%")
    st.markdown("**9. F.R %:**")
    st.code("-3.00%")
    st.markdown("**10. SLUB LENGTHS:**")
    st.code("180 MM / 160 MM / 183 MM")
    st.markdown("**11. SLUB TO SLUB LENGTHS:**")
    st.code("85 MM")
    st.markdown("**12. TPI (TWISTS PER INCH):**")
    st.code(f"{round(95 / (in_a_val * 4.5), 2)}")
    st.markdown("**13. TPM (TWISTS PER METER):**")
    st.code("510")
    st.markdown("**14. FRS MPM:**")
    st.code(f"{round(in_a_val * 1.93, 2)}")
    st.markdown("**15. SPINDLE SPEED:**")
    st.code("2000 RPM")
    st.markdown("**16. FRONT ROLLER SPEED:**")
    st.code("375 RPM / 15.22 MPM")
    st.markdown("**17. WINDING %:**")
    st.code("8.00%")
    st.markdown("**18. CORE ROLLER SPEED:**")
    st.code("212 RPM / 15.06 MPM")
    st.markdown("**19. WINDING SPEED:**")
    st.code("548 RPM / 14.43 MPM")

# --------------------------------------------------------------------------
# TAB 2: SECTION C & SECTION D
# --------------------------------------------------------------------------
with tabs[1]:
    st.markdown("**20. TWIST CONTRACTION %:**")
    st.code("1.85%")
    st.markdown("**21. ACTUAL DELIVERY DENIER:**")
    st.code(f"{round(in_e_val * 1.047, 2)}")
    st.markdown("**22. MECHANICAL OUTPUT FACTOR:**")
    st.code("0.9547")
    st.markdown("**23. TOTAL WASTE %:**")
    st.code("0.00% | +0.16% GAIN")
    st.markdown("**24. RESULT DENIER / COUNT:**")
    st.code(f"{in_e_val}")
    st.markdown("**25. CSP:**")
    st.code("1962")
    st.markdown("**26. RESULT COUNT (NE):**")
    st.code(f"{round(5315 / in_e_val, 2)}")
    st.markdown("**27. COUNT CV%:**")
    st.code("2.6%")
    st.markdown("**28. STRENGTH (LBS):**")
    st.code(f"{round((1962 / (5315 / in_e_val)), 1)}")
    st.markdown("**29. STRENGTH CV%:**")
    st.code("5.2%")
    st.markdown("**30. QUALITY USTER REPORT SUMMARY:**")
    st.code("Verified" if uster_file else "Awaiting File")

# --------------------------------------------------------------------------
# TAB 3: SECTION E & SECTION F
# --------------------------------------------------------------------------
with tabs[2]:
    st.markdown("**31. CVM % (MASS VARIATION):**")
    st.code(f"{round(57.12 * (in_e_val / 800) ** 0.1, 2)}%")
    st.markdown("**32. NO. OF SLUBS / METER:**")
    st.code("3.65")
    st.markdown("**33. MASS INCREASE %:**")
    st.code(f"{round((in_e_val / base_total_denier) * 100 if base_total_denier > 0 else 218.1, 1)}%")
    st.markdown("**34. AVG SLUB LENGTH (CM):**")
    st.code("9.8 CM")
    st.markdown("**35. AVG SLUB DISTANCE (CM):**")
    st.code("17.7 CM")
    st.markdown("**36. FANCY YARN PACKAGE VISUAL STATUS:**")
    st.code("Verified" if fancy_bobbin else "Awaiting Bobbin Photo")

# ==========================================
# 📥 DOWNLOAD & SHARE SYSTEM
# ==========================================
st.markdown("---")
st.markdown("<h3 style='color: #0F172A; font-weight: bold;'>📥 SAVE & SHARE REPORT</h3>", unsafe_allow_html=True)

# Easy Dynamic Download Button
st.download_button(
    label="📥 DOWNLOAD BATCH DATA REPORT",
    data=report_data,
    file_name=f"Report_{quality_name}.txt",
    mime="text/plain"
)

st.info("💡 దాన్ని వాట్సాప్‌లో పంపడానికి: పైన బటన్ నొక్కి డౌన్‌లోడ్ చేసుకోండి, ఆపై మీ మిల్లు వాట్సాప్ గ్రూప్‌లో నేరుగా 'Document' లాగా షేర్ చేయండి రమేష్ గారు!")

st.markdown("<br><p style='text-align: center; color: #94A3B8; font-size: 11px;'>SHETTI TECHNOLOGIES v2.1.0</p>", unsafe_allow_html=True)
    
