import pandas as pd
import plotly.express as px

# Read data from Excel sheet
df = pd.read_excel("data.xlsx")

# Create Gantt chart
fig = px.timeline(df, x_start="StartDate", x_end="EndDate", y="Task", color="Status")

# Customize the layout
fig.update_layout(xaxis_title="Timeline", yaxis_title="Tasks", xaxis_nticks=20)

# Tilt the x-axis labels
fig.update_xaxes(tickangle=45)

# Show the plot
fig.show()
