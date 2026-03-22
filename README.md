# Virtual Column Processor

A lightweight Python tool for dynamically adding calculated columns to a Pandas DataFrame using string expressions.

## Key Features
- **Fast Calculations**: Uses `pd.eval()` for optimized vectorized operations.
- **Robust Validation**: Custom regex-based parsing and error handling for mathematical expressions.
- **Clean Architecture**: Separation of concerns between core logic, validation, and custom exceptions.
- **Full Test Coverage**: Includes unit tests for standard operations and edge cases (invalid characters, missing columns, etc.).

## Project Structure
```text
virtual-column-pandas/
├── config/             # Validation logic and custom exceptions
├── src/                # Core processing function
├── tests/              # Unit tests with pytest
├── requirements.txt    # Project dependencies
└── .gitignore          # Python-specific ignore rules
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pln6/virtual-column-pandas
   cd virtual-column-pandas
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```


## Testing Scenarios
The project includes tests for:
- Standard arithmetic: `+`, `-`, `*`
- Handling extra spaces in expressions
- Validation of new and existing column names
- Returning an empty DataFrame on invalid input (as per requirements)

## Tech Stack
- **Python 3.14**
- **Pandas**
- **Pytest**
- **Regex**
