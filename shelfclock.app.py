import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Shelf Clock",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# PROFESSIONAL CSS STYLING
# ============================================
st.markdown("""
    <style>
        .stApp {
            background-color: #F8FAFC;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .main-header {
            font-size: 2.8rem;
            font-weight: 700;
            color: #0F172A;
            letter-spacing: -0.02em;
            margin-bottom: 0.25rem;
        }
        .main-subheader {
            font-size: 1.1rem;
            color: #64748B;
            margin-bottom: 2rem;
            font-weight: 400;
        }

        .kpi-card {
            background: white;
            padding: 1.25rem 1rem;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 1px 3px rgba(0,0,0,0.06);
            border: 1px solid #E2E8F0;
            transition: all 0.2s;
        }
        .kpi-card:hover {
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            border-color: #CBD5E1;
        }
        .kpi-number {
            font-size: 2.4rem;
            font-weight: 700;
            color: #0F172A;
            line-height: 1.2;
        }
        .kpi-number.green { color: #059669; }
        .kpi-number.red { color: #DC2626; }
        .kpi-number.yellow { color: #D97706; }
        .kpi-number.blue { color: #2563EB; }
        .kpi-label {
            font-size: 0.8rem;
            color: #64748B;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            margin-top: 0.25rem;
        }

        .option-card {
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid #E2E8F0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
            height: 100%;
            transition: all 0.2s;
        }
        .option-card:hover {
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            border-color: #CBD5E1;
        }
        .option-card .tag {
            font-size: 0.7rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            padding: 0.2rem 0.7rem;
            border-radius: 20px;
            display: inline-block;
            margin-bottom: 0.75rem;
        }
        .tag.aggressive { background: #FEE2E2; color: #991B1B; }
        .tag.conservative { background: #FEF3C7; color: #92400E; }
        .tag.contrarian { background: #D1FAE5; color: #065F46; }

        .option-card .amount {
            font-size: 1.5rem;
            font-weight: 700;
            color: #0F172A;
        }
        .option-card .detail {
            font-size: 0.85rem;
            color: #64748B;
            margin: 0.25rem 0;
        }

        .alert-box {
            padding: 1.25rem;
            border-radius: 12px;
            border-left: 4px solid;
            margin: 0.75rem 0;
            background: white;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        }
        .alert-box.danger { border-left-color: #DC2626; background: #FEF2F2; }
        .alert-box.warning { border-left-color: #D97706; background: #FFFBEB; }
        .alert-box.success { border-left-color: #059669; background: #ECFDF5; }
        .alert-box.info { border-left-color: #2563EB; background: #EFF6FF; }

        .section-divider {
            margin: 2.5rem 0 1.5rem 0;
            border: none;
            border-top: 1px solid #E2E8F0;
        }

        .stSidebar {
            background-color: white;
            border-right: 1px solid #E2E8F0;
        }

        .stButton > button {
            background-color: #0F172A;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1.5rem;
            font-weight: 500;
            width: 100%;
            transition: all 0.2s;
        }
        .stButton > button:hover {
            background-color: #1E293B;
            box-shadow: 0 4px 12px rgba(15,23,42,0.2);
        }

        .stNumberInput label, .stTextInput label, .stSlider label {
            font-weight: 500;
            color: #334155;
            font-size: 0.85rem;
        }
    </style>
""", unsafe_allow_html=True)

# ============================================
# HEADER
# ============================================
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<div class="main-header">📦 Shelf Clock</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subheader">Inventory Forecasting & Turnover Optimization</div>', unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div style="text-align:right;padding-top:0.5rem;">
            <span style="background:#E2E8F0;padding:0.3rem 1rem;border-radius:20px;font-size:0.7rem;color:#475569;font-weight:500;">v1.0 · LIVE</span>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ============================================
# SIDEBAR
# ============================================
with st.sidebar:
    st.markdown("### 📊 Inventory Data")
    st.caption("Enter your product details below")

    product = st.text_input("Product Name / SKU", placeholder="e.g., Wireless Headphones")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        units = st.number_input("Units on Hand", value=847, step=10)
        cost = st.number_input("Unit Cost ($)", value=14.50, step=0.50)
        lead_time = st.number_input("Lead Time (days)", value=14, step=1)
    with col2:
        daily = st.number_input("Daily Sales (avg)", value=22, step=1)
        price = st.number_input("Sell Price ($)", value=39.99, step=0.50)
        moq = st.number_input("MOQ (units)", value=500, step=50)

    storage_cost = st.number_input("Storage Cost ($/unit/month)", value=0.85, step=0.05)
    marketing_spend = st.number_input("Marketing Spend ($/month)", value=450, step=50)
    returns = st.slider("Return Rate (%)", 0.0, 30.0, 6.2, 0.1)

    st.markdown("---")
    generate = st.button("🚀 Generate Forecast", type="primary", use_container_width=True)

