from loop import run_loop

def main():

    user_prompt = input("Enter your prompt: ")

    result = run_loop(user_prompt)

    print("\nFINAL OUTPUT\n")
    print(result)


if __name__ == "__main__":
    main()