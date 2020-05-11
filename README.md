# LZW-Technique

* **1. Abstract**

The LZW algorithm is a very common compression technique. This algorithm is typically used in GIF and optionally in PDF and TIFF. Unix’s ‘compress’ command, among other uses. It is lossless, meaning no data is lost when compressing. The algorithm is simple to implement and has the potential for very high throughput in hardware implementations. It is the algorithm of the widely used Unix file compression utility compress, and is used in the GIF image format.

The Idea relies on reoccurring patterns to save data space. LZW is the foremost technique for general purpose data compression due to its simplicity and versatility. It is the basis of many PC utilities that claim to “double the capacity of your hard drive”.

* **2. The way it works**

LZW compression works by reading a sequence of symbols, grouping the symbols into strings, and converting the strings into codes. Because the codes take up less space than the strings they replace, we get compression.Characteristic features of LZW includes:

- LZW compression uses a code table, with 4096 as a common choice for the number of table entries. Codes 0-255 in the code table are always assigned to represent single bytes from the input file.

- When encoding begins the code table contains only the first 256 entries, with the remainder of the table being blanks. Compression is achieved by using codes 256 through 4095 to represent sequences of bytes.

- As the encoding continues, LZW identifies repeated sequences in the data, and adds them to the code table. Decoding is achieved by taking each code from the compressed file and translating it through the code table to find what character or characters it represents.

a. Compress process (pipeline):

 <p align= "center">
  <img src = "https://user-images.githubusercontent.com/51883796/81542438-d8d25400-939e-11ea-9223-b33e224be0b6.PNG">
  </p>

b> Decompress process (pipeline):

<p align = "center">
  <img src = "https://user-images.githubusercontent.com/51883796/81542617-264ec100-939f-11ea-834b-7b99620fd216.png">
</p>

c. Result:

<p align = "center">
  <img src = "https://user-images.githubusercontent.com/51883796/81542716-4ed6bb00-939f-11ea-85f3-1b7091f2d29e.png">
</p>

-----

## Group member
* Dinh Phuoc Loc
* Nguyen Hoang Phung
* Kieu Ngoc Anh

  

