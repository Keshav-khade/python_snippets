"""
# how to copy two binary file or images using binary file.

fn1 = input("Enter your file name: ")
fn2 = input("Enter your file name: ")

with open(fn1,"rb") as f1:
    data = f1.read()

with open(fn2, "wb") as f2:
    f2.write(data)


# b'\\xff\\xd8\\xff\\xe0 -> unique starting number for jpeg file.
fn = input("Enter your file name: ")
with open(fn,"rb") as f1:
    data = f1.read(10)
    print((data))

# how to convert a string into binary format or file.
s = "Hello world"
text = s.encode("utf-8")
print(text)

with open("data.bin","wb") as file:
          file.write(text)

with open("data.bin","rb") as file:
          content = file.read()
          print(content)

# how to convert raw binary file into a string
with open("data.bin","rb") as file:
          content = file.read()
          text = content.decode("utf-8")
          print(text)
          print(type(text))
"""

"""
# how to copy small size files.
src = input("Enter file name: ")
dest = input("Enter file name")
def copy_small_file(src,dest):
          with open(src,"rb") as f1, open(dest, "wb") as f2:
                    data = f1.read()
                    f2.write(data)
                    # alternative one shot f2.write(f1.read())
# function alias for large name function
f = copy_small_file
f(src,dest)

# how to copy large files into small files.
src = input("Enter file name: ")
dest = input("Enter file name")
def copy_large_file(src,dest,chunk_size=1024):
        '''this function copies large files efficiently'''
        with open(src,"rb") as f1, open(dest,"wb") as f2:
                while True:
                    chunk = f1.read(chunk_size)
                    if not chunk:
                        break
                    f2.write(chunk)
f1 = copy_large_file
f1(src,dest)
print("Thank you !")
"""

"""
# how to identify file type
def identify_file_type(filename):
    with open(filename, "rb") as f:
        header = f.read(8)

    signatures = {
        b"\x89PNG": "PNG image",
        b"\xff\xd8\xff": "JPEG image",
        b"PK\x03\x04": "ZIP archive (or .docx/.xlsx/.pptx)",
        b"%PDF": "PDF document",
        b"GIF87a": "GIF image",
        b"GIF89a": "GIF image",
    }

    for sig, filetype in signatures.items():
        if header.startswith(sig):
            return filetype
    return "Unknown file type"

print(identify_file_type("photo.jpg"))   # JPEG image
"""
