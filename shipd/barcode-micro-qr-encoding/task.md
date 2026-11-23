Add qr.EncodeMicro(content string, level ErrorCorrectionLevel, mode Encoding) (barcode.Barcode, error) for the smallest ISO/IEC 18004 Micro QR symbol M1-M4 at the requested level, without a quiet zone. Return errors for empty content, content exceeding that level's capacity, unsupported levels or modes, Numeric content outside ASCII digits, or AlphaNumeric content outside its existing alphabet. Unicode preserves and counts raw bytes, including invalid UTF-8. Auto encodes one segment using the first mode that can encode all content at that level: Numeric, AlphaNumeric, Unicode.

Version n is 2n+9 modules square. M1 supports only Numeric, AlphaNumeric needs M2 or later, and Unicode M3 or later. The mode indicator uses n-1 bits: Numeric=0, AlphaNumeric=1, Unicode=2. Character counts use n+2 bits for Numeric and n+1 for AlphaNumeric/Unicode. Terminate with 2n+1 zero bits, truncated at capacity.

Symbol numbers 0-7 are M1-L, M2-L, M2-M, M3-L, M3-M, M4-L, M4-M, M4-Q, with respectively 2, 5, 6, 6, 8, 8, 10, 14 error-correction codewords in one block. M1/M3's last data codeword contains four bits. Pad codewords never fill it; unused bits are zero. Error correction takes these as a byte's high half, with a zero low half.

Use one top-left finder, light right/bottom separators and top/left timing patterns alternating from dark beside the separator. The 15 format bits concatenate the 3-bit symbol number, 2-bit mask number and ten BCH check bits (generator 10100110111), then XOR with 100010001000101.

Apply Micro masks 0-3, respectively QR masks 1, 4, 6, 7, only to data/error-correction modules. For rightmost-column and bottom-row dark counts a,b, maximize 16*min(a,b)+max(a,b), breaking ties toward the lower mask number.

Define barcode.TypeMicroQR = "Micro QR Code" and return it in Metadata. ColorModel conversion must keep dark and light modules distinct.
