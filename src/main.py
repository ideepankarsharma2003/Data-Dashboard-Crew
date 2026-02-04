from crew import crew

if __name__ == "__main__":
    result = crew.kickoff(
        inputs={
            "query": "I want to visualize all the information in these csv files in a neat dashboard about the portfolio `Garfield`",
            "csv_path": "src/data/holdings.csv, src/data/trades.csv"
        }
    )

    print("Dashboard generated:", result)
