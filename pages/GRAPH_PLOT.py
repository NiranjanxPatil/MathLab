import streamlit as st
import numpy as np
import plotly.graph_objects as go
import sympy as sp
from scipy.stats import norm

# Function to generate cartesian graph
def plot_cartesian(equation, x_range):
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    y_vals = [eval(equation, {"x": x, "np": np}) for x in x_vals]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name=equation))
    fig.update_layout(title="Cartesian Graph", xaxis_title="X", yaxis_title="Y", grid=dict(visible=True))
    return fig

# Function to generate polar graph
def plot_polar(equation, theta_range):
    theta_vals = np.linspace(theta_range[0], theta_range[1], 400)
    r_vals = [eval(equation, {"theta": t, "np": np}) for t in theta_vals]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=r_vals, theta=np.degrees(theta_vals), mode='lines', name=equation))
    fig.update_layout(title="Polar Graph")
    return fig

# Function to generate parametric graph
def plot_parametric(x_eq, y_eq, t_range):
    t_vals = np.linspace(t_range[0], t_range[1], 400)
    x_vals = [eval(x_eq, {"t": t, "np": np}) for t in t_vals]
    y_vals = [eval(y_eq, {"t": t, "np": np}) for t in t_vals]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name="Parametric Curve"))
    fig.update_layout(title="Parametric Graph", xaxis_title="X", yaxis_title="Y")
    return fig

# Function to generate 3D graph
def plot_3d(equation, x_range, y_range):
    x_vals = np.linspace(x_range[0], x_range[1], 40)
    y_vals = np.linspace(y_range[0], y_range[1], 40)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = np.array([[eval(equation, {"x": x, "y": y, "np": np}) for x in x_vals] for y in y_vals])
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
    fig.update_layout(title="3D Surface Plot", scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"))
    return fig

# Function to generate line graph
def plot_line(x_vals, y_vals):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name="Line Graph"))
    fig.update_layout(title="Line Graph", xaxis_title="X", yaxis_title="Y")
    return fig

# Function to generate pie chart
def plot_pie(labels, values):
    fig = go.Figure()
    fig.add_trace(go.Pie(labels=labels, values=values))
    fig.update_layout(title="Pie Chart")
    return fig

# Function to generate parabola
def plot_parabola(a, b, c, x_range):
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    y_vals = a * x_vals**2 + b * x_vals + c
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name="Parabola"))
    fig.update_layout(title="Parabola Graph", xaxis_title="X", yaxis_title="Y")
    return fig

# Function to generate double bar graph
def plot_double_bar(categories, values1, values2):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=categories, y=values1, name="Set 1"))
    fig.add_trace(go.Bar(x=categories, y=values2, name="Set 2"))
    fig.update_layout(title="Double Bar Graph", barmode='group')
    return fig

# Function to generate histogram
def plot_histogram(values, bins):
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=values, nbinsx=bins))
    fig.update_layout(title="Histogram", xaxis_title="Value", yaxis_title="Frequency")
    return fig

# Function to generate frequency polygon
def plot_frequency_polygon(values, bins):
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=values, nbinsx=bins, histfunc='count', cumulative_enabled=True, name="Frequency Polygon", line=dict(color='blue')))
    fig.update_layout(title="Frequency Polygon", xaxis_title="Value", yaxis_title="Cumulative Frequency")
    return fig

# Function to generate logarithmic graph
def plot_logarithmic(a, b, x_range):
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    y_vals = a * np.log(b * x_vals)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name="Logarithmic Graph"))
    fig.update_layout(title="Logarithmic Graph", xaxis_title="X", yaxis_title="Y")
    return fig

# Function to generate exponential graph
def plot_exponential(a, b, x_range):
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    y_vals = a * np.exp(b * x_vals)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name="Exponential Graph"))
    fig.update_layout(title="Exponential Graph", xaxis_title="X", yaxis_title="Y")
    return fig

# Function to generate trigonometric graph
def plot_trigonometric(func, x_range):
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    y_vals = func(x_vals)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name=f"{func.__name__} Graph"))
    fig.update_layout(title=f"{func.__name__.capitalize()} Graph", xaxis_title="X", yaxis_title="Y")
    return fig

# Function to generate normal distribution graph (bell curve)
def plot_probability_distribution(mu, sigma, x_range):
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    y_vals = norm.pdf(x_vals, mu, sigma)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name="Normal Distribution"))
    fig.update_layout(title="Probability Distribution (Bell Curve)", xaxis_title="X", yaxis_title="Density")
    return fig

# Streamlit UI
st.image('graphplot.png')

st.title("Advanced Real-Time Graphing App 📈")

graph_type = st.selectbox("Select Graph Type:", [
    "Cartesian", "Polar", "Parametric", "3D Surface", "Line Graph", "Pie Chart", "Parabola", "Double Bar Graph",
    "Histogram", "Frequency Polygon", "Logarithmic", "Exponential", "Trigonometric", "Probability Distribution"
])

