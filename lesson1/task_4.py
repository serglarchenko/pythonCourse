import math

byte_ = 1024


def file_size(size_in_bytes):
    if size_in_bytes / byte_ < 1:
        return '%sB' % float(size_in_bytes)
    if (size_in_bytes / byte_ < byte_) and (size_in_bytes / byte_ > 1):
        return '%sKb' % round(float(size_in_bytes / byte_), 1)
    if size_in_bytes / math.pow(byte_, 2) < byte_:
        return '%sMb' % round(float(size_in_bytes / math.pow(byte_, 2)), 1)
    else:
        return '%sGb' % round(float(size_in_bytes / math.pow(byte_, 3)), 1)


print(file_size(999999999999))
