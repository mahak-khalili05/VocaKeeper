from database import add_word, show_words, search_word, delete_word

while True:

    print("\n========== VocaKeeper ==========")
    print("1. Add Word")
    print("2. Show Words")
    print("3. Search Word")
    print("4. Delete Word")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":

        korean = input("Korean: ")
        persian = input("Persian: ")

        add_word(korean, persian)

        print("\n✅ Word added!")

    elif choice == "2":

        words = show_words()

        if not words:
            print("\nNo words found.")

        else:
            print("\n========== Vocabulary ==========\n")

            for word in words:
                print(f"ID      : {word[0]}")
                print(f"Korean  : {word[1]}")
                print(f"Persian : {word[2]}")
                print("-------------------------------")

    elif choice == "3":

        keyword = input("Search: ")

        results = search_word(keyword)

        if not results:
            print("\nNo words found.")

        else:
            print()

            for word in results:
                print(f"{word[0]} | {word[1]} | {word[2]}")

    elif choice == "4":

        try:
            word_id = int(input("Word ID: "))
            delete_word(word_id)
            print("\n✅ Word deleted.")

        except ValueError:
            print("\n❌ Invalid ID.")

    elif choice == "5":

        print("\n👋 Goodbye!")
        break

    else:

        print("\n❌ Invalid choice.")
