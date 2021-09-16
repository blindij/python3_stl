import zlib

lorem = open('lorem.txt','rb').read()
compressed = zlib.compress(lorem)
combined = compressed + lorem

decompressor = zlib.decompressobj()
decompressed = decompressor.decompress(combined)

decompress_matches = decompressed == lorem
print('Decompress mathces lorem:', decompress_matches)

unused_matches = decompressor.unused_data == lorem
print('Unused data matches lorem:', unused_matches)
