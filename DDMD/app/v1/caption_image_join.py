def join():
    import os
    import re

    all_image_path = "../../datasets/all_images.txt"
    all_caption_path = "../../datasets/captions.token.txt"

    out_path = "../../datasets/ddmd.token.txt"

    data = ""

    with open(all_image_path) as fh1, open(all_caption_path) as fh2:
        # for line1, line2 in zip(fh1, fh2):
        #     # line1 from abc.txt, line2 from test.txtg
        #     if (line2 != '\n'):
        #         data = data +  line1.rstrip('\n') + '\t' + line2

        for line1 in fh1:
            with open(all_caption_path) as fh2:
                for line2 in fh2:
                    if (line2 != '\n'):
                        data = data + line1.rstrip('\n') + '\t' + line2

    with open(out_path, 'w') as outfile:
        outfile.write(data)
        outfile.write("\n")

# if __name__ == "__main__":
#     join()

