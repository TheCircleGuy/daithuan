import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def display_summary_statistics2():
    summary_text = """
    # Summary Statistics and Percentages for Travel Time: 
    ---------------------------------------------------
    - Mean Travel Time: 19.45 minutes
    - Mode Travel Time: 15.00 minutes
    - Max Travel Time: 57.00 minutes
    - Total Data Points: 2016
    - Percentage of Data Less Than 5 minutes: 1.64%
    - Percentage of Data Less Than 10 minutes: 11.76%
    - Percentage of Data Less Than 15 minutes: 28.97%
    - Percentage of Data Less Than 20 minutes: 54.12%
    - Percentage of Data Less Than 30 minutes: 89.38%
    - Percentage of Data Less Than 45 minutes: 98.56%
    - Percentage of Data Less Than 60 minutes: 100.00%
    """
    st.markdown(summary_text)
def display_summary_statistics3():
    summary_text = """
    # Summary Statistics and Percentages for Travel Time: 
    ---------------------------------------------------
    - Mean Travel Time: 19.45 minutes
    - Mode Travel Time: 15.00 minutes
    - Max Travel Time: 57.00 minutes
    - Total Data Points: 2016
    - Percentage of Data Less Than 5 minutes: 1.64%
    - Percentage of Data Less Than 10 minutes: 11.76%
    - Percentage of Data Less Than 15 minutes: 28.97%
    - Percentage of Data Less Than 20 minutes: 54.12%
    - Percentage of Data Less Than 30 minutes: 89.38%
    - Percentage of Data Less Than 45 minutes: 98.56%
    - Percentage of Data Less Than 60 minutes: 100.00%
    """
    st.markdown(summary_text)

def display_summary_statistics5():
    summary_text = """
    # Summary Statistics and Percentages for Travel Time:  5WH
 ---------------------------------------------------
- Mean Travel Time: 19.45 minutes
- Mode Travel Time: 15.00 minutes
- Max Travel Time: 57.00 minutes
- Total Data Points: 2016
- Percentage of Data Less Than 5 minutes: 1.64%
- Percentage of Data Less Than 10 minutes: 11.76%
- Percentage of Data Less Than 15 minutes: 28.97%
- Percentage of Data Less Than 20 minutes: 54.12%
- Percentage of Data Less Than 30 minutes: 89.38%
- Percentage of Data Less Than 45 minutes: 98.56%
- Percentage of Data Less Than 60 minutes: 100.00%
    """
    st.markdown(summary_text)

def generate_histogram(df, num_warehouses):
    # Sort the DataFrame by 'travel time' column
    df_sorted = df.sort_values(by=f'travel time {num_warehouses}')

    # Extract numeric values from 'travel time' column
    df_sorted['travel_time_numeric'] = df_sorted[f'travel time {num_warehouses}'].str.extract(r'(\d+)').astype(float)

    # Define bin edges
    bin_edges = range(0, int(df_sorted['travel_time_numeric'].max()) + 6, 5)

    # Create a wider figure
    plt.figure(figsize=(10, 6))

    # Plot a histogram of travel times
    plt.hist(df_sorted['travel_time_numeric'], bins=bin_edges, color='skyblue', edgecolor='black')
    plt.title(f'Distribution of Travel Times for {num_warehouses} warehouses delivery')
    plt.xlabel('Travel Time (minutes)')
    plt.ylabel('Frequency')
    plt.axvline(x=30, color='red', linestyle='--', linewidth=2)  # Draw vertical line at 30 minutes
    plt.xticks(bin_edges)  # Set x-axis ticks to bin edges

    plt.tight_layout()  # Adjust layout to prevent label overlap
    st.pyplot(plt)  # Display the plot in Streamlit
