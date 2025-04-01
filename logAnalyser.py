import re
from collections import Counter

def analyze_log_file(log_file_path):
    """
    Analyzes a log file and counts occurrences of all words.
    
    Args:
        log_file_path (str): Path to the log file
    
    Returns:
        dict: Dictionary with word counts sorted by frequency
    """
    word_counts = Counter()
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                words = re.findall(r'\b[a-zA-Z]+\b', line.lower())  # Exclude numbers
                word_counts.update(words)
        
        return dict(word_counts.most_common())
    
    except FileNotFoundError:
        print(f"Error: File '{log_file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def print_results(results):
    """Prints the word count analysis results in a readable format."""
    if not results:
        return
    
    print("\nLog File Word Count Analysis:")
    print("=" * 50)
    
    print("Words:")
    print("-" * 50)
    print(" ".join(results.keys()))
    
    print("=" * 50)

if __name__ == "__main__":
    # Configuration - set log file path
    log_file = "C:/Users/jk475/OneDrive/Desktop/PRojectsa/as/log.txt"  # Change to your log file path
    
    # Analyze the log file
    results = analyze_log_file(log_file)
    
    # Print results
    if results:
        print_results(results)
    else:
        print("No results to display.")
