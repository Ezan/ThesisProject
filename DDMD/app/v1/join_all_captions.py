def join_all():
    import os
    import sys
    import re
    in_path = '../../datasets/image_desc_joined'  # image description extracted path
    out_path = '../../datasets/captions.token.txt'  # image description split path
    # Creating a list of filenames
    filenames = []
    for file in os.listdir(in_path):
        full_file = os.path.join(in_path, file)
        filenames.append(full_file)

    # Open file3 in write mode
    with open(out_path, 'w') as outfile:
        # Iterate through list

        for names in filenames:
            # Open each file in read mode
            with open(names) as infile:
                # read the data from file1 and
                # file2 and write it in file3
                outfile.write(infile.read())

            # Add '\n' to enter data of file2
            # from next line
            outfile.write("\n")

# if __name__ == "__main__":
#     join_all()