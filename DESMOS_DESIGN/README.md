# Let's learn to create DESMOS art! 🎨

**Topics covered:** 
- Basic graph functions (Outlining)
- Integration (Colouring)
- Bezier curves (Advanced) 

A beginner-friendly guide to make your first **DESMOS art**. 

--- 

##  Lossy vs Lossless Compression 🤔
**[Section for general audience]** <br>

Before diving into algorithms, it is important to understand the two types of image compression: **Lossy and Lossless**

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

<img width="608" height="546" alt="Image" src="https://github.com/user-attachments/assets/a927b895-8ee9-4e29-8284-28d9beac2228" />
https://www.desmos.com/calculator/lxoldwv14q
