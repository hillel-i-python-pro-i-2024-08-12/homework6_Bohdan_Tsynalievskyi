from DataProcessing.process_data import DataProvider, get_formatted_output, organize_data


def main():
    """
    You have a list of humans. Every human has "name" and "group".
    Your task is to show all groups, with amount and names of members
    for each group.
    """
    group_members = DataProvider().generate_group_members()
    organized_data = organize_data(humans=group_members)
    output = get_formatted_output(data=organized_data)
    print(output)


if __name__ == "__main__":
    main()
