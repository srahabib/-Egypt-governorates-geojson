# Create a scatter plot on Mapbox
import pandas as pd
import plotly.express as px

df = pd.read_csv("Eg_subdivs.csv")

fig = px.scatter_mapbox(df,
                        lat='Latitude',
                        lon='Longitude',
                        hover_name='Subdivision_en',
                        title='Governorate Scatter Plot on Mapbox',
                        template='plotly',
                        zoom=5,
                        center={"lat": df['Latitude'].mean(), "lon": df['Longitude'].mean()},
                        mapbox_style="carto-positron")

# Show the map
fig.show()