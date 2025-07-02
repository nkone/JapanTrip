from locale import DAY_1
import streamlit as st

# Helper function
import os

def count_files_non_recursively(directory_path):
    """
    Counts the number of files in a specified directory, non-recursively.
    """
    try:
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        return len(files)
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Page setups

information_pg = st.Page(
    page="pages/Information.py",
    title="Information"

)
home_pg = st.Page(
    page="pages/Home.py",
    title="Home"
)
resource_pg = st.Page(
    page="pages/Resources.py",
    title="Resources"
)
# day1_pg = st.Page(
#     page="pages/itinerary/day_1.py",
#     title="Day 1"
# )

# Days are dynamically added as more files for itinerary folder are added
# Files must follow this naming covention day_x where x is the day number

total_days = count_files_non_recursively("pages/itinerary")
days_list = []
for days in range(1, total_days + 1):
    days_list.append(st.Page(
        page="pages/itinerary/day_" + str(days) + ".py",
        title="Day " + str(days)
    ))


st.set_page_config(page_title="Japan 2026")
pg = st.navigation(
    {
        "Main": [home_pg, information_pg],
        "Iternary": days_list,
        "Reference": [resource_pg]
    }
)
pg.run()