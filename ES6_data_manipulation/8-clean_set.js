export default function cleanSet(set, startString) {
  if (startString === '') {
    return '';
  }
  const resultArray = [...set].map((value) => {
    if (value.startsWith(startString)) {
      return value.substring(startString.length);
    }
    return '';
  });
  const filterArray = resultArray.filter((value) => value !== '');
  return filterArray.join('-');
}
