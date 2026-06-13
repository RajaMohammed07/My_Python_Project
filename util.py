def main():
    print("This is the initial utility function v1.")
    buggy_feature()

def buggy_feature():
    print("Executing new feature...")
    x = 1 / 0

if __name__ == "__main__":
    main()
