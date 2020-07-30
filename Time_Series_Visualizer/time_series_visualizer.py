import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16,4))
    plt.plot(df, color="r")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar2 = df.copy()
    df_bar2.reset_index(inplace=True)
    df_bar2["year"] = [d.year for d in df_bar2.date]
    df_bar2["month"] = [d.strftime("%B") for d in df_bar2.date]

    # Draw bar plot
    order_bar = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    fig, ax = plt.subplots(figsize=(12,10))
    sns.barplot(x="year", y="value", hue="month", data=df_bar2, palette="muted", hue_order=order_bar, ci=None)
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(loc="upper left", prop={"size":15})  

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    order_box = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16,6))
    sns.boxplot(x="year", y="value", data=df_box, ax=ax1)
    sns.boxplot(x="month", y="value", data=df_box, ax=ax2, order=order_box)
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax2.set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
