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

    def basic_cleaning(self):
        """Basic cleaning placeholder (real logic will be added later)."""
        # We will add detailed cleaning logic in the next steps.
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
                .basic_cleaning()
                .save()
        )
