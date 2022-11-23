def sorted_union_files(files: list, result_path: str) -> None:
    temp_dict = {sum(1 for _ in open(one_file, encoding="UTF-8")): one_file for one_file in files}
    with open(result_path, "w") as file_write:
        file_write.write("")
    with open(result_path, "a") as file_write:
        for key in sorted(temp_dict.keys()):
            file_write.write(temp_dict[key] + "\n")
            file_write.write(str(key) + "\n")
            file_write.writelines(line for line in open(temp_dict[key], "r", encoding="UTF-8"))
            file_write.write("\n")

def main():
    files = ["1.txt", "2.txt", "3.txt"]
    sorted_union_files(files, "file.txt")

if __name__ == "__main__":
    main()