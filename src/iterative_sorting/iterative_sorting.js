const arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
const arr3 = [0, 1, 2, 3, 4, 5]

function selectionSort(arr) {

    for (let i = 0; i < arr.length; i++) {
        let currentIndex = i
        let smallestIndex = currentIndex

        for (let j = currentIndex + 1; j < arr.length; j++) {
            if (arr[smallestIndex] > arr[j]) {
                smallestIndex = j
            }
        }
        let temp = arr[currentIndex]
        arr[currentIndex] = arr[smallestIndex]
        arr[smallestIndex] = temp

    }
    return arr

}

console.log('selection1:', selectionSort(arr1))
console.log('selection2:', selectionSort(arr3))

function bubbleSort(arr) {
    let swapCounter = -1
    while (swapCounter !== 0) {
        swapCounter = 0
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] > arr[i + 1]) {
                let temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swapCounter += 1
            }
        }
    }
    return arr

}

console.log('bubble1:', bubbleSort(arr1))
console.log('bubble2:', bubbleSort(arr3))