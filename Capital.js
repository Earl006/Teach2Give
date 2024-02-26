function capitalizeFirstLetter(str: string): string {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

const input = prompt('Enter a string');
const capitalized = capitalizeFirstLetter(input);
console.log(capitalized);
