##  Basic graph functions 🥱
**[Section for general audience]** <br>

Amazing youtube video for which I learnt from: https://www.youtube.com/watch?v=C1OOghkd0W8 

There are many complex equations to trace a picture 

--- 

### Lossy Compression
Lossy compression reduces file size by eliminating 'non-essential' data from your image.

- Produces significantly smaller files (Good for storing, handling and transmitting data)
- Loses data/information
- Might not be fully reversible

**Example uses:**
- MP3 audio format, removes audio that are outside human hearing range or too loud
- JPEG file format, changes color/reduce quality for more better file sharing


### Lossless Compression 
Lossless compression reduces file size while preserving all original content

- Achieves smaller reductions compared to lossy compressions
- 100% data integrity
- Fully reversible

**Example uses:**
- zip archive file format, one or more files/directories compressed
- PNG file format, keeps all original color and detail of original image

In general, lossy compression prioritises efficiency, while lossless compression prioritises transparency/data integrity 

---

## DEFLATE Compression 🎈 
**[Section for people with coding expertise]** <br>

While exploring Huffman Coding, I realised it's a component for many compression algorithms, which led me to the **DEFLATE** algorithm

DEFLATE is a lossless compression algorithm, originally designed for the **ZIP format**

However, it can also be used in: 
- zlib
- gzip
- PNG

## How DEFLATE works
DEFLATE comprises two core algorithms: 

### LZ77 
- Detects repeated substrings
- Replaces them with (offset, length, next character) tuples (Command-like prompts)
- Removes redundacy in data

### Huffman Coding
- A prefix code (Useful for decoding, explained more in code)
- Assigns a shorter bit representation to frequent symbols and a longer bit representation to rarer symbols
- Uses a binary tree
- Minimises encoding length

In short, 
- LZ77 reduces repeated substring patterns
- Huffman Coding optimises symbol encoding

Combined together, they form an efficient lossless compression pipeline called 'DEFLATE'. 

--- 

## Here is my attempt: (October 25 2025) 

### Original photo
<img width="517" height="478" alt="Image" src="https://github.com/user-attachments/assets/1f9bd3fc-930a-43cc-bb00-d1b99bd9102c" />

### My graph (~80 equations)
<img width="608" height="546" alt="Image" src="https://github.com/user-attachments/assets/a927b895-8ee9-4e29-8284-28d9beac2228" /> <br>
Link: https://www.desmos.com/calculator/lxoldwv14q