# ============================================
# MAIN CONTENT
# ============================================
if generate:
    if not product:
        st.error("⚠️ Please enter a product name to continue.")
    else:
        with st.spinner("Analyzing inventory data..."):
            # ---- CALCULATIONS ----
            net_daily = daily * (1 - returns / 100)
            monthly_sold = net_daily * 30
            turnover = monthly_sold / units
            stockout_days = int(units / net_daily)
            reorder_trigger = max(0, stockout_days - lead_time)
            gross_margin = price - cost
            monthly_storage = units * storage_cost

            aggressive_cost = moq * cost
            new_storage = (units + moq) * storage_cost

            contrarian_turnover = ((daily * 1.27 * (1 - returns/100) * 30) / units)

            gross_stockout = int(units / daily)
            lost_units = (stockout_days - gross_stockout) * daily if stockout_days > gross_stockout else 0
            lost_revenue = lost_units * gross_margin

            # ---- REPORT HEADER ----
            st.markdown(f"""
                <div style="background:white;padding:1.5rem;border-radius:12px;border:1px solid #E2E8F0;margin-bottom:1.5rem;">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <div>
                            <span style="font-size:0.7rem;color:#64748B;text-transform:uppercase;letter-spacing:0.04em;">Forecast Report</span>
                            <h2 style="color:#0F172A;margin:0.25rem 0 0 0;">{product}</h2>
                        </div>
                        <span style="font-size:0.8rem;color:#64748B;">{datetime.now().strftime('%B %d, %Y')}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            # ---- KPI ROW ----
            st.markdown("### Key Metrics")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                color = "green" if turnover >= 1.0 else "red" if turnover < 0.7 else "yellow"
                st.markdown(f"""
                    <div class="kpi-card">
                        <div class="kpi-number {color}">{turnover:.2f}x</div>
                        <div class="kpi-label">Turnover Rate</div>
                    </div>
                """, unsafe_allow_html=True)

            with col2:
                color = "green" if stockout_days > 30 else "red" if stockout_days < 15 else "yellow"
                st.markdown(f"""
                    <div class="kpi-card">
                        <div class="kpi-number {color}">Day {stockout_days}</div>
                        <div class="kpi-label">Stockout Date</div>
                    </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                    <div class="kpi-card">
                        <div class="kpi-number blue">Day {reorder_trigger}</div>
                        <div class="kpi-label">Reorder Trigger</div>
                    </div>
                """, unsafe_allow_html=True)

            with col4:
                st.markdown(f"""
                    <div class="kpi-card">
                        <div class="kpi-number blue">{monthly_sold:,.0f}</div>
                        <div class="kpi-label">Monthly Units Sold</div>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

            # ---- THREE OPTIONS ----
            st.markdown("### 🎯 Three Strategic Options")
            st.caption("Choose your path based on risk tolerance and growth goals")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(f"""
                    <div class="option-card">
                        <span class="tag aggressive">HIGH RISK</span>
                        <div style="font-weight:600;font-size:1.1rem;color:#0F172A;">Aggressive</div>
                        <div style="margin:0.5rem 0;">
                            <span class="amount">${aggressive_cost:,.2f}</span>
                            <div class="detail">Order {moq} units NOW</div>
                        </div>
                        <div class="detail">📦 Storage: ${new_storage:,.2f}/month</div>
                        <div class="detail">📈 Turnover: ~{((monthly_sold)/(units+moq)):.2f}x</div>
                        <div style="margin-top:0.75rem;font-size:0.8rem;color:#64748B;">Trades cash-now for stockout protection</div>
                    </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                    <div class="option-card">
                        <span class="tag conservative">LOW RISK</span>
                        <div style="font-weight:600;font-size:1.1rem;color:#0F172A;">Conservative</div>
                        <div style="margin:0.5rem 0;">
                            <span class="amount">${monthly_storage:,.2f}</span>
                            <div class="detail">Hold until Day {reorder_trigger}</div>
                        </div>
                        <div class="detail">📦 Storage: ${monthly_storage:,.2f}/month</div>
                        <div class="detail">📈 Turnover: {turnover:.2f}x</div>
                        <div style="margin-top:0.75rem;font-size:0.8rem;color:#64748B;">Safest, but does nothing to fix slow turnover</div>
                    </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                    <div class="option-card">
                        <span class="tag contrarian">HIGH REWARD</span>
                        <div style="font-weight:600;font-size:1.1rem;color:#0F172A;">Contrarian</div>
                        <div style="margin:0.5rem 0;">
                            <span class="amount">+${marketing_spend:,.0f}</span>
                            <div class="detail">Double marketing spend</div>
                        </div>
                        <div class="detail">📈 Projected Turnover: {contrarian_turnover:.2f}x</div>
                        <div class="detail">📊 Tests demand elasticity</div>
                        <div style="margin-top:0.75rem;font-size:0.8rem;color:#64748B;">Estimate — not a guarantee</div>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

            # ---- HIDDEN VARIABLE ----
            st.markdown("### 🔍 Hidden Variable")

            st.markdown(f"""
                <div class="alert-box warning">
                    <strong>⚠️ Return Processing Time — Unknown</strong><br>
                    You provided a return rate of {returns}%, but didn't specify how long returns take to become sellable stock again.
                    <br><br>
                    <strong>Impact:</strong> If processing takes 3+ days, your real depletion rate is closer to the gross {daily} units/day, not the net {net_daily:.2f} units/day.
                    <br>
                    <strong>Risk:</strong> Stockout could move from Day {stockout_days} to ~Day {gross_stockout}.
                </div>
            """, unsafe_allow_html=True)

            st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

            # ---- FAILURE SCENARIO ----
            st.markdown("### 💀 Failure Scenario")

            if lost_units > 0:
                st.markdown(f"""
                    <div class="alert-box danger">
                        <strong>⚠️ If returns are NOT immediately resellable:</strong><br>
                        True stockout lands at Day {gross_stockout}, not Day {stockout_days}.<br><br>
                        Under the Conservative option, your order placed at Day {reorder_trigger} arrives Day {reorder_trigger + lead_time} — <strong>{abs(stockout_days - gross_stockout)} days late</strong>.<br><br>
                        Lost margin: <strong style="color:#DC2626;font-size:1.2rem;">${lost_revenue:,.0f}</strong> before counting customers who buy from competitors and don't come back.
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="alert-box success">
                        <strong>✅ Current buffer holds.</strong><br>
                        Even without immediate return processing, your stockout date stays at Day {stockout_days}. Your lead-time buffer of {lead_time} days provides enough cushion.
                    </div>
                """, unsafe_allow_html=True)

            st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

            # ---- RECOMMENDATIONS ----
            st.markdown("### 📌 Recommended Next Steps")

            if turnover < 1.0:
                st.markdown(f"""
                    <div class="alert-box warning">
                        <strong>📉 Turnover Alert:</strong> Your turnover rate of {turnover:.2f}x is below the healthy 1.0x benchmark.<br>
                        Consider the <strong>Contrarian</strong> option to lift demand, or review your pricing strategy.
                    </div>
                """, unsafe_allow_html=True)
            elif turnover < 1.5:
                st.markdown(f"""
                    <div class="alert-box success">
                        <strong>✅ Healthy Turnover:</strong> Your {turnover:.2f}x turnover rate is in the healthy range (1.0x–1.5x).<br>
                        The Conservative option keeps you safe, but the Contrarian option could unlock additional growth.
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="alert-box success">
                        <strong>🚀 Strong Turnover:</strong> Your {turnover:.2f}x turnover rate is excellent (>1.5x).<br>
                        Focus on maintaining current velocity while exploring the Aggressive option to scale.
                    </div>
                """, unsafe_allow_html=True)

            st.markdown(f"""
                <div style="background:white;padding:1.25rem;border-radius:12px;border:1px solid #E2E8F0;margin-top:1rem;">
                    <strong>📋 Data Needed to Sharpen This Forecast:</strong><br>
                    • Return processing time (days from return to resellable stock)<br>
                    • Historical demand elasticity (sales response to past price/marketing changes)<br>
                    • Vendor reliability score (% of orders delivered on time)
                </div>
            """, unsafe_allow_html=True)

# ============================================
# EMPTY STATE
# ============================================
else:
    st.markdown("""
        <div style="text-align:center;padding:4rem 0;">
            <div style="font-size:4rem;margin-bottom:1rem;">📦</div>
            <h2 style="color:#0F172A;font-weight:600;">Enter your inventory data to get started</h2>
            <p style="color:#64748B;font-size:1.1rem;">Fill in the numbers in the sidebar and click <strong>"Generate Forecast"</strong></p>
            <p style="color:#94A3B8;font-size:0.9rem;margin-top:0.5rem;">Shelf Clock will analyze turnover, stockout risk, and recommend 3 strategic options</p>
        </div>
    """, unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================
st.markdown("""
    <div style="margin-top:3rem;padding-top:1.5rem;border-top:1px solid #E2E8F0;text-align:center;">
        <span style="color:#94A3B8;font-size:0.75rem;">📦 Shelf Clock — Inventory Forecasting & Turnover Optimization</span>
    </div>
""", unsafe_allow_html=True)