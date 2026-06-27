import matplotlib.pyplot as plt
from config import CHARTS_DIR
import os

def create_dashboard(df):
    fig, axes = plt.subplots(3, 2, figsize=(18, 15))
    fig.suptitle("Sales Analytics Dashboard", fontsize=20, fontweight="bold")
    
    monthly_sales = (df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum())

    axes[0, 0].plot(
        monthly_sales.index.astype(str), monthly_sales.values, marker="o")

    axes[0, 0].set_title("Monthly Sales")
    axes[0, 0].tick_params(axis="x", rotation=45)
    
    category_sales = (df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

    axes[0, 1].bar(
        category_sales.index,
        category_sales.values
    )

    axes[0, 1].set_title("Sales by Category")
    axes[0, 1].tick_params(axis="x", rotation=20)
    
    region_sales = (df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

    axes[1, 0].bar(region_sales.index, region_sales.values)

    axes[1, 0].set_title("Sales by Region")
    axes[1, 0].set_xlabel("Region")
    axes[1, 0].set_ylabel("Sales ($)")
    axes[1, 0].tick_params(axis="x", rotation=20)
    
    segment_sales = (df.groupby("Segment")["Sales"].sum())

    axes[1, 1].pie(segment_sales.values, labels=segment_sales.index, autopct="%1.1f%%", startangle=90)

    axes[1, 1].set_title("Sales by Segment")
    
    top_products = (df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10))

    top_products = top_products[::-1]

    axes[2, 0].barh(top_products.index, top_products.values)

    axes[2, 0].set_title("Top 10 Products")
    axes[2, 0].set_xlabel("Sales ($)")
    axes[2, 0].set_ylabel("Product")
    
    top_customers = (df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10))

    top_customers = top_customers[::-1]

    axes[2, 1].barh(top_customers.index,top_customers.values)

    axes[2, 1].set_title("Top 10 Customers")
    axes[2, 1].set_xlabel("Sales ($)")
    axes[2, 1].set_ylabel("Customer")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(os.path.join(CHARTS_DIR, "dashboard.png"), dpi=300, bbox_inches="tight")
    plt.close()