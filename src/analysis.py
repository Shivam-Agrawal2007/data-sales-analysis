import pandas as pd
import os
from config import REPORTS_DIR
from logger import logger

def total_sales(df):
    return df["Sales"].sum()


def average_sales(df):
    return df["Sales"].mean()


def total_orders(df):
    return df["Order ID"].nunique()


def unique_customers(df):
    return df["Customer ID"].nunique()


def unique_products(df):
    return df["Product ID"].nunique()


def sales_by_category(df):
    return df.groupby("Category")["Sales"].sum().sort_values(ascending=False)


def sales_by_region(df):
    return df.groupby("Region")["Sales"].sum().sort_values(ascending=False)


def sales_by_segment(df):
    return df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)


def top_10_products(df):
    return (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )


def top_10_customers(df):
    return (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )


def generate_reports(df):

    os.makedirs(REPORTS_DIR, exist_ok=True)

    sales_by_category(df).to_csv(
        os.path.join(REPORTS_DIR, "category_report.csv"),
        header=["Sales"]
    )

    sales_by_region(df).to_csv(
        os.path.join(REPORTS_DIR, "region_report.csv"),
        header=["Sales"]
    )

    sales_by_segment(df).to_csv(
        os.path.join(REPORTS_DIR, "segment_report.csv"),
        header=["Sales"]
    )

    top_10_products(df).to_csv(
        os.path.join(REPORTS_DIR, "top_products.csv"),
        header=["Sales"]
    )

    top_10_customers(df).to_csv(
        os.path.join(REPORTS_DIR, "top_customers.csv"),
        header=["Sales"]
    )

    logger.info("Reports generated successfully!")