def main():
    # Load the Excel file
    # Load the Excel file



    excel_file_path5 = 'warehouse_data_5_clusters.xlsx'
    excel_file_path3 = 'warehouse_data_3_clusters.xlsx'
    excel_file_path2 = 'warehouse_data_2_clusters.xlsx'
    df5 = pd.read_excel(excel_file_path5, sheet_name='warehouse')
    df3 = pd.read_excel(excel_file_path3, sheet_name='warehouse')
    df2 = pd.read_excel(excel_file_path2, sheet_name='warehouse')

    # Load POS data for travel time 5
    pos_data_path = 'Consol_pos_info.xlsx'
    df_pos = pd.read_excel(pos_data_path, sheet_name='POS')
    

    st.title("Microwarehouse Generator")
    
    # Section 1: Description
    st.header("Description")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    
    # Section 2: Delivery Time Selection
    st.header("Select Delivery Time")
    delivery_time = st.selectbox("Select delivery time", ["SELECT TIME OPTION", "30 min", "45 min", "60 min"])
    # Determine the optimal number of warehouses based on the selected time interval
    if delivery_time == "30 min":
        num_warehouses = 5
        st.write("The optimal number of warehouses is:", num_warehouses)
        st.table(df5) 
        st.link_button("Open Your Map", "map5.html")
        
        st.markdown(
            """
            <style>
                button[title^=Exit]+div [data-testid=stImage]{
                    text-align: center;
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 100%;
                }
            </style>
            """, unsafe_allow_html=True
        )

        st.image("plt5.png")
        display_summary_statistics5()



    elif delivery_time == "45 min":
        num_warehouses = 3
        st.write("The optimal number of warehouses is:", num_warehouses)
        st.table(df3)
        st.link_button("Open Your Map", "map 3.html")
        st.markdown(
            """
            <style>
                button[title^=Exit]+div [data-testid=stImage]{
                    text-align: center;
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 100%;
                }
            </style>
            """, unsafe_allow_html=True
        )

        st.image("plt3.png")
        display_summary_statistics3()
        pass
    elif delivery_time == "60 min":
        num_warehouses = 2
        st.write("The optimal number of warehouses is:", num_warehouses)
        st.table(df2)
        st.link_button("Open Your Map", "map 2.html")
        st.markdown(
            """
            <style>
                button[title^=Exit]+div [data-testid=stImage]{
                    text-align: center;
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 100%;
                }
            </style>
            """, unsafe_allow_html=True
        )

        st.image("plt2.png")

        display_summary_statistics2()
        pass




if __name__ == "__main__":
    main()







#     Summary Statistics and Percentages for Travel Time: 2 WH
# ---------------------------------------------------
# Mean Travel Time: 19.45 minutes
# Mode Travel Time: 15.00 minutes
# Max Travel Time: 57.00 minutes
# Total Data Points: 2016
# Percentage of Data Less Than 5 minutes: 1.64%
# Percentage of Data Less Than 10 minutes: 11.76%
# Percentage of Data Less Than 15 minutes: 28.97%
# Percentage of Data Less Than 20 minutes: 54.12%
# Percentage of Data Less Than 30 minutes: 89.38%
# Percentage of Data Less Than 45 minutes: 98.56%
# Percentage of Data Less Than 60 minutes: 100.00%
    

# Summary Statistics and Percentages for Travel Time:  5WH
# ---------------------------------------------------
# Mean Travel Time: 19.45 minutes
# Mode Travel Time: 15.00 minutes
# Max Travel Time: 57.00 minutes
# Total Data Points: 2016
# Percentage of Data Less Than 5 minutes: 1.64%
# Percentage of Data Less Than 10 minutes: 11.76%
# Percentage of Data Less Than 15 minutes: 28.97%
# Percentage of Data Less Than 20 minutes: 54.12%
# Percentage of Data Less Than 30 minutes: 89.38%
# Percentage of Data Less Than 45 minutes: 98.56%
# Percentage of Data Less Than 60 minutes: 100.00%
    

#     Summary Statistics and Percentages for Travel Time:  3WH
# ---------------------------------------------------
# Mean Travel Time: 18.42 minutes
# Mode Travel Time: 19.00 minutes
# Max Travel Time: 58.00 minutes
# Total Data Points: 2016
# Percentage of Data Less Than 5 minutes: 1.64%
# Percentage of Data Less Than 10 minutes: 9.38%
# Percentage of Data Less Than 15 minutes: 28.82%
# Percentage of Data Less Than 20 minutes: 58.23%
# Percentage of Data Less Than 30 minutes: 94.44%
# Percentage of Data Less Than 45 minutes: 99.60%
# Percentage of Data Less Than 60 minutes: 100.00%
