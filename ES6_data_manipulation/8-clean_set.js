function cleanSet(set, startString) {
  if (!(set instanceof Set) || typeof startString !== 'string' || startString.length === 0) {
    return '';
  }

  const filtVal = [];
  for (const value of set) {
    if (typeof value === 'string' && value.startsWith(startString)) {
        filtVal.push(value.slice(startString.length));
    }
  }

  return filtVal.join('-');
}

export default cleanSet;
