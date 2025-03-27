export function taskFirst() {
    const task = 'I prefer const when I can.';
    return task;
}

export function getLast() {
    return ' is okay';
}

export function taskNext() {
    let comb = 'But sometimes let';
    comb += getLast();

    return comb;
}