def segment(str):
    """
    Breaks a message string into segments of 160 characters.

    Args:
        str (String): contains 'A-Z','a-z',space( ),comma(,),periods(.).
    """
    message_size = len(str)
    print(message_size)
    if message_size <= 160:
        return str              # Messages that do not require segmentation

    # Calculate number of segments: 155 chars for message + 5 chars for suffix
    num_of_segments = int(message_size/155) + 1
    segmented_res = []
    start = 0
    for i in range(1, num_of_segments+1):
        if i != num_of_segments:
            end = 155 * i
            segmented_res.append(
                str[start:end]+("({}/{})".format(i, num_of_segments)))
        else:
            segmented_res.append(
                str[start:]+("({}/{})".format(num_of_segments,
                                              num_of_segments)))
        start = end
    return segmented_res


print(segment("""Contrary to popular belief, Lorem Ipsum is not simply
random text. It has roots in a piece of classical Latin literature from 45
BC, making it over 2000 years old. Richard McClintock, a Latin professor at
Hampden-Sydney College in Virginia, looked up one of the more obscure Latin
 words, consectetur, from a Lorem Ipsum passage, and going through the cites
 of the word in classical literature, discovered the undoubtable source.
Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum
et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC.
This book is a treatise on the theory of ethics, very popular during the
Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..",
comes from a line in section 1.10.32. The standard chunk of Lorem Ipsum used
since the 1500s is reproduced below for those interested. Sections 1.10.32
and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also
reproduced in their exact original form, accompanied by English versions
from the 1914 translation by H. Rackham."""))
print(len("""t Malorum by Cicero are also reproduced in their exact original
          form, accompanied by English versions from the 1914 translation by
          H. Rackham.(7/7)"""))