if graph_type == "Cartesian":
    equation = st.text_input("Enter a function of x:", "np.sin(x)")
    x_range = st.slider("Select X-axis range:", -10, 10, (-5, 5))
    if st.button("Plot Graph"):
        st.plotly_chart(plot_cartesian(equation, x_range))
elif graph_type == "Polar":
    equation = st.text_input("Enter a function of θ (theta):", "1 + np.sin(theta)")
    theta_range = st.slider("Select θ range (in radians):", 0, 6, (0, 6))
    if st.button("Plot Graph"):
        st.plotly_chart(plot_polar(equation, theta_range))
elif graph_type == "Parametric":
    x_eq = st.text_input("Enter X equation in terms of t:", "np.sin(t)")
    y_eq = st.text_input("Enter Y equation in terms of t:", "np.cos(t)")
    t_range = st.slider("Select t range:", 0, 10, (0, 6))
    if st.button("Plot Graph"):
        st.plotly_chart(plot_parametric(x_eq, y_eq, t_range))
elif graph_type == "3D Surface":
    equation = st.text_input("Enter a function of x and y:", "np.sin(np.sqrt(x**2 + y**2))")
    x_range = st.slider("Select X-axis range:", -10, 10, (-5, 5))
    y_range = st.slider("Select Y-axis range:", -10, 10, (-5, 5))
    if st.button("Plot Graph"):
        st.plotly_chart(plot_3d(equation, x_range, y_range))
elif graph_type == "Line Graph":
    x_vals = st.text_area("Enter X values (comma-separated):", "1,2,3,4,5")
    y_vals = st.text_area("Enter Y values (comma-separated):", "2,3,5,7,11")
    if st.button("Plot Graph"):
        st.plotly_chart(plot_line(list(map(float, x_vals.split(','))), list(map(float, y_vals.split(',')))))
elif graph_type == "Pie Chart":
    labels = st.text_area("Enter Labels (comma-separated):", "A,B,C,D")
    values = st.text_area("Enter Values (comma-separated):", "10,20,30,40")
    if st.button("Plot Graph"):
        st.plotly_chart(plot_pie(labels.split(','), list(map(float, values.split(',')))))
elif graph_type == "Parabola":
    a = st.number_input("Enter coefficient a:", value=1.0)
    b = st.number_input("Enter coefficient b:", value=0.0)
    c = st.number_input("Enter coefficient c:", value=0.0)
    x_range = st.slider("Select X-axis range:", -10, 10, (-5, 5))
    if st.button("Plot Graph"):
        st.plotly_chart(plot_parabola(a, b, c, x_range))
elif graph_type == "Double Bar Graph":
    categories = st.text_area("Enter Categories (comma-separated):", "Category 1, Category 2")
    values1 = st.text_area("Enter Values for Set 1 (comma-separated):", "10,20")
    values2 = st.text_area("Enter Values for Set 2 (comma-separated):", "15,25")
    if st.button("Plot Graph"):
        st.plotly_chart(plot_double_bar(categories.split(','), list(map(float, values1.split(','))), list(map(float, values2.split(',')))))
elif graph_type == "Histogram":
    values = st.text_area("Enter Values (comma-separated):", "10,20,20,30,40,40,40,50,50,50")
    bins = st.slider("Select Number of Bins:", 5, 20, 10)
    if st.button("Plot Graph"):
        st.plotly_chart(plot_histogram(list(map(float, values.split(','))), bins))
elif graph_type == "Frequency Polygon":
    values = st.text_area("Enter Values (comma-separated):", "10,20,20,30,40,40,40,50,50,50")
    bins = st.slider("Select Number of Bins:", 5, 20, 10)
    if st.button("Plot Graph"):
        st.plotly_chart(plot_frequency_polygon(list(map(float, values.split(','))), bins))
elif graph_type == "Logarithmic":
    a = st.number_input("Enter coefficient a:", value=1.0)
    b = st.number_input("Enter coefficient b:", value=1.0)
    x_range = st.slider("Select X-axis range:", 1, 10, (1, 5))
    if st.button("Plot Graph"):
        st.plotly_chart(plot_logarithmic(a, b, x_range))
elif graph_type == "Exponential":
    a = st.number_input("Enter coefficient a:", value=1.0)
    b = st.number_input("Enter coefficient b:", value=1.0)
    x_range = st.slider("Select X-axis range:", 0, 10, (1, 5))
    if st.button("Plot Graph"):
        st.plotly_chart(plot_exponential(a, b, x_range))
elif graph_type == "Trigonometric":
    func = st.selectbox("Select Trigonometric Function:", [np.sin, np.cos, np.tan])
    x_range = st.slider("Select X-axis range:", -10, 10, (-5, 5))
    if st.button("Plot Graph"):
        st.plotly_chart(plot_trigonometric(func, x_range))
elif graph_type == "Probability Distribution":
    mu = st.number_input("Enter mean (μ):", value=0.0)
    sigma = st.number_input("Enter standard deviation (σ):", value=1.0)
    x_range = st.slider("Select X-axis range:", -10, 10, (-5, 5))
    if st.button("Plot Graph"):
        st.plotly_chart(plot_probability_distribution(mu, sigma, x_range))
