import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
import time

st.set_page_config(
    page_title="Dias - Dai Thuan Warehouse Location Optimisation",
    page_icon="🧊",

    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/svenroering/',
        'Report a bug': "https://www.linkedin.com/in/svenroering/",
        'About': "https://www.linkedin.com/in/svenroering/"
    }
)

# Function to create a download link
def create_download_link(file_path, button_text="Download File"):
    with open(file_path, "rb") as file:
        contents = file.read()
        encoded_file = base64.b64encode(contents).decode()
        href = f'<a href="data:file/html;base64,{encoded_file}" download="{file_path}">{button_text}</a>'
    return href

st.markdown('<img src="https://raw.githubusercontent.com/TheCircleGuy/daithuan/master/banner.jpg" style="width:100%;" />', unsafe_allow_html=True)
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
    - Mean Travel Time: 18.42 minutes
    - Mode Travel Time: 19.00 minutes
    - Max Travel Time: 58.00 minutes
    - Total Data Points: 2016
    - Percentage of Data Less Than 5 minutes: 1.64%
    - Percentage of Data Less Than 10 minutes: 9.38%
    - Percentage of Data Less Than 15 minutes: 28.82%
    - Percentage of Data Less Than 20 minutes: 58.23%
    - Percentage of Data Less Than 30 minutes: 94.44%
    - Percentage of Data Less Than 45 minutes: 99.60%
    - Percentage of Data Less Than 60 minutes: 100.00%
    """
    st.markdown(summary_text)

def display_summary_statistics5():
    summary_text = """
    # Summary Statistics and Percentages for Travel Time: 
     ---------------------------------------------------
    - Mean Travel Time: 15.04 minutes
    - Mode Travel Time: 13.00 minutes
    - Max Travel Time: 58.00 minutes
    - Total Data Points: 2016
    - Percentage of Data Less Than 5 minutes: 3.08%
    - Percentage of Data Less Than 10 minutes: 19.00%
    - Percentage of Data Less Than 15 minutes: 48.51%
    - Percentage of Data Less Than 20 minutes: 78.52%
    - Percentage of Data Less Than 30 minutes: 98.07%
    - Percentage of Data Less Than 45 minutes: 99.95%
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



    excel_file_path5 = 'warehouse_5.csv'
    excel_file_path3 = 'warehouse_3.csv'
    excel_file_path2 = 'warehouse_2.csv'
    df5 = pd.read_csv(excel_file_path5)
    df3 = pd.read_csv(excel_file_path3)
    df2 = pd.read_csv(excel_file_path2)

  
    

    st.title("Microwarehouse Location Generator")
    
    

    # Section 1: Description
    st.header("Description")
    st.write("The objective of this tool is to optimize the microwarehouse network for Dai Thuan. The optimal network is determined by minimizing warehouse and transportation costs, achieved through the strategic determination of the most effective number of warehouse locations to meet the required delivery time.")
    st.write("The equation for optimizing Micro Warehouse locations can be described as the equation below: ")
    st.latex(r'''
            \text{Optimal cold chain} = \min(\text{warehouse cost}) + \min(\text{transport cost of DC \& POS})
            ''')
    st.write("For the minimized warehouse cost:")
    st.write("- Ensure the right number of warehouses, avoiding excess or shortages.")
    st.write("- Ensure each warehouse is sized appropriately to accommodate all point-of-sale (POS) demand and hold enough inventory to minimize trips from the distribution center (i.e. enough to hold one month's worth of inventory).")
    
    st.write("For the minimized transport cost:")
    st.write("- Minimize the time it takes for deliveries from the main warehouse (MW) to the point of sale (POS).")
    st.write("- Ensure the right number of trucks and bikes are used for transportation.")



    st.markdown("Point of Sales (POS) addresses are used as inputs to the generator which combines the [Google Maps API](https://developers.google.com/maps) (to fetch the road distance and travel times between POS and warehouses) and [K-Means clustering algorithm](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) (to identify clusters of POS) using the Python programming language.")
    
    

    # Section 2: Delivery Time Selection
    st.header("Select Delivery Time")
    delivery_time = st.selectbox("Select delivery time", ["SELECT TIME OPTION", "30 min", "45 min", "60 min"])
    # Determine the optimal number of warehouses based on the selected time interval
    if delivery_time == "30 min":

        with st.spinner('Optimizing the warehouse locations'):
            time.sleep(5)
            st.success('Done!')

        num_warehouses = 5
        
        st.write("The optimal number of warehouses is:", num_warehouses)
        st.table(df5) 

        
        file_path = "map 5.html"
        # Create a download button
        download_button = st.button("Download Map 5.html")

        # Display the download link when the button is clicked
        if download_button:
            st.markdown(create_download_link(file_path), unsafe_allow_html=True)
        
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

        # file_path = "map 5.html"
        # Create a download button
        # download_button = st.button("Download Map 5.html")
        
        st.image("https://raw.githubusercontent.com/TheCircleGuy/daithuan/master/plt5.png")  
        display_summary_statistics5()



    elif delivery_time == "45 min":

        with st.spinner('Optimizing the warehouse locations'):
            time.sleep(5)
            st.success('Done!')

        
        num_warehouses = 3
        st.write("The optimal number of warehouses is:", num_warehouses)
        st.table(df3)
        # st.link_button("Open Your Map", "map 3.html")


        file_path = "map 3.html"
        # Create a download button
        download_button = st.button("Download Map 3.html")

        # Display the download link when the button is clicked
        if download_button:
            st.markdown(create_download_link(file_path), unsafe_allow_html=True)
  
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

       

        st.image("https://raw.githubusercontent.com/TheCircleGuy/daithuan/master/plt3.png")  
        display_summary_statistics3()
        pass
    elif delivery_time == "60 min":

        with st.spinner('Optimizing the warehouse locations'):
            time.sleep(5)
            st.success('Done!')

        
        num_warehouses = 2
        st.write("The optimal number of warehouses is:", num_warehouses)
        st.table(df2)
        # st.link_button("Open Your Map", "map 2.html")

        file_path = "map 2.html"
        # Create a download button
        download_button = st.button("Download Map 2.html")

        # Display the download link when the button is clicked
        if download_button:
            st.markdown(create_download_link(file_path), unsafe_allow_html=True)
        
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


      

        st.image("https://raw.githubusercontent.com/TheCircleGuy/daithuan/master/plt2.png")

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

html_string = "<html>
<head>

