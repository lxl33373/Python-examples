def count_and_replace(text):
    count = 0
    words = text.split()
    for i in range(len(words)):
        if words[i] == "terrible":
            count += 1
            if count % 2 == 0:
                words[i] = "pathetic"
            else:
                words[i] = "marvellous"
    return count, " ".join(words)

def main():
    with open("file_to_read.txt", "r") as file:
        content = file.read()

    count, new_content = count_and_replace(content)

    print(f"Total occurrences of 'terrible': {count}")

    with open("result.txt", "w") as file:
        file.write(new_content)

    print("Done! The modified text has been written to 'result.txt'.")

if __name__ == "__main__":
    main()