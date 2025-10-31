import argparse

from etl.extract import read_dataset
from etl.transform import data_processing
from etl.load import save_to_parquet, save_to_db


def get_cli_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="ETL pipeline")
    parser.add_argument(
        "-db", "--save-to-db", 
        action="store_true", 
        help="Save data to database. DB config stored in .env"
    )
    parser.add_argument(
        "-all", "--save-to-all", 
        action="store_true", 
        help="Save data to database and parquet file. Path - data/processed/"
    )
    parser.add_argument(
        "-ext-l", "--extract-local",
        action="store", # Default action
        type=str, 
        default="gaschromatography.csv", 
        help="Extract data from local csv file. Put your file into data/raw/. Enter file name"
    )
    parser.add_argument(
        "-ext-g", "--extract-gdrive", 
        action="store", # Default action
        type=str, 
        default=None, # "14jdCxjCsB0NT5ExKhWByxMiNHvd6V_3g"
        help="Extract data from Google Drive. Enter file ID"
    )
    args = parser.parse_args()
    return args


def run_etl(args: argparse.Namespace):
    # Data extraction
    if args.ext_g is not None:
        file_id = args.ext_g
        data_path = f"https://drive.google.com/uc?id={file_id}"
    else:
        data_path = "data/raw/" + args.ext_l
    df = read_dataset(data_path)

    # Data transormation
    df = data_processing(df)

    # Data loading
    if args.all:
        save_to_parquet(df)
        save_to_db(df)
    elif args.db:
        save_to_db(df)
    else:
        save_to_parquet(df)


def main():
    args = get_cli_args()

    run_etl(args)


if __name__ == "__main__":
    main()
