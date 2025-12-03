import pandas as pd
from pathlib import Path

class CustomerBehaviorPreprocessor:
    """
    This class will perform all preprocessing steps for the customer behavior dataset.
    Each method returns self so that we can chain operations easily.
    """

    def __init__(self, input_path: str, output_path: str):
        self.input_path = Path(input_path)
        self.output_path = Path(output_path)
        self.df = None

    def load_data(self):
        """Load the raw CSV file."""
        self.df = pd.read_csv(self.input_path)
        return self
    
    def inspect (self):
        print("\n=== Dataset Info ===")
        print("Shape:", self.df.shape)
        print("\nColumns:", list(self.df.columns))
        print("\n=== Data Types ===")
        print(self.df.dtypes)

        print("\n=== Missing Values ===")
        print(self.df.isnull().sum())

        print("\n=== Sample Rows ===")
        print(self.df.head())

        return self

    def basic_cleaning(self):
        """Basic cleaning placeholder (real logic will be added later)."""
         # Trim column names
        self.df.columns = self.df.columns.str.strip()

        # Ensure Boolean columns are proper booleans
        if "Weekend" in self.df.columns:
            self.df["Weekend"] = self.df["Weekend"].astype(bool)

        if "Revenue" in self.df.columns:
            self.df["Revenue"] = self.df["Revenue"].astype(bool)

        # Remove duplicates
        self.df = self.df.drop_duplicates()

        return self
    
    def validate(self):
        """Validate the structure and logic of the cleaned data."""

        expected_columns = [
            "Administrative", "Administrative_Duration",
            "Informational", "Informational_Duration",
            "ProductRelated", "ProductRelated_Duration",
            "BounceRates", "ExitRates",
            "PageValues", "SpecialDay",
            "Month", "OperatingSystems", "Browser",
            "Region", "TrafficType",
            "VisitorType", "Weekend", "Revenue"
    ]

        # Check columns
        if list(self.df.columns) != expected_columns:
            raise ValueError("Column mismatch detected!")

        # Check missing values
        if self.df.isnull().sum().sum() > 0:
            raise ValueError("Missing values detected!")

        # Validate booleans
        if self.df["Weekend"].dtype != bool:
            raise TypeError("Weekend column must be boolean.")

        if self.df["Revenue"].dtype != bool:
            raise TypeError("Revenue column must be boolean.")

        print("Validation passed.")
        return self


    def save(self):
        """Save the processed dataset."""
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.df.to_csv(self.output_path, index=False)
        return self

    def run(self):
        """
        Runs the entire preprocessing pipeline.
        We will expand this later as we add more methods.
        """
        return (
            self.load_data()
                .inspect()
                .basic_cleaning()
                .validate()
                .save()
        )
