import streamlit as st

# ------------------ APP CONFIG ------------------
st.set_page_config(page_title="iCollege Virtual Employee", layout="centered")

st.title("iCollege Virtual Employee App")
st.caption("Simulated corporate task environment for skill evaluation")

# ------------------ USER DETAILS ------------------
st.subheader("Employee Onboarding")

employee_name = st.text_input("Enter your name")

if employee_name:
    st.success(f"Welcome, {employee_name} 👋")

    # ------------------ TASK SELECTION ------------------
    st.subheader("Assigned Task")

    task = st.selectbox(
        "Select a task",
        ["Automation Feasibility Evaluation"]
    )

    # ------------------ TASK MODULE ------------------
    if task == "Automation Feasibility Evaluation":
        st.markdown("### Task Description")
        st.write(
            "You are required to evaluate whether a business process is worth automating "
            "based on effort, frequency, and cost."
        )

        st.markdown("### Task Inputs")

        manual_minutes = st.number_input("Manual effort per task (minutes)", min_value=1)
        frequency = st.selectbox("Frequency", ["Daily", "Weekly", "Monthly"])
        users = st.number_input("Number of users", min_value=1)
        dev_hours = st.number_input("Automation development effort (hours)", min_value=1)
        maintenance_hours = st.number_input("Maintenance effort per month (hours)", min_value=0)
        cost_per_hour = st.number_input("Cost per hour", min_value=1)

        if st.button("Submit Task"):
            # Convert frequency
            runs = 22 if frequency == "Daily" else 4 if frequency == "Weekly" else 1

            # Calculations
            manual_cost = ((manual_minutes * runs * users) / 60) * cost_per_hour
            automation_cost = ((dev_hours * cost_per_hour) / 12) + (maintenance_hours * cost_per_hour)
            roi = ((manual_cost - automation_cost) / automation_cost) * 100

            # Evaluation logic
            if roi > 30:
                decision = "Automate"
                score = 90
            else:
                decision = "Not Recommended"
                score = 70

            # ------------------ RESULTS ------------------
            st.subheader("Evaluation Result")

            st.write(f"**Manual Cost:** ₹{manual_cost:,.2f}")
            st.write(f"**Automation Cost:** ₹{automation_cost:,.2f}")
            st.write(f"**ROI:** {roi:.2f}%")
            st.write(f"**Decision:** {decision}")

            st.success(f"Task Score: {score}/100")

            st.info(
                "This task evaluates decision-making and cost-analysis skills "
                "expected from a corporate automation role."
            )

else:
    st.warning("Please enter your name to begin.")