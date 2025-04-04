function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  const buf = new ArrayBuffer(length);
  const datview = new DataView(buf);
  datview.setInt8(position, value);
  return datview;
}

export default createInt8TypedArray;
