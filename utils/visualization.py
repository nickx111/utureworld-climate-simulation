import plotly.graph_objects as go
import plotly.express as px
import numpy as np

def plot_temperature_trends(simulation_results):
    """Create temperature trend visualization"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=simulation_results['year'],
        y=simulation_results['temperature'],
        mode='lines',
        name='Projected Temperature',
        line=dict(color='#FF4B4B')
    ))
    
    fig.update_layout(
        template='plotly_dark',
        title='Global Temperature Projection',
        xaxis_title='Year',
        yaxis_title='Temperature (°C)',
        hovermode='x'
    )
    return fig

def plot_sea_level_rise(simulation_results):
    """Create sea level rise visualization"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=simulation_results['year'],
        y=simulation_results['sea_level'],
        mode='lines',
        name='Sea Level Rise',
        line=dict(color='#00AB88')
    ))
    
    fig.update_layout(
        template='plotly_dark',
        title='Sea Level Rise Projection',
        xaxis_title='Year',
        yaxis_title='Rise (meters)',
        hovermode='x'
    )
    return fig

def plot_resource_depletion(simulation_results):
    """Create resource depletion visualization"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=simulation_results['year'],
        y=simulation_results['resource_index'],
        mode='lines',
        name='Resource Index',
        line=dict(color='#FFA500')
    ))
    
    fig.update_layout(
        template='plotly_dark',
        title='Resource Depletion Index',
        xaxis_title='Year',
        yaxis_title='Resource Index (100 = 2000 levels)',
        hovermode='x'
    )
    return fig

def plot_correlation_matrix(simulation_results):
    """Create correlation matrix visualization"""
    df = pd.DataFrame(simulation_results)
    corr_matrix = df.corr()
    
    fig = px.imshow(
        corr_matrix,
        color_continuous_scale='RdBu',
        aspect='auto'
    )
    
    fig.update_layout(
        template='plotly_dark',
        title='Impact Correlation Matrix'
    )
    return fig
