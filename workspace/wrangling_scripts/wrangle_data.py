import pandas as pd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
    # read the energy data
    energy_df = pd.read_csv("data/all_energy_statistics.csv")
    
    color1 = 'rgb(0,153,0)'
    color2 = 'rgb(02,102,255)'
    color3 = 'rgb(255,204,153)'
    color4 = 'rgb(153,0,153)'
    
    # CHART 1 ================================================
    # select data about Aviation gasoline - Final Consumption
    # as a line chart
    selected_energy_df = energy_df[energy_df["commodity_transaction"].isin(["Aviation gasoline - Final consumption"])]
    fr_dt = selected_energy_df[selected_energy_df["country_or_area"].isin(["France"])]
    uk_dt = selected_energy_df[selected_energy_df["country_or_area"].isin(["United Kingdom"])]
    us_dt = selected_energy_df[selected_energy_df["country_or_area"].isin(["United States"])]
    pt_dt = selected_energy_df[selected_energy_df["country_or_area"].isin(["Portugal"])]
    mx_dt = selected_energy_df[selected_energy_df["country_or_area"].isin(["Mexico"])]
    x1 = fr_dt["year"].values
    y1 = fr_dt["quantity"].values
    x2 = uk_dt["year"].values
    y2 = uk_dt["quantity"].values
    x3 = pt_dt["year"].values
    y3 = pt_dt["quantity"].values
    x4 = mx_dt["year"].values
    y4 = mx_dt["quantity"].values

    graph_one = []    
    graph_one.append(
      go.Scatter(
      x = x1,
      y = y1,
      name = 'France',
      mode = 'lines',
      line=dict(color=color1)
      )
    )
    graph_one.append(
      go.Scatter(
      x = x2,
      y = y2,
      name = 'UK',
      mode = 'lines',
      line=dict(color=color2)
      )
    )
    graph_one.append(
      go.Scatter(
      x = x3,
      y = y3,
      name = 'Portugal',
      mode = 'lines',
      line=dict(color=color3)
      )
    )
    graph_one.append(
      go.Scatter(
      x = x4,
      y = y4,
      name = 'Mexico',
      mode = 'lines',
      line=dict(color=color4)
      )
    )

    layout_one = dict(title = 'Aviation Gasoline Consumption',
                xaxis = dict(title = 'Years'),
                yaxis = dict(title = 'Metric Tons (thousand)'),
                )

    # CHART 2 ================================================
    # select data about Aviation gasoline - Exports
    # as a line chart
    aviation_gas_exp = energy_df[energy_df["commodity_transaction"].isin(["Aviation gasoline - Exports"])]
    fr_av_exp = aviation_gas_exp[aviation_gas_exp["country_or_area"].isin(["France"])]
    uk_av_exp = aviation_gas_exp[aviation_gas_exp["country_or_area"].isin(["United Kingdom"])]
    us_av_exp = aviation_gas_exp[aviation_gas_exp["country_or_area"].isin(["United States"])]
    pt_av_exp = aviation_gas_exp[aviation_gas_exp["country_or_area"].isin(["Portugal"])]
    mx_av_exp = aviation_gas_exp[aviation_gas_exp["country_or_area"].isin(["Mexico"])]

    x1 = fr_av_exp["year"].values
    y1 = fr_av_exp["quantity"].values
    x2 = uk_av_exp["year"].values
    y2 = uk_av_exp["quantity"].values
    x3 = pt_av_exp["year"].values
    y3 = pt_av_exp["quantity"].values
    x4 = mx_av_exp["year"].values
    y4 = mx_av_exp["quantity"].values

    graph_two = []    
    graph_two.append(
      go.Scatter(
      x = x1,
      y = y1,
      name = 'France',
      line=dict(color=color1),
      mode = 'lines'
      )
    )
    graph_two.append(
      go.Scatter(
      x = x2,
      y = y2,
      name = 'UK',
      mode = 'lines',
      line=dict(color=color2)
      )
    )
    graph_two.append(
      go.Scatter(
      x = x3,
      y = y3,
      name = 'Portugal',
      mode = 'lines',
      line=dict(color=color3)
      )
    )
    graph_two.append(
      go.Scatter(
      x = x4,
      y = y4,
      name = 'Mexico',
      mode = 'lines',
      line=dict(color=color4)
      )
    )

    layout_two = dict(title = 'Aviation gasoline - Exports',
                xaxis = dict(title = 'Years'),
                yaxis = dict(title = 'Metric Tons (thousand)'),
                )

