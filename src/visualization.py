import matplotlib.pyplot as plt
import os
from logger import logger

def get_charts_directory():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    charts_dir = os.path.join(project_root, "charts")
    os.makedirs(charts_dir, exist_ok=True)
    return charts_dir

def plot_sales_by_category(df):

    logger.info("Creating chart...")

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    charts_dir = get_charts_directory()

    output_file = os.path.join(charts_dir, "sales_by_category.png")

    plt.figure(figsize=(8,5))
    plt.bar(
        category_sales.index,
        category_sales.values
    )
    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales ($)")
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

    logger.info(f"Chart saved successfully!")
    
def plot_sales_by_region(df):

    region_sales = (
        df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
    )

    charts_dir = get_charts_directory()

    plt.figure(figsize=(8,5))
    plt.bar(region_sales.index, region_sales.values)
    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales ($)")
    plt.tight_layout()
    plt.savefig(os.path.join(charts_dir, "sales_by_region.png"))
    plt.close()
    
def plot_sales_by_segment(df):

    segment_sales = (
        df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
    )

    charts_dir = get_charts_directory()

    plt.figure(figsize=(8,5))
    plt.pie(
        segment_sales.values,
        labels=segment_sales.index,
        autopct="%1.1f%%"
    )
    plt.title("Sales by Segment")
    plt.savefig(os.path.join(charts_dir, "sales_by_segment.png"))
    plt.close()
    
def plot_top_products(df):
    top_products = (df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10))
    
    charts_dir = get_charts_directory()
    
    plt.figure(figsize=(12,6))
    plt.barh(top_products.index, top_products.values)
    plt.title("Top 10 Products")
    plt.ylabel("Product")
    plt.xlabel("Sales($)")
    plt.tight_layout()
    plt.savefig(os.path.join(charts_dir, "top_products.png"))
    plt.close()
    
def plot_top_customers(df):
    top_customers = (df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10))
    
    charts_dir = get_charts_directory()
    
    plt.figure(figsize=(12,6))
    plt.barh(top_customers.index, top_customers.values)
    plt.title("Top 10 Customers")
    plt.ylabel("Customer")
    plt.xlabel("Sales($)")
    plt.tight_layout()
    plt.savefig(os.path.join(charts_dir, "top_customers.png"))
    plt.close()
    
def plot_monthly_sales(df):
    monthly_sales = (
        df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
    )
    
    charts_dir = get_charts_directory()
    
    plt.figure(figsize=(12,6))
    plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker="o")
    plt.title("Monthly sales")
    plt.ylabel("Sales($)")
    plt.xlabel("Month")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(charts_dir, "monthly_sales.png"))
    plt.close()