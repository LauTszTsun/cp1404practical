import wikipedia

def main():
    user_input = input("Enter page title: ")
    while user_input.strip() != "":

        try:
            # get page - disable autosuggest to avoid strange redirects
            page = wikipedia.page(user_input, auto_suggest=False)

            print(page.title)
            print(page.summary)
            print(page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)  # list of possible pages

        except wikipedia.exceptions.PageError:
            print(f'Page id "{user_input}" does not match any pages. Try another id!')

        except Exception as e:
            # generic fallback for unknown issues (rare)
            print(f"An error occurred: {e}")

        print()
        user_input = input("Enter page title: ")

    print("Thank you.")


if __name__ == "__main__":
    main()