<title>Google Maps - gmplot</title>
<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?libraries=visualization&key=AIzaSyB03oDbAvpWOEdmOiYJ_R6GA3pVH7dy1E0"></script>
<script type="text/javascript">
    function initialize() {
        var map = new google.maps.Map(document.getElementById("map_canvas"), {
            zoom: 10,
            center: new google.maps.LatLng(10.792756, 106.683079)
        });

        var marker_icon_0000FF = {
            url: "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAiCAYAAACwaJKDAAAABmJLR0QA/wD/AP+gvaeTAAAB/UlEQVRIia3VMWsUQRgG4GcvJCqopZhITgs7EcVCLMTKwkJTqoj4C4ToT1AbRZSIjWCrRbCL2JigRlJFDCiIpBCSwogYRFGjiXKfxewSOS93l9t7Ydhjdr7n5nZn5jLNsweHsQMV1PAeU3jTova/HMU0gmpwPDibX6uR+k3n41omw1WyGqeDmaAWRF2biXQ/q6XxsmbgCFuChw2gRm0s0ngja8HDbAym2gSLNhWpznA9OIAf3FgnWLSbkeoN/IteYWew0iG6EuyK5KRlAkOcQ287L7NBeqV6Q0VPD5aZ6HCWRZuI5Oip5F/TR7XDWRapSo7eympnlERX6ytYSW2+JDqvsIr9/JbJkuik5KgVPZcZDJZLLKnBSM5q+vGNax2i1yPV66+f/3n6gmfrBCeDDZHqG+dWOiBetAm+DLZGqls7Ge4zECy0ABeL5ziqydFXZBNecywan6VFOxWYxeZWYJH9+M29NcDxkFb7kXbBIrfTz/tVB9aCg4EH6wVhG5a4W4c+CWmB7+0EhTvsq0NPBiY6BeEAglc5+CXyv44zZVCY5VKOjgaWtHjjlWY38zxiPP/4GJ7ie6lp4kTahsvB7sDFsiBsR34mZIFD3UDhExcCf6Qd1zTtPFOY4znpeP/ZLXSRdwXaMu2in/lKOoi7hn7MrwvdRD/k17l2Bv8FssfECaMr+zoAAAAASUVORK5CYII=",
            labelOrigin: new google.maps.Point(10, 11)
        };

        new google.maps.Marker({
            position: new google.maps.LatLng(10.762394, 106.702165),
            icon: marker_icon_0000FF,
            map: map
        });

        new google.maps.Marker({
            position: new google.maps.LatLng(10.759086, 106.633869),
            icon: marker_icon_0000FF,
            map: map
        });

        new google.maps.Marker({
            position: new google.maps.LatLng(10.825544, 106.762138),
            icon: marker_icon_0000FF,
            map: map
        });

        new google.maps.Marker({
            position: new google.maps.LatLng(10.837152, 106.646195),
            icon: marker_icon_0000FF,
            map: map
        });

        new google.maps.Marker({
            position: new google.maps.LatLng(10.969655, 106.528510),
            icon: marker_icon_0000FF,
            map: map
        });

        var marker_icon_008000 = {
            url: "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAiCAYAAACwaJKDAAAABmJLR0QA/wD/AP+gvaeTAAACSElEQVRIia3VO2gUURTG8d/uGiUBSRALH0XAF8EQLQQfGLuAYGFpI1ppkcpCEOxEC8FGsIlYCGonNgoWATUgiiaKGJMQjUayiIkvjMFowrrJWMysruvsI5v9muGee77/zL1zzr0JpdWKdqxFEvN4jwcYKuP9Tx3oQ6BRYJPAlujZKEAQzXfEmRMx47MSTmiVsBurYrIm8BBDAoFzOBm9CKQKgOctc9wBCXuwPAYoim/GagmvtZvThO446DFLnHII6+IWFaOVaMaAneZNojf3dbAGr+3VYFeFwHw9Qref2IjxZBTu1KTB9iqAsB1NGtBJWCaw31b/bsZClMLWiBNBU2jRXCUwp9DfglQSdViqcZHQ0L8UdcnSmdUpiQwyvi2SFPozyOT6eVh6kdDQP4z53PJv6cdclcA59Eccf0uqy5Rpj6uE9mLKNLr4W5nT+C5tn2Y0LQCYxk3MO457+VDoE1hh2A7rhYdGOU3gGn65gNO5cGEPdZuz0Yg2bVhWAvgTV/DDdRzJn4o72OrRa4M2B4tkwA0MGsE24fb9UVzxz+CwN7IGigDfYhAcLQQWg8JzXHQX2YKZAHf/fOv9OHOpNj1jyowXBdExvBfI+zELgX7CVX0F0acIS6fY5pSEwiUf8DEazeIVuFzKVA76DCNeRqNRZM2I2rFaKNw2mgelR8wfXyi0x7jw0BgDd8oZKoE+kcU7TCK8O2uiz3YKhFVbXy650utkLDqE08KOqwn0S7T0iu6HSqFfzYLvtYTmyn+8ltCJ6DlWSfJvIeeYne8ZJ7UAAAAASUVORK5CYII=",
            labelOrigin: new google.maps.Point(10, 11)
        };

        new google.maps.Marker({
            position: new google.maps.LatLng(10.756011693929803, 106.7430666136251),
            icon: marker_icon_008000,
            map: map
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.4123896, 106.9679781),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.4630405, 106.9004472),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.673586, 106.7628707),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6331823, 106.7623761),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6732641, 106.7610858),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7621195, 106.7588704),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6779618, 106.7521571),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7763117, 106.7504402),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6786857, 106.7504381),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6797391, 106.7497752),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6769688, 106.7473992),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7253913, 106.7432788),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7269979, 106.74321),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7228811, 106.7428988),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7228811, 106.7428988),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7217704, 106.7428377),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7216395, 106.7428358),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7299898, 106.7426687),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.5902604, 106.7424806),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.714418, 106.742177),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6892559, 106.741824),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.738621, 106.7416191),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7424251, 106.7407466),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.67846, 106.740692),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7479449, 106.7403622),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.700635, 106.7381879),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7142129, 106.7376942),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.73174, 106.7373315),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7121121, 106.7373087),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6753922, 106.7372051),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7053203, 106.7371987),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7053203, 106.7371987),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7189806, 106.736848),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7363323, 106.7368077),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7363323, 106.7368077),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7363323, 106.7368077),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7830453, 106.7367328),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7432388, 106.7362812),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7493074, 106.7361028),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7158462, 106.7358753),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.780773, 106.7355882),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.780773, 106.7355882),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7316923, 106.7352369),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7292815, 106.7350511),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6414034, 106.7341238),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7167324, 106.7336689),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7140343, 106.73311),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7086731, 106.7330205),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7006989, 106.7329876),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7006989, 106.7329876),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7438059, 106.7329424),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7284221, 106.732685),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7440185, 106.7326323),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7439875, 106.7326284),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7220317, 106.7323788),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7087244, 106.7318383),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7087244, 106.7318383),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7437002, 106.7317433),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7239778, 106.7313883),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7322039, 106.7311925),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6474652, 106.731117),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7001695, 106.730909),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7001695, 106.730909),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7503207, 106.7305359),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7408075, 106.7305244),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7206299, 106.7305107),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7393832, 106.7302824),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7243771, 106.730272),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7176328, 106.7300973),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7421252, 106.7298483),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.704034, 106.7298103),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7223235, 106.7297757),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6731454, 106.7297412),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7228265, 106.7296753),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7435281, 106.7296259),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7207384, 106.7295053),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7453367, 106.7293496),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7835316, 106.7292805),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7321115, 106.7291998),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7081906, 106.729006),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7244595, 106.729004),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7495201, 106.7286372),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7042478, 106.7285837),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7225174, 106.7278284),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7740031, 106.7274062),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.707768, 106.727403),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7236514, 106.7271676),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7205786, 106.727141),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7219266, 106.7265083),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6589009, 106.7264858),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7221958, 106.7257872),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7432093, 106.7256419),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7374411, 106.725445),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7374411, 106.725445),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7374411, 106.725445),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7379001, 106.725273),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7430433, 106.7249575),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7703281, 106.7246937),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7934308, 106.7243981),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7490504, 106.7241363),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7719447, 106.7241273),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7495216, 106.7235012),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7495216, 106.7235012),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7494894, 106.7234441),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.751032, 106.7234205),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7951119, 106.722096),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7937237, 106.7220665),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7720828, 106.7220318),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7947506, 106.7219896),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8020033, 106.7217892),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7955034, 106.721567),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7969443, 106.7214526),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7969443, 106.7214526),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.791388, 106.7212182),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.797232, 106.7211926),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7719353, 106.7210912),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7719353, 106.7210912),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8001986, 106.7210541),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8005701, 106.7209896),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7987119, 106.7206794),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7272316, 106.7204944),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7260656, 106.7204693),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7416217, 106.7201698),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.799628, 106.720034),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7286242, 106.7200175),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7898224, 106.7199395),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7519208, 106.7198006),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7371426, 106.7196631),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7505506, 106.7196611),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7903463, 106.7194792),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7982001, 106.7193809),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7380074, 106.7192795),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7285352, 106.7187468),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8054501, 106.7187016),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7315531, 106.7186329),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.790486, 106.7185866),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7998926, 106.7184884),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7910047, 106.7184597),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7909873, 106.7184276),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7371782, 106.7183982),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7550937, 106.718353),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.787863, 106.7182718),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.787863, 106.7182718),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8035925, 106.7181046),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7938761, 106.7179309),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7938761, 106.7179309),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7474922, 106.7176981),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7979771, 106.7176132),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8007453, 106.7173538),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7311289, 106.7169339),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7411847, 106.7164251),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7323721, 106.7164131),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7957992, 106.7162457),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7732956, 106.7160926),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7732956, 106.7160926),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7393854, 106.7159919),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7510045, 106.7159565),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.747143, 106.7158652),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8011816, 106.7158591),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7430534, 106.7157513),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8054913, 106.7157076),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7464599, 106.715701),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7505873, 106.715655),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8060649, 106.7155338),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7325761, 106.7155283),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.753972, 106.7153901),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.803914, 106.7153382),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.746605, 106.715128),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7490493, 106.71501),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8040318, 106.7148147),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8041612, 106.7148127),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7227394, 106.7148028),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8015626, 106.7145954),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.791828, 106.7145336),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8016954, 106.7145032),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8017151, 106.7144547),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7912427, 106.7144456),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.748247, 106.7141347),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7213783, 106.7140886),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7872152, 106.7139965),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8065571, 106.7135358),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8092908, 106.7134931),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8092908, 106.7134931),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7450735, 106.7134875),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8108938, 106.7133947),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.730078, 106.7133676),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7983296, 106.7133249),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.722559, 106.713313),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7693917, 106.7131947),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7880449, 106.7131852),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8094752, 106.7129198),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.745461, 106.7126655),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8066225, 106.7122673),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7982386, 106.7121883),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.792728, 106.712084),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8119403, 106.7120126),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7930904, 106.7118473),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7278211, 106.7118364),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7941807, 106.7116346),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7983995, 106.711473),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.798227, 106.7112238),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7500662, 106.7111792),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7275169, 106.7109507),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.721922, 106.7108408),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7867421, 106.710601),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.799476, 106.7106006),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7899619, 106.7104665),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7448105, 106.7102633),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7434274, 106.7101485),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.726634, 106.7100792),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7309763, 106.7099922),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.729413, 106.7099022),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.732546, 106.7098848),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7093632, 106.7098336),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7233748, 106.7098252),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7090218, 106.7097785),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7093628, 106.7097624),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7617562, 106.709716),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.755345, 106.709634),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7504056, 106.7096036),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7903684, 106.7095183),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7292247, 106.7094062),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7237227, 106.7091622),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7949921, 106.7091562),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8105831, 106.7091422),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7921168, 106.7091),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8111359, 106.7090019),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7299158, 106.7087275),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7894147, 106.708641),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8160195, 106.708619),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.790461, 106.708529),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7250792, 106.7084554),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7393279, 106.7083737),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7265643, 106.7082587),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7381071, 106.7082299),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7455826, 106.7080782),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.727489, 106.7079039),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7614453, 106.7078809),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7956595, 106.707757),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8105321, 106.7077228),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7618294, 106.707651),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8063025, 106.7074051),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7956188, 106.7073053),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7783352, 106.7072891),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8165919, 106.7071159),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.731216, 106.7070056),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8061706, 106.7069965),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.811207, 106.7068225),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8119665, 106.7067396),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7665822, 106.706723),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.758103, 106.70669),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7296145, 106.7066436),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.738447, 106.706642),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7637905, 106.706614),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8162933, 106.706451),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7324502, 106.7064451),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8169308, 106.7064305),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.793899, 106.7064067),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7808287, 106.7063711),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8003567, 106.7062972),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7320433, 106.7062461),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7988163, 106.7061912),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8145226, 106.706176),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8034494, 106.7061302),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7345314, 106.705904),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7345314, 106.705904),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7999063, 106.70589),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7983337, 106.7058831),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7455301, 106.7058545),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7813164, 106.7058308),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7305992, 106.705825),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7305992, 106.705825),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7305992, 106.705825),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7814616, 106.7057042),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7814485, 106.7056668),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8165839, 106.7056603),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7451297, 106.7056014),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7398409, 106.7055775),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.793115, 106.7055415),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8067551, 106.7053356),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7760999, 106.7053042),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7752135, 106.7050892),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7767438, 106.7050041),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7597977, 106.7048454),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7811155, 106.7048256),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.776704, 106.7047972),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7302037, 106.7047197),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.779393, 106.7046446),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7821207, 106.7045525),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.772836, 106.704515),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7559946, 106.704501),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8111504, 106.7044433),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.779608, 106.704426),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6998842, 106.7043838),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.710998, 106.7042815),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.710998, 106.7042815),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7400293, 106.7042659),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7754271, 106.7042415),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7757706, 106.7042346),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7004781, 106.7041086),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.700533, 106.7041017),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7168092, 106.7039138),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7769958, 106.7039012),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7412095, 106.7038598),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7712162, 106.70385),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7672042, 106.7038333),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7532291, 106.7038139),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7167197, 106.7038033),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7167197, 106.7038033),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.702902, 106.7037818),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.741768, 106.7037612),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7403167, 106.7037156),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7719101, 106.703706),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7943931, 106.7036989),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8197634, 106.7036242),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7404952, 106.7035675),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7203798, 106.7033471),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7666787, 106.7033196),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7916276, 106.7033166),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7108299, 106.7033115),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7298577, 106.7032856),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7298577, 106.7032856),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.809498, 106.703158),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8013, 106.702931),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7697079, 106.7028463),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7750747, 106.7027861),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8108232, 106.7027601),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.762689, 106.7026494),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.802693, 106.7025419),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7894771, 106.70243),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7857849, 106.7024178),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.771577, 106.702389),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7857442, 106.7022879),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7653075, 106.7022376),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7615542, 106.7021673),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.773576, 106.702112),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7774368, 106.7020771),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7169639, 106.7020562),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7410229, 106.702043),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7191302, 106.7020404),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7784074, 106.7020199),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7786477, 106.7019699),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7354777, 106.7019038),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7858249, 106.7017863),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7400941, 106.7015867),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8044783, 106.7015788),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7559375, 106.7014555),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8159309, 106.7013969),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7688408, 106.7013412),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.78591, 106.701127),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7557186, 106.7010399),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7588024, 106.7010336),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7141987, 106.7009815),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.779898, 106.700971),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8188843, 106.7008957),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8188739, 106.7008764),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7200365, 106.7007584),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7421038, 106.7007115),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7200964, 106.7007087),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7137907, 106.700678),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7456079, 106.7006088),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7456079, 106.7006088),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.743171, 106.7006065),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7413084, 106.7005935),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7791736, 106.7005216),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7733616, 106.7005025),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7733616, 106.7005025),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6863092, 106.7003719),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7723449, 106.7003489),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7675598, 106.7003326),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.788795, 106.7001109),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8041042, 106.6999804),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7850875, 106.6999343),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.763127, 106.6997365),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7573705, 106.6997058),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8011796, 106.6996284),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7906401, 106.6995427),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7170229, 106.6995197),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7547966, 106.6994391),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8047008, 106.699425),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7675056, 106.6993821),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.797086, 106.6993803),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8001334, 106.6992993),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7182345, 106.6992815),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7998459, 106.6992663),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7452347, 106.699118),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7452347, 106.699118),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.773874, 106.6990802),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7622894, 106.6990238),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7215438, 106.6989733),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7215438, 106.6989733),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7975919, 106.6989235),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7738757, 106.6989188),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7199546, 106.6988556),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.767972, 106.698611),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7679449, 106.698584),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8034905, 106.6984324),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.754449, 106.698359),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7831967, 106.6980132),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7744663, 106.697789),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7887303, 106.6976981),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7409665, 106.6976655),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7919509, 106.697452),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7608126, 106.6972928),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7516599, 106.6972553),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7726027, 106.6971724),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8133391, 106.6968939),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7796288, 106.696843),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8128275, 106.6968102),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7729112, 106.6967688),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.773993, 106.6967236),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7726132, 106.6966014),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7912866, 106.6962773),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7888, 106.696208),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.766299, 106.696147),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7618331, 106.6959748),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7798794, 106.6957281),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7717079, 106.6956962),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7633589, 106.6956435),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7438381, 106.6955671),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.810797, 106.695563),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8156399, 106.6955155),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7532619, 106.6954429),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7830985, 106.6953682),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8135423, 106.6953315),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8133854, 106.6953271),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.753365, 106.695092),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8064034, 106.6948918),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7670844, 106.6948786),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7725912, 106.6948152),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7679306, 106.6947521),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7580992, 106.694623),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7675851, 106.6944755),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.768898, 106.694372),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7557157, 106.6943258),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7957578, 106.6943143),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7833209, 106.6941437),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7549068, 106.6940829),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7716992, 106.6939227),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7674322, 106.6938112),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7994052, 106.6936991),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7958207, 106.6936757),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7416211, 106.69367),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.801491, 106.693523),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7848998, 106.6933281),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.757322, 106.6932025),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.802559, 106.693197),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.763744, 106.6931626),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7709185, 106.6930185),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7715065, 106.6929142),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7635691, 106.6928632),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7294136, 106.6927826),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7294136, 106.6927826),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7963809, 106.6925429),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8117522, 106.6924947),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7932014, 106.6924486),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7814923, 106.6924141),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7955018, 106.6923872),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7698875, 106.6923006),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7861061, 106.6922644),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.761083, 106.6922355),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.767992, 106.692138),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7904497, 106.6921152),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7649846, 106.6920686),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7707765, 106.6920643),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7549049, 106.6920479),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8104922, 106.6919995),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7649184, 106.6919189),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8047869, 106.69185),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.806993, 106.691802),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.756279, 106.6917678),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7896616, 106.6917382),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7359261, 106.6916886),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7712179, 106.691654),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.764685, 106.691497),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7922442, 106.6914245),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7359226, 106.6913661),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8056578, 106.6911128),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7911807, 106.6910781),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7810481, 106.6908249),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7969464, 106.6907616),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7388985, 106.6906783),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8007824, 106.6906056),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7662658, 106.6905763),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7979533, 106.6904606),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7674363, 106.6904235),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7341497, 106.6903527),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7768105, 106.6903297),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7966085, 106.6902721),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.772105, 106.6902602),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.76163, 106.6902232),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7973371, 106.6899842),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.747528, 106.6898937),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.781727, 106.6898921),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7710678, 106.6898539),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.765549, 106.689781),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.765549, 106.689781),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7326956, 106.6897308),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8067991, 106.6897079),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7838485, 106.689682),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7658364, 106.689633),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7777644, 106.6895553),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8034184, 106.6894021),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7990967, 106.6892897),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.762161, 106.689194),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7984417, 106.6891665),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7308936, 106.6891603),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8094485, 106.6891164),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7693876, 106.6891116),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7332863, 106.6889298),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7880597, 106.6888556),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7999112, 106.6888326),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.748051, 106.688429),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7915293, 106.6880495),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7302409, 106.687899),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7917188, 106.6878628),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7662713, 106.6878114),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7627699, 106.6877358),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.764597, 106.687703),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7613973, 106.6875225),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7646401, 106.6874382),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.658456, 106.687339),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8067442, 106.6872341),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7624917, 106.6870174),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7685464, 106.6868634),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8048686, 106.6868115),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7455339, 106.686784),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7452967, 106.6867704),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7988403, 106.6866182),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.771159, 106.6865409),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7602237, 106.6865255),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7602167, 106.6865195),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.790032, 106.686456),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.745338, 106.6862275),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7990245, 106.6862094),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7665242, 106.6861057),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7899714, 106.6859802),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8055041, 106.6859482),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7896882, 106.6859231),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8058827, 106.6858845),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7880342, 106.6858484),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.792683, 106.6856959),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7491805, 106.6853548),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7734081, 106.6850453),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8016179, 106.6848942),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7874529, 106.6848481),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7731054, 106.6847946),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7431344, 106.6847099),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.746653, 106.684411),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.797511, 106.6842623),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.743807, 106.684),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7187549, 106.6839746),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.800502, 106.6839142),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7694994, 106.6839142),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7669128, 106.6835874),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7456549, 106.6833046),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7564195, 106.6832217),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7689349, 106.6831293),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7572431, 106.6831284),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7729984, 106.6831186),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7675628, 106.6830565),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7614953, 106.6830056),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7691392, 106.6828153),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.802387, 106.6827177),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8007975, 106.6826025),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7850898, 106.6824849),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.766315, 106.6822859),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7935721, 106.6822014),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8041135, 106.6821492),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7824188, 106.6820667),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7700753, 106.6818811),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7538208, 106.6818772),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.796184, 106.68183),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.802913, 106.681773),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7664167, 106.6816928),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7606525, 106.6816874),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7784417, 106.6815919),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7548033, 106.6815201),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.782757, 106.6814279),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7951377, 106.6812552),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7721499, 106.6810253),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.771706, 106.6808522),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7603085, 106.6807216),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7743269, 106.6806737),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7608262, 106.6806679),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7798798, 106.6802682),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7534138, 106.6802515),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7726117, 106.6802094),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.786787, 106.680201),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.777824, 106.6801643),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7502549, 106.68007),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7864214, 106.6800466),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.797166, 106.679995),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7719091, 106.679882),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7924736, 106.6798648),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7681728, 106.6798331),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7943904, 106.679678),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7758108, 106.6795789),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7758108, 106.6795789),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7610735, 106.6794588),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7867379, 106.6794473),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7377354, 106.6789587),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7850295, 106.6787893),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7394725, 106.6786461),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7807289, 106.6786429),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8001401, 106.6785682),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.784957, 106.678549),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.756322, 106.6785311),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.785544, 106.678514),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7795015, 106.6784515),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7627853, 106.6783667),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.787903, 106.6780648),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7885047, 106.6778732),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7932857, 106.6778006),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7427393, 106.677766),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7986086, 106.6777315),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7411078, 106.6777271),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7769944, 106.6776261),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8004206, 106.677563),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7370547, 106.6772659),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.797371, 106.6772087),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7484387, 106.676983),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7825892, 106.6769701),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7359894, 106.6768316),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7945417, 106.6768217),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.788828, 106.6767303),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7915247, 106.6766631),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7702968, 106.6765775),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8010887, 106.6764989),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7394881, 106.6761052),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7697436, 106.6760751),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7890895, 106.6759581),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7550842, 106.6758366),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7500267, 106.6757755),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7690912, 106.6756638),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7480526, 106.6756317),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.774927, 106.6755249),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7396179, 106.6754572),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7484051, 106.6754148),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7893965, 106.6754054),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7617546, 106.675078),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.797601, 106.6748786),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7742527, 106.674772),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7336085, 106.6745353),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.762821, 106.6745251),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7805477, 106.6745129),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7443223, 106.67436),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7630381, 106.6743396),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7965637, 106.6742999),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.747118, 106.6742),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7948466, 106.6741847),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7523711, 106.6740823),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7440656, 106.6739561),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7789065, 106.6739461),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7444201, 106.6738738),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7979884, 106.6737357),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7594404, 106.6736156),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7711384, 106.6733844),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7981974, 106.6729712),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7423992, 106.6729181),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7982406, 106.6726875),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.734587, 106.672492),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7520091, 106.6723769),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7426663, 106.672201),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7758743, 106.6720851),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.792543, 106.672016),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7603462, 106.6719854),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.755477, 106.6719806),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.791658, 106.6716019),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7681189, 106.6715317),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7647624, 106.6715191),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7594768, 106.6714632),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7836666, 106.6712829),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7521121, 106.671272),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7929726, 106.6712591),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7690195, 106.6711486),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.760546, 106.671091),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7643331, 106.6708454),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7714752, 106.670546),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.764376, 106.670077),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7802294, 106.6700746),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7715048, 106.6699473),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7362618, 106.6698666),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7790466, 106.6698622),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7705861, 106.6694828),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7705861, 106.6694828),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7356582, 106.6692973),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7727331, 106.6689561),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7813064, 106.6689419),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7736576, 106.6686812),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7619998, 106.6686317),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7880144, 106.668629),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7562347, 106.668623),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.795148, 106.6684949),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.77828, 106.6683639),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7616421, 106.6683351),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7606038, 106.6680703),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7684763, 106.6680242),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7913979, 106.668017),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.792004, 106.667873),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#88D2F1',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7918452, 106.6676442),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.747724, 106.668004),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.735347, 106.6678805),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7526642, 106.6675036),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7539585, 106.6672757),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7656796, 106.6670712),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7564493, 106.6669637),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7602393, 106.6667691),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7224114, 106.6667242),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7692523, 106.6665791),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7692523, 106.6665791),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7693834, 106.6663318),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.792762, 106.6661123),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7692388, 106.6660626),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.745506, 106.666059),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7815015, 106.6659746),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7550521, 106.6657872),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7584247, 106.6656026),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.776301, 106.6655715),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7427808, 106.6655715),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7784782, 106.6654456),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7630497, 106.6654088),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7858829, 106.6653592),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7731832, 106.6647252),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7864004, 106.6646803),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7537942, 106.6645622),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7822481, 106.6645265),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7822481, 106.6645265),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7531244, 106.6644546),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7754058, 106.6642473),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7748849, 106.6641783),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.75456, 106.6640798),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7821178, 106.663948),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7684857, 106.663829),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.766467, 106.6635565),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7937537, 106.6632691),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7553356, 106.6631957),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7569443, 106.6629303),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7654202, 106.6627545),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7360076, 106.6626698),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7819303, 106.6620605),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7907816, 106.6618695),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7912538, 106.6618123),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7545055, 106.6616084),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7825857, 106.6615414),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7648025, 106.6614932),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7648258, 106.6614873),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7371009, 106.6611429),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.788562, 106.6610981),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7172873, 106.6609486),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.735004, 106.6608045),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.768595, 106.6608038),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7228245, 106.6606769),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7722407, 106.6605708),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7829231, 106.6603062),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7528911, 106.6602835),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7546247, 106.6602073),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7919889, 106.660196),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.65345, 106.6596385),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.751374, 106.659212),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7950489, 106.659133),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7458432, 106.6588796),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7828323, 106.6585073),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7414834, 106.658398),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7452139, 106.6582906),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7505193, 106.6582626),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7947507, 106.6581562),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.741045, 106.658),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7379719, 106.657982),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.772075, 106.6579018),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7787853, 106.6573361),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.759264, 106.6572812),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7536011, 106.6572287),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7722488, 106.657108),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.762939, 106.6570253),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.761126, 106.656915),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7846527, 106.6568358),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7868052, 106.6567744),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7886651, 106.6566132),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7343277, 106.6566106),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7936316, 106.6565779),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7885963, 106.6565096),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7545639, 106.6562754),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7266581, 106.6560188),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7937744, 106.6560134),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7238876, 106.6559507),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7778808, 106.6558082),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7258268, 106.6557099),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7440166, 106.6556345),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7647319, 106.6556001),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7130833, 106.6553811),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7527354, 106.655366),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7529553, 106.6553425),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7160951, 106.6553192),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.759943, 106.6551532),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7370607, 106.6550293),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7443202, 106.6550285),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.763438, 106.654801),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7872215, 106.6547988),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7767827, 106.6547571),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7717795, 106.6546905),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7712835, 106.6546788),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7519196, 106.6545848),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7011288, 106.6542473),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7492195, 106.6542151),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.771122, 106.654113),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7711201, 106.654046),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7655699, 106.6539782),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7040588, 106.653692),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7708611, 106.6535464),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7340502, 106.6534626),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7340502, 106.6534626),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7342516, 106.6533069),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7271943, 106.6531549),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7738738, 106.6531477),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7491908, 106.6530536),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.766162, 106.653002),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.758603, 106.6528998),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7689578, 106.6527842),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7729852, 106.6527445),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7464688, 106.652382),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7612539, 106.6522551),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.782275, 106.6519305),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7779507, 106.6516575),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7959412, 106.6516163),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.724188, 106.6511885),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6696759, 106.6510661),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7557638, 106.6508446),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7123301, 106.6507992),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7522675, 106.6507124),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7755593, 106.6506395),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7714789, 106.6506375),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7669531, 106.6504441),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7375542, 106.6501538),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7629739, 106.650084),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7498566, 106.6499697),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7913259, 106.6499456),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7882253, 106.6497163),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7144145, 106.6497007),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7615803, 106.649328),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7565247, 106.6493138),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7732425, 106.6492212),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7750086, 106.6492008),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7932873, 106.6491751),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7272418, 106.6491016),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.767659, 106.648996),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7483211, 106.6487782),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.759772, 106.648705),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7827837, 106.6485777),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7668178, 106.6485476),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.790303, 106.648422),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.796756, 106.648309),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7606898, 106.6482886),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7334671, 106.6482886),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7851081, 106.6481534),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7031207, 106.6480272),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7888562, 106.6477943),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7908653, 106.6477491),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7927105, 106.6475466),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7797125, 106.6472408),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7837363, 106.6471245),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.79212, 106.647049),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.775829, 106.646931),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7588603, 106.6469223),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7434142, 106.646875),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7764779, 106.6468639),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7449889, 106.6466191),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7627354, 106.6462852),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.771899, 106.6461815),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7497794, 106.64617),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7717406, 106.64582),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7563553, 106.6457979),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7482133, 106.6456058),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7913409, 106.645488),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7845988, 106.6454094),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7123502, 106.6452007),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7866111, 106.6450186),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7752713, 106.6445293),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7638662, 106.6444775),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.774117, 106.644311),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7688097, 106.6443062),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.732813, 106.6441163),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7108126, 106.6440126),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.733451, 106.643965),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7873516, 106.6438985),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7058637, 106.6437291),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6872732, 106.6436576),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7900869, 106.6435502),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.749985, 106.643181),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7702675, 106.64285),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7672444, 106.6428195),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.775533, 106.642798),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7071945, 106.6427911),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7660019, 106.6427647),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6919737, 106.6427286),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.792157, 106.642724),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7623911, 106.642235),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7936622, 106.6422332),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7798811, 106.6421966),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7930211, 106.6421589),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7924135, 106.6421256),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.77905, 106.64206),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7604687, 106.6419237),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.763596, 106.6418318),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.759456, 106.6417224),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7375623, 106.6416608),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7961587, 106.6415864),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7920538, 106.6415526),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.768383, 106.641475),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7321338, 106.6413688),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7956115, 106.6409393),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7860504, 106.6408968),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7521559, 106.6408666),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7852862, 106.640856),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7720439, 106.6406484),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.780008, 106.6405812),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7889356, 106.6400542),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7842342, 106.6397062),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7285679, 106.639652),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7840995, 106.6395566),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7755758, 106.6393705),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7894205, 106.6393604),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.758773, 106.6393314),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7963797, 106.639261),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7416699, 106.639082),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7700494, 106.6389043),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7973099, 106.6382711),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.778132, 106.63806),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7689876, 106.6379839),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7455953, 106.6378192),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7463022, 106.6377599),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7463953, 106.6376819),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7816541, 106.63765),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7638014, 106.637567),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7512969, 106.6374729),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7902698, 106.6374623),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7509281, 106.6373967),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.718523, 106.6369212),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7963841, 106.6368951),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7963841, 106.6368951),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7483077, 106.6368172),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.756211, 106.636454),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7928237, 106.6363944),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7956828, 106.6357964),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7744693, 106.6357741),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.796411, 106.6354819),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7232086, 106.6353941),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7503949, 106.6352224),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7729649, 106.6350941),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7754505, 106.6347717),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7752803, 106.6347717),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7458847, 106.6347257),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7766602, 106.6345357),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7941358, 106.6344744),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7533851, 106.6344496),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.792153, 106.6342534),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7872809, 106.6341845),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7723129, 106.6340119),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7755445, 106.6337604),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7907559, 106.633678),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7878518, 106.633566),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7552893, 106.633505),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7728236, 106.6327312),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7757358, 106.6324806),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7566396, 106.6324656),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7385624, 106.6324247),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7363139, 106.6322043),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.792277, 106.631953),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7502237, 106.6318057),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7369206, 106.6317119),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.78777, 106.631688),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7642753, 106.6316199),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7521546, 106.6315003),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7963406, 106.6312835),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7963479, 106.6312698),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7796692, 106.6312038),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7988716, 106.6310466),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7906769, 106.6309619),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7448077, 106.6308918),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7179938, 106.6306093),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.776958, 106.6301135),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7670654, 106.6300416),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.777035, 106.629883),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7584663, 106.6296715),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7880447, 106.6291879),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.776323, 106.629122),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7594766, 106.6290387),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7715859, 106.629008),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7621937, 106.6289637),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7726157, 106.6286365),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7240878, 106.6286259),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7516105, 106.6284095),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7212469, 106.6283839),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7900517, 106.6281901),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7879371, 106.6281427),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.771561, 106.6278946),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7895225, 106.6276782),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7863307, 106.6276567),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.753272, 106.6274149),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7390094, 106.6273983),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7595119, 106.6272083),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7949631, 106.6272077),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7366926, 106.6270239),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7776096, 106.6270235),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7699958, 106.6269248),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7726345, 106.6267325),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7730955, 106.6266697),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7730955, 106.6266697),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7950329, 106.6266536),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7785696, 106.6262954),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7457193, 106.6261883),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.716563, 106.6259555),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7721517, 106.625893),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7668899, 106.6256075),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.73874, 106.625503),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7800111, 106.6254894),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7597745, 106.6254002),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7597467, 106.6253929),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7467247, 106.6253412),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.73629, 106.6250548),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7723004, 106.624992),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7881722, 106.6249282),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7959705, 106.6248552),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7294539, 106.6248432),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7294539, 106.6248432),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7790501, 106.6248131),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7881609, 106.624727),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7843984, 106.6243673),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7283572, 106.6242967),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.730849, 106.6238921),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.730849, 106.6238921),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7088169, 106.6238723),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7398728, 106.6237148),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7563623, 106.6236851),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7436684, 106.6235915),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7292212, 106.6234267),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7292212, 106.6234267),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.786897, 106.6233557),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7476691, 106.6233532),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.786438, 106.6232356),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.706411, 106.6231668),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7179654, 106.6227637),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7060625, 106.6227183),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7691519, 106.6223659),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7905564, 106.6223367),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7604267, 106.6218429),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7902772, 106.621083),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7299325, 106.6209449),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7326645, 106.6208599),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7674151, 106.6206347),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.791753, 106.6205773),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7033003, 106.6205351),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7033003, 106.6205351),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7795138, 106.6203918),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7255903, 106.6202733),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7890618, 106.6201968),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7519339, 106.6201888),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7482673, 106.620139),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7211882, 106.6199651),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7235721, 106.6197777),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7802364, 106.6193852),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7535562, 106.6190122),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7513609, 106.6186079),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7443622, 106.6182141),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7406234, 106.6181474),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8013384, 106.6179585),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7485726, 106.6173724),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.789377, 106.6171358),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.771439, 106.6171343),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.71976, 106.6169962),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7485905, 106.6166187),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7985708, 106.6165472),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7801681, 106.6164551),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7484536, 106.6163938),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7321797, 106.6158724),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7620511, 106.6158569),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7676279, 106.6154232),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7731759, 106.6143537),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7731759, 106.6143537),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7535098, 106.613991),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7578254, 106.6139442),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7374519, 106.6135195),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7624277, 106.6134773),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7631743, 106.6132147),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7267987, 106.613131),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7517218, 106.6129839),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7535001, 106.6129439),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7564129, 106.6125739),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7427958, 106.6119311),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7427958, 106.6119311),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7427497, 106.6119309),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7427497, 106.6119309),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7603693, 106.61162),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7131441, 106.6112178),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7131441, 106.6112178),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7131441, 106.6112178),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7309484, 106.6111219),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7762823, 106.6103613),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7623433, 106.610153),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7683163, 106.6099048),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7011398, 106.6094447),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.693729, 106.6093564),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7722132, 106.6093399),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.776155, 106.6092574),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7410973, 106.6092539),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7747207, 106.6091837),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7726136, 106.6091395),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7272953, 106.6091062),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7256684, 106.6089408),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.792291, 106.608851),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6606913, 106.6087898),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6880126, 106.6085003),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7550738, 106.6078239),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7177051, 106.6068546),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6818876, 106.606528),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7760736, 106.6057555),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8033545, 106.6050563),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7660228, 106.605045),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7761878, 106.604773),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7881497, 106.6045536),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7879528, 106.6045528),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7955162, 106.6043802),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.5124204, 106.6041108),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7536326, 106.6040852),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7648115, 106.6040554),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7652581, 106.6038535),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7659708, 106.6037952),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7804923, 106.6036304),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7831629, 106.6035752),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7736229, 106.6031157),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.788574, 106.602568),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7515018, 106.601597),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7650898, 106.6013632),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7388148, 106.6005765),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7595741, 106.6003051),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.722604, 106.599961),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7510413, 106.5986995),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7593839, 106.5983242),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7520254, 106.5963652),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7273631, 106.5963181),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7795958, 106.5955566),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7981523, 106.5955222),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6966328, 106.5949526),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7133866, 106.5949086),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8045647, 106.5936751),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7895236, 106.5935193),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6761375, 106.5917006),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7900875, 106.5914914),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7629267, 106.5910092),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6581454, 106.5907105),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7708962, 106.589737),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6805392, 106.587968),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7993536, 106.5879298),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8014777, 106.5879282),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.801599, 106.5871586),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7558072, 106.5866384),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7539857, 106.5840017),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7539857, 106.5840017),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7861735, 106.5820019),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.663848, 106.5773104),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7959288, 106.576431),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7592705, 106.576402),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7091197, 106.5761318),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6623657, 106.5734283),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6631877, 106.5720112),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.6633793, 106.571115),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7604576, 106.5695589),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8066519, 106.5681831),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7703429, 106.5658278),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7883633, 106.5532511),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.744532, 106.5507001),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#05320B',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.744532, 106.5507001),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8120286, 106.8600377),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8355943, 106.8490493),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8466018, 106.8396174),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8440123, 106.8393641),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8440123, 106.8393641),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8440123, 106.8393641),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8440148, 106.8391068),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8442132, 106.8379446),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8377387, 106.8377076),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8428625, 106.8372031),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8428625, 106.8372031),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8455828, 106.8367896),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8477074, 106.8367198),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8477074, 106.8367198),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8477074, 106.8367198),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8477074, 106.8367198),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8600373, 106.8366319),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.837219, 106.8315365),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8303278, 106.8300637),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.837335, 106.828289),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8421138, 106.8279999),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8419848, 106.827595),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8419848, 106.827595),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8412713, 106.8254198),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8421949, 106.8237374),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8085077, 106.8235047),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8085077, 106.8235047),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8079076, 106.8227359),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8062156, 106.8211601),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8061905, 106.8205801),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.805893, 106.8188998),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8263507, 106.8187134),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8058726, 106.8183116),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8260324, 106.8173653),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8693057, 106.8141735),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.825702, 106.8139431),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8262875, 106.8110129),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8008469, 106.8106534),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8638209, 106.8105757),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8546039, 106.8093687),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7993783, 106.809242),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7987836, 106.8090483),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8407049, 106.808937),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8673783, 106.8081944),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8247051, 106.8075943),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7873391, 106.8009157),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7890603, 106.8001396),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8703158, 106.7995405),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7915753, 106.7994598),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8473167, 106.7990425),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8478339, 106.7985945),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8409809, 106.797681),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8054234, 106.7966745),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7910818, 106.7962338),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8395354, 106.7957809),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8537319, 106.7952124),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8016022, 106.7942758),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8016022, 106.7942758),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8016022, 106.7942758),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8479138, 106.7936527),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7800507, 106.7931027),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7684818, 106.7927943),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8712764, 106.7917617),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8037425, 106.7911758),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8413831, 106.7910402),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8476026, 106.7907035),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7909506, 106.7902984),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8479796, 106.7895941),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8070586, 106.7891827),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8442429, 106.7891366),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.800823, 106.7888565),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8442913, 106.7887734),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8602653, 106.7878004),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8487645, 106.7875024),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8626948, 106.7874294),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8478278, 106.7871657),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8474088, 106.7871204),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8472578, 106.787078),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7701664, 106.7868143),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7969741, 106.7851185),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8131639, 106.7849956),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.767454, 106.784935),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8124813, 106.784724),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.841555, 106.784614),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8069728, 106.784554),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7952934, 106.7845026),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8339838, 106.7828569),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8491535, 106.7819705),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7914371, 106.7816484),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8274569, 106.7815787),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7927035, 106.7814944),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7648767, 106.7813084),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7903162, 106.7812851),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.790129, 106.7804009),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7901661, 106.7803885),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8392975, 106.7801316),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8255513, 106.7799774),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.86065, 106.77899),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8449727, 106.7786146),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8462177, 106.7785435),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8610082, 106.7783728),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8073691, 106.7778582),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.788544, 106.7776242),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8151155, 106.777512),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8191348, 106.7774001),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8186447, 106.7771664),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7917499, 106.776959),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8149525, 106.7769575),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8683347, 106.7766202),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.812367, 106.7760604),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8313742, 106.7756928),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8291193, 106.7751157),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.815568, 106.7749199),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8288768, 106.7748577),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8480181, 106.7742073),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8323414, 106.7740367),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8575045, 106.7739867),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.788353, 106.7737399),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.880166, 106.773694),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8447706, 106.773619),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.823572, 106.773505),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8518047, 106.7723024),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8213824, 106.7720031),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8813421, 106.7717315),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8436934, 106.7716645),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.849472, 106.771663),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8437604, 106.7716366),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.849466, 106.7715905),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7886515, 106.7712794),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.77148, 106.7710951),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8538968, 106.7710079),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8417162, 106.7708428),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7904484, 106.7705377),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7904484, 106.7705377),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8272944, 106.7704011),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8232131, 106.7702276),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8462851, 106.7701469),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8844188, 106.7698028),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7839148, 106.769204),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.855388, 106.7688235),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7896709, 106.76853),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8473848, 106.768457),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8545922, 106.768346),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7838778, 106.7680077),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7888635, 106.767928),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8313327, 106.7678755),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8807742, 106.7677445),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7772447, 106.7674644),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7773967, 106.7673925),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8528475, 106.7673852),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7695433, 106.7669018),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8519545, 106.7666249),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8581185, 106.7665816),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.776221, 106.7665743),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8265801, 106.7662566),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7867328, 106.7661052),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7878947, 106.7655539),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7770734, 106.765312),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.78451, 106.7652314),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8464204, 106.7651392),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8019128, 106.7647475),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7877669, 106.7645978),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8568892, 106.7642486),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8370085, 106.7640933),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8795208, 106.7639411),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.826244, 106.7638835),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.842321, 106.7635729),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8372172, 106.7634109),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8365165, 106.7633882),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8261544, 106.7633037),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8397068, 106.7630805),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7799809, 106.7627898),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8581867, 106.7625127),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7780395, 106.7624551),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8196058, 106.7624372),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7741304, 106.7622869),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7745132, 106.7621459),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8342017, 106.7621256),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.865228, 106.7619918),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7834024, 106.7618801),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8338793, 106.7617638),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7877626, 106.7610991),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8602976, 106.7606268),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8339456, 106.7604506),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7844627, 106.7603239),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8597888, 106.7602489),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8518964, 106.7600827),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8532325, 106.7599438),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7880365, 106.7598769),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.780883, 106.7598746),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8505009, 106.7597388),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8479738, 106.7595982),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8632695, 106.7595695),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8652841, 106.7590447),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7879404, 106.758821),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7828438, 106.7586518),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.822556, 106.7581423),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8514325, 106.7580641),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8172712, 106.7579071),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8471749, 106.7578933),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7838674, 106.7578242),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8603309, 106.7574555),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7877154, 106.7566952),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8118486, 106.7566722),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7769957, 106.7565283),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7769957, 106.7565283),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.860642, 106.7560949),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8369882, 106.755925),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.832358, 106.7559004),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8363086, 106.755647),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.849241, 106.7555663),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.849241, 106.7555663),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7902396, 106.7552386),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7771512, 106.755165),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8083844, 106.7548752),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7900837, 106.7542672),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7904944, 106.7539421),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8494094, 106.7537055),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8560516, 106.7535475),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8625442, 106.7535447),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8505483, 106.7532331),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7906183, 106.7521082),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8476723, 106.7518225),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8052193, 106.7516806),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8054731, 106.7516501),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7766821, 106.7515555),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7984162, 106.7512452),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7984162, 106.7512452),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7993494, 106.7506694),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8385494, 106.7506681),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7971282, 106.7503393),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8000781, 106.7494956),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8018536, 106.7493055),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8018536, 106.7493055),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8018536, 106.7493055),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8018536, 106.7493055),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8582119, 106.7491653),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8016322, 106.7491511),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8018608, 106.748619),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8018828, 106.7485813),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7851524, 106.7484688),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8515643, 106.7479941),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.859617, 106.7477576),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8506727, 106.7476746),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8756622, 106.7476296),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8564142, 106.7474212),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8006157, 106.7473231),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8759076, 106.747305),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.86139, 106.7471354),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8696571, 106.7470882),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8041163, 106.7470677),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8057914, 106.7468102),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7845658, 106.7466792),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7843967, 106.7463996),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.858449, 106.7463394),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.863641, 106.745857),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8414035, 106.7455331),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8382, 106.7454678),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.795435, 106.745126),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8674269, 106.7448242),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8425329, 106.7443442),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7993367, 106.7442545),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8048693, 106.743644),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8773765, 106.7435034),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7978109, 106.7428752),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.798496, 106.7427285),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8034215, 106.7425152),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.870896, 106.7422387),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7998381, 106.7421704),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7902241, 106.741728),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8021184, 106.7409876),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8054138, 106.7408371),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8064516, 106.7408104),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8441125, 106.7407742),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8441125, 106.7407742),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8004335, 106.7400041),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7964949, 106.7396815),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7931669, 106.7393566),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7974198, 106.7393228),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8023923, 106.7392886),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7979215, 106.7391703),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8589834, 106.738723),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7898457, 106.7387009),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7995952, 106.7385357),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8019043, 106.7383414),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8019043, 106.7383414),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8019043, 106.7383414),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8018859, 106.7383383),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8557654, 106.7379538),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8043702, 106.7376773),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7955364, 106.7368756),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7955364, 106.7368756),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7955364, 106.7368756),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8722698, 106.7367525),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8722698, 106.7367525),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7994936, 106.7366176),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8692107, 106.7365702),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.804205, 106.736553),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8048983, 106.7363988),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8688907, 106.7360071),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.794707, 106.7358574),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8051481, 106.7357307),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8035516, 106.7342103),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.793852, 106.7338851),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9523318, 106.7334038),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8721202, 106.733227),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.872354, 106.7330871),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7968609, 106.7330087),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8014082, 106.7329086),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8729461, 106.7328887),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8660188, 106.7328175),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.872013, 106.7324068),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8064331, 106.7323097),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8387088, 106.7322027),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.802194, 106.7321377),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8037904, 106.7320103),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8097949, 106.7319181),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8409543, 106.731474),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8424883, 106.7313427),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.79685, 106.7313),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8066709, 106.731243),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8168381, 106.7311114),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8321824, 106.7309868),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.829795, 106.7302019),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8137589, 106.7300299),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8499691, 106.7298854),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.880219, 106.7298564),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8104033, 106.7293841),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8855534, 106.7288888),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.802927, 106.728841),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8451271, 106.728693),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8135037, 106.7285542),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8129649, 106.7284096),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8307238, 106.7280365),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8033541, 106.7279789),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.865741, 106.727853),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8051096, 106.7273987),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8151737, 106.72738),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8033743, 106.7271792),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.836799, 106.7269912),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8451756, 106.7268617),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8517858, 106.7257413),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8248022, 106.7257247),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8248022, 106.7257247),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8314351, 106.7253045),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8507899, 106.7246502),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8460388, 106.7243541),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8499332, 106.7241561),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8186691, 106.7238541),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8270793, 106.7233171),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8770026, 106.7228351),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8472908, 106.7227044),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8468705, 106.7218284),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8274793, 106.7217033),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8276275, 106.7216355),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8276425, 106.7214707),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8276425, 106.7214707),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8141944, 106.721333),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8276003, 106.7212132),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8276003, 106.7212132),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8892194, 106.7208802),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8892194, 106.7208802),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8603231, 106.7206628),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8603231, 106.7206628),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.813159, 106.7204405),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.816074, 106.7204319),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8062049, 106.7202047),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8161824, 106.7201713),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8233226, 106.7195026),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8388177, 106.7194319),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.816056, 106.719382),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.825859, 106.7190566),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8686196, 106.7190341),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8108271, 106.7190263),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8256397, 106.7184076),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8459593, 106.7183534),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8160571, 106.7179585),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8250338, 106.7160926),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8126903, 106.7160376),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8273107, 106.7159599),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.827461, 106.714838),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.827461, 106.714838),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8294524, 106.7139274),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.843836, 106.7125367),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8375733, 106.7106334),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8223431, 106.7058844),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8291225, 106.7058813),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#80BB09',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8310469, 106.7049654),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8340344, 106.7040318),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8293909, 106.7026584),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.81655, 106.6953968),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8180965, 106.6949722),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8176956, 106.6937269),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8249808, 106.6936215),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8183929, 106.6928352),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.82514, 106.6907544),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8187044, 106.6907283),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8278762, 106.6906982),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8191779, 106.6904603),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8331598, 106.6904103),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8142932, 106.6897472),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8184409, 106.689567),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.822658, 106.689355),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8271138, 106.6892817),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8698087, 106.6892472),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8125202, 106.6891215),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8981871, 106.6888441),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8577365, 106.6887046),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8359801, 106.6884274),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8253383, 106.6883744),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8127927, 106.6880092),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.814663, 106.687483),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8144675, 106.6870259),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8317654, 106.6868315),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8354468, 106.6867624),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8220799, 106.6865985),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.822945, 106.6865409),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.83422, 106.686441),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8282734, 106.6864027),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8321426, 106.6863518),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8257891, 106.685889),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8541399, 106.6858625),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8206148, 106.6857694),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8142896, 106.6857384),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8298572, 106.6856776),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8373238, 106.6855247),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8677503, 106.6852857),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8094173, 106.6846662),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8096094, 106.6842992),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8182201, 106.6841738),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8354795, 106.6841189),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.82394, 106.6838515),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8698751, 106.6832316),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.833343, 106.6823612),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.829894, 106.682245),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8322783, 106.6821738),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.805595, 106.681776),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8134703, 106.6817162),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8847974, 106.6812915),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8604904, 106.6811463),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8437874, 106.6810944),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8627533, 106.6805741),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8786293, 106.6805284),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8268151, 106.6803044),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.830437, 106.6802253),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8492252, 106.6801382),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8258685, 106.680128),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8187692, 106.6801151),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8073687, 106.6799136),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.840244, 106.679762),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8396465, 106.679314),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8331893, 106.6792976),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8526366, 106.6790968),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8684529, 106.6789795),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.804672, 106.6789299),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.829112, 106.67885),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8740729, 106.6788481),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8478061, 106.6787961),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8404253, 106.678608),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8166108, 106.6785669),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8480002, 106.6784195),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8408484, 106.6782151),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8086339, 106.6781527),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8407458, 106.678146),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8684792, 106.6780327),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8329372, 106.6777948),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8700568, 106.6772367),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.85861, 106.677092),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8700843, 106.677007),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8423299, 106.6769393),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8167644, 106.6768759),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8083625, 106.6768618),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8027221, 106.6764667),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8464241, 106.6761308),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8399428, 106.676039),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8401137, 106.676038),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8174288, 106.6759035),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8356608, 106.6756426),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8764437, 106.675593),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8152238, 106.6755203),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8154845, 106.6750855),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8154136, 106.674774),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8387127, 106.6734828),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.867202, 106.6734625),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8147485, 106.672427),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8084733, 106.6717013),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.845626, 106.6714154),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.814472, 106.6711705),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.814472, 106.6711705),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.814472, 106.6711705),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8090454, 106.6710733),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8084798, 106.6710181),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8097795, 106.6706035),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8463688, 106.6705635),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7993008, 106.6704924),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8084579, 106.6702581),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8084371, 106.6700987),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7971891, 106.6699011),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8302557, 106.6698583),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8109053, 106.6695582),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8109053, 106.6695582),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8308757, 106.6695557),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8101359, 106.6693973),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8470456, 106.6693254),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8310994, 106.6692553),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8307752, 106.6691665),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8339292, 106.6686115),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7999525, 106.6685999),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8116589, 106.6684966),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.798285, 106.6684672),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8131207, 106.6683377),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8127327, 106.6680487),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8150325, 106.6680035),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8154021, 106.667808),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8346462, 106.6677709),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8346462, 106.6677709),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8346439, 106.6677707),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.795059, 106.6677327),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8432839, 106.667543),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8102319, 106.667327),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8369335, 106.6671851),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7982751, 106.6671836),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8101054, 106.6670109),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8099191, 106.666723),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8118483, 106.6664697),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8487994, 106.6664028),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8350807, 106.6662332),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8032768, 106.6661583),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8630302, 106.666131),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8052573, 106.6660372),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8052573, 106.6660372),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7959814, 106.665826),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8528959, 106.6655018),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7961873, 106.6654909),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8655833, 106.6651667),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8456003, 106.6649082),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8648762, 106.6647812),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8455373, 106.6646504),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8360169, 106.6646184),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.848198, 106.6645133),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8437297, 106.6643987),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.834998, 106.6643413),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8096767, 106.6641213),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.816143, 106.6640352),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.831946, 106.6637906),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8077224, 106.6631419),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8078482, 106.662405),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.845498, 106.6621488),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8349689, 106.6620909),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8528856, 106.6620766),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.805157, 106.6613932),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8457695, 106.6613499),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8525948, 106.6605466),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8022968, 106.6604245),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.802262, 106.660377),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.836209, 106.6598915),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7977566, 106.6590197),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8516634, 106.6585937),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8006145, 106.6582463),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.847248, 106.6578101),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8451563, 106.6571316),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.847426, 106.657103),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8007966, 106.6564298),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8504871, 106.6563073),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.799435, 106.656257),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.841356, 106.6561411),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8536565, 106.6561017),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8763116, 106.6545385),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8760334, 106.654391),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8609538, 106.6541352),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8009497, 106.6535375),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.852515, 106.653205),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8565483, 106.6530297),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8409104, 106.6530263),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8585922, 106.6524601),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8006325, 106.6524536),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7989777, 106.6523927),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7978838, 106.6522478),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7962692, 106.6521264),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8451296, 106.6516161),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8008832, 106.6511415),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.906045, 106.651098),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8436321, 106.6510683),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8836743, 106.6510289),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8573574, 106.6510133),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8436495, 106.6506806),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8436495, 106.6506806),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8000549, 106.6496471),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.848718, 106.6491591),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8549349, 106.649106),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8657006, 106.648545),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9089878, 106.6480468),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8046692, 106.6478741),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.843882, 106.647664),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.804519, 106.647551),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8027273, 106.6473891),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8056139, 106.6473859),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7975713, 106.6472775),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8889554, 106.6472152),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8910401, 106.6472038),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8910416, 106.6472037),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7977994, 106.6471711),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7992129, 106.647131),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8063683, 106.6466121),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8045816, 106.646594),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8445524, 106.6465935),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8757455, 106.6463403),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.837876, 106.645467),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8355874, 106.6452257),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.80049, 106.6451223),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8049101, 106.6447915),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.800534, 106.6447547),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8464834, 106.644728),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8076421, 106.6447078),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7991022, 106.6443944),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8358137, 106.6443622),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8353581, 106.6442893),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9059392, 106.6442569),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8339795, 106.6440858),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8644019, 106.6436953),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8046709, 106.6427217),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.804306, 106.6426814),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.845236, 106.642364),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8395645, 106.6423245),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8686267, 106.6421006),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8699216, 106.6418716),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8296916, 106.641739),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8770285, 106.6416221),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8008792, 106.64153),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8701769, 106.6410565),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.870373, 106.6410332),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8448127, 106.6408981),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8772253, 106.640463),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8048461, 106.6404526),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8251064, 106.6402783),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9057142, 106.6402405),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8728973, 106.6401989),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8777493, 106.6399527),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8040126, 106.6398009),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8016283, 106.6391027),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8423521, 106.6389878),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8419675, 106.638732),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8296768, 106.6386402),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9053464, 106.6384214),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8530496, 106.6379544),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.901004, 106.6377237),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.840402, 106.6375897),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8638728, 106.6374669),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8986017, 106.6368187),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8306725, 106.6367306),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8499055, 106.6366944),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8445813, 106.6366829),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9042027, 106.6365145),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8487288, 106.6361388),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8521367, 106.6359624),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8199509, 106.6358395),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8199937, 106.635566),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8234106, 106.635497),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.817488, 106.635272),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8304946, 106.6351977),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8342641, 106.6349283),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8064862, 106.6341961),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8282945, 106.6339685),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8188041, 106.6334771),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.825663, 106.6328975),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8190094, 106.6326939),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8731044, 106.6324806),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8225181, 106.6322341),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8865777, 106.631984),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8614377, 106.6318244),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8471145, 106.631664),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8438744, 106.6315077),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8014728, 106.6313178),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8691434, 106.631179),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8557817, 106.6311375),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.818204, 106.6310522),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8032436, 106.6309873),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8582918, 106.6308586),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8258193, 106.6307968),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8637111, 106.6307652),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7997882, 106.630604),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.7997882, 106.630604),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8759661, 106.6297453),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8230989, 106.6296638),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8230989, 106.6296638),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8230989, 106.6296638),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.823577, 106.629578),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8353756, 106.6288979),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8083311, 106.6285731),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8846364, 106.6285632),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.827811, 106.6284626),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8000474, 106.6281724),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8433646, 106.6280597),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8074818, 106.6278985),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.801168, 106.6278169),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.839902, 106.6276114),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.83605, 106.6274496),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8748689, 106.6272145),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9010101, 106.6265285),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8099268, 106.6262061),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8054823, 106.6259413),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8765138, 106.6258301),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8105658, 106.6254233),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8540977, 106.6251469),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8078116, 106.6249517),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8531707, 106.6248136),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8699685, 106.6246488),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.803481, 106.6245689),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8015268, 106.6244508),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8073512, 106.6233527),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8161485, 106.6230053),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8577648, 106.622948),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8130791, 106.622879),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8313748, 106.6223202),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8229352, 106.6222921),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8693564, 106.6220731),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8120418, 106.6217661),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8727747, 106.6216932),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8736494, 106.621506),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8426002, 106.621369),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8135366, 106.6211598),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8345118, 106.6203008),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8720024, 106.6201593),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.828469, 106.619707),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.830116, 106.6187444),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8619867, 106.6185707),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.85966, 106.6172412),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8038306, 106.6171726),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8663763, 106.6158285),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8852, 106.6157989),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8679336, 106.6156377),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8560371, 106.6154766),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8720171, 106.6152022),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8663418, 106.6149585),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.887043, 106.6148319),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8666217, 106.6143254),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8487514, 106.6136768),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.832676, 106.6128058),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8970481, 106.6127477),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8484324, 106.6124823),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8288664, 106.612465),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8029049, 106.6119122),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8976059, 106.6114474),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8314976, 106.6114194),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8269414, 106.6108474),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8673479, 106.6107339),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8322554, 106.610584),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8366271, 106.6102342),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.858821, 106.609685),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8039295, 106.6096025),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8066672, 106.6095627),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.850986, 106.6094241),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8589297, 106.6094032),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8569768, 106.609128),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8100736, 106.6090184),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.846125, 106.608919),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8465613, 106.608858),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8360737, 106.6059396),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.860146, 106.605847),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8199804, 106.6057721),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8202172, 106.605585),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8532494, 106.6055047),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8062116, 106.6053116),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8060783, 106.6051896),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8518957, 106.6046345),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.889362, 106.6044223),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.874043, 106.60406),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8151822, 106.6027849),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8550733, 106.6013795),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8272908, 106.6007876),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.819365, 106.6003156),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8197058, 106.5999243),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8179339, 106.5998207),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8977682, 106.5993762),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8799502, 106.5993289),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8162236, 106.599176),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8088181, 106.59913),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8868317, 106.5986235),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8160179, 106.5981657),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.825627, 106.5980572),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8878573, 106.5979971),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8771603, 106.5970714),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8869473, 106.5961856),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8130138, 106.5958408),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8481633, 106.595481),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.808063, 106.5946753),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8158785, 106.5938399),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8100949, 106.5936828),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8906193, 106.5925457),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8863934, 106.5922924),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8681161, 106.5918004),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8474964, 106.5903816),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8165988, 106.5899566),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8587641, 106.5897237),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8092127, 106.5891315),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8634206, 106.5890064),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8635362, 106.5888992),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8143989, 106.588844),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8504579, 106.5886205),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8843774, 106.5874533),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8895788, 106.5852151),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8889325, 106.5837617),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8170769, 106.5813114),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8784296, 106.5802524),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.813776, 106.579979),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8689013, 106.5798572),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8108766, 106.578687),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.8540974, 106.5742165),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#68A131',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.831876, 106.5668687),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9632494, 106.6427059),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9491072, 106.6047001),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9813106, 106.6038727),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9515983, 106.6030784),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9665789, 106.5911644),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9876013, 106.5857198),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9838472, 106.5784453),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9834932, 106.5754181),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.899419, 106.5749278),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9902003, 106.5739103),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9838016, 106.5736124),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9170024, 106.5622972),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9266034, 106.5563046),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9608808, 106.5273832),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9614709, 106.525606),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9847734, 106.5245617),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9472959, 106.523503),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(11.0890989, 106.5137912),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.961425, 106.5064616),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9643604, 106.5042984),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9634677, 106.5037899),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9602885, 106.5027863),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.97632, 106.5003168),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9764829, 106.5002942),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9694534, 106.4970727),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9814348, 106.4963396),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9803118, 106.4934035),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9674188, 106.488983),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9730227, 106.4886622),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.971171, 106.4872804),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9830763, 106.4840413),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9682018, 106.482668),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(11.0082966, 106.471336),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(11.0053283, 106.4279577),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#6DAB31',
            fillOpacity: 0.3,
            map: map,
            center: new google.maps.LatLng(10.9005341, 106.4211513),
            radius: 100
        });

        new google.maps.Circle({
            strokeColor: '#88D2F1',
            strokeOpacity: 1.0,
            strokeWeight: 2,
            fillColor: '#88D2F1',
            fillOpacity: 0.5,
            map: map,
            center: new google.maps.LatLng(10.76239412460882, 106.70216496244666),
            radius: 0.10298029328030657
        });

        new google.maps.Circle({
            strokeColor: '#05320B',
            strokeOpacity: 1.0,
            strokeWeight: 2,
            fillColor: '#05320B',
            fillOpacity: 0.5,
            map: map,
            center: new google.maps.LatLng(10.759086480210525, 106.63386896021052),
            radius: 0.11830458392499156
        });

        new google.maps.Circle({
            strokeColor: '#80BB09',
            strokeOpacity: 1.0,
            strokeWeight: 2,
            fillColor: '#80BB09',
            fillOpacity: 0.5,
            map: map,
            center: new google.maps.LatLng(10.825544151804124, 106.76213829484536),
            radius: 0.1408708657721183
        });

        new google.maps.Circle({
            strokeColor: '#68A131',
            strokeOpacity: 1.0,
            strokeWeight: 2,
            fillColor: '#68A131',
            fillOpacity: 0.5,
            map: map,
            center: new google.maps.LatLng(10.837152335903614, 106.64619500578313),
            radius: 0.12153795638287145
        });

        new google.maps.Circle({
            strokeColor: '#6DAB31',
            strokeOpacity: 1.0,
            strokeWeight: 2,
            fillColor: '#6DAB31',
            fillOpacity: 0.5,
            map: map,
            center: new google.maps.LatLng(10.969655051428571, 106.52850985714285),
            radius: 0.2815623479670554
        });

    }
</script>
</head>
<body style="margin:0px; padding:0px;" onload="initialize()">
    <div id="map_canvas" style="width: 100%; height: 100%;" />
</body>
</html>
"

st.markdown(html_string, unsafe_allow_html=True)
