export default function updateUniqueItems(updated_map) {
  if (!(updated_map instanceof Map)) {
    throw new Error('Cannot process');
  }
  updated_map.forEach((value, key) => {
    if (value === 1) {
      updated_map.set(key, 100);
    }
  });
}