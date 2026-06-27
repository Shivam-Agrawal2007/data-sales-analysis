import os
from config import REPORTS_DIR
from analysis import *
from logger import logger

def generate_summary(df):

    os.makedirs(REPORTS_DIR, exist_ok=True)

    summary_file = os.path.join(REPORTS_DIR, "summary.txt")

    with open(summary_file, "w") as file:

        file.write("=====================================\n")
        file.write("      SALES ANALYTICS SUMMARY\n")
        file.write("=====================================\n\n")

        file.write(f"Total Sales          : ${total_sales(df):,.2f}\n")
        file.write(f"Average Sales        : ${average_sales(df):,.2f}\n")
        file.write(f"Total Orders         : {total_orders(df)}\n")
        file.write(f"Unique Customers     : {unique_customers(df)}\n")
        file.write(f"Unique Products      : {unique_products(df)}\n\n")

        file.write("Top Category\n")
        file.write(f"{sales_by_category(df).idxmax()}\n\n")

        file.write("Top Region\n")
        file.write(f"{sales_by_region(df).idxmax()}\n\n")

        file.write("Top Customer\n")
        file.write(f"{top_10_customers(df).idxmax()}\n\n")

        file.write("Top Product\n")
        file.write(f"{top_10_products(df).idxmax()}\n\n")

    logger.info("Summary report generated successfully!")