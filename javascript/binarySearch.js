// This creates an array filled with consecutive numbers up to 20
let n = 21;
const list = Array.from(Array(n).keys());

function binarySearch(orderedArray, searchedValue) {
    let low = 0;
    let high = orderedArray.length - 1;

    while(low <= high) {
        let middle = Math.floor((low + high) / 2);

        if (orderedArray[middle] === searchedValue) {
            return orderedArray[middle];
        }
        if(orderedArray[middle] > searchedValue) {
            high = middle - 1;
        } else {
            low = middle + 1;
        }
    }
    return 'Not in Array';
}

let value = binarySearch(list, 0);
console.log(value);