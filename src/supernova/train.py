from .preprocess import load_and_clean

def main():
    print("✅ Supernova translation pipeline: training step ready!")
    try:
        df = load_and_clean("sample.csv")
        print(f"Loaded {len(df)} rows.")
    except FileNotFoundError:
        print("No sample.csv found — that’s OK for now.")

if __name__ == "__main__":
    main()