# CHART 3 ================================================
    # select data about Crude Petroleum - Refinery Capacity
    # as a line chart
    petroleum_ref_cap = energy_df[energy_df["commodity_transaction"].isin(["Crude petroleum - refinery capacity"])]
    fr_ref_cap = petroleum_ref_cap[petroleum_ref_cap["country_or_area"].isin(["France"])]
    uk_ref_cap = petroleum_ref_cap[petroleum_ref_cap["country_or_area"].isin(["United Kingdom"])]
    us_ref_cap = petroleum_ref_cap[petroleum_ref_cap["country_or_area"].isin(["United States"])]
    pt_ref_cap = petroleum_ref_cap[petroleum_ref_cap["country_or_area"].isin(["Portugal"])]
    mx_ref_cap = petroleum_ref_cap[petroleum_ref_cap["country_or_area"].isin(["Mexico"])]

    x1 = fr_ref_cap["year"].values
    y1 = fr_ref_cap["quantity"].values
    x2 = uk_ref_cap["year"].values
    y2 = uk_ref_cap["quantity"].values
    x3 = pt_ref_cap["year"].values
    y3 = pt_ref_cap["quantity"].values
    x4 = mx_ref_cap["year"].values
    y4 = mx_ref_cap["quantity"].values

    graph_three = []    
    graph_three.append(
      go.Scatter(
      x = x1,
      y = y1,
      name = 'France',
      mode = 'lines',
      line=dict(color=color1)
      )
    )
    graph_three.append(
      go.Scatter(
      x = x2,
      y = y2,
      name = 'UK',
      mode = 'lines',
      line=dict(color=color2)
      )
    )
    graph_three.append(
      go.Scatter(
      x = x3,
      y = y3,
      name = 'Portugal',
      mode = 'lines',
      line=dict(color=color3)
      )
    )
    graph_three.append(
      go.Scatter(
      x = x4,
      y = y4,
      name = 'Mexico',
      mode = 'lines',
      line=dict(color=color4)
      )
    )

    layout_three = dict(title = 'Crude Petroleum - Refinery Capacity',
                xaxis = dict(title = 'Years'),
                yaxis = dict(title = 'Metric Tons (thousand)'),
                )

# CHART 4 ================================================
    # select data about Conventional crude oil - total energy supply
    # as a line chart
    petroleum_supply = energy_df[energy_df["commodity_transaction"].isin(["Conventional crude oil - total energy supply"])]
    fr_petr_sup = petroleum_supply[petroleum_supply["country_or_area"].isin(["France"])]
    uk_petr_sup = petroleum_supply[petroleum_supply["country_or_area"].isin(["United Kingdom"])]
    us_petr_sup = petroleum_supply[petroleum_supply["country_or_area"].isin(["United States"])]
    pt_petr_sup = petroleum_supply[petroleum_supply["country_or_area"].isin(["Portugal"])]
    mx_petr_sup = petroleum_supply[petroleum_supply["country_or_area"].isin(["Mexico"])]

    x1 = fr_petr_sup["year"].values
    y1 = fr_petr_sup["quantity"].values
    x2 = uk_petr_sup["year"].values
    y2 = uk_petr_sup["quantity"].values
    x3 = pt_petr_sup["year"].values
    y3 = pt_petr_sup["quantity"].values
    x4 = mx_petr_sup["year"].values
    y4 = mx_petr_sup["quantity"].values

    graph_four = []    
    graph_four.append(
      go.Scatter(
      x = x1,
      y = y1,
      name = 'France',
      mode = 'lines',
      line=dict(color=color1)
      )
    )
    graph_four.append(
      go.Scatter(
      x = x2,
      y = y2,
      name = 'UK',
      mode = 'lines',
      line=dict(color=color2)
      )
    )
    graph_four.append(
      go.Scatter(
      x = x3,
      y = y3,
      name = 'Portugal',
      mode = 'lines',
      line=dict(color=color3)
      )
    )
    graph_four.append(
      go.Scatter(
      x = x4,
      y = y4,
      name = 'Mexico',
      mode = 'lines',
      line=dict(color=color4)
      )
    )

    layout_four = dict(title = 'Conventional crude oil - total energy supply',
                xaxis = dict(title = 'Years'),
                yaxis = dict(title = 'Metric Tons (thousand)'),
                )

    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures