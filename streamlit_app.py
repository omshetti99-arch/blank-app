import streamlit as st

# Setup dynamic vertical configuration profile layout for smartphones
st.set_page_config(
    page_title="SHETTI TECHNICAL APP",
    layout="centered"
)

# Application Identity Headers (Strictly in CAPITAL LETTERS)
st.markdown("<h2 style='text-align: center; color: #1E3A8A; font-weight: bold;'>SHETTI TECHNICAL APP</h2>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: #475569; margin-top: -10px; letter-spacing: 1px;'>FANCY YARN SPECIFICATIONS</h5>", unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# {INPUT} MASTER LEDGER SECTION
# ==========================================
st.markdown("<h3 style='color: #0F172A; font-weight: bold;'>📥 {INPUT} SPECIFICATIONS</h3>", unsafe_allow_html=True)

with st.container(border=True):
    st.markdown("**QUALITY NAME:**\n<div style='font-size: 18px; color: #1E3A8A; font-weight: bold;'>GMPD HERITAGE</div>", unsafe_allow_html=True)
    st.markdown("<div style='margin-top: 5px;'><strong>MACHINE ALLOCATION:</strong></div><div style='font-size: 14px; color: #475569; font-weight: bold;'>M/C NO-01 (WHITE TIP)</div>", unsafe_allow_html=True)

st.markdown("<br><h4 style='color: #1E3A8A; font-weight: bold; text-transform: uppercase; font-size: 10pt;'>🧵 MASTER MATERIAL INTAKE SPECIFICATIONS</h4>", unsafe_allow_html=True)

st.markdown("**A) ROVING HANK:**")
st.success("0.60 HANK")

st.markdown("**B) BASE YARN (1):**")
st.success("150 DENIER")

st.markdown("**C) BASE YARN (2):**")
st.success("150 DENIER")

st.markdown("**D) COVER YARN:**")
st.success("75 DENIER")

st.markdown("**E) RESULT DENIER:**")
st.success("800 DENIER (LAB CONFIRMED)")

st.markdown("**F) FANCY YARN STATUS:**")
st.success("PACKAGE VISUAL VERIFIED {PHOTO LOGGED}")

st.markdown("---")

# ==========================================
# {OUTPUT} PERFORMANCE LEDGER SECTION
# ==========================================
st.markdown("<h3 style='color: #0F172A; font-weight: bold;'>📤 {OUTPUT} PERFORMANCE LEDGER</h3>", unsafe_allow_html=True)

# Separate functional profiles into standard UI Tabs for floor inspection
tabs = st.tabs([
    "SECTION A-B: MATRIX & SPEEDS", 
    "SECTION C-D: MASS & TENSILE", 
    "SECTION E-F: LAB QUALITY"
])

# --------------------------------------------------------------------------
# TAB 1: SECTION A & SECTION B
# --------------------------------------------------------------------------
with tabs[0]:
    st.markdown("<h4 style='color: #1E3A8A; font-weight: bold; font-size: 11pt;'>📋 SECTION A: DRAFTING & PATTERN STRUCTURAL MATRIX</h4>", unsafe_allow_html=True)
    
    st.markdown("**1. TOTAL DRAFT:**")
    st.code("21.84 (PEAK STRUCTURAL DRAFTING RATIO DURING SLUB GENERATION)")
    
    st.markdown("**2. MAIN DRAFT:**")
    st.code("25.24 (FRONT TO INTERMEDIATE ROLLER NIP BREAK)")
    
    st.markdown("**3. I.R DRAFT (INTERMEDIATE ROLLER):**")
    st.code("26.50 (SLUB STEPS) / 6.20 (BASE STEPS) (DUAL-PROFILE ELECTRONIC DRAFTING VARIATION)")
    
    st.markdown("**4. B.R DRAFT (BACK ROLLER):**")
    st.code("1.05 CONSTANT MECHANICAL BREAKDOWN DRAFT PROFILE")
    
    st.markdown("**5. AVG SLUB LENGTH:**")
    st.code("176.6 MM (MEAN LENGTH OF HEAVY FANCY STEPS)")
    
    st.markdown("**6. AVG DRAFT:**")
    st.code("19.90 (LENGTH-WEIGHTED LOOP CYCLE AVERAGE DRAFT)")
    
    st.markdown("**7. RANDOM LENGTHS:**")
    st.code("SLUB STEPS: 49.0% / 58.0% / 60.0% | BASE STEPS: 12.0% (PATTERN RANDOMIZATION BOUNDARIES TO AVOID FABRIC BARRE DEFECTS)")
    
    st.markdown("**8. CORE %:**")
    st.code("-1.00% (PROGRAMMED STRUCTURAL UNDER-FEED LOCKING TENSION)")
    
    st.markdown("**9. F.R % (FRONT ROLLER MODIFIER):**")
    st.code("-3.00% CONSTANT OVERFEED ADJUSTMENT BASELINE SETTING")
    
    st.markdown("**10. SLUB LENGTHS:**")
    st.code("180 MM (STEP 1) / 160 MM (STEP 3) / 183 MM (STEP 5) (INDIVIDUAL PROGRAMMED STEP LENGTHS FOR FANCY SEGMENTS)")
    
    st.markdown("**11. SLUB TO SLUB LENGTHS:**")
    st.code("85 MM CONSTANT SPACE SEGMENTS (STEPS 2, 4, 6, 8, 10 SEPARATING CONSECUTIVE SLUBS)")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #1E3A8A; font-weight: bold; font-size: 11pt;'>⚙️ SECTION B: MECHANICAL DRIVE SPEEDS & CONSTANTS</h4>", unsafe_allow_html=True)
    
    st.markdown("**12. TPI (TWISTS PER INCH):**")
    st.code("12.95 TPI (DERIVED COUNT TWIST STRUCTURE CALCULATION)")
    
    st.markdown("**13. TPM (TWISTS PER METER):**")
    st.code("510 TPM CONSTANT LOCKED TARGET TWIST INTENSITY")
    
    st.markdown("**14. FRS MPM:**")
    st.code("0.58 MPM RUNNING SPEED AT FANCY ROVING FEED SERVO")
    
    st.markdown("**15. SPINDLE SPEED:**")
    st.code("8000 RPM (TARGET PROGRAMMED) / 1149 RPM (ACTIVE MONITOR LOG)")
    
    st.markdown("**16. FRONT ROLLER SPEED:**")
    st.code("375 RPM MECHANICAL SHAFT SPEED / 15.22 MPM LINEAR DELIVERY RATE")
    
    st.markdown("**17. WINDING %:**")
    st.code("8.00% CONSTANT BOBBIN COMPACTING TENSION OVERFEED RATE")
    
    st.markdown("**18. CORE ROLLER SPEED:**")
    st.code("212 RPM MECHANICAL SHAFT SPEED / 15.06 MPM ACTIVE CORE DELIVERY SPEED")
    
    st.markdown("**19. WINDING SPEED:**")
    st.code("548 RPM DRIVE DRUM MOTOR / 14.43 MPM SURFACE PACKAGE TAKE-UP")

# --------------------------------------------------------------------------
# TAB 2: SECTION C & SECTION D
# --------------------------------------------------------------------------
with tabs[1]:
    st.markdown("<h4 style='color: #1E3A8A; font-weight: bold; font-size: 11pt;'>⚖️ SECTION C: CONTRACTION, YIELD & MASS BALANCE</h4>", unsafe_allow_html=True)
    
    st.markdown("**20. TWIST CONTRACTION %:**")
    st.code("1.85% PHYSICAL LINEAR CONTRACTION UNDER TWIST TORQUE FORCE")
    
    st.markdown("**21. ACTUAL DELIVERY DENIER:**")
    st.code("838.10 DENIER (WEIGHT AT FRONT NIP ROLL BEFORE STRUCTURAL RELAXLAXATION)")
    
    st.markdown("**22. MECHANICAL OUTPUT TO TECH DIFF:**")
    st.code("0.9547 MACHINE CORRECTION PROFILE FACTOR (K FACTOR)")
    
    st.markdown("**23. TOTAL WASTE %:**")
    st.code("0.00% WASTE | +0.16% POSITIVE MASS MOISTURE BALANCE GAIN")
    
    st.markdown("**24. RESULT DENIER / COUNT:**")
    st.code("800 DENIER (LABORATORY WRAP REEL TARGET BALANCED STANDARD)")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #1E3A8A; font-weight: bold; font-size: 11pt;'>🧪 SECTION D: LABORATORY TENSILE PERFORMANCE</h4>", unsafe_allow_html=True)
    
    st.markdown("**25. CSP (COUNT STRENGTH PRODUCT):**")
    st.code("1962 PREMIUM TENSILE TARGET BOUNDARY LIMIT")
    
    st.markdown("**26. RESULT COUNT (NE):**")
    st.code("6.64 NE COMPOSITE SLUB COUNT (NOMINAL CORE BASELINE: 9.41 NE)")
    
    st.markdown("**27. COUNT CV%:**")
    st.code("2.6% (EXCEPTIONAL COUNT UNIFORMITY ACROSS BOBBINS)")
    
    st.markdown("**28. STRENGTH (LBS):**")
    st.code("295.5 LBS (CALCULATED SINGLE STRAND SKEIN BREAKING FORCE)")
    
    st.markdown("**29. STRENGTH CV%:**")
    st.code("5.2% (PREMIUM WEAVE LOOP RUNNING EFFICIENCY BENCHMARK)")
    
    st.markdown("**30. QUALITY USTER REPORT SUMMARY:**")
    st.code("FULLY PROCESSED (DATA ARRAY SYSTEMATICALLY INDEXED INTO SLOTS 31-35 BELOW)")

# --------------------------------------------------------------------------
# TAB 3: SECTION E & SECTION F
# --------------------------------------------------------------------------
with tabs[2]:
    st.markdown("<h4 style='color: #1E3A8A; font-weight: bold; font-size: 11pt;'>📊 SECTION E: ADVANCED USTER TESTER 5 MASS MATRIX</h4>", unsafe_allow_html=True)
    
    st.markdown("**31. CVM % (MASS VARIATION):**")
    st.code("57.12% (EXPECTED HIGH RANGE CONFIRMING ROBUST STRUCTURAL SLUB DEFINITION)")
    
    st.markdown("**32. NO. OF SLUBS / METER:**")
    st.code("3.65 SLUBS/M (PERFECT STRUCTURAL TRACKING OF PROGRAMMED FRONT ROLL CYCLES)")
    
    st.markdown("**33. MASS INCREASE %:**")
    st.code("218.1% (HIGH INJECTION CONTRAST RATIO AGAINST BASELINE CORE YARN)")
    
    st.markdown("**34. AVG SLUB LENGTH (CM):**")
    st.code("9.8 CM (PHYSICAL SLUB LENGTH AFTER RELAXATION AND TWIST CONTRACTION)")
    
    st.markdown("**35. AVG SLUB DISTANCE (CM):**")
    st.code("17.7 CM (UNIFORM SPACING PROFILE PREVENTING FABRIC BARRE/TRACKING PATTERNS)")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #1E3A8A; font-weight: bold; font-size: 11pt;'>👁️ SECTION F: PACKAGE VISUAL VERIFICATION</h4>", unsafe_allow_html=True)
    
    st.markdown("**36. FANCY YARN PACKAGE VISUAL STATUS:**")
    st.code("VERIFIED COMPACT CHEESE BUILD (WHITE TIP FANCY EFFECT ACTIVE AS PER PHOTO VALIDATION)")

st.markdown("<br><p style='text-align: center; color: #94A3B8; font-size: 11px;'>SHETTI TECHNOLOGIES v1.0.4</p>", unsafe_allow_html=True)
