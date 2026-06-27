from load_data import load_data
from clean_data import clean_data
from analysis import *
from visualization import *
from dashboard import create_dashboard
from config import TRAIN_DATA, CLEANED_DATA
from summary import generate_summary
from logger import logger

def main():
    file_path = TRAIN_DATA
    df = load_data(file_path)
    
    if df is None:
        return
    
    df = clean_data(df)
    
    # print(df.head())
    # print(df.info())
    df.to_csv(CLEANED_DATA, index=False)
    logger.info("Clean data saved successsfully.")
    
    print("\n========== SALES ANALYTICS ==========\n")

    print(f"Total Sales: ${total_sales(df):,.2f}")
    print(f"Average Sales: ${average_sales(df):,.2f}")
    print(f"Total Orders: {total_orders(df)}")
    print(f"Unique Customers: {unique_customers(df)}")
    print(f"Unique Products: {unique_products(df)}")

    print("\nSales by Category")
    print(sales_by_category(df))

    print("\nSales by Region")
    print(sales_by_region(df))

    print("\nSales by Segment")
    print(sales_by_segment(df))

    print("\nTop 10 Products")
    print(top_10_products(df))

    print("\nTop 10 Customers")
    print(top_10_customers(df))
    
    generate_reports(df)
    generate_summary(df)
    
    plot_sales_by_category(df)
    plot_sales_by_region(df)
    plot_sales_by_segment(df)
    plot_top_products(df)
    plot_top_customers(df)
    plot_monthly_sales(df)
    create_dashboard(df)
    
if __name__ == "__main__":
    